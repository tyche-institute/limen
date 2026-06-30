#!/usr/bin/env python3
"""
LIMEN edge-case ingestion lane: NVD CVE 2.0 API, AI/ML-filtered.
================================================================================

WHY THIS LANE (second dense edge-case lane, sibling to ingest_ghsa_ai.py)
------------------------------------------------------------------------
The GHSA lane (ingest_ghsa_ai.py) is high precision but narrow: it is driven by
the GitHub `affects=<package>` filter, so it only sees vulnerabilities whose
*affected component is a package GitHub indexes* (PyPI/npm/etc.). It misses:
  - AI/ML systems that are not a packaged library (model-serving appliances,
    vendor cloud products, ML platforms, hardware/firmware AI accelerators);
  - CVEs published by non-GitHub CNAs that never get a GHSA;
  - the large body of "prompt injection" / "LLM" / "machine learning" CVEs that
    name an AI system in the description but whose CPE is a broader product.

The NVD CVE 2.0 API is the authoritative US-government feed of *all* CVEs and is
fully reachable headless with no auth (the unauthenticated limit, 5 req / 30 s,
is plenty for a small weekly pull). It exposes two precise, documented filters:
  1. keywordSearch (+ keywordExactMatch) — exact-phrase match over the CVE
     description: the high-precision "strong AI term" strategy.
  2. virtualMatchString=cpe:2.3:a:<vendor>:<product> — vendor/product CPE match:
     the high-precision "this CVE's affected product IS an AI system" strategy.
This is strictly BROADER than GHSA's package-affects approach (per the task), and
the two lanes overlap only on the subset of AI CVEs that also got a GHSA — which
this lane explicitly de-duplicates against by CVE id.

WHY NOT AIID
------------
The AI Incident Database is NOT tractable headless: its GraphQL endpoint is
locked to its own browser client. NVD is the tractable, no-auth, dense,
genuine-edge-case alternative.

WHAT THIS SCRIPT DOES
---------------------
1. Pulls a SMALL sample from the live NVD CVE 2.0 API. Two query families:
     a. exact-phrase keyword queries for a curated AI/agentic vocabulary;
     b. CPE virtualMatchString queries for a curated list of AI vendor:product
        pairs (vllm, langchain, huggingface, ...).
   No auth required. With `--dry-run` (or no network) it re-maps cached raw
   pages under <out-dir>/raw-cache/ and clearly marks the run as a dry run.
2. AI-relevance filter (transparent, conservative): a STRONG AI term in the
   description, OR the CVE's CPE vendor/product is on the curated AI allow-list,
   keeps the record. A single weak prose token with no AI CPE -> low-confidence,
   excluded. (Same discipline as the GHSA lane: a security CWE is NEVER treated
   as an AI signal — every CVE has one.)
3. De-duplicates by CVE id against (a) existing reviewed-core security TSVs and
   (b) the most recent GHSA lane run, so the same CVE is not re-proposed.
4. Maps each kept CVE to the LIMEN candidate schema (title, summary, authority,
   source_url, proposed evidence_tier, claim_ceiling + the full 25-col
   extraction-draft TSV the project's human-review pipeline consumes, plus
   appended NVD-native provenance columns).
5. Writes candidates to a NEW staging dir under
   results/review-candidates/ingest-nvd-<date>/ as a TSV, a JSONL, a
   low-confidence exclusions file, a duplicates file, and a run-manifest.json.
   NOTHING is promoted; cases.json is NOT touched; reviewed-core is NOT written.

ANTI-FABRICATION
----------------
- Every emitted field traces to a real NVD CVE field (id, description, CWE, CVSS,
  CPE, references, published date, vulnStatus, sourceIdentifier). No invented
  numbers, quotes, dates, or URLs.
- `year` comes from the CVE id / published date; if absent it is left blank.
- `proposed_evidence_tier` is conservative: a CVE with a CWE AND a reference
  tagged Patch/Exploit (a corroborated technical finding) is
  `T4_reproducible_technical_finding`; otherwise `T1_single_public_source`.
  The lane NEVER claims T3 authoritative-finding status from a CVE alone.
- Records matching AI vocabulary only weakly (single prose token, no AI CPE) go
  to the low-confidence file with low_confidence=yes and are NOT promotable.

USAGE
-----
  python3 ingest_nvd_ai.py                  # live pull, small sample
  python3 ingest_nvd_ai.py --dry-run        # no network; re-map cached pages
  python3 ingest_nvd_ai.py --per-query 5    # tune sample size per query
  python3 ingest_nvd_ai.py --max-queries 6  # cap number of queries this run

The script is read-only against the network and write-only into a fresh dated
staging dir; it never edits existing LIMEN artifacts.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import glob
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

SOURCE_KEY = "nvd"
SOURCE_AUTHORITY = (
    "U.S. National Vulnerability Database (NVD), NIST "
    "(services.nvd.nist.gov, CVE 2.0 API); CVE records issued by CVE "
    "Numbering Authorities and enriched by NIST/NVD analysts"
)
API_ROOT = "https://services.nvd.nist.gov/rest/json/cves/2.0"
USER_AGENT = "tyche-limen-nvd-ingest/0.1 (+research; contact anton.sokolov@tyche.institute)"

PROJ = "/srv/tyche/projects/limen-ai-edge-case-atlas"

# --- query strategy ---------------------------------------------------------
# A) STRONG AI/agentic terms, run as EXACT-PHRASE keyword queries
#    (keywordExactMatch). An exact match of one of these phrases in the CVE
#    description is a high-precision AI signal.
STRONG_KEYWORDS = [
    "prompt injection",
    "large language model",
    "MCP server",
    "model context protocol",
    "AI agent",
    "LLM agent",
    "agentic",
    "machine learning model",
    "jailbreak",
    "retrieval augmented generation",
    "vector database",
    "inference server",
]

# B) AI vendor:product CPE pairs, run as virtualMatchString queries. The CVE's
#    affected product IS an AI system. High precision; broader than GHSA's
#    package-affects (covers products with no GitHub package).
AI_CPE_VENDOR_PRODUCT = [
    "vllm:vllm",
    "langchain:langchain",
    "langchain:langchain_core",
    "huggingface:transformers",
    "ollama:ollama",
    "ggml:llama.cpp",
    "lunary:lunary",
    "mintplexlabs:anythingllm",
    "pytorch:pytorch",
    "ray_project:ray",
    "mlflow:mlflow",
    "gradio_project:gradio",
    "h2o:h2o",
    "berriai:litellm",
    "comfyanonymous:comfyui",
]

# AI vendor / product tokens used to recognise an AI CPE when scanning a record's
# CPE list (lowercased substring match against vendor or product). Kept narrow to
# avoid false positives.
AI_CPE_TOKENS = {
    "vllm", "langchain", "transformers", "huggingface", "ollama", "llama.cpp",
    "llama_cpp", "lunary", "anythingllm", "litellm", "mlflow", "gradio",
    "comfyui", "ray", "pytorch", "h2o", "tensorflow", "onnx", "triton",
    "llamaindex", "llama_index", "chromadb", "qdrant", "weaviate", "haystack",
    "autogen", "crewai", "dspy", "semantic_kernel", "langsmith", "langflow",
    "open-webui", "open_webui", "localai", "text-generation-inference",
    "stable-diffusion", "stable_diffusion", "deepspeed", "fastchat",
}

# Strong AI vocabulary recognised in description prose (used to keep keyword-hit
# records and to flag categories). Mirror of STRONG_KEYWORDS plus close variants.
STRONG_PROSE_TERMS = [
    "prompt injection", "prompt-injection", "large language model", "llm",
    "mcp server", "model context protocol", "ai agent", "llm agent", "agentic",
    "machine learning model", "jailbreak", "retrieval augmented generation",
    "retrieval-augmented generation", "rag pipeline", "vector database",
    "vector store", "inference server", "model serving", "neural network",
    "generative ai", "genai", "chatbot", "embeddings model",
]
# Weak prose tokens: only trustworthy WITH an AI CPE; alone -> low confidence.
WEAK_PROSE_TERMS = [
    "ai", "ml", "model", "inference", "embedding", "transformer", "gpt",
    "openai", "anthropic", "generative", "neural",
]

# Map CWE -> LIMEN category (NVD weaknesses carry CWE-### strings). Same mapping
# discipline as the GHSA lane; only explicit signals, no semantic guessing.
CWE_TO_LIMEN = {
    "CWE-306": "agentic_control_failure",
    "CWE-862": "agentic_control_failure",
    "CWE-863": "agentic_control_failure",
    "CWE-94": "security_risk",
    "CWE-95": "security_risk",
    "CWE-78": "security_risk",
    "CWE-77": "security_risk",
    "CWE-918": "security_risk",
    "CWE-22": "security_risk",
    "CWE-502": "security_risk",
    "CWE-1336": "security_risk",
    "CWE-74": "security_risk",
    "CWE-1426": "security_risk",  # improper validation of generative AI output
}

# NVD asks unauthenticated clients to sleep ~6 s between requests (5 req / 30 s).
REQUEST_SLEEP_S = 6.5


# ----------------------------------------------------------------------------
# Fetch layer
# ----------------------------------------------------------------------------

def _http_get_json(url: str, timeout: int = 30):
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _safe(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _build_queries(max_queries: int) -> list[tuple[str, str, dict]]:
    """Return a list of (kind, label, params) query specs, capped to max_queries.

    Interleaves keyword and CPE queries so a small cap still samples both.
    """
    kw = [("keyword", k, {"keywordSearch": k, "keywordExactMatch": ""})
          for k in STRONG_KEYWORDS]
    cpe = [("cpe", vp, {"virtualMatchString": f"cpe:2.3:a:{vp}"})
           for vp in AI_CPE_VENDOR_PRODUCT]
    interleaved: list[tuple[str, str, dict]] = []
    for a, b in zip(kw, cpe):
        interleaved.append(a)
        interleaved.append(b)
    interleaved.extend(kw[len(cpe):])
    interleaved.extend(cpe[len(kw):])
    if max_queries > 0:
        interleaved = interleaved[:max_queries]
    return interleaved


def fetch_live(per_query: int, max_queries: int, cache_dir: str
               ) -> tuple[list[dict], list[str]]:
    """Pull a small sample from the live NVD API. Returns (cve_records, notes)."""
    os.makedirs(cache_dir, exist_ok=True)
    seen: dict[str, dict] = {}
    notes: list[str] = []
    queries = _build_queries(max_queries)
    for i, (kind, label, base_params) in enumerate(queries):
        params = dict(base_params)
        params["resultsPerPage"] = str(max(1, min(per_query, 50)))
        params["startIndex"] = "0"
        # urlencode drops empty values awkwardly; keywordExactMatch is a flag
        flag = "keywordExactMatch" in params and params.pop("keywordExactMatch") == ""
        qs = urllib.parse.urlencode(params)
        if flag:
            qs += "&keywordExactMatch"
        url = API_ROOT + "?" + qs
        try:
            data = _http_get_json(url)
        except urllib.error.HTTPError as e:
            notes.append(f"{kind}:{label!r} HTTPError {e.code}: {e.reason}")
            time.sleep(REQUEST_SLEEP_S)
            continue
        except Exception as e:  # noqa: BLE001 - report any network failure plainly
            notes.append(f"{kind}:{label!r} fetch failed: {e!r}")
            time.sleep(REQUEST_SLEEP_S)
            continue
        vulns = data.get("vulnerabilities") if isinstance(data, dict) else None
        if not isinstance(vulns, list):
            notes.append(f"{kind}:{label!r} unexpected response shape")
            time.sleep(REQUEST_SLEEP_S)
            continue
        cache_name = f"raw-{kind}-{_safe(label)}.json"
        with open(os.path.join(cache_dir, cache_name), "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
        added = 0
        for item in vulns:
            cve = item.get("cve") or {}
            cid = cve.get("id")
            if cid and cid not in seen:
                cve["_query_kind"] = kind
                cve["_query_label"] = label
                seen[cid] = cve
                added += 1
        notes.append(f"{kind}:{label!r} -> {len(vulns)} returned "
                     f"(total {data.get('totalResults')}), {added} new distinct")
        if i < len(queries) - 1:
            time.sleep(REQUEST_SLEEP_S)
    return list(seen.values()), notes


def fetch_cached(cache_dir: str) -> tuple[list[dict], list[str]]:
    """Dry-run path: re-map cached raw-*.json pages from a prior live run."""
    seen: dict[str, dict] = {}
    notes: list[str] = []
    if not os.path.isdir(cache_dir):
        notes.append(f"no cache dir at {cache_dir}; dry run produced 0 records")
        return [], notes
    files = sorted(f for f in os.listdir(cache_dir)
                   if f.startswith("raw-") and f.endswith(".json"))
    for f in files:
        try:
            with open(os.path.join(cache_dir, f), encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception as e:  # noqa: BLE001
            notes.append(f"cache file {f} unreadable: {e!r}")
            continue
        vulns = data.get("vulnerabilities") if isinstance(data, dict) else []
        for item in vulns or []:
            cve = item.get("cve") or {}
            cid = cve.get("id")
            if cid and cid not in seen:
                seen[cid] = cve
        notes.append(f"cache {f} -> {len(vulns or [])} CVEs")
    return list(seen.values()), notes


# ----------------------------------------------------------------------------
# Dedup index (reviewed-core + GHSA lane)
# ----------------------------------------------------------------------------

def load_known_cves() -> tuple[set[str], list[str]]:
    """CVE ids already in reviewed-core security TSVs and the latest GHSA lane."""
    known: set[str] = set()
    sources: list[str] = []
    cve_re = re.compile(r"CVE-\d{4}-\d+", re.IGNORECASE)

    for path in sorted(glob.glob(os.path.join(
            PROJ, "results", "security", "limen-reviewed-core-*.tsv"))):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                hits = {m.group(0).upper() for m in cve_re.finditer(fh.read())}
        except Exception:  # noqa: BLE001
            continue
        if hits:
            known |= hits
            sources.append(f"{os.path.basename(path)} ({len(hits)} CVE ids)")

    # latest GHSA lane candidates (any dated dir)
    ghsa_dirs = sorted(glob.glob(os.path.join(
        PROJ, "results", "review-candidates", "ingest-ghsa-*")))
    for d in ghsa_dirs[-1:]:  # most recent only
        for jl in glob.glob(os.path.join(d, "*.candidates.jsonl")):
            n = 0
            try:
                for line in open(jl, encoding="utf-8"):
                    rec = json.loads(line)
                    cve = (rec.get("cve_id") or "").upper()
                    if cve:
                        known.add(cve)
                        n += 1
            except Exception:  # noqa: BLE001
                continue
            sources.append(f"{os.path.basename(d)}/{os.path.basename(jl)} ({n} CVE ids)")
    return known, sources


# ----------------------------------------------------------------------------
# Field extraction (NVD-native only)
# ----------------------------------------------------------------------------

def en_description(cve: dict) -> str:
    for d in cve.get("descriptions") or []:
        if d.get("lang") == "en":
            return (d.get("value") or "").strip()
    descs = cve.get("descriptions") or []
    return (descs[0].get("value") or "").strip() if descs else ""


def cwe_ids(cve: dict) -> list[str]:
    out: list[str] = []
    for w in cve.get("weaknesses") or []:
        for d in w.get("description") or []:
            v = (d.get("value") or "").strip()
            if v.startswith("CWE-") and v not in out:
                out.append(v)
    return out


def cvss_summary(cve: dict) -> str:
    metrics = cve.get("metrics") or {}
    for key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        arr = metrics.get(key) or []
        for m in arr:
            data = m.get("cvssData") or {}
            score = data.get("baseScore")
            if score is not None:
                sev = data.get("baseSeverity") or m.get("baseSeverity") or ""
                vec = data.get("vectorString") or ""
                return f"{score} ({key}, {sev}; {vec})".strip()
    return ""


def severity_word(cve: dict) -> str:
    metrics = cve.get("metrics") or {}
    for key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30"):
        for m in metrics.get(key) or []:
            sev = (m.get("cvssData") or {}).get("baseSeverity")
            if sev:
                return sev.lower()
    for m in metrics.get("cvssMetricV2") or []:
        sev = m.get("baseSeverity")
        if sev:
            return sev.lower()
    return "unknown"


def cpe_vendor_products(cve: dict) -> list[str]:
    """Distinct vendor:product strings from the CVE's CPE configurations."""
    out: set[str] = set()
    for cfg in cve.get("configurations") or []:
        for node in cfg.get("nodes") or []:
            for m in node.get("cpeMatch") or []:
                crit = m.get("criteria") or ""
                parts = crit.split(":")
                if len(parts) > 5 and parts[3] not in ("", "*") and parts[4] not in ("", "*"):
                    out.add(f"{parts[3]}:{parts[4]}")
    return sorted(out)


