#!/usr/bin/env python3
"""
LIMEN edge-case ingestion lane: GitHub Security Advisories (GHSA), AI-filtered.
================================================================================

WHY THIS LANE
-------------
The existing LIMEN candidate pool is dominated by *register entries* (e.g. the
Dutch Algorithm Register), which the project itself classifies as
`public_register_entry_noncase` / `closed_noncase_source_surface`: a register
listing proves a *source surface* exists, it is NOT a documented edge-case
event, incident, or finding. That pool cannot grow the atlas of genuine edge
cases.

GHSA is a high-yield public source of *genuine* AI edge cases: each reviewed
advisory describes a concrete, reproducible technical failure in a real,
named software component, with a stable citable URL, an issuing authority
(the GitHub Advisory Database, a CNA), severity, CWE, and dates. Filtered for
AI/agentic systems (MCP servers, LLM frameworks, prompt-injection, agent tool
abuse) it yields exactly the "agentic control failure" / "security_risk" /
confused-deputy material LIMEN tracks (cf. reviewed-core LIMEN-000008
LangChain, LIMEN-000010 export-control).

WHAT THIS SCRIPT DOES
---------------------
1. Pulls a SMALL sample of *reviewed* advisories from the public GitHub REST
   API (`/advisories`), one page per AI keyword query. No auth required
   (unauth rate limit ~60/hr is enough for a small sample). If `--dry-run`
   or no network, it reads any locally cached JSON under `--cache-dir`
   instead and clearly marks the run as a dry run.
2. AI-relevance filter: keeps only advisories whose summary/description/package
   match an AI/agentic vocabulary, with a transparent matched-terms trail.
3. Maps each kept advisory to the LIMEN candidate schema:
   title, summary, authority, source_url, proposed evidence_tier, claim_ceiling
   (plus the full 25-column extraction-draft TSV the project's human-review
   pipeline already consumes).
4. Writes candidates to a NEW staging dir under
   results/review-candidates/ingest-ghsa-<date>/ as both a 25-column TSV and a
   JSONL of the canonical candidate fields, plus a low-confidence exclusions
   file and a SCOPE.md. NOTHING is promoted; cases.json is NOT touched.

ANTI-FABRICATION
----------------
- Every emitted field traces to a real GHSA record field. No invented numbers,
  quotes, dates, or URLs.
- Advisories that match the AI vocabulary only weakly (single generic token,
  no package/CWE corroboration) are written to the low-confidence file with
  `low_confidence=yes`, NOT to the promotable set.
- `proposed_evidence_tier` is conservative: a reviewed GHSA with a reproduction
  / patched-version / CWE is a `T4_reproducible_technical_finding`; otherwise
  `T1_single_public_source`. The script NEVER claims T3 authoritative-finding
  status from a GHSA alone.

USAGE
-----
  python3 ingest_ghsa_ai.py                 # live pull, small sample
  python3 ingest_ghsa_ai.py --dry-run       # no network; use cache-dir
  python3 ingest_ghsa_ai.py --per-query 5   # tune sample size

The script is read-only against the network and write-only into a fresh dated
staging dir; it never edits existing LIMEN artifacts.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# ----------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------

SOURCE_KEY = "ghsa"
SOURCE_AUTHORITY = (
    "GitHub Advisory Database (github.com/advisories), a CVE Numbering "
    "Authority (CNA) operated by GitHub; advisories shown are GitHub-'reviewed'"
)
API_ROOT = "https://api.github.com/advisories"
USER_AGENT = "tyche-limen-ghsa-ingest/0.1 (+research; contact anton.sokolov@tyche.institute)"

# AI / agentic vocabulary. A STRONG term alone is enough to keep a record;
# a WEAK term needs corroboration (package match or a second term) or the
# record is routed to low-confidence.
STRONG_TERMS = [
    "mcp server", "model context protocol", "prompt injection",
    "prompt-injection", "jailbreak", "agentic", "ai agent", "llm agent",
    "tool invocation", "tool poisoning", "confused deputy", "rag pipeline",
    "vector store", "system prompt", "function calling",
]
WEAK_TERMS = [
    "llm", "large language model", "ai model", "machine learning",
    "inference", "embedding", "chatbot", "openai", "anthropic", "gpt",
    "langchain", "llamaindex", "transformers", "huggingface", "ollama",
    "generative", "neural", "model serving",
]
# --- API query strategy -----------------------------------------------------
# IMPORTANT: the GitHub /advisories endpoint does NOT support free-text search.
# A `query`/keyword param is silently ignored (verified: query=MCP and
# query=langchain return the identical newest-first list). The endpoint DOES
# support the structured `affects=<comma-separated package names>` filter, which
# returns advisories whose vulnerable package matches. We therefore drive the
# lane off a curated list of known AI / agentic / LLM-tooling package names.
# This is high precision (the affected component is itself an AI package) and
# respects the documented API contract. Add packages here to widen the net.
AI_PACKAGES = [
    # LLM application frameworks / orchestration
    "langchain", "langchain-core", "langchain-community", "langchain-experimental",
    "langsmith", "llama-index", "llama_index", "haystack-ai", "guidance",
    "dspy", "semantic-kernel", "autogen", "crewai", "litellm",
    # Model Context Protocol (agentic tool plane)
    "mcp", "modelcontextprotocol", "fastmcp", "mcp-server", "@modelcontextprotocol/sdk",
    # model runtimes / inference / serving
    "transformers", "vllm", "ollama", "text-generation-inference", "llama-cpp-python",
    "ctransformers", "sentence-transformers",
    # vector stores / RAG
    "chromadb", "qdrant-client", "weaviate-client", "faiss-cpu",
    # provider SDKs
    "openai", "anthropic", "google-generativeai", "cohere",
    # agent frameworks
    "gradio", "streamlit-chat", "open-interpreter", "superagi", "agentgpt",
]

# Each fetch sends one page per chunk of package names. The endpoint accepts a
# comma-separated `affects` list, so we batch to stay well under rate limits.
PACKAGE_CHUNK = 8

# Map of LIMEN category hints derived ONLY from GHSA-native fields (CWE id,
# severity, matched terms). No semantic guessing beyond these explicit signals.
CWE_TO_LIMEN = {
    "CWE-306": "agentic_control_failure",   # missing auth for critical fn
    "CWE-862": "agentic_control_failure",   # missing authorization
    "CWE-94": "security_risk",              # code injection
    "CWE-78": "security_risk",              # OS command injection
    "CWE-77": "security_risk",              # command injection
    "CWE-918": "security_risk",             # SSRF
    "CWE-22": "security_risk",              # path traversal
    "CWE-502": "security_risk",             # deserialization
    "CWE-1336": "security_risk",            # template injection
    "CWE-74": "security_risk",              # injection (generic)
}


# ----------------------------------------------------------------------------
# Fetch layer
# ----------------------------------------------------------------------------

def _http_get_json(url: str, timeout: int = 25):
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": USER_AGENT,
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def fetch_live(per_query: int, cache_dir: str) -> tuple[list[dict], list[str]]:
    """Pull a small sample from the live API via the `affects` package filter."""
    os.makedirs(cache_dir, exist_ok=True)
    seen: dict[str, dict] = {}
    notes: list[str] = []
    for batch in _chunks(AI_PACKAGES, PACKAGE_CHUNK):
        affects = ",".join(batch)
        params = {
            "per_page": str(max(1, min(per_query, 100))),
            "type": "reviewed",
            "sort": "published",
            "direction": "desc",
            "affects": affects,
        }
        url = API_ROOT + "?" + urllib.parse.urlencode(params)
        try:
            data = _http_get_json(url)
        except urllib.error.HTTPError as e:
            notes.append(f"affects={affects!r} HTTPError {e.code}: {e.reason}")
            continue
        except Exception as e:  # noqa: BLE001 - report any network failure plainly
            notes.append(f"affects={affects!r} fetch failed: {e!r}")
            continue
        if not isinstance(data, list):
            notes.append(f"affects={affects!r} unexpected response: {str(data)[:120]}")
            continue
        # cache the raw page verbatim for reproducibility / dry-run reuse
        safe = re.sub(r"[^a-z0-9]+", "-", batch[0].lower()).strip("-")
        with open(os.path.join(cache_dir, f"raw-{safe}.json"), "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
        for adv in data:
            gid = adv.get("ghsa_id")
            if gid and gid not in seen:
                seen[gid] = adv
        notes.append(f"affects[{batch[0]}...] ({len(batch)} pkgs) -> {len(data)} advisories")
        time.sleep(1.0)  # be polite to the 60/hr unauth limit
    return list(seen.values()), notes


def fetch_cached(cache_dir: str) -> tuple[list[dict], list[str]]:
    """Dry-run path: read any cached raw-*.json pages from a prior live run."""
    seen: dict[str, dict] = {}
    notes: list[str] = []
    if not os.path.isdir(cache_dir):
        notes.append(f"no cache dir at {cache_dir}; dry run produced 0 records")
        return [], notes
    files = sorted(f for f in os.listdir(cache_dir) if f.startswith("raw-") and f.endswith(".json"))
    for f in files:
        try:
            with open(os.path.join(cache_dir, f), encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception as e:  # noqa: BLE001
            notes.append(f"cache file {f} unreadable: {e!r}")
            continue
        for adv in data if isinstance(data, list) else []:
            gid = adv.get("ghsa_id")
            if gid and gid not in seen:
                seen[gid] = adv
        notes.append(f"cache {f} -> {len(data) if isinstance(data, list) else 0} advisories")
    return list(seen.values()), notes


# ----------------------------------------------------------------------------
# Relevance + mapping
# ----------------------------------------------------------------------------

def _haystack(adv: dict) -> str:
    parts = [adv.get("summary") or "", adv.get("description") or ""]
    for v in adv.get("vulnerabilities") or []:
        pkg = (v.get("package") or {})
        parts.append(pkg.get("name") or "")
        parts.append(pkg.get("ecosystem") or "")
    return " ".join(parts).lower()


def _package_is_ai(adv: dict) -> list[str]:
    """Weak terms that appear in the AFFECTED PACKAGE name/ecosystem.

    A weak AI token is only trustworthy when the *vulnerable component itself*
    is an AI component (e.g. package name 'langchain'), not when a model name
    is merely mentioned in prose (e.g. 'patch authored by gpt-5'). This kills
    the common false positive where an advisory credits an AI tool in an
    authorship/credit line.
    """
    names = []
    for v in adv.get("vulnerabilities") or []:
        pkg = v.get("package") or {}
        names.append((pkg.get("name") or "").lower())
        names.append((pkg.get("ecosystem") or "").lower())
    blob = " ".join(names)
    hits = {t for t in WEAK_TERMS if re.search(r"\b" + re.escape(t) + r"\b", blob)}
    # Also treat an exact match against the curated AI-package allow-list as a
    # package-level AI signal (covers AI packages whose name is not in the
    # generic WEAK_TERMS vocabulary, e.g. 'llama-index', 'fastmcp').
    pkg_names = {n for n in names if n}
    hits |= {p for p in AI_PACKAGES if p.lower() in pkg_names}
    return sorted(hits)


def relevance(adv: dict) -> dict:
    """Return matched strong/weak terms and a keep/low_confidence decision."""
    hay = _haystack(adv)
    strong = sorted({t for t in STRONG_TERMS if t in hay})
    weak = sorted({t for t in WEAK_TERMS if re.search(r"\b" + re.escape(t) + r"\b", hay)})
    weak_in_pkg = _package_is_ai(adv)

    # Decision rules (transparent, conservative). NOTE: every GHSA record has a
    # security CWE, so a security CWE is NOT evidence of AI relevance and is
    # never used to upgrade a weak match. AI relevance must come from AI-specific
    # vocabulary, with prose-only weak tokens treated as untrustworthy.
    #  - >=1 STRONG term                          -> keep (high precision)
    #  - >=1 weak token IN THE AFFECTED PACKAGE    -> keep (the component is AI)
    #  - >=2 distinct weak tokens in prose         -> keep, flagged weaker
    #  - exactly 1 weak token, prose-only          -> low_confidence (exclude)
    #  - nothing                                   -> low_confidence (exclude)
    if strong:
        return {"keep": True, "low_confidence": False, "strong": strong, "weak": weak,
                "reason": f"matched strong AI/agentic term(s): {', '.join(strong)}"}
    if weak_in_pkg:
        return {"keep": True, "low_confidence": False, "strong": strong, "weak": weak,
                "reason": "affected package is an AI component "
                          f"(package matched: {', '.join(weak_in_pkg)})"}
    if len(weak) >= 2:
        return {"keep": True, "low_confidence": False, "strong": strong, "weak": weak,
                "reason": f"multiple AI terms in advisory text ({', '.join(weak)})"}
    if weak:
        return {"keep": False, "low_confidence": True, "strong": strong, "weak": weak,
                "reason": f"only a single weak AI token in prose ({', '.join(weak)}); "
                          "the affected component is not itself an AI package "
                          "(likely an authorship/credit mention, not an AI edge case)"}
    return {"keep": False, "low_confidence": True, "strong": strong, "weak": weak,
            "reason": "no AI/agentic vocabulary matched"}


def propose_tier(adv: dict) -> tuple[str, str]:
    """Conservative evidence tier from GHSA-native corroboration only."""
    desc = (adv.get("description") or "").lower()
    has_repro = ("## reproduction" in desc) or ("reproduction" in desc and "```" in (adv.get("description") or ""))
    patched = any(
        (v.get("first_patched_version"))
        for v in (adv.get("vulnerabilities") or [])
    )
    cwe = bool(adv.get("cwes"))
    if (has_repro or patched) and cwe:
        return ("T4_reproducible_technical_finding",
                "reviewed advisory with a CWE plus a reproduction and/or a "
                "first-patched version (technical finding is corroborated)")
    return ("T1_single_public_source",
            "single reviewed public advisory; not independently corroborated here")


def limen_categories(adv: dict, rel: dict) -> list[str]:
    cats: set[str] = set()
    for c in (adv.get("cwes") or []):
        cid = c.get("cwe_id")
        if cid in CWE_TO_LIMEN:
            cats.add(CWE_TO_LIMEN[cid])
    # agentic signal from matched strong terms
    if any(t in rel["strong"] for t in ("mcp server", "model context protocol",
                                        "agentic", "ai agent", "llm agent",
                                        "tool invocation", "tool poisoning",
                                        "confused deputy")):
        cats.add("agentic_control_failure")
    if "prompt injection" in rel["strong"] or "prompt-injection" in rel["strong"]:
        cats.add("security_risk")
    if not cats:
        cats.add("security_risk")  # all GHSA records are, at minimum, security signals
    cats.add("software_supply_chain_surface")
    return sorted(cats)


def primary_package(adv: dict) -> str:
    for v in adv.get("vulnerabilities") or []:
        pkg = v.get("package") or {}
        name = pkg.get("name")
        if name:
            eco = pkg.get("ecosystem") or "?"
            return f"{name} ({eco})"
    return ""


def cvss_score(adv: dict) -> str:
    sev = adv.get("cvss_severities") or {}
    for k in ("cvss_v4", "cvss_v3"):
        node = sev.get(k) or {}
        if node.get("score"):
            return f"{node.get('score')} ({k}, {node.get('vector_string') or 'no vector'})"
    return ""


def first_sentence(text: str, limit: int = 320) -> str:
    text = re.sub(r"\s+", " ", (text or "").strip())
    # drop leading "## Resolution ..." preamble; find first real summary block
    m = re.search(r"## summary\s*(.+)", text, flags=re.IGNORECASE)
    if m:
        text = m.group(1).strip()
    return (text[:limit].rstrip() + "...") if len(text) > limit else text


def map_record(adv: dict, rel: dict, run_date: str) -> dict:
    gid = adv.get("ghsa_id") or "GHSA-UNKNOWN"
    tier, tier_reason = propose_tier(adv)
    cats = limen_categories(adv, rel)
    pkg = primary_package(adv)
    cve = adv.get("cve_id") or ""
    published = adv.get("published_at") or ""
    year = published[:4] if published[:4].isdigit() else ""
    sev = adv.get("severity") or "unknown"
    cvss = cvss_score(adv)
    desc_summary = first_sentence(adv.get("description") or adv.get("summary") or "")

    summary = (
        f"GitHub-reviewed security advisory {gid}"
        + (f" / {cve}" if cve else "")
        + f": {adv.get('summary','').strip()}. "
        + (f"Affected package: {pkg}. " if pkg else "")
        + (f"Severity: {sev}" + (f"; CVSS {cvss}" if cvss else "") + ". ")
        + f"Advisory detail: {desc_summary} "
        + "This record captures a reviewed public advisory describing a "
        + "concrete technical failure in a named AI/agentic software "
        + "component; it is a candidate edge case for human review, not a "
        + "promoted reviewed-core case."
    )

    bounded_claim = (
        f"A GitHub-reviewed advisory {gid}"
        + (f" (alias {cve})" if cve else "")
        + f" exists at the cited URL describing a {sev}-severity issue"
        + (f" in {pkg}" if pkg else "")
        + "."
    )

    claim_ceiling = (
        "Advisory-surface finding only: confirms a GitHub-reviewed advisory "
        "exists describing the stated technical issue in the named component. "
        "Records the advisory's own claims and metadata; does not independently "
        "verify exploitation in the wild, real-world harm, prevalence, or "
        "vendor culpability beyond the advisory text."
    )
    forbidden = (
        "Do not infer real-world exploitation, realized harm, victim count, "
        "prevalence across deployments, legal liability, or that the issue is "
        "unpatched/ongoing beyond what the advisory and its first-patched "
        "version state. Do not upgrade tier on GHSA evidence alone."
    )

    refs = adv.get("references") or []
    return {
        # ---- canonical candidate fields requested by the task ----
        "case_id": f"LIMEN-DRAFT-GHSA-{gid.replace('GHSA-', '')}",
        "title": (adv.get("summary") or gid).strip(),
        "summary": summary,
        "authority": SOURCE_AUTHORITY,
        "source_url": adv.get("html_url") or (API_ROOT + "/" + gid),
        "proposed_evidence_tier": tier,
        "claim_ceiling": claim_ceiling,
        # ---- extra LIMEN extraction-draft fields ----
        "draft_status": "draft_for_human_review",
        "jurisdiction_country": "global",  # software advisory; no single jurisdiction
        "year": year,
        "accession_snapshot_date": run_date,
        "proposed_limen_categories": "; ".join(cats),
        "forbidden_overread": forbidden,
        "required_before_reviewed_core": (
            "Human review to confirm AI/agentic relevance and to decide whether "
            "this advisory is a distinct LIMEN edge case (not a duplicate of an "
            "existing reviewed-core entry); optionally corroborate with a second "
            "independent source (NVD entry, vendor writeup, or media report)."
        ),
        "required_before_obscure_ai": (
            "Not ObscureAI material unless promoted to a sourced reviewed-core "
            "case with confirmed AI relevance and bounded behaviour claim."
        ),
        "bounded_claim_candidate": bounded_claim,
        "source_record_id": gid,
        "cve_id": cve,
        "severity": sev,
        "cvss": cvss,
        "affected_package": pkg,
        "cwe_ids": "; ".join(c.get("cwe_id", "") for c in (adv.get("cwes") or [])),
        "published_at": published,
        "references": " | ".join(refs[:6]),
        "tier_rationale": tier_reason,
        "relevance_reason": rel["reason"],
        "matched_strong_terms": "; ".join(rel["strong"]),
        "matched_weak_terms": "; ".join(rel["weak"]),
        "low_confidence": "no",
        "promotable": "yes_as_candidate_edge_case_draft",
        "next_action": (
            "Human accept/reject as an AI edge-case candidate; confirm AI "
            "relevance + non-duplication before any reviewed-core or cases.json "
            "addition."
        ),
    }


# 25-column order mirroring the project's extraction-drafts TSV, with GHSA-native
# columns appended (kept additive so existing readers still find the first 25).
TSV_COLUMNS = [
    "case_id", "draft_status", "title", "summary", "authority",
    "jurisdiction_country", "year", "accession_snapshot_date",
    "proposed_evidence_tier", "primary_source_url", "claim_ceiling",
    "proposed_limen_categories", "forbidden_overread",
    "required_before_reviewed_core", "required_before_obscure_ai",
    "bounded_claim_candidate", "source_record_id", "source_signal_ids",
    "source_signal_count", "source_adjudication_path", "source_registry_csv",
    "rationale", "low_confidence", "promotable", "next_action",
    # appended GHSA-native provenance columns
    "cve_id", "severity", "cvss", "affected_package", "cwe_ids",
    "published_at", "references", "tier_rationale", "relevance_reason",
    "matched_strong_terms", "matched_weak_terms",
]


def to_tsv_row(rec: dict, source_path: str) -> dict:
    row = {
        "case_id": rec["case_id"],
        "draft_status": rec["draft_status"],
        "title": rec["title"],
        "summary": rec["summary"],
        "authority": rec["authority"],
        "jurisdiction_country": rec["jurisdiction_country"],
        "year": rec["year"],
        "accession_snapshot_date": rec["accession_snapshot_date"],
        "proposed_evidence_tier": rec["proposed_evidence_tier"],
        "primary_source_url": rec["source_url"],
        "claim_ceiling": rec["claim_ceiling"],
        "proposed_limen_categories": rec["proposed_limen_categories"],
        "forbidden_overread": rec["forbidden_overread"],
        "required_before_reviewed_core": rec["required_before_reviewed_core"],
        "required_before_obscure_ai": rec["required_before_obscure_ai"],
        "bounded_claim_candidate": rec["bounded_claim_candidate"],
        "source_record_id": rec["source_record_id"],
        "source_signal_ids": rec["source_record_id"],
        "source_signal_count": "1",
        "source_adjudication_path": source_path,
        "source_registry_csv": "live:" + API_ROOT,
        "rationale": rec["relevance_reason"] + " | " + rec["tier_rationale"],
        "low_confidence": rec["low_confidence"],
        "promotable": rec["promotable"],
        "next_action": rec["next_action"],
        "cve_id": rec["cve_id"],
        "severity": rec["severity"],
        "cvss": rec["cvss"],
        "affected_package": rec["affected_package"],
        "cwe_ids": rec["cwe_ids"],
        "published_at": rec["published_at"],
        "references": rec["references"],
        "tier_rationale": rec["tier_rationale"],
        "relevance_reason": rec["relevance_reason"],
        "matched_strong_terms": rec["matched_strong_terms"],
        "matched_weak_terms": rec["matched_weak_terms"],
    }
    return row


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true",
                    help="do not hit the network; read cached raw-*.json instead")
    ap.add_argument("--per-query", type=int, default=10,
                    help="advisories per keyword query (max 100; keep small)")
    proj = "/srv/tyche/projects/limen-ai-edge-case-atlas"
    run_date = dt.date.today().isoformat()
    default_out = os.path.join(proj, "results", "review-candidates",
                               f"ingest-{SOURCE_KEY}-{run_date}")
    ap.add_argument("--out-dir", default=default_out)
    ap.add_argument("--cache-dir", default=None,
                    help="raw-response cache (default: <out-dir>/raw-cache)")
    args = ap.parse_args()

    out_dir = args.out_dir
    cache_dir = args.cache_dir or os.path.join(out_dir, "raw-cache")
    os.makedirs(out_dir, exist_ok=True)

    mode = "DRY-RUN (no network; cached pages only)" if args.dry_run else "LIVE"
    print(f"[ingest-ghsa] mode={mode} out={out_dir}", file=sys.stderr)

    if args.dry_run:
        advisories, fetch_notes = fetch_cached(cache_dir)
    else:
        advisories, fetch_notes = fetch_live(args.per_query, cache_dir)

    kept_rows: list[dict] = []
    kept_records: list[dict] = []
    low_conf_rows: list[dict] = []
    source_path = f"{mode}:{API_ROOT}"

    for adv in advisories:
        rel = relevance(adv)
        if rel["keep"]:
            rec = map_record(adv, rel, run_date)
            kept_records.append({
                "case_id": rec["case_id"],
                "title": rec["title"],
                "summary": rec["summary"],
                "authority": rec["authority"],
                "source_url": rec["source_url"],
                "proposed_evidence_tier": rec["proposed_evidence_tier"],
                "claim_ceiling": rec["claim_ceiling"],
                "proposed_limen_categories": rec["proposed_limen_categories"].split("; "),
                "bounded_claim_candidate": rec["bounded_claim_candidate"],
                "source_record_id": rec["source_record_id"],
                "cve_id": rec["cve_id"],
                "severity": rec["severity"],
                "low_confidence": False,
                "promotable": rec["promotable"],
                "relevance_reason": rec["relevance_reason"],
            })
            kept_rows.append(to_tsv_row(rec, source_path))
        else:
            low_conf_rows.append({
                "ghsa_id": adv.get("ghsa_id", ""),
                "cve_id": adv.get("cve_id", "") or "",
                "summary": (adv.get("summary") or "").strip(),
                "source_url": adv.get("html_url", ""),
                "exclusion_reason": rel["reason"],
                "matched_strong_terms": "; ".join(rel["strong"]),
                "matched_weak_terms": "; ".join(rel["weak"]),
                "low_confidence": "yes",
            })

    # ---- write TSV (extraction-draft compatible) ----
    tsv_path = os.path.join(out_dir, f"ingest-{SOURCE_KEY}-{run_date}.tsv")
    with open(tsv_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=TSV_COLUMNS, delimiter="\t",
                           extrasaction="ignore")
        w.writeheader()
        for r in kept_rows:
            w.writerow(r)

    # ---- write JSONL (canonical candidate fields) ----
    jsonl_path = os.path.join(out_dir, f"ingest-{SOURCE_KEY}-{run_date}.candidates.jsonl")
    with open(jsonl_path, "w", encoding="utf-8") as fh:
        for rec in kept_records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # ---- write low-confidence exclusions ----
    low_path = os.path.join(out_dir, f"low-confidence-excluded-{run_date}.tsv")
    low_cols = ["ghsa_id", "cve_id", "summary", "source_url", "exclusion_reason",
                "matched_strong_terms", "matched_weak_terms", "low_confidence"]
    with open(low_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=low_cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for r in low_conf_rows:
            w.writerow(r)

    # ---- run manifest ----
    manifest = {
        "lane": "ingest-ghsa-ai",
        "source": "GitHub Security Advisories (GHSA) REST API",
        "api_root": API_ROOT,
        "mode": mode,
        "run_date": run_date,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "query_strategy": "structured affects=<ai-package> filter (free-text query is unsupported by the endpoint)",
        "ai_packages_queried": AI_PACKAGES,
        "per_query": args.per_query,
        "advisories_pulled_distinct": len(advisories),
        "candidates_kept": len(kept_rows),
        "low_confidence_excluded": len(low_conf_rows),
        "promoted_to_reviewed_core": 0,
        "cases_json_touched": False,
        "fetch_notes": fetch_notes,
        "outputs": {
            "tsv": tsv_path,
            "candidates_jsonl": jsonl_path,
            "low_confidence_tsv": low_path,
        },
    }
    man_path = os.path.join(out_dir, "run-manifest.json")
    with open(man_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)

    print(json.dumps({
        "mode": mode,
        "advisories_pulled_distinct": len(advisories),
        "candidates_kept": len(kept_rows),
        "low_confidence_excluded": len(low_conf_rows),
        "out_dir": out_dir,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
