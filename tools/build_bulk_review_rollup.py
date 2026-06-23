#!/usr/bin/env python3
"""Roll up LIMEN bulk Hermes review batches into coverage-checked artifacts."""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
BATCH_ROOT = REVIEW_ROOT / "bulk-review-batches"
QUEUE_ROOT = REVIEW_ROOT / "bulk-review-queues"
DASHBOARD_ROOT = PROJECT_ROOT / "results" / "dashboard"


@dataclass(frozen=True)
class RollupConfig:
    name: str
    queue: Path
    batch_subdir: str
    result_file: str
    verdict_field: str
    out: Path
    dashboard_copy: Path
    result_fields: list[str]


SOURCE_FIELDS = [
    "queue_id",
    "signal_id",
    "bulk_source_verdict",
    "extracted_source_url",
    "source_name",
    "evidence_location",
    "reason",
    "claim_ceiling",
    "next_action",
]

TRANSLATION_FIELDS = [
    "queue_id",
    "signal_id",
    "bulk_translation_verdict",
    "language_reviewed",
    "source_url_or_locator",
    "source_name",
    "reason",
    "claim_ceiling",
    "next_action",
]

QUEUE_CONTEXT_FIELDS = [
    "review_priority",
    "source_review_role",
    "shards",
    "queries",
    "source_path",
    "source_line",
]

CONFIGS = [
    RollupConfig(
        name="parent_source_extraction",
        queue=QUEUE_ROOT / "parent-source-extraction-queue.tsv",
        batch_subdir="parent-source-extraction",
        result_file="parent-source-extraction-results.tsv",
        verdict_field="bulk_source_verdict",
        out=REVIEW_ROOT / "bulk-parent-source-extraction-results-v0.1.tsv",
        dashboard_copy=DASHBOARD_ROOT / "bulk-parent-source-extraction-results.tsv",
        result_fields=SOURCE_FIELDS,
    ),
    RollupConfig(
        name="bulk_translation_review",
        queue=QUEUE_ROOT / "bulk-translation-review-queue.tsv",
        batch_subdir="bulk-translation-review",
        result_file="bulk-translation-review-results.tsv",
        verdict_field="bulk_translation_verdict",
        out=REVIEW_ROOT / "bulk-translation-review-results-v0.1.tsv",
        dashboard_copy=DASHBOARD_ROOT / "bulk-translation-review-results.tsv",
        result_fields=TRANSLATION_FIELDS,
    ),
    RollupConfig(
        name="translation_parent_source_extraction",
        queue=QUEUE_ROOT / "translation-parent-source-extraction-queue.tsv",
        batch_subdir="translation-parent-source-extraction",
        result_file="translation-parent-source-extraction-results.tsv",
        verdict_field="bulk_source_verdict",
        out=REVIEW_ROOT / "bulk-translation-parent-source-extraction-results-v0.1.tsv",
        dashboard_copy=DASHBOARD_ROOT / "bulk-translation-parent-source-extraction-results.tsv",
        result_fields=SOURCE_FIELDS,
    ),
]

STATUS = REVIEW_ROOT / "bulk-review-rollup-status.json"
SUMMARY = REVIEW_ROOT / "bulk-review-rollup-summary-v0.1.md"


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