def ai_cpe_match(cve: dict) -> list[str]:
    """vendor:product pairs whose vendor or product token is on the AI allow-list."""
    hits: list[str] = []
    for vp in cpe_vendor_products(cve):
        vendor, _, product = vp.partition(":")
        blob = f"{vendor} {product}".lower()
        if any(tok in blob for tok in AI_CPE_TOKENS):
            hits.append(vp)
    return hits


def references(cve: dict) -> tuple[list[str], set[str]]:
    """Return (urls, tag-set). Tags drive the evidence tier (Patch/Exploit)."""
    urls: list[str] = []
    tags: set[str] = set()
    for r in cve.get("references") or []:
        u = r.get("url")
        if u:
            urls.append(u)
        for t in r.get("tags") or []:
            tags.add(t)
    return urls, tags


# ----------------------------------------------------------------------------
# Relevance + mapping
# ----------------------------------------------------------------------------

def relevance(cve: dict) -> dict:
    desc = en_description(cve).lower()
    strong = sorted({t for t in STRONG_PROSE_TERMS
                     if re.search(r"\b" + re.escape(t) + r"\b", desc)})
    weak = sorted({t for t in WEAK_PROSE_TERMS
                   if re.search(r"\b" + re.escape(t) + r"\b", desc)})
    ai_cpe = ai_cpe_match(cve)

    # Decision rules (transparent, conservative). A security CWE is NEVER an AI
    # signal. AI relevance comes only from strong AI vocabulary or an AI CPE.
    if strong:
        return {"keep": True, "low_confidence": False, "strong": strong,
                "weak": weak, "ai_cpe": ai_cpe,
                "reason": f"matched strong AI term(s) in description: {', '.join(strong)}"}
    if ai_cpe:
        return {"keep": True, "low_confidence": False, "strong": strong,
                "weak": weak, "ai_cpe": ai_cpe,
                "reason": f"affected product is an AI system (CPE matched: {', '.join(ai_cpe)})"}
    if weak:
        return {"keep": False, "low_confidence": True, "strong": strong,
                "weak": weak, "ai_cpe": ai_cpe,
                "reason": f"only weak AI token(s) in prose ({', '.join(weak)}) and no AI "
                          "CPE; the affected product is not an AI system "
                          "(likely an incidental mention, not an AI edge case)"}
    return {"keep": False, "low_confidence": True, "strong": strong, "weak": weak,
            "ai_cpe": ai_cpe, "reason": "no AI/agentic vocabulary or AI CPE matched"}


