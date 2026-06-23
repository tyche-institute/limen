#!/usr/bin/env python3
"""Prepare LIMEN hardening review queues for Hermes/Codex lanes."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
QUEUE_ROOT = REVIEW_ROOT / "hardening-review-queues"
HARDENING = REVIEW_ROOT / "source-reviewed-promotion-hardening-v0.1.tsv"
TRANSLATION = REVIEW_ROOT / "translation-held-review-board-v0.1.tsv"

URL_QUEUE = QUEUE_ROOT / "named-url-extraction-queue.tsv"
TRANSLATION_QUEUE = QUEUE_ROOT / "translation-source-review-queue.tsv"
STATUS = QUEUE_ROOT / "hardening-review-queue-status.json"

URL_FIELDS = [
    "row_id",
    "signal_id",
    "promotion_gate",
    "promotion_priority",
    "source_surface_class",
    "source_review_role",
    "shards",
    "queries",
    "source_path",
    "source_line",
    "title_or_snippet",
    "source_review_reason",
    "claim_ceiling",
    "required_hardening_step",
    "forbidden_overread",
]

TRANSLATION_FIELDS = [
    "row_id",
    "signal_id",
    "translation_hold_class",
    "review_priority",
    "shards",
    "queries",
    "language_hint",
    "source_path_family",
    "source_url",
    "source_path",
    "source_line",
    "title_or_snippet",
    "claim_ceiling",
    "next_action",
    "forbidden_overread",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, delimiter="\t", fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    url_rows = [row for row in read_tsv(HARDENING) if row.get("promotion_gate") == "needs_named_url_extraction"]
    translation_rows = read_tsv(TRANSLATION)
    write_tsv(URL_QUEUE, url_rows, URL_FIELDS)
    write_tsv(TRANSLATION_QUEUE, translation_rows, TRANSLATION_FIELDS)

    status = {
        "generated_at_utc": utc_now(),
        "url_queue": str(URL_QUEUE),
        "url_queue_rows": len(url_rows),
        "url_queue_class_counts": dict(Counter(row.get("source_surface_class", "") for row in url_rows)),
        "translation_queue": str(TRANSLATION_QUEUE),
        "translation_queue_rows": len(translation_rows),
        "translation_queue_class_counts": dict(Counter(row.get("translation_hold_class", "") for row in translation_rows)),
        "boundary": "Queues are hardening review inputs only; no promotion, legal finding, deployment proof, prevalence, or completeness claim.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(status, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
