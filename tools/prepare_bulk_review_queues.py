#!/usr/bin/env python3
"""Prepare bulk follow-up queues after source-reviewed layer closure."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
QUEUE_ROOT = REVIEW_ROOT / "bulk-review-queues"
BATCH_ROOT = REVIEW_ROOT / "bulk-review-batches"
NAMED_UNRESOLVED = REVIEW_ROOT / "bulk-named-source-unresolved-queue-v0.1.tsv"
BULK_ROUTING = REVIEW_ROOT / "bulk-source-review-routing-v0.1.tsv"
SOURCE_QUEUE = QUEUE_ROOT / "parent-source-extraction-queue.tsv"
TRANSLATION_QUEUE = QUEUE_ROOT / "bulk-translation-review-queue.tsv"
STATUS = QUEUE_ROOT / "bulk-review-queue-status.json"

SOURCE_FIELDS = [
    "queue_id",
    "signal_id",
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

TRANSLATION_FIELDS = [
    "queue_id",
    "signal_id",
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


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def existing_queue_ids(path: Path, result_glob: str = "") -> tuple[dict[str, str], int]:
    def add_rows(rows: list[dict[str, str]]) -> None:
        nonlocal max_seen
        for row in rows:
            signal_id = row.get("signal_id", "")
            queue_id = row.get("queue_id", "")
            if signal_id and queue_id and signal_id not in mapping:
                mapping[signal_id] = queue_id
            try:
                max_seen = max(max_seen, int(queue_id.rsplit("-", 1)[-1]))
            except Exception:
                pass

    mapping: dict[str, str] = {}
    max_seen = 0
    if result_glob:
        for result_path in sorted(BATCH_ROOT.glob(result_glob)):
            try:
                add_rows(read_tsv(result_path))
            except Exception:
                continue
    if not path.exists():
        add_rows([])
    else:
        add_rows(read_tsv(path))
    return mapping, max_seen


def with_queue_ids(
    rows: list[dict[str, str]],
    prefix: str,
    fields: list[str],
    existing_path: Path,
    result_glob: str = "",
) -> list[dict[str, str]]:
    existing_by_signal, next_index = existing_queue_ids(existing_path, result_glob)
    used = set(existing_by_signal.values())
    out = []
    for row in rows:
        item = {field: row.get(field, "") for field in fields}
        queue_id = existing_by_signal.get(row.get("signal_id", ""))
        if not queue_id:
            next_index += 1
            queue_id = f"{prefix}-{next_index:05d}"
            while queue_id in used:
                next_index += 1
                queue_id = f"{prefix}-{next_index:05d}"
        item["queue_id"] = queue_id
        used.add(queue_id)
        out.append(item)
    return out


def main() -> int:
    source_rows = read_tsv(NAMED_UNRESOLVED)
    source_queue = with_queue_ids(
        source_rows,
        "BPSE",
        SOURCE_FIELDS,
        SOURCE_QUEUE,
        "parent-source-extraction/*/parent-source-extraction-results.tsv",
    )
    routing_rows = [row for row in read_tsv(BULK_ROUTING) if row.get("bulk_route") == "next_translation_or_language_review"]
    translation_queue = with_queue_ids(
        routing_rows,
        "BTR",
        TRANSLATION_FIELDS,
        TRANSLATION_QUEUE,
        "bulk-translation-review/*/bulk-translation-review-results.tsv",
    )

    write_tsv(SOURCE_QUEUE, source_queue, SOURCE_FIELDS)
    write_tsv(TRANSLATION_QUEUE, translation_queue, TRANSLATION_FIELDS)

    status = {
        "generated_at_utc": utc_now(),
        "source_queue": str(SOURCE_QUEUE),
        "source_queue_rows": len(source_queue),
        "source_queue_role_counts": dict(Counter(row.get("source_review_role", "") for row in source_queue).most_common(30)),
        "translation_queue": str(TRANSLATION_QUEUE),
        "translation_queue_rows": len(translation_queue),
        "translation_queue_role_counts": dict(Counter(row.get("source_review_role", "") for row in translation_queue).most_common(30)),
        "boundary": "Bulk follow-up queues only; no reviewed-core promotion or ObscureAI addition.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(status, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