def propose_tier(cve: dict) -> tuple[str, str]:
    cwe = bool(cwe_ids(cve))
    _, tags = references(cve)
    corroborated = bool(tags & {"Patch", "Exploit", "Vendor Advisory", "Third Party Advisory"})
    if cwe and corroborated:
        return ("T4_reproducible_technical_finding",
                "CVE carries a CWE plus a reference tagged Patch/Exploit/Advisory "
                "(technical finding is corroborated by the NVD record)")
    return ("T1_single_public_source",
            "single public CVE record; not independently corroborated here")


def limen_categories(cve: dict, rel: dict) -> list[str]:
    cats: set[str] = set()
    for cid in cwe_ids(cve):
        if cid in CWE_TO_LIMEN:
            cats.add(CWE_TO_LIMEN[cid])
    if any(t in rel["strong"] for t in (
            "mcp server", "model context protocol", "agentic", "ai agent",
            "llm agent")):
        cats.add("agentic_control_failure")
    if "prompt injection" in rel["strong"] or "prompt-injection" in rel["strong"]:
        cats.add("security_risk")
    if not cats:
        cats.add("security_risk")  # every CVE is at minimum a security signal
    cats.add("software_supply_chain_surface")
    return sorted(cats)


def trim(text: str, limit: int = 320) -> str:
    text = re.sub(r"\s+", " ", (text or "").strip())
    return (text[:limit].rstrip() + "...") if len(text) > limit else text


