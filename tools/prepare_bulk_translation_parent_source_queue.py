#!/usr/bin/env python3
"""Prepare parent-source extraction queue from bulk translation review outputs."""

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
TRANSLATION_RESULTS = REVIEW_ROOT / "bulk-translation-review-results-v0.1.tsv"
OUT = QUEUE_ROOT / "translation-parent-source-extraction-queue.tsv"
STATUS = QUEUE_ROOT / "translation-parent-source-extraction-queue-status.json"

FIELDS = [
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
    if path.exists():
        add_rows(read_tsv(path))
    if result_glob:
        for result_path in sorted(BATCH_ROOT.glob(result_glob)):
            try:
                add_rows(read_tsv(result_path))
            except Exception:
                continue
    return mapping, max_seen


def main() -> int:
    rows = []
    existing_by_signal, next_index = existing_queue_ids(
        OUT,
        "translation-parent-source-extraction/*/translation-parent-source-extraction-results.tsv",
    )
    reserved_queue_ids = set(existing_by_signal.values())
    used_queue_ids: set[str] = set()
    for row in [item for item in read_tsv(TRANSLATION_RESULTS) if item.get("bulk_translation_verdict") == "candidate_for_parent_source_extraction"]:
        queue_id = existing_by_signal.get(row.get("signal_id", ""))
        if queue_id in used_queue_ids:
            queue_id = ""
        if not queue_id:
            next_index += 1
            queue_id = f"BTPS-{next_index:05d}"
            while queue_id in reserved_queue_ids or queue_id in used_queue_ids:
                next_index += 1
                queue_id = f"BTPS-{next_index:05d}"
        used_queue_ids.add(queue_id)
        locator = row.get("source_url_or_locator", "")
        reason_bits = [row.get("reason", "")]
        if locator:
            reason_bits.append(f"translation locator: {locator}")
        rows.append(
            {
                "queue_id": queue_id,
                "signal_id": row.get("signal_id", ""),
                "source_review_role": "translation_candidate_parent_source_extraction",
                "review_priority": row.get("review_priority", ""),
                "shards": row.get("shards", ""),
                "queries": row.get("queries", ""),
                "source_path": row.get("source_path", ""),
                "source_line": row.get("source_line", ""),
                "reason": " ".join(bit for bit in reason_bits if bit),
                "claim_ceiling": row.get("claim_ceiling", ""),
                "next_action": row.get("next_action", "") or "Recover concrete original source URL if locally present; otherwise keep as wrapper/source hold.",
            }
        )

    write_tsv(OUT, rows, FIELDS)
    status = {
        "generated_at_utc": utc_now(),
        "input": str(TRANSLATION_RESULTS),
        "output": str(OUT),
        "queue_rows": len(rows),
        "review_priority_counts": dict(Counter(row.get("review_priority", "") for row in rows).most_common(20)),
        "shard_counts": dict(Counter(row.get("shards", "") for row in rows).most_common(20)),
        "boundary": "Translation-derived parent-source extraction only; no reviewed-core promotion or ObscureAI addition.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(status, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