def read_manifest(path: Path) -> dict[str, object]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def rollup_one(config: RollupConfig) -> dict[str, object]:
    if not config.queue.exists():
        return {
            "name": config.name,
            "queue": str(config.queue),
            "queue_rows": 0,
            "output": str(config.out),
            "dashboard_copy": str(config.dashboard_copy),
            "result_files": 0,
            "result_rows_seen": 0,
            "completed_unique_queue_ids": 0,
            "missing_queue_ids": 0,
            "duplicate_queue_ids": 0,
            "extra_queue_ids": 0,
            "manifest_statuses": {},
            "manifest_verdict_counts": {},
            "verdict_counts": {},
            "failed_batches": [],
            "sample_missing_queue_ids": [],
            "sample_duplicate_queue_ids": [],
            "sample_extra_queue_ids": [],
            "queue_absent": True,
        }
    queue_rows = read_tsv(config.queue)
    queue_id_counts = Counter(row.get("queue_id", "") for row in queue_rows if row.get("queue_id", ""))
    duplicate_queue_ids_in_queue = {queue_id: count for queue_id, count in queue_id_counts.items() if count > 1}
    queue_by_id = {row.get("queue_id", ""): row for row in queue_rows if row.get("queue_id", "")}
    queue_ids = set(queue_by_id)
    queue_signal_ids = {row.get("signal_id", "") for row in queue_rows if row.get("signal_id", "")}
    seen: dict[str, dict[str, str]] = {}
    duplicate_ids: dict[str, list[str]] = defaultdict(list)
    extra_ids: dict[str, list[str]] = defaultdict(list)
    stale_result_ids: dict[str, list[str]] = defaultdict(list)
    signal_mismatch_ids: dict[str, list[str]] = defaultdict(list)
    result_files = 0
    result_rows_seen = 0
    manifest_statuses: Counter[str] = Counter()
    manifest_verdict_counts: Counter[str] = Counter()
    failed_batches: list[dict[str, str]] = []

    task_root = BATCH_ROOT / config.batch_subdir
    for manifest_path in sorted(task_root.glob("*/manifest.json")):
        manifest = read_manifest(manifest_path)
        status = str(manifest.get("status", "unknown"))
        manifest_statuses[status] += 1
        manifest_verdict_counts.update({str(k): int(v) for k, v in (manifest.get("verdict_counts") or {}).items()})
        if status == "failed":
            failed_batches.append(
                {
                    "batch_id": manifest_path.parent.name,
                    "failure_reason": str(manifest.get("failure_reason", "")),
                }
            )

        result_path = manifest_path.parent / config.result_file
        if not result_path.exists():
            continue
        result_files += 1
        for row in read_tsv(result_path):
            result_rows_seen += 1
            queue_id = row.get("queue_id", "")
            signal_id = row.get("signal_id", "")
            if queue_id not in queue_ids:
                if signal_id and signal_id not in queue_signal_ids:
                    stale_result_ids[queue_id].append(manifest_path.parent.name)
                else:
                    extra_ids[queue_id].append(manifest_path.parent.name)
                continue
            if queue_by_id[queue_id].get("signal_id", "") != signal_id:
                signal_mismatch_ids[queue_id].append(manifest_path.parent.name)
                continue
            normalized = {field: row.get(field, "") for field in config.result_fields}
            normalized["batch_id"] = manifest_path.parent.name
            if queue_id in seen:
                duplicate_ids[queue_id].append(manifest_path.parent.name)
                continue
            seen[queue_id] = normalized

    output_fields = config.result_fields + ["batch_id"] + QUEUE_CONTEXT_FIELDS
    out_rows = []
    for queue_id in sorted(queue_ids):
        result = seen.get(queue_id)
        if not result:
            continue
        queue_row = queue_by_id[queue_id]
        merged = dict(result)
        for field in QUEUE_CONTEXT_FIELDS:
            merged[field] = queue_row.get(field, "")
        out_rows.append(merged)

    out_rows.sort(key=lambda row: (row.get(config.verdict_field, ""), row.get("review_priority", ""), row.get("queue_id", "")))
    write_tsv(config.out, out_rows, output_fields)
    write_tsv(config.dashboard_copy, out_rows[:500], output_fields)

    verdict_counts = Counter(row.get(config.verdict_field, "") for row in out_rows)
    missing_ids = sorted(queue_ids - set(seen))
    status_payload = {
        "name": config.name,
        "queue": str(config.queue),
        "queue_rows": len(queue_rows),
        "output": str(config.out),
        "dashboard_copy": str(config.dashboard_copy),
        "result_files": result_files,
        "result_rows_seen": result_rows_seen,
        "completed_unique_queue_ids": len(seen),
        "missing_queue_ids": len(missing_ids),
        "duplicate_queue_ids": len(duplicate_ids),
        "duplicate_queue_ids_in_queue": len(duplicate_queue_ids_in_queue),
        "extra_queue_ids": len(extra_ids),
        "stale_result_queue_ids": len(stale_result_ids),
        "signal_mismatch_queue_ids": len(signal_mismatch_ids),
        "manifest_statuses": dict(sorted(manifest_statuses.items())),
        "manifest_verdict_counts": dict(sorted(manifest_verdict_counts.items())),
        "verdict_counts": dict(sorted(verdict_counts.items())),
        "failed_batches": failed_batches[:20],
        "sample_missing_queue_ids": missing_ids[:20],
        "sample_duplicate_queue_ids": sorted(duplicate_ids)[:20],
        "sample_duplicate_queue_ids_in_queue": sorted(duplicate_queue_ids_in_queue)[:20],
        "sample_extra_queue_ids": sorted(extra_ids)[:20],
        "sample_stale_result_queue_ids": sorted(stale_result_ids)[:20],
        "sample_signal_mismatch_queue_ids": sorted(signal_mismatch_ids)[:20],
    }
    return status_payload


