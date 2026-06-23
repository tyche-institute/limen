#!/usr/bin/env python3
"""Build the next bulk routing table after source-reviewed completion."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
QUEUE = REVIEW_ROOT / "direct-source-review-queue.tsv"
BATCH_ROOT = REVIEW_ROOT / "source-review-batches"
OUT = REVIEW_ROOT / "bulk-source-review-routing-v0.1.tsv"
STATUS = REVIEW_ROOT / "bulk-source-review-routing-status.json"
SUMMARY = REVIEW_ROOT / "bulk-source-review-routing-summary-v0.1.md"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "bulk-source-review-routing.tsv"

FIELDS = [
    "signal_id",
    "bulk_route",
    "source_review_verdict",
    "source_review_role",
    "review_priority",
    "shards",
    "queries",
    "source_path",
    "source_line",
    "reason",
    "claim_ceiling",
    "next_action",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def verdict_route(verdict: str) -> str:
    return {
        "source_reviewed_candidate": "done_source_reviewed_layer_closed",
        "needs_named_source_extraction": "next_named_source_extraction",
        "translation_review_needed": "next_translation_or_language_review",
        "negative_evidence_candidate": "closed_negative_evidence",
        "merge_existing_surface": "closed_merge_existing_surface",
        "reject_noise": "closed_reject_noise",
    }.get(verdict, "unknown_route")


def latest_source_reviews() -> dict[str, dict[str, str]]:
    latest: dict[str, dict[str, str]] = {}
    for result_path in sorted(BATCH_ROOT.glob("*/source-review-results.tsv")):
        for row in read_tsv(result_path):
            signal_id = row.get("signal_id", "")
            if signal_id:
                latest[signal_id] = row
    return latest


def build() -> dict[str, object]:
    queue_rows = read_tsv(QUEUE)
    reviews = latest_source_reviews()
    out_rows: list[dict[str, str]] = []
    for src in queue_rows:
        signal_id = src.get("signal_id", "")
        review = reviews.get(signal_id, {})
        verdict = review.get("source_review_verdict", "missing_source_review")
        out_rows.append(
            {
                "signal_id": signal_id,
                "bulk_route": verdict_route(verdict),
                "source_review_verdict": verdict,
                "source_review_role": review.get("source_review_role", ""),
                "review_priority": src.get("review_priority", ""),
                "shards": src.get("shards", ""),
                "queries": src.get("queries", ""),
                "source_path": src.get("source_path", ""),
                "source_line": src.get("source_line", ""),
                "reason": review.get("reason", ""),
                "claim_ceiling": review.get("claim_ceiling", ""),
                "next_action": review.get("next_action", ""),
            }
        )
    out_rows.sort(key=lambda row: (row["bulk_route"], row["review_priority"], row["signal_id"]))
    write_tsv(OUT, out_rows)
    write_tsv(DASHBOARD_COPY, out_rows[:250])

    route_counts = Counter(row["bulk_route"] for row in out_rows)
    verdict_counts = Counter(row["source_review_verdict"] for row in out_rows)
    status = {
        "generated_at_utc": utc_now(),
        "queue": str(QUEUE),
        "output": str(OUT),
        "dashboard_copy": str(DASHBOARD_COPY),
        "current_queue_rows": len(queue_rows),
        "current_queue_reviewed_rows": sum(1 for row in out_rows if row["source_review_verdict"] != "missing_source_review"),
        "current_queue_missing_rows": sum(1 for row in out_rows if row["source_review_verdict"] == "missing_source_review"),
        "bulk_route_counts": dict(sorted(route_counts.items())),
        "source_review_verdict_counts": dict(sorted(verdict_counts.items())),
        "boundary": "Bulk routing is processing-state only; no promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY.write_text(
        "\n".join(
            [
                "# Bulk source-review routing",
                "",
                f"- Generated: {status['generated_at_utc']}",
                f"- Current direct-source queue rows: `{status['current_queue_rows']}`",
                f"- Reviewed rows: `{status['current_queue_reviewed_rows']}`",
                f"- Missing rows: `{status['current_queue_missing_rows']}`",
                f"- Routes: `{json.dumps(status['bulk_route_counts'], sort_keys=True)}`",
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