def map_record(cve: dict, rel: dict, run_date: str) -> dict:
    cid = cve.get("id") or "CVE-UNKNOWN"
    tier, tier_reason = propose_tier(cve)
    cats = limen_categories(cve, rel)
    desc = en_description(cve)
    vps = cpe_vendor_products(cve)
    primary_product = (rel["ai_cpe"][0] if rel["ai_cpe"] else (vps[0] if vps else ""))
    published = cve.get("published") or ""
    year = ""
    m = re.match(r"CVE-(\d{4})-", cid)
    if m:
        year = m.group(1)
    elif published[:4].isdigit():
        year = published[:4]
    sev = severity_word(cve)
    cvss = cvss_summary(cve)
    cwes = cwe_ids(cve)
    ref_urls, ref_tags = references(cve)
    status = cve.get("vulnStatus") or ""

    title = trim(desc, 160) if desc else cid

    summary = (
        f"NVD CVE record {cid}: {trim(desc, 360)} "
        + (f"Affected product (CPE): {primary_product}. " if primary_product else "")
        + (f"Severity: {sev}" + (f"; CVSS {cvss}" if cvss else "") + ". ")
        + (f"CWE: {', '.join(cwes)}. " if cwes else "")
        + (f"NVD status: {status}. " if status else "")
        + "This record captures a public CVE describing a concrete technical "
        + "issue affecting an AI/ML system; it is a candidate edge case for "
        + "human review, not a promoted reviewed-core case."
    )

    bounded_claim = (
        f"An NVD CVE record {cid} exists at the cited URL describing a "
        f"{sev}-severity issue"
        + (f" affecting {primary_product}" if primary_product else "")
        + "."
    )

    claim_ceiling = (
        "Advisory-surface finding only: confirms a public NVD CVE record exists "
        "describing the stated technical issue in the named AI/ML component. "
        "Records the CVE's own claims and metadata; does not independently "
        "verify exploitation in the wild, real-world harm, prevalence, or vendor "
        "culpability beyond the CVE text."
    )
    forbidden = (
        "Do not infer real-world exploitation, realized harm, victim count, "
        "prevalence across deployments, legal liability, or that the issue is "
        "unpatched/ongoing beyond what the CVE record and its references state. "
        "Do not upgrade tier on a single CVE record alone."
    )

    return {
        # ---- canonical candidate fields ----
        "case_id": f"LIMEN-DRAFT-NVD-{cid.replace('CVE-', '')}",
        "title": title,
        "summary": summary,
        "authority": SOURCE_AUTHORITY,
        "source_url": f"https://nvd.nist.gov/vuln/detail/{cid}",
        "proposed_evidence_tier": tier,
        "claim_ceiling": claim_ceiling,
        # ---- extra LIMEN extraction-draft fields ----
        "draft_status": "draft_for_human_review",
        "jurisdiction_country": "global",  # software CVE; no single jurisdiction
        "year": year,
        "accession_snapshot_date": run_date,
        "proposed_limen_categories": "; ".join(cats),
        "forbidden_overread": forbidden,
        "required_before_reviewed_core": (
            "Human review to confirm AI/agentic relevance and to decide whether "
            "this CVE is a distinct LIMEN edge case (not a duplicate of an "
            "existing reviewed-core entry); optionally corroborate with a second "
            "independent source (vendor advisory, GHSA, or media report)."
        ),
        "required_before_obscure_ai": (
            "Not ObscureAI material unless promoted to a sourced reviewed-core "
            "case with confirmed AI relevance and bounded behaviour claim."
        ),
        "bounded_claim_candidate": bounded_claim,
        "source_record_id": cid,
        "cve_id": cid,
        "severity": sev,
        "cvss": cvss,
        "affected_product": primary_product,
        "all_cpe_vendor_products": "; ".join(vps[:8]),
        "cwe_ids": "; ".join(cwes),
        "published_at": published,
        "vuln_status": status,
        "source_identifier": cve.get("sourceIdentifier") or "",
        "reference_tags": "; ".join(sorted(ref_tags)),
        "references": " | ".join(ref_urls[:6]),
        "query_origin": f"{cve.get('_query_kind','')}:{cve.get('_query_label','')}",
        "tier_rationale": tier_reason,
        "relevance_reason": rel["reason"],
        "matched_strong_terms": "; ".join(rel["strong"]),
        "matched_weak_terms": "; ".join(rel["weak"]),
        "matched_ai_cpe": "; ".join(rel["ai_cpe"]),
        "low_confidence": "no",
        "promotable": "yes_as_candidate_edge_case_draft",
        "next_action": (
            "Human accept/reject as an AI edge-case candidate; confirm AI "
            "relevance + non-duplication before any reviewed-core or cases.json "
            "addition."
        ),
    }