def build() -> dict[str, object]:
    task_statuses = [rollup_one(config) for config in CONFIGS]
    archived_stale_result_queue_ids = sum(int(item.get("stale_result_queue_ids") or 0) for item in task_statuses)
    has_blocking_integrity_issue = any(
        item.get("missing_queue_ids", 0)
        or item.get("duplicate_queue_ids", 0)
        or item.get("duplicate_queue_ids_in_queue", 0)
        or item.get("failed_batches", [])
        for item in task_statuses
    )
    status = {
        "generated_at_utc": utc_now(),
        "tasks": {item["name"]: item for item in task_statuses},
        "all_queues_complete": all(item.get("missing_queue_ids", 0) == 0 for item in task_statuses),
        "current_output_clean": not has_blocking_integrity_issue,
        "has_blocking_integrity_issue": has_blocking_integrity_issue,
        "has_duplicate_queue_ids": any(item.get("duplicate_queue_ids", 0) for item in task_statuses),
        "has_duplicate_queue_ids_in_queue": any(item.get("duplicate_queue_ids_in_queue", 0) for item in task_statuses),
        "has_extra_queue_ids": any(item.get("extra_queue_ids", 0) for item in task_statuses),
        "has_signal_mismatch_queue_ids": any(item.get("signal_mismatch_queue_ids", 0) for item in task_statuses),
        "archived_stale_result_queue_ids": archived_stale_result_queue_ids,
        "has_stale_result_queue_ids": any(item.get("stale_result_queue_ids", 0) for item in task_statuses),
        "has_failed_batches": any(item.get("failed_batches", []) for item in task_statuses),
        "boundary": "Bulk rollup is processing-state only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY.write_text(summary_text(status), encoding="utf-8")
    return status


def summary_text(status: dict[str, object]) -> str:
    lines = [
        "# LIMEN Bulk Review Rollup",
        "",
        f"Generated UTC: {status['generated_at_utc']}",
        "",
        f"- All queues complete: `{status['all_queues_complete']}`",
        f"- Current output clean: `{status['current_output_clean']}`",
        f"- Blocking integrity issue: `{status['has_blocking_integrity_issue']}`",
        f"- Duplicate queue IDs: `{status['has_duplicate_queue_ids']}`",
        f"- Duplicate queue IDs in queues: `{status['has_duplicate_queue_ids_in_queue']}`",
        f"- Extra queue IDs: `{status['has_extra_queue_ids']}`",
        f"- Signal mismatch queue IDs: `{status['has_signal_mismatch_queue_ids']}`",
        f"- Superseded historical result queue IDs: `{status['archived_stale_result_queue_ids']}`",
        f"- Failed batches: `{status['has_failed_batches']}`",
        "",
    ]
    tasks = status["tasks"]
    assert isinstance(tasks, dict)
    for name, task in tasks.items():
        assert isinstance(task, dict)
        lines.extend(
            [
                f"## {name}",
                "",
                f"- Queue rows: `{task['queue_rows']}`",
                f"- Completed unique queue IDs: `{task['completed_unique_queue_ids']}`",
                f"- Missing queue IDs: `{task['missing_queue_ids']}`",
                f"- Result files: `{task['result_files']}`",
                f"- Verdict counts: `{json.dumps(task['verdict_counts'], sort_keys=True)}`",
                "",
            ]
        )
    lines.extend(["## Boundary", "", str(status["boundary"]), ""])
    return "\n".join(lines)


def main() -> int:
    print(json.dumps(build(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
