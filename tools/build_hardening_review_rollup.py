#!/usr/bin/env python3
"""Consolidate LIMEN hardening-review lane outputs.

The lane outputs are review evidence only. This script validates that the
named-URL extraction and translation-source-review tasks covered their current
queues exactly once, then writes stable consolidated TSVs and a public status
payload for the observatory.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
QUEUE_ROOT = REVIEW_ROOT / "hardening-review-queues"
BATCH_ROOT = REVIEW_ROOT / "hardening-review-batches"
DASHBOARD_ROOT = PROJECT_ROOT / "results" / "dashboard"
STATUS = REVIEW_ROOT / "hardening-review-rollup-status.json"
SUMMARY = REVIEW_ROOT / "hardening-review-rollup-summary-v0.1.md"


@dataclass(frozen=True)
class TaskConfig:
    task: str
    queue: Path
    batch_subdir: str
    result_file: str
    output: Path
    dashboard_copy: Path
    result_fields: list[str]
    verdict_field: str


TASKS = [
    TaskConfig(
        task="named-url-extraction",
        queue=QUEUE_ROOT / "named-url-extraction-queue.tsv",
        batch_subdir="named-url-extraction",
        result_file="named-url-extraction-results.tsv",
        output=REVIEW_ROOT / "named-url-extraction-results-v0.1.tsv",
        dashboard_copy=DASHBOARD_ROOT / "named-url-extraction-results.tsv",
        result_fields=[
            "row_id",
            "signal_id",
            "url_extraction_verdict",
            "extracted_source_url",
            "source_name",
            "evidence_location",
            "reason",
            "claim_ceiling",
            "next_action",
        ],
        verdict_field="url_extraction_verdict",
    ),
    TaskConfig(
        task="translation-source-review",
        queue=QUEUE_ROOT / "translation-source-review-queue.tsv",
        batch_subdir="translation-source-review",
        result_file="translation-source-review-results.tsv",
        output=REVIEW_ROOT / "translation-source-review-results-v0.1.tsv",
        dashboard_copy=DASHBOARD_ROOT / "translation-source-review-results.tsv",
        result_fields=[
            "row_id",
            "signal_id",
            "translation_review_verdict",
            "language_reviewed",
            "source_url_or_locator",
            "source_name",
            "reason",
            "claim_ceiling",
            "next_action",
        ],
        verdict_field="translation_review_verdict",
    ),
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


def read_json(path: Path) -> dict[str, object]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def batch_sort_key(path: Path) -> tuple[str, str]:
    manifest = read_json(path.parent / "manifest.json")
    return (
        str(manifest.get("completed_at_utc") or manifest.get("updated_at_utc") or path.parent.name),
        path.parent.name,
    )


def load_valid_result_file(config: TaskConfig, result_path: Path) -> tuple[list[dict[str, str]], str]:
    input_path = result_path.parent / "input.tsv"
    if not input_path.exists():
        return [], "missing input.tsv"
    input_rows = read_tsv(input_path)
    result_rows = read_tsv(result_path)
    if len(result_rows) != len(input_rows):
        return [], f"row count mismatch input={len(input_rows)} result={len(result_rows)}"
    input_ids = {row.get("row_id", "") for row in input_rows}
    result_ids = [row.get("row_id", "") for row in result_rows]
    if set(result_ids) != input_ids:
        return [], "row_id set mismatch"
    if len(result_ids) != len(set(result_ids)):
        return [], "duplicate row_id in batch result"
    with result_path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != config.result_fields:
            return [], f"unexpected header {reader.fieldnames}"
    return result_rows, "ok"


def consolidate_task(config: TaskConfig) -> dict[str, object]:
    queue_rows = read_tsv(config.queue)
    queue_by_id = {row.get("row_id", ""): row for row in queue_rows if row.get("row_id", "")}
    result_by_id: dict[str, dict[str, str]] = {}
    result_source_by_id: dict[str, str] = {}
    skipped_files: list[dict[str, str]] = []
    duplicate_rows: Counter[str] = Counter()
    manifest_counts: Counter[str] = Counter()

    for manifest_path in sorted((BATCH_ROOT / config.batch_subdir).glob("*/manifest.json")):
        manifest = read_json(manifest_path)
        manifest_counts[str(manifest.get("status") or "unknown")] += 1

    for result_path in sorted((BATCH_ROOT / config.batch_subdir).glob(f"*/{config.result_file}"), key=batch_sort_key):
        rows, reason = load_valid_result_file(config, result_path)
        if reason != "ok":
            skipped_files.append({"path": str(result_path), "reason": reason})
            continue
        for row in rows:
            row_id = row.get("row_id", "")
            if row_id in result_by_id:
                duplicate_rows[row_id] += 1
            result_by_id[row_id] = row
            result_source_by_id[row_id] = str(result_path)

    ordered_rows = [result_by_id[row["row_id"]] for row in queue_rows if row.get("row_id", "") in result_by_id]
    missing_ids = sorted(set(queue_by_id) - set(result_by_id))
    extra_ids = sorted(set(result_by_id) - set(queue_by_id))
    verdict_counts = Counter(row.get(config.verdict_field, "") or "unknown" for row in ordered_rows)

    write_tsv(config.output, ordered_rows, config.result_fields)
    write_tsv(config.dashboard_copy, ordered_rows, config.result_fields)

    return {
        "task": config.task,
        "queue": str(config.queue),
        "queue_rows": len(queue_rows),
        "result_rows": len(ordered_rows),
        "unique_result_rows": len(result_by_id),
        "complete": len(ordered_rows) == len(queue_rows) and not missing_ids,
        "missing_row_ids": missing_ids[:50],
        "extra_row_ids": extra_ids[:50],
        "has_stale_extra_result_rows": bool(extra_ids),
        "stale_extra_result_row_count": len(extra_ids),
        "duplicate_row_ids": dict(sorted(duplicate_rows.items())),
        "skipped_result_files": skipped_files,
        "manifest_status_counts": dict(sorted(manifest_counts.items())),
        "verdict_counts": dict(sorted(verdict_counts.items())),
        "output": str(config.output),
        "dashboard_copy": str(config.dashboard_copy),
        "result_files": len(list((BATCH_ROOT / config.batch_subdir).glob(f"*/{config.result_file}"))),
        "boundary": "Hardening review output only; not reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.",
        "result_sources": result_source_by_id,
    }


def public_task_status(task_status: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in task_status.items() if key != "result_sources"}


def main() -> int:
    task_statuses = [consolidate_task(config) for config in TASKS]
    payload = {
        "generated_at_utc": utc_now(),
        "tasks": {status["task"]: public_task_status(status) for status in task_statuses},
        "all_complete": all(bool(status["complete"]) for status in task_statuses),
        "current_output_clean": all(bool(status["complete"]) for status in task_statuses),
        "has_stale_extra_result_rows": any(bool(status["has_stale_extra_result_rows"]) for status in task_statuses),
        "boundary": "Hardening review outputs are bounded source-review aids only. Promotion to reviewed core remains a separate human case-hardening step.",
    }
    STATUS.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# LIMEN hardening review rollup",
        "",
        f"- Generated: {payload['generated_at_utc']}",
        f"- All queues complete: `{payload['all_complete']}`",
        f"- Current output clean: `{payload['current_output_clean']}`",
        f"- Has stale extra result rows: `{payload['has_stale_extra_result_rows']}`",
        "",
    ]
    for task in task_statuses:
        lines.extend(
            [
                f"## {task['task']}",
                "",
                f"- Queue rows: `{task['queue_rows']}`",
                f"- Result rows: `{task['result_rows']}`",
                f"- Complete: `{task['complete']}`",
                f"- Verdict counts: `{json.dumps(task['verdict_counts'], sort_keys=True)}`",
                f"- Output: `{task['output']}`",
                "",
            ]
        )
    lines.extend(["## Boundary", "", str(payload["boundary"]), ""])
    SUMMARY.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["all_complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
