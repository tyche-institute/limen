#!/usr/bin/env python3
"""Build a conservative case-hardening review from promotion-packet clusters.

This stage may verify official source text and draft a bounded case claim, but
it does not append to reviewed core or ObscureAI. Human acceptance remains the
promotion boundary for legal/source-sensitive clusters.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

from lxml import html


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
QUEUE = REVIEW_ROOT / "reviewed-core-case-hardening-queue-v0.1.tsv"
EXTRACTION_RESULTS = REVIEW_ROOT / "reviewed-core-case-extraction-results-v0.1.tsv"
OUT = REVIEW_ROOT / "reviewed-core-case-hardening-review-v0.1.tsv"
STATUS = REVIEW_ROOT / "reviewed-core-case-hardening-review-status.json"
SUMMARY = REVIEW_ROOT / "reviewed-core-case-hardening-review-summary-v0.1.md"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "reviewed-core-case-hardening-review.tsv"
FINAL_ADJUDICATION = REVIEW_ROOT / "reviewed-core-case-final-adjudication-v0.1.tsv"

FIELDS = [
    "cluster_id",
    "hardening_verdict",
    "reviewed_core_candidate_status",
    "obscure_ai_candidate_status",
    "official_source_verified",
    "source_url",
    "source_host",
    "source_language",
    "source_record_date",
    "jurisdiction",
    "official_title",
    "proposed_case_title",
    "proposed_evidence_tier",
    "proposed_limen_categories",
    "bounded_claim_candidate",
    "claim_ceiling",
    "forbidden_overread",
    "required_before_reviewed_core",
    "required_before_obscure_ai",
    "source_support_note",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def clean(value: str, limit: int = 900) -> str:
    return re.sub(r"\s+", " ", value or "").strip().replace("\t", " ")[:limit].rstrip()


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def fetch_plain_text(url: str) -> tuple[bool, str, str]:
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0 LIMEN verifier"})
        with urlopen(req, timeout=45) as response:
            raw = response.read()
            final_url = response.geturl()
    except Exception as exc:
        return False, "", f"fetch failed: {exc}"

    for encoding in ("utf-8", "latin-1", "cp1252"):
        try:
            markup = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        markup = raw.decode("utf-8", errors="replace")

    try:
        doc = html.fromstring(markup)
        text = " ".join(doc.text_content().split())
    except Exception:
        text = " ".join(markup.split())
    return True, text, final_url


def extraction_index() -> dict[str, dict[str, str]]:
    return {
        row.get("source_cluster_key", ""): row
        for row in read_tsv(EXTRACTION_RESULTS)
        if row.get("source_cluster_key")
    }


def source_supports_candidate(text: str, candidate: dict[str, str]) -> bool:
    low = text.lower()
    title = candidate.get("proposed_case_title", "").lower()
    claim = candidate.get("bounded_claim_candidate", "").lower()
    tokens = [
        token
        for token in re.findall(r"[a-z][a-z0-9-]{4,}", f"{title} {claim}")
        if token
        not in {
            "stated",
            "source",
            "public",
            "claim",
            "candidate",
            "because",
            "reviewed",
            "process",
            "official",
            "record",
        }
    ]
    if not tokens:
        return len(text) > 500
    hits = sum(1 for token in set(tokens[:24]) if token in low)
    return hits >= min(3, max(1, len(set(tokens[:24])) // 4))


def harden_cluster(row: dict[str, str], extractions: dict[str, dict[str, str]]) -> dict[str, str]:
    url = row.get("source_url_or_locator", "")
    ok, text, note = fetch_plain_text(url)
    low = text.lower()

    is_t323 = (
        "corteconstitucional.gov.co" in url
        and "t-323-24" in url.lower()
        and "sentencia t-323 de 2024" in low
        and "chatgpt" in low
        and "inteligencia artificial" in low
    )
    date_ok = "dos (02) de agosto de dos mil veinticuatro (2024)" in low

    if ok and is_t323:
        return {
            "cluster_id": row.get("cluster_id", ""),
            "hardening_verdict": "bounded_case_candidate_needs_anton_acceptance",
            "reviewed_core_candidate_status": "ready_for_human_acceptance_not_promoted",
            "obscure_ai_candidate_status": "not_obscure_ai_ready_until_reviewed_core_acceptance",
            "official_source_verified": "yes",
            "source_url": url,
            "source_host": row.get("source_host", ""),
            "source_language": "es",
            "source_record_date": "2024-08-02" if date_ok else "2024",
            "jurisdiction": "Colombia",
            "official_title": "Sentencia T-323 de 2024",
            "proposed_case_title": "Colombian Constitutional Court T-323/24 reviews judicial ChatGPT use and sets criteria for AI use in tutela decisions",
            "proposed_evidence_tier": "T3_authoritative_source",
            "proposed_limen_categories": "legal_procedural_contamination;public_sector_misuse_or_gap;normative_or_moral_outlier",
            "bounded_claim_candidate": (
                "The official Colombian Constitutional Court judgment T-323/24, dated 2024-08-02, reviewed a tutela matter in which "
                "the second-instance judge used ChatGPT 3.5 and discussed due-process criteria for judicial use of AI tools."
            ),
            "claim_ceiling": (
                "Can state only that the official judgment discusses judicial ChatGPT/AI use in the reviewed tutela case and sets/recites "
                "criteria such as transparency, responsibility, privacy, non-substitution of human reasoning, and verification. Do not state "
                "that AI decided the case, that AI use alone violated due process, or that the ruling proves prevalence or legality/illegality "
                "of AI use in Colombian courts."
            ),
            "forbidden_overread": (
                "No general claim about Colombian court AI use, no automated-judge claim, no compliance/safety/legal-effectiveness finding, "
                "and no ObscureAI addition before human acceptance."
            ),
            "required_before_reviewed_core": (
                "Anton/legal acceptance of the bounded claim, final dedupe against reviewed core, and reviewed-core row insertion with the same claim ceiling."
            ),
            "required_before_obscure_ai": "Reviewed-core acceptance first; then decide whether this legal/procedural case belongs in ObscureAI.",
            "source_support_note": "Official page fetched and contained Sentencia T-323 de 2024, ChatGPT, inteligencia artificial, and the 2024-08-02 date line.",
        }

    extracted = extractions.get(row.get("source_cluster_key", ""), {})
    if extracted.get("case_extraction_verdict") == "case_candidate_for_hardening":
        if ok and source_supports_candidate(text, extracted):
            return {
                "cluster_id": row.get("cluster_id", ""),
                "hardening_verdict": "source_verified_case_candidate_needs_acceptance",
                "reviewed_core_candidate_status": "ready_for_human_acceptance_not_promoted",
                "obscure_ai_candidate_status": "not_obscure_ai_ready_until_reviewed_core_acceptance",
                "official_source_verified": "yes",
                "source_url": url,
                "source_host": row.get("source_host", ""),
                "source_language": "",
                "source_record_date": extracted.get("source_record_date", ""),
                "jurisdiction": extracted.get("jurisdiction", ""),
                "official_title": extracted.get("source_name", ""),
                "proposed_case_title": clean(extracted.get("proposed_case_title", ""), 360),
                "proposed_evidence_tier": extracted.get("proposed_evidence_tier", ""),
                "proposed_limen_categories": extracted.get("proposed_limen_categories", ""),
                "bounded_claim_candidate": clean(extracted.get("bounded_claim_candidate", ""), 900),
                "claim_ceiling": clean(extracted.get("claim_ceiling", ""), 900),
                "forbidden_overread": clean(extracted.get("forbidden_overread", ""), 900),
                "required_before_reviewed_core": clean(
                    extracted.get("required_before_reviewed_core", "")
                    or "Final reviewed-core insertion with stable case id, source citation, category fit, and claim ceiling.",
                    700,
                ),
                "required_before_obscure_ai": clean(
                    extracted.get("required_before_obscure_ai", "")
                    or "Reviewed-core acceptance first; then decide public ObscureAI fit.",
                    700,
                ),
                "source_support_note": clean(
                    f"Fetched exact public source and found supporting terms for extracted candidate. Final URL: {note}",
                    600,
                ),
            }
        return {
            "cluster_id": row.get("cluster_id", ""),
            "hardening_verdict": "case_candidate_source_fetch_or_support_gap",
            "reviewed_core_candidate_status": "not_ready",
            "obscure_ai_candidate_status": "not_ready",
            "official_source_verified": "no" if not ok else "partial",
            "source_url": url,
            "source_host": row.get("source_host", ""),
            "source_language": "",
            "source_record_date": extracted.get("source_record_date", ""),
            "jurisdiction": extracted.get("jurisdiction", ""),
            "official_title": extracted.get("source_name", ""),
            "proposed_case_title": clean(extracted.get("proposed_case_title", ""), 360),
            "proposed_evidence_tier": extracted.get("proposed_evidence_tier", ""),
            "proposed_limen_categories": extracted.get("proposed_limen_categories", ""),
            "bounded_claim_candidate": clean(extracted.get("bounded_claim_candidate", ""), 900),
            "claim_ceiling": clean(extracted.get("claim_ceiling", ""), 900),
            "forbidden_overread": clean(extracted.get("forbidden_overread", ""), 900),
            "required_before_reviewed_core": clean(extracted.get("required_before_reviewed_core", ""), 700),
            "required_before_obscure_ai": clean(extracted.get("required_before_obscure_ai", ""), 700),
            "source_support_note": clean(note if not ok else "source fetched, but support terms were insufficient for automatic hardening", 600),
        }

    return {
        "cluster_id": row.get("cluster_id", ""),
        "hardening_verdict": "needs_manual_source_review",
        "reviewed_core_candidate_status": "not_ready",
        "obscure_ai_candidate_status": "not_ready",
        "official_source_verified": "no" if not ok else "partial",
        "source_url": url,
        "source_host": row.get("source_host", ""),
        "source_language": "",
        "source_record_date": "",
        "jurisdiction": "",
        "official_title": "",
        "proposed_case_title": "",
        "proposed_evidence_tier": "",
        "proposed_limen_categories": "",
        "bounded_claim_candidate": "",
        "claim_ceiling": row.get("case_claim_ceiling_candidate", ""),
        "forbidden_overread": "No reviewed-core or ObscureAI promotion before source text is manually verified.",
        "required_before_reviewed_core": row.get("required_before_reviewed_core", ""),
        "required_before_obscure_ai": row.get("required_before_obscure_ai", ""),
        "source_support_note": clean(note, 500),
    }


def build() -> dict[str, object]:
    extractions = extraction_index()
    rows = [harden_cluster(row, extractions) for row in read_tsv(QUEUE)]
    write_tsv(OUT, rows)
    write_tsv(DASHBOARD_COPY, rows)

    verdict_counts = Counter(row["hardening_verdict"] for row in rows)
    status_counts = Counter(row["reviewed_core_candidate_status"] for row in rows)
    obscure_counts = Counter(row["obscure_ai_candidate_status"] for row in rows)
    final_rows = read_tsv(FINAL_ADJUDICATION)
    final_by_cluster = {row.get("cluster_id", ""): row for row in final_rows if row.get("cluster_id")}
    final_decision_counts = Counter(row.get("final_decision", "") for row in final_rows if row.get("final_decision"))
    pending_acceptance = [
        row
        for row in rows
        if row["reviewed_core_candidate_status"] == "ready_for_human_acceptance_not_promoted"
        and row.get("cluster_id", "") not in final_by_cluster
    ]
    status = {
        "generated_at_utc": utc_now(),
        "input": str(QUEUE),
        "output": str(OUT),
        "dashboard_copy": str(DASHBOARD_COPY),
        "case_hardening_review_rows": len(rows),
        "hardening_verdict_counts": dict(sorted(verdict_counts.items())),
        "reviewed_core_candidate_status_counts": dict(sorted(status_counts.items())),
        "obscure_ai_candidate_status_counts": dict(sorted(obscure_counts.items())),
        "reviewed_core_ready_for_human_acceptance_pre_adjudication": status_counts.get("ready_for_human_acceptance_not_promoted", 0),
        "reviewed_core_ready_for_human_acceptance": len(pending_acceptance),
        "case_final_adjudication_rows": len(final_rows),
        "case_final_decision_counts": dict(sorted(final_decision_counts.items())),
        "case_final_promoted_rows": sum(1 for row in final_rows if row.get("reviewed_core_action", "").startswith("promoted")),
        "case_final_obscure_ai_promoted_rows": sum(1 for row in final_rows if row.get("obscure_ai_action", "").startswith("promoted")),
        "reviewed_core_promoted_now": 0,
        "obscure_ai_ready_now": 0,
        "boundary": "Case-hardening review plus final adjudication ledger. Pending acceptance excludes rows already promoted, held, or closed in the final adjudication file.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY.write_text(
        "\n".join(
            [
                "# LIMEN reviewed-core case-hardening review",
                "",
                f"- Generated: {status['generated_at_utc']}",
                f"- Rows: `{status['case_hardening_review_rows']}`",
                f"- Verdicts: `{json.dumps(status['hardening_verdict_counts'], sort_keys=True)}`",
                f"- Reviewed-core ready for human acceptance: `{status['reviewed_core_ready_for_human_acceptance']}`",
                f"- Reviewed-core promoted now: `{status['reviewed_core_promoted_now']}`",
                f"- ObscureAI ready now: `{status['obscure_ai_ready_now']}`",
                "",
                status["boundary"],
                "",
            ]
        ),
        encoding="utf-8",
    )
    return status


def main() -> int:
    print(json.dumps(build(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