# 25-column canonical order (identical to extraction-drafts schema), with
# NVD-native provenance columns appended (additive; first 25 stay compatible).
TSV_COLUMNS = [
    "case_id", "draft_status", "title", "summary", "authority",
    "jurisdiction_country", "year", "accession_snapshot_date",
    "proposed_evidence_tier", "primary_source_url", "claim_ceiling",
    "proposed_limen_categories", "forbidden_overread",
    "required_before_reviewed_core", "required_before_obscure_ai",
    "bounded_claim_candidate", "source_record_id", "source_signal_ids",
    "source_signal_count", "source_adjudication_path", "source_registry_csv",
    "rationale", "low_confidence", "promotable", "next_action",
    # appended NVD-native provenance columns
    "cve_id", "severity", "cvss", "affected_product", "all_cpe_vendor_products",
    "cwe_ids", "published_at", "vuln_status", "source_identifier",
    "reference_tags", "references", "query_origin", "tier_rationale",
    "relevance_reason", "matched_strong_terms", "matched_weak_terms",
    "matched_ai_cpe",
]


def to_tsv_row(rec: dict, source_path: str) -> dict:
    return {
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
        "affected_product": rec["affected_product"],
        "all_cpe_vendor_products": rec["all_cpe_vendor_products"],
        "cwe_ids": rec["cwe_ids"],
        "published_at": rec["published_at"],
        "vuln_status": rec["vuln_status"],
        "source_identifier": rec["source_identifier"],
        "reference_tags": rec["reference_tags"],
        "references": rec["references"],
        "query_origin": rec["query_origin"],
        "tier_rationale": rec["tier_rationale"],
        "relevance_reason": rec["relevance_reason"],
        "matched_strong_terms": rec["matched_strong_terms"],
        "matched_weak_terms": rec["matched_weak_terms"],
        "matched_ai_cpe": rec["matched_ai_cpe"],
    }


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true",
                    help="do not hit the network; re-map cached raw-*.json")
    ap.add_argument("--per-query", type=int, default=10,
                    help="CVEs per query (max 50; keep small)")
    ap.add_argument("--max-queries", type=int, default=10,
                    help="cap number of queries this run (0 = all)")
    run_date = dt.date.today().isoformat()
    default_out = os.path.join(PROJ, "results", "review-candidates",
                               f"ingest-{SOURCE_KEY}-{run_date}")
    ap.add_argument("--out-dir", default=default_out)
    ap.add_argument("--cache-dir", default=None,
                    help="raw-response cache (default: <out-dir>/raw-cache)")
    args = ap.parse_args()

    out_dir = args.out_dir
    cache_dir = args.cache_dir or os.path.join(out_dir, "raw-cache")
    os.makedirs(out_dir, exist_ok=True)

    mode = "DRY-RUN (no network; cached pages only)" if args.dry_run else "LIVE"
    print(f"[ingest-nvd] mode={mode} out={out_dir}", file=sys.stderr)

    known_cves, dedup_sources = load_known_cves()
    print(f"[ingest-nvd] dedup index: {len(known_cves)} known CVE ids "
          f"from {len(dedup_sources)} sources", file=sys.stderr)

    if args.dry_run:
        cves, fetch_notes = fetch_cached(cache_dir)
    else:
        cves, fetch_notes = fetch_live(args.per_query, args.max_queries, cache_dir)

    kept_rows: list[dict] = []
    kept_records: list[dict] = []
    low_conf_rows: list[dict] = []
    dup_rows: list[dict] = []
    source_path = f"{mode}:{API_ROOT}"

    for cve in cves:
        cid = (cve.get("id") or "").upper()
        rel = relevance(cve)
        if not rel["keep"]:
            low_conf_rows.append({
                "cve_id": cid,
                "description": trim(en_description(cve), 240),
                "source_url": f"https://nvd.nist.gov/vuln/detail/{cid}",
                "exclusion_reason": rel["reason"],
                "matched_strong_terms": "; ".join(rel["strong"]),
                "matched_weak_terms": "; ".join(rel["weak"]),
                "matched_ai_cpe": "; ".join(rel["ai_cpe"]),
                "low_confidence": "yes",
            })
            continue
        if cid in known_cves:
            dup_rows.append({
                "cve_id": cid,
                "description": trim(en_description(cve), 240),
                "source_url": f"https://nvd.nist.gov/vuln/detail/{cid}",
                "dedup_reason": "CVE id already present in reviewed-core and/or the "
                                "latest GHSA lane; not re-proposed",
            })
            continue
        rec = map_record(cve, rel, run_date)
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
            "affected_product": rec["affected_product"],
            "low_confidence": False,
            "promotable": rec["promotable"],
            "relevance_reason": rec["relevance_reason"],
            "query_origin": rec["query_origin"],
        })
        kept_rows.append(to_tsv_row(rec, source_path))

    # ---- write TSV (extraction-draft compatible: first 25 cols identical) ----
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
    low_cols = ["cve_id", "description", "source_url", "exclusion_reason",
                "matched_strong_terms", "matched_weak_terms", "matched_ai_cpe",
                "low_confidence"]
    with open(low_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=low_cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for r in low_conf_rows:
            w.writerow(r)

    # ---- write duplicates (already in reviewed-core / GHSA lane) ----
    dup_path = os.path.join(out_dir, f"duplicates-excluded-{run_date}.tsv")
    dup_cols = ["cve_id", "description", "source_url", "dedup_reason"]
    with open(dup_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=dup_cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for r in dup_rows:
            w.writerow(r)

    # ---- run manifest ----
    manifest = {
        "lane": "ingest-nvd-ai",
        "source": "NVD CVE 2.0 API (services.nvd.nist.gov)",
        "api_root": API_ROOT,
        "mode": mode,
        "run_date": run_date,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "query_strategy": "exact-phrase keywordSearch (AI vocabulary) + "
                          "virtualMatchString CPE filter (AI vendor:product)",
        "strong_keywords": STRONG_KEYWORDS,
        "ai_cpe_vendor_product": AI_CPE_VENDOR_PRODUCT,
        "per_query": args.per_query,
        "max_queries": args.max_queries,
        "cves_pulled_distinct": len(cves),
        "candidates_kept": len(kept_rows),
        "low_confidence_excluded": len(low_conf_rows),
        "duplicates_excluded": len(dup_rows),
        "dedup_index_size": len(known_cves),
        "dedup_sources": dedup_sources,
        "promoted_to_reviewed_core": 0,
        "cases_json_touched": False,
        "fetch_notes": fetch_notes,
        "outputs": {
            "tsv": tsv_path,
            "candidates_jsonl": jsonl_path,
            "low_confidence_tsv": low_path,
            "duplicates_tsv": dup_path,
        },
    }
    man_path = os.path.join(out_dir, "run-manifest.json")
    with open(man_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)

    print(json.dumps({
        "mode": mode,
        "cves_pulled_distinct": len(cves),
        "candidates_kept": len(kept_rows),
        "low_confidence_excluded": len(low_conf_rows),
        "duplicates_excluded": len(dup_rows),
        "dedup_index_size": len(known_cves),
        "out_dir": out_dir,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
