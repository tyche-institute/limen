#!/usr/bin/env python3
"""Build token-free case-review recommendations from hardened case candidates.

This script is deliberately conservative: it does not call an LLM, does not
mine new sources, and does not promote rows into reviewed core. It turns the
current case-hardening rows into deterministic final-review recommendations
and a draft adjudication ledger for human acceptance.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
HARDENING_REVIEW = REVIEW_ROOT / "reviewed-core-case-hardening-review-v0.1.tsv"
FINAL_ADJUDICATION = REVIEW_ROOT / "reviewed-core-case-final-adjudication-v0.1.tsv"
OUT = REVIEW_ROOT / "reviewed-core-case-autoreview-v0.1.tsv"
DRAFT_FINAL = REVIEW_ROOT / "reviewed-core-case-final-adjudication-draft-v0.1.tsv"
STATUS = REVIEW_ROOT / "reviewed-core-case-autoreview-status.json"
SUMMARY = REVIEW_ROOT / "reviewed-core-case-autoreview-summary-v0.1.md"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "reviewed-core-case-autoreview.tsv"

CORE_JSONL_GLOB = "data/cases/*.jsonl"
CORE_TSV_GLOB = "results/security/limen-reviewed-core-web-verified*.tsv"

FIELDS = [
    "cluster_id",
    "source_host",
    "source_url",
    "hardening_verdict",
    "reviewed_core_candidate_status",
    "existing_final_decision",
    "existing_reviewed_core_action",
    "existing_obscure_ai_action",
    "autoreview_decision",
    "effective_decision",
    "reviewed_core_recommendation",
    "obscure_ai_recommendation",
    "confidence",
    "rule_ids",
    "matched_existing_case_ids",
    "matched_existing_source_urls",
    "paid_token_required",
    "human_acceptance_required",
    "proposed_case_title",
    "proposed_evidence_tier",
    "bounded_claim_candidate",
    "claim_ceiling",
    "forbidden_overread",
    "rationale",
    "next_action",
    "boundary",
]

DRAFT_FINAL_FIELDS = [
    "cluster_id",
    "source_host",
    "final_decision",
    "reviewed_core_action",
    "obscure_ai_action",
    "rationale",
]

OFFICIAL_HOST_SUFFIXES = (
    ".gov",
    ".gov.uk",
    ".gov.au",
    ".gov.il",
    ".gov.lk",
    ".gob.es",
    ".go.jp",
)

PRIMARY_OR_AUTHORITATIVE_MARKERS = (
    "official",
    "primary",
    "authoritative",
    "government",
    "regulator",
    "court",
    "security_advisory",
    "vendor_security",
)

WEAK_SOURCE_MARKERS = (
    "social",
    "linkedin",
    "allegation",
    "public first-person",
    "needs original source",
)

SCHOLARLY_ONLY_MARKERS = (
    "preprint",
    "scholarly",
    "secondary",
    "paper",
    "scientometric",
    "research_integrity",
)

ANNOUNCEMENT_ONLY_MARKERS = (
    "pilot",
    "sandbox",
    "announcement",
    "vendor-reported",
    "vendor_public",
    "press_release",
    "program",
    "launched",
    "launch",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def clean(value: str, limit: int = 1000) -> str:
    return re.sub(r"\s+", " ", value or "").strip().replace("\t", " ")[:limit].rstrip()


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def normalize_url(value: str) -> str:
    match = re.search(r"https?://[^\s;|]+", value or "")
    if not match:
        return ""
    raw = match.group(0).rstrip(".,)]}\"'")
    try:
        parsed = urlsplit(raw)
    except Exception:
        return clean(raw.lower().rstrip("/"), 500)
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = re.sub(r"/+", "/", parsed.path or "").rstrip("/")
    query = parsed.query
    if host in {"api.github.com", "github.com"} and "/security-advisories/" in path:
        query = ""
    if host == "arxiv.org" and path.startswith("/abs/"):
        query = ""
    scheme = "https" if parsed.scheme.lower() in {"http", "https"} else parsed.scheme.lower()
    return urlunsplit((scheme, host, path, query, ""))


def public_ids(value: str) -> set[str]:
    ids = set(re.findall(r"\bCVE-\d{4}-\d{4,8}\b", value or "", flags=re.I))
    ids.update(re.findall(r"\bGHSA-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}\b", value or "", flags=re.I))
    return {item.upper() for item in ids}


TITLE_STOPWORDS = {
    "about",
    "advisory",
    "allowed",
    "and",
    "candidate",
    "case",
    "claim",
    "could",
    "describes",
    "enabled",
    "existing",
    "for",
    "ghsa",
    "overly",
    "public",
    "review",
    "reviewed",
    "source",
    "states",
    "through",
    "using",
    "with",
}


def title_tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9][a-z0-9-]{2,}", (value or "").lower())
        if token not in TITLE_STOPWORDS
    }


def title_similarity(left: str, right: str) -> float:
    left_tokens = title_tokens(left)
    right_tokens = title_tokens(right)
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens | right_tokens)


def title_containment(left: str, right: str) -> float:
    left_tokens = title_tokens(left)
    right_tokens = title_tokens(right)
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / min(len(left_tokens), len(right_tokens))


def canonical_host(host: str) -> str:
    host = (host or "").strip().lower()
    return host[4:] if host.startswith("www.") else host


def is_official_host(host: str) -> bool:
    host = canonical_host(host)
    return host.endswith(OFFICIAL_HOST_SUFFIXES) or host in {
        "api.github.com",
        "github.com",
        "irs.gov",
        "crfm.stanford.edu",
        "sakana.ai",
    }


def load_existing_core_index(project_root: Path) -> dict[str, dict[str, list[dict[str, str]]]]:
    by_url: dict[str, list[dict[str, str]]] = {}
    by_id: dict[str, list[dict[str, str]]] = {}
    records: list[dict[str, str]] = []

    def add(record: dict[str, str]) -> None:
        records.append(record)
        url = normalize_url(record.get("source_url", ""))
        if url:
            by_url.setdefault(url, []).append(record)
        text = json.dumps(record, ensure_ascii=False)
        for public_id in public_ids(text):
            by_id.setdefault(public_id, []).append(record)

    for path in sorted(project_root.glob(CORE_TSV_GLOB)):
        for row in read_tsv(path):
            add(
                {
                    "case_id": row.get("case_id", ""),
                    "title": row.get("title", ""),
                    "source_url": row.get("primary_source_url", ""),
                    "source_path": str(path),
                }
            )

    for path in sorted(project_root.glob(CORE_JSONL_GLOB)):
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                except Exception:
                    continue
                urls = set(re.findall(r"https?://[^\s\"'<>]+", line))
                if data.get("source_url"):
                    urls.add(str(data.get("source_url")))
                for url in sorted(urls):
                    add(
                        {
                            "case_id": str(data.get("case_id") or data.get("candidate_id") or ""),
                            "title": str(data.get("title") or data.get("title_en_gloss") or ""),
                            "source_url": url,
                            "source_path": str(path),
                        }
                    )

    return {"by_url": by_url, "by_id": by_id, "records": {"_all": records}}


def existing_matches(row: dict[str, str], index: dict[str, dict[str, list[dict[str, str]]]]) -> list[dict[str, str]]:
    matches: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    url = normalize_url(row.get("source_url", ""))
    if url:
        for record in index["by_url"].get(url, []):
            key = (record.get("case_id", ""), normalize_url(record.get("source_url", "")))
            if key not in seen:
                matches.append(record)
                seen.add(key)
    row_text = json.dumps(row, ensure_ascii=False)
    for public_id in public_ids(row_text):
        for record in index["by_id"].get(public_id, []):
            key = (record.get("case_id", ""), normalize_url(record.get("source_url", "")))
            if key not in seen:
                matches.append(record)
                seen.add(key)
    proposed_title = row.get("proposed_case_title", "")
    for record in index.get("records", {}).get("_all", []):
        similarity = title_similarity(proposed_title, record.get("title", ""))
        containment = title_containment(proposed_title, record.get("title", ""))
        if similarity < 0.55 and containment < 0.75:
            continue
        overlap = title_tokens(proposed_title) & title_tokens(record.get("title", ""))
        if len(overlap) < 3:
            continue
        key = (record.get("case_id", ""), normalize_url(record.get("source_url", "")))
        if key not in seen:
            record = dict(record)
            record["match_type"] = "title_similarity"
            matches.append(record)
            seen.add(key)
    return matches


def final_index() -> dict[str, dict[str, str]]:
    return {row.get("cluster_id", ""): row for row in read_tsv(FINAL_ADJUDICATION) if row.get("cluster_id")}


def contains_any(text: str, markers: tuple[str, ...]) -> bool:
    low = text.lower()
    return any(marker.lower() in low for marker in markers)


def recommendation_from_decision(decision: str) -> tuple[str, str]:
    if decision == "auto_close_duplicate_existing_core":
        return "no_new_row_duplicate_existing_core", "no_new_obscure_ai_case"
    if decision.startswith("auto_hold"):
        return "no_new_row_hold", "no_new_obscure_ai_case"
    if decision == "token_free_promote_candidate_needs_human_acceptance":
        return "promote_candidate_after_human_acceptance", "candidate_after_reviewed_core_acceptance"
    return "needs_human_review", "needs_human_review"


def draft_final_decision(decision: str) -> str:
    mapping = {
        "auto_close_duplicate_existing_core": "duplicate_existing_core",
        "auto_hold_source_gap": "hold_source_gap",
        "auto_hold_social_or_allegation_needs_primary": "hold_source_only",
        "auto_hold_scholarly_or_preprint_source_only": "hold_source_only",
        "auto_hold_announcement_or_pilot_needs_corroboration": "hold_source_only",
        "auto_hold_not_ready": "hold_source_gap",
    }
    return mapping.get(decision, "needs_human_acceptance")


def review_row(row: dict[str, str], index: dict[str, dict[str, list[dict[str, str]]]], finals: dict[str, dict[str, str]]) -> dict[str, str]:
    cluster_id = row.get("cluster_id", "")
    host = canonical_host(row.get("source_host", ""))
    evidence = row.get("proposed_evidence_tier", "")
    text = " ".join(
        [
            row.get("source_host", ""),
            row.get("source_url", ""),
            evidence,
            row.get("proposed_limen_categories", ""),
            row.get("proposed_case_title", ""),
            row.get("bounded_claim_candidate", ""),
            row.get("claim_ceiling", ""),
            row.get("required_before_reviewed_core", ""),
            row.get("required_before_obscure_ai", ""),
            row.get("source_support_note", ""),
        ]
    )
    matches = existing_matches(row, index)
    rule_ids: list[str] = []
    confidence = "medium"
    decision = "needs_human_judgment"
    rationale = "No deterministic rule was strong enough for automatic closure or promotion recommendation."
    next_action = "human review bounded claim and source fit"

    if matches:
        rule_ids.append("duplicate_by_exact_source_url_or_public_id")
        decision = "auto_close_duplicate_existing_core"
        confidence = "high"
        rationale = "The source URL or public identifier already appears in reviewed-core data."
        next_action = "do not create a new reviewed-core or ObscureAI row"
    elif row.get("official_source_verified") != "yes" or row.get("reviewed_core_candidate_status") != "ready_for_human_acceptance_not_promoted":
        rule_ids.append("not_source_verified_or_not_ready")
        decision = "auto_hold_source_gap"
        confidence = "high"
        rationale = "The hardened row is not source-verified and ready for acceptance."
        next_action = "retry source hardening or keep held; no paid token is required for this closure"
    elif contains_any(text, WEAK_SOURCE_MARKERS) or host in {"linkedin.com", "x.com", "twitter.com"}:
        rule_ids.append("weak_or_allegation_source")
        decision = "auto_hold_social_or_allegation_needs_primary"
        confidence = "high"
        rationale = "The row is grounded in a social/allegation source and needs primary-source corroboration."
        next_action = "find primary source or keep held"
    elif contains_any(text, SCHOLARLY_ONLY_MARKERS) and not contains_any(text, ("official", "security_advisory")):
        rule_ids.append("scholarly_or_preprint_source_only")
        decision = "auto_hold_scholarly_or_preprint_source_only"
        confidence = "high"
        rationale = "The row is useful as research/source surface, but not a bounded real-world case by itself."
        next_action = "keep as source-surface unless a bounded institutional case is verified"
    elif contains_any(text, ANNOUNCEMENT_ONLY_MARKERS) and not contains_any(text, ("disabled", "advisory", "judgment", "fined")):
        rule_ids.append("announcement_or_pilot_not_case")
        decision = "auto_hold_announcement_or_pilot_needs_corroboration"
        confidence = "medium"
        rationale = "The row appears to be an announcement, pilot, or program surface rather than verified case outcome."
        next_action = "require implementation/outcome/source corroboration before reviewed-core promotion"
    elif contains_any(text, PRIMARY_OR_AUTHORITATIVE_MARKERS) or is_official_host(host):
        rule_ids.append("source_verified_authoritative_with_claim_ceiling")
        decision = "token_free_promote_candidate_needs_human_acceptance"
        confidence = "medium"
        rationale = "The row is source-verified and has bounded claim text; deterministic review can queue it for human acceptance without LLM tokens."
        next_action = "human accept/reject bounded claim; then append reviewed-core row if accepted"
    else:
        rule_ids.append("unclassified_needs_human")

    reviewed_core_rec, obscure_rec = recommendation_from_decision(decision)
    existing_final = finals.get(cluster_id, {})
    effective_decision = existing_final.get("final_decision") or draft_final_decision(decision)

    if existing_final:
        rule_ids.append("already_final_adjudicated")
        next_action = "none; final adjudication ledger already covers this row"

    return {
        "cluster_id": cluster_id,
        "source_host": row.get("source_host", ""),
        "source_url": row.get("source_url", ""),
        "hardening_verdict": row.get("hardening_verdict", ""),
        "reviewed_core_candidate_status": row.get("reviewed_core_candidate_status", ""),
        "existing_final_decision": existing_final.get("final_decision", ""),
        "existing_reviewed_core_action": existing_final.get("reviewed_core_action", ""),
        "existing_obscure_ai_action": existing_final.get("obscure_ai_action", ""),
        "autoreview_decision": decision,
        "effective_decision": effective_decision,
        "reviewed_core_recommendation": reviewed_core_rec,
        "obscure_ai_recommendation": obscure_rec,
        "confidence": confidence,
        "rule_ids": ";".join(rule_ids),
        "matched_existing_case_ids": ";".join(sorted({m.get("case_id", "") for m in matches if m.get("case_id")})),
        "matched_existing_source_urls": ";".join(sorted({normalize_url(m.get("source_url", "")) for m in matches if normalize_url(m.get("source_url", ""))})),
        "paid_token_required": "no",
        "human_acceptance_required": "yes" if decision in {"token_free_promote_candidate_needs_human_acceptance", "needs_human_judgment"} and not existing_final else "no",
        "proposed_case_title": clean(row.get("proposed_case_title", ""), 360),
        "proposed_evidence_tier": row.get("proposed_evidence_tier", ""),
        "bounded_claim_candidate": clean(row.get("bounded_claim_candidate", ""), 900),
        "claim_ceiling": clean(row.get("claim_ceiling", ""), 900),
        "forbidden_overread": clean(row.get("forbidden_overread", ""), 900),
        "rationale": clean(rationale, 700),
        "next_action": clean(next_action, 400),
        "boundary": "Token-free autoreview only; no reviewed-core or ObscureAI promotion occurred.",
    }


def build(project_root: Path) -> dict[str, object]:
    rows = read_tsv(HARDENING_REVIEW)
    finals = final_index()
    index = load_existing_core_index(project_root)
    reviewed = [review_row(row, index, finals) for row in rows]
    write_tsv(OUT, reviewed, FIELDS)
    write_tsv(DASHBOARD_COPY, reviewed, FIELDS)

    draft_rows = []
    for row in reviewed:
        final_decision = draft_final_decision(row["autoreview_decision"])
        reviewed_action, obscure_action = recommendation_from_decision(row["autoreview_decision"])
        draft_rows.append(
            {
                "cluster_id": row["cluster_id"],
                "source_host": row["source_host"],
                "final_decision": row["existing_final_decision"] or final_decision,
                "reviewed_core_action": row["existing_reviewed_core_action"] or reviewed_action,
                "obscure_ai_action": row["existing_obscure_ai_action"] or obscure_action,
                "rationale": row["rationale"],
            }
        )
    write_tsv(DRAFT_FINAL, draft_rows, DRAFT_FINAL_FIELDS)

    decision_counts = Counter(row["autoreview_decision"] for row in reviewed)
    effective_counts = Counter(row["effective_decision"] for row in reviewed)
    non_final = [row for row in reviewed if not row["existing_final_decision"]]
    status = {
        "generated_at_utc": utc_now(),
        "input": str(HARDENING_REVIEW),
        "output": str(OUT),
        "dashboard_copy": str(DASHBOARD_COPY),
        "draft_final_adjudication": str(DRAFT_FINAL),
        "rows": len(reviewed),
        "already_final_adjudicated_rows": sum(1 for row in reviewed if row["existing_final_decision"]),
        "rows_without_final_adjudication": len(non_final),
        "paid_token_required_rows": sum(1 for row in non_final if row["paid_token_required"] == "yes"),
        "human_acceptance_required_rows": sum(1 for row in non_final if row["human_acceptance_required"] == "yes"),
        "token_free_auto_close_rows": sum(
            1
            for row in non_final
            if row["autoreview_decision"].startswith("auto_hold")
            or row["autoreview_decision"] == "auto_close_duplicate_existing_core"
        ),
        "token_free_promotion_candidate_rows": sum(
            1
            for row in non_final
            if row["autoreview_decision"] == "token_free_promote_candidate_needs_human_acceptance"
        ),
        "autoreview_decision_counts": dict(sorted(decision_counts.items())),
        "effective_decision_counts": dict(sorted(effective_counts.items())),
        "boundary": "Deterministic no-LLM autoreview; draft recommendations only unless copied into final adjudication by a human-controlled process.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY.write_text(
        "\n".join(
            [
                "# LIMEN token-free case autoreview",
                "",
                f"- Generated: `{status['generated_at_utc']}`",
                f"- Rows: `{status['rows']}`",
                f"- Already final-adjudicated: `{status['already_final_adjudicated_rows']}`",
                f"- Rows without final adjudication: `{status['rows_without_final_adjudication']}`",
                f"- Paid-token-required rows: `{status['paid_token_required_rows']}`",
                f"- Human-acceptance rows: `{status['human_acceptance_required_rows']}`",
                f"- Token-free auto-close rows: `{status['token_free_auto_close_rows']}`",
                f"- Token-free promotion-candidate rows: `{status['token_free_promotion_candidate_rows']}`",
                f"- Decisions: `{json.dumps(status['autoreview_decision_counts'], sort_keys=True)}`",
                "",
                str(status["boundary"]),
                "",
            ]
        ),
        encoding="utf-8",
    )
    return status


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(PROJECT_ROOT))
    args = parser.parse_args()
    print(json.dumps(build(Path(args.project_root)), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
