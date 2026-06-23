#!/usr/bin/env python3
"""Roll up source-surface case extraction lanes into hardening candidates."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
QUEUE = REVIEW_ROOT / "reviewed-core-source-surface-disposition-v0.1.tsv"
BATCH_ROOT = REVIEW_ROOT / "case-extraction-batches"
RESULT_FILE = "case-extraction-results.tsv"
OUT = REVIEW_ROOT / "reviewed-core-case-extraction-results-v0.1.tsv"
STATUS = REVIEW_ROOT / "reviewed-core-case-extraction-rollup-status.json"
SUMMARY = REVIEW_ROOT / "reviewed-core-case-extraction-rollup-summary-v0.1.md"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "reviewed-core-case-extraction-results.tsv"

CASE_QUEUE = REVIEW_ROOT / "reviewed-core-case-hardening-queue-v0.1.tsv"
CASE_QUEUE_DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "reviewed-core-case-hardening-queue.tsv"

RESULT_FIELDS = [
    "source_cluster_key",
    "case_extraction_verdict",
    "source_url_or_locator",
    "source_name",
    "source_host",
    "proposed_case_title",
    "proposed_evidence_tier",
    "proposed_limen_categories",
    "source_record_date",
    "jurisdiction",
    "bounded_claim_candidate",
    "claim_ceiling",
    "forbidden_overread",
    "rationale",
    "required_before_reviewed_core",
    "required_before_obscure_ai",
    "next_action",
]

CASE_QUEUE_FIELDS = [
    "cluster_id",
    "source_cluster_key",
    "candidate_packet_rows",
    "signal_ids",
    "source_lanes",
    "source_url_or_locator",
    "normalized_source_url",
    "source_host",
    "source_name",
    "queries",
    "case_hardening_status",
    "case_claim_ceiling_candidate",
    "required_before_reviewed_core",
    "required_before_obscure_ai",
    "boundary",
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
    scheme = "https" if parsed.scheme.lower() in {"http", "https"} else parsed.scheme.lower()
    return urlunsplit((scheme, host, path, parsed.query, ""))


def load_manifests() -> list[dict[str, object]]:
    manifests = []
    for path in sorted(BATCH_ROOT.glob("*/manifest.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            data = {"status": "unreadable", "path": str(path)}
        data["_manifest_path"] = str(path)
        manifests.append(data)
    return manifests


def build() -> dict[str, object]:
    queue_rows = read_tsv(QUEUE)
    queue_by_key = {row.get("source_cluster_key", ""): row for row in queue_rows if row.get("source_cluster_key")}
    results_by_key: dict[str, dict[str, str]] = {}
    duplicate_result_keys: list[str] = []
    extra_result_keys: list[str] = []

    for path in sorted(BATCH_ROOT.glob(f"*/{RESULT_FILE}")):
        for row in read_tsv(path):
            key = row.get("source_cluster_key", "")
            if not key:
                continue
            if key in results_by_key:
                duplicate_result_keys.append(key)
                continue
            if key not in queue_by_key:
                extra_result_keys.append(key)
            row["_result_path"] = str(path)
            results_by_key[key] = row

    missing_keys = sorted(set(queue_by_key) - set(results_by_key))
    result_rows = [results_by_key[key] for key in sorted(queue_by_key) if key in results_by_key]
    write_tsv(OUT, result_rows, RESULT_FIELDS)
    write_tsv(DASHBOARD_COPY, result_rows[:300], RESULT_FIELDS)

    case_rows: list[dict[str, str]] = []
    for index, row in enumerate(
        [row for row in result_rows if row.get("case_extraction_verdict") == "case_candidate_for_hardening"],
        start=1,
    ):
        source = queue_by_key.get(row.get("source_cluster_key", ""), {})
        source_url = row.get("source_url_or_locator") or source.get("source_url_or_locator", "")
        case_rows.append(
            {
                "cluster_id": f"RCCQ-{index:05d}",
                "source_cluster_key": row.get("source_cluster_key", ""),
                "candidate_packet_rows": source.get("packet_rows", "1"),
                "signal_ids": source.get("signal_ids", ""),
                "source_lanes": source.get("source_lanes", ""),
                "source_url_or_locator": clean(source_url, 700),
                "normalized_source_url": normalize_url(source_url),
                "source_host": row.get("source_host") or source.get("source_host", ""),
                "source_name": row.get("source_name") or source.get("source_name", ""),
                "queries": source.get("queries", ""),
                "case_hardening_status": "case_extraction_candidate_needs_source_hardening",
                "case_claim_ceiling_candidate": clean(row.get("bounded_claim_candidate") or row.get("claim_ceiling", ""), 700),
                "required_before_reviewed_core": clean(row.get("required_before_reviewed_core", ""), 500),
                "required_before_obscure_ai": clean(row.get("required_before_obscure_ai", ""), 500),
                "boundary": "Case-extraction candidate only; no reviewed-core promotion or ObscureAI addition occurred.",
            }
        )
    write_tsv(CASE_QUEUE, case_rows, CASE_QUEUE_FIELDS)
    write_tsv(CASE_QUEUE_DASHBOARD_COPY, case_rows, CASE_QUEUE_FIELDS)

    manifests = load_manifests()
    manifest_counts = Counter(str(m.get("status", "unknown")) for m in manifests)
    verdict_counts = Counter(row.get("case_extraction_verdict", "") for row in result_rows)
    failed_batches = [
        str(m.get("_manifest_path", ""))
        for m in manifests
        if str(m.get("status", "")) == "failed"
    ]

    blocking_integrity = bool(duplicate_result_keys or failed_batches)
    current_output_clean = not missing_keys and not blocking_integrity
    status = {
        "generated_at_utc": utc_now(),
        "queue": str(QUEUE),
        "output": str(OUT),
        "dashboard_copy": str(DASHBOARD_COPY),
        "case_hardening_queue": str(CASE_QUEUE),
        "case_hardening_dashboard_copy": str(CASE_QUEUE_DASHBOARD_COPY),
        "queue_rows": len(queue_rows),
        "completed_unique_source_clusters": len(set(results_by_key) & set(queue_by_key)),
        "missing_source_clusters": len(missing_keys),
        "extra_source_clusters": len(set(extra_result_keys)),
        "stale_extra_result_source_clusters": len(set(extra_result_keys)),
        "duplicate_result_source_clusters": len(set(duplicate_result_keys)),
        "all_complete": not missing_keys,
        "current_output_clean": current_output_clean,
        "has_integrity_warnings": blocking_integrity,
        "has_stale_extra_result_source_clusters": bool(extra_result_keys),
        "has_failed_batches": bool(failed_batches),
        "result_files": len(list(BATCH_ROOT.glob(f"*/{RESULT_FILE}"))),
        "manifest_statuses": dict(sorted(manifest_counts.items())),
        "failed_batches": failed_batches,
        "verdict_counts": dict(sorted(verdict_counts.items())),
        "case_candidate_rows": verdict_counts.get("case_candidate_for_hardening", 0),
        "case_hardening_clusters": len(case_rows),
        "obscure_ai_ready_now": 0,
        "boundary": "Case extraction rollup only; no reviewed-core promotion or ObscureAI addition occurred.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY.write_text(
        "\n".join(
            [
                "# LIMEN source-surface case extraction rollup",
                "",
                f"- Generated: `{status['generated_at_utc']}`",
                f"- Completed: `{status['completed_unique_source_clusters']} / {status['queue_rows']}`",
                f"- Missing: `{status['missing_source_clusters']}`",
                f"- Extra/stale result clusters: `{status['extra_source_clusters']}`",
                f"- Duplicate result clusters: `{status['duplicate_result_source_clusters']}`",
                f"- Failed batches: `{len(failed_batches)}`",
                f"- Verdicts: `{json.dumps(status['verdict_counts'], sort_keys=True)}`",
                f"- Case-hardening clusters: `{status['case_hardening_clusters']}`",
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
