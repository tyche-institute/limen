#!/usr/bin/env python3
"""Run Hermes/Codex lanes for LIMEN bulk follow-up queues."""

from __future__ import annotations

import argparse
import csv
import fcntl
import json
import subprocess
import time
import uuid
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
QUEUE_ROOT = REVIEW_ROOT / "bulk-review-queues"
BATCH_ROOT = REVIEW_ROOT / "bulk-review-batches"


@dataclass(frozen=True)
class TaskConfig:
    task: str
    queue: Path
    batch_subdir: str
    result_file: str
    summary_file: str
    prompt_file: str
    source_tag: str
    result_fields: list[str]
    verdict_field: str
    valid_verdicts: set[str]


TASKS = {
    "source": TaskConfig(
        task="parent-source-extraction",
        queue=QUEUE_ROOT / "parent-source-extraction-queue.tsv",
        batch_subdir="parent-source-extraction",
        result_file="parent-source-extraction-results.tsv",
        summary_file="parent-source-extraction-summary.md",
        prompt_file="parent-source-extraction-prompt.md",
        source_tag="limen-bulk-parent-source-extraction",
        result_fields=[
            "queue_id",
            "signal_id",
            "bulk_source_verdict",
            "extracted_source_url",
            "source_name",
            "evidence_location",
            "reason",
            "claim_ceiling",
            "next_action",
        ],
        verdict_field="bulk_source_verdict",
        valid_verdicts={
            "source_url_extracted",
            "parent_source_wrapper",
            "country_gap_no_parent_source",
            "source_surface_only_no_case",
            "duplicate_existing_core",
            "reject_noise",
        },
    ),
    "translation": TaskConfig(
        task="bulk-translation-review",
        queue=QUEUE_ROOT / "bulk-translation-review-queue.tsv",
        batch_subdir="bulk-translation-review",
        result_file="bulk-translation-review-results.tsv",
        summary_file="bulk-translation-review-summary.md",
        prompt_file="bulk-translation-review-prompt.md",
        source_tag="limen-bulk-translation-review",
        result_fields=[
            "queue_id",
            "signal_id",
            "bulk_translation_verdict",
            "language_reviewed",
            "source_url_or_locator",
            "source_name",
            "reason",
            "claim_ceiling",
            "next_action",
        ],
        verdict_field="bulk_translation_verdict",
        valid_verdicts={
            "translation_source_reviewed",
            "needs_original_language_source",
            "cross_project_duplicate",
            "machine_translation_hold",
            "candidate_for_parent_source_extraction",
            "source_surface_only_no_case",
            "reject_noise",
        },
    ),
    "translation-source": TaskConfig(
        task="translation-parent-source-extraction",
        queue=QUEUE_ROOT / "translation-parent-source-extraction-queue.tsv",
        batch_subdir="translation-parent-source-extraction",
        result_file="translation-parent-source-extraction-results.tsv",
        summary_file="translation-parent-source-extraction-summary.md",
        prompt_file="translation-parent-source-extraction-prompt.md",
        source_tag="limen-bulk-translation-parent-source-extraction",
        result_fields=[
            "queue_id",
            "signal_id",
            "bulk_source_verdict",
            "extracted_source_url",
            "source_name",
            "evidence_location",
            "reason",
            "claim_ceiling",
            "next_action",
        ],
        verdict_field="bulk_source_verdict",
        valid_verdicts={
            "source_url_extracted",
            "parent_source_wrapper",
            "country_gap_no_parent_source",
            "source_surface_only_no_case",
            "duplicate_existing_core",
            "reject_noise",
        },
    ),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, delimiter="\t", fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def task_root(config: TaskConfig) -> Path:
    return BATCH_ROOT / config.batch_subdir


def row_key(row: dict[str, str]) -> tuple[str, str]:
    return (row.get("queue_id", ""), row.get("signal_id", ""))


def completed_keys(config: TaskConfig) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    for path in sorted(task_root(config).glob(f"*/{config.result_file}")):
        try:
            for row in load_tsv(path):
                key = row_key(row)
                if key[0]:
                    keys.add(key)
        except Exception:
            continue
    return keys


def active_keys(config: TaskConfig) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    for manifest_path in sorted(task_root(config).glob("*/manifest.json")):
        if (manifest_path.parent / config.result_file).exists():
            continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if manifest.get("status") not in {"leased", "running"}:
            continue
        input_path = manifest_path.parent / "input.tsv"
        if not input_path.exists():
            continue
        for row in load_tsv(input_path):
            key = row_key(row)
            if key[0]:
                keys.add(key)
    return keys


def allocate_batch(config: TaskConfig, lane_id: str, batch_size: int) -> Path | None:
    root = task_root(config)
    root.mkdir(parents=True, exist_ok=True)
    lock_path = root / ".lease.lock"
    with lock_path.open("a+", encoding="utf-8") as lock_fh:
        fcntl.flock(lock_fh, fcntl.LOCK_EX)
        queue_rows = load_tsv(config.queue)
        done = completed_keys(config)
        active = active_keys(config)
        selected = [
            row
            for row in queue_rows
            if row.get("queue_id", "") and row_key(row) not in done and row_key(row) not in active
        ][:batch_size]
        if not selected:
            return None
        batch_id = f"{stamp()}-{lane_id}-{uuid.uuid4().hex[:8]}"
        batch_dir = root / batch_id
        write_tsv(batch_dir / "input.tsv", selected, list(selected[0].keys()))
        write_json(
            batch_dir / "manifest.json",
            {
                "batch_id": batch_id,
                "task": config.task,
                "batch_size": batch_size,
                "created_at_utc": utc_now(),
                "input": str(batch_dir / "input.tsv"),
                "input_rows": len(selected),
                "lane_id": lane_id,
                "queue": str(config.queue),
                "queue_rows": len(queue_rows),
                "remaining_unleased_at_allocation": sum(
                    1
                    for row in queue_rows
                    if row.get("queue_id", "") and row_key(row) not in done and row_key(row) not in active
                ),
                "status": "leased",
                "updated_at_utc": utc_now(),
            },
        )
        return batch_dir


def prompt_for_batch(config: TaskConfig, batch_dir: Path) -> str:
    input_path = batch_dir / "input.tsv"
    result_path = batch_dir / config.result_file
    summary_path = batch_dir / config.summary_file
    manifest_path = batch_dir / "manifest.json"
    if config.verdict_field == "bulk_source_verdict":
        task_body = """Task:
- Review every row in input.tsv exactly once.
- Use local metadata and local source files only. Inspect relevant local lines and nearby context.
- Recover a concrete original public URL only when explicitly present in local metadata, local source context, or a local source-pack/ledger pointer. Do not invent URLs from source names.
- If a row is just a country gap/profile/score placeholder with no extractable parent source URL, mark `country_gap_no_parent_source`.
- If a row points to a wrapper/source-pack that needs a human to choose among multiple parent sources, mark `parent_source_wrapper`.
- Do not broad web crawl. Do not submit, publish, upload, email, register, pay, or use portal forms.

Write the configured result TSV with exactly this header:
queue_id	signal_id	bulk_source_verdict	extracted_source_url	source_name	evidence_location	reason	claim_ceiling	next_action

Allowed bulk_source_verdict values:
- source_url_extracted
- parent_source_wrapper
- country_gap_no_parent_source
- source_surface_only_no_case
- duplicate_existing_core
- reject_noise
"""
    else:
        task_body = """Task:
- Review every row in input.tsv exactly once.
- Use local metadata and local source files only. You may use multilingual understanding, but do not turn machine translation into a factual/legal/policy claim.
- Distinguish concrete source-surface review from case-level promotion. Most rows should remain source-surface/context unless a concrete edge-case claim is explicit.
- Do not broad web crawl. Do not submit, publish, upload, email, register, pay, or use portal forms.

Write bulk-translation-review-results.tsv with exactly this header:
queue_id	signal_id	bulk_translation_verdict	language_reviewed	source_url_or_locator	source_name	reason	claim_ceiling	next_action

Allowed bulk_translation_verdict values:
- translation_source_reviewed
- needs_original_language_source
- cross_project_duplicate
- machine_translation_hold
- candidate_for_parent_source_extraction
- source_surface_only_no_case
- reject_noise
"""
    return f"""You are Hermes/Codex performing a bounded LIMEN {config.task} batch.

Input TSV:
{input_path}

Required outputs:
{result_path}
{summary_path}

Update this manifest when complete:
{manifest_path}

{task_body}
Keep reasons concise. Replace tabs and newlines inside fields with spaces.
Write one output row per input queue_id, no omissions, no extras, no duplicate queue_id values.
Before stopping, verify that the result TSV has exactly the same queue_id set and row count as input.tsv.
Boundary: this is processing-state review only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
"""


def update_manifest(batch_dir: Path, **updates: object) -> None:
    path = batch_dir / "manifest.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        manifest = {"batch_id": batch_dir.name}
    manifest.update(updates)
    manifest["updated_at_utc"] = utc_now()
    write_json(path, manifest)


def run_hermes(config: TaskConfig, batch_dir: Path, provider: str, model: str, max_turns: int) -> int:
    update_manifest(batch_dir, status="running", started_at_utc=utc_now())
    prompt = prompt_for_batch(config, batch_dir)
    (batch_dir / config.prompt_file).write_text(prompt, encoding="utf-8")
    cmd = [
        "hermes",
        "chat",
        "--provider",
        provider,
        "--model",
        model,
        "--max-turns",
        str(max_turns),
        "--source",
        config.source_tag,
        "--yolo",
        "--quiet",
        "--query",
        prompt,
    ]
    with (batch_dir / "hermes.log").open("w", encoding="utf-8") as log_fh:
        proc = subprocess.run(cmd, cwd=str(PROJECT_ROOT), text=True, stdout=log_fh, stderr=subprocess.STDOUT)
    return proc.returncode


def validate_batch(config: TaskConfig, batch_dir: Path) -> tuple[bool, str, Counter[str]]:
    input_rows = load_tsv(batch_dir / "input.tsv")
    result_path = batch_dir / config.result_file
    if not result_path.exists():
        return False, f"missing {config.result_file}", Counter()
    with result_path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != config.result_fields:
            return False, f"unexpected result header: {reader.fieldnames}", Counter()
    result_rows = load_tsv(result_path)
    if len(result_rows) != len(input_rows):
        return False, f"row count mismatch: input={len(input_rows)} result={len(result_rows)}", Counter()
    input_ids = [row["queue_id"] for row in input_rows]
    result_ids = [row.get("queue_id", "") for row in result_rows]
    if set(input_ids) != set(result_ids):
        return False, "queue_id set mismatch", Counter()
    if len(result_ids) != len(set(result_ids)):
        return False, "duplicate queue_id in result", Counter()
    for row in result_rows:
        if None in row:
            return False, "extra TSV columns detected, likely embedded tab", Counter()
        verdict = row.get(config.verdict_field, "")
        if verdict not in config.valid_verdicts:
            return False, f"invalid verdict: {verdict}", Counter()
        if config.verdict_field == "bulk_source_verdict" and verdict == "source_url_extracted" and not row.get("extracted_source_url", "").startswith(("http://", "https://")):
            return False, "source_url_extracted without http(s) extracted_source_url", Counter()
    return True, "ok", Counter(row[config.verdict_field] for row in result_rows)


def lane_loop(args: argparse.Namespace) -> int:
    config = TASKS[args.task]
    empty_rounds = 0
    while True:
        batch_dir = allocate_batch(config, args.lane_id, args.batch_size)
        if batch_dir is None:
            empty_rounds += 1
            if empty_rounds >= args.empty_exit_rounds:
                print(json.dumps({"lane_id": args.lane_id, "task": config.task, "status": "empty", "timestamp": utc_now()}), flush=True)
                return 0
            time.sleep(args.sleep_empty_seconds)
            continue
        empty_rounds = 0
        print(json.dumps({"lane_id": args.lane_id, "task": config.task, "batch": str(batch_dir), "status": "allocated"}), flush=True)
        returncode = run_hermes(config, batch_dir, args.provider, args.model, args.max_turns)
        ok, reason, counts = validate_batch(config, batch_dir)
        if ok and returncode == 0:
            update_manifest(batch_dir, status="complete", completed_at_utc=utc_now(), hermes_returncode=returncode, verdict_counts=dict(sorted(counts.items())))
            print(json.dumps({"lane_id": args.lane_id, "task": config.task, "batch": str(batch_dir), "status": "complete", "verdict_counts": dict(sorted(counts.items()))}), flush=True)
        else:
            update_manifest(batch_dir, status="failed", failed_at_utc=utc_now(), hermes_returncode=returncode, failure_reason=reason)
            print(json.dumps({"lane_id": args.lane_id, "task": config.task, "batch": str(batch_dir), "status": "failed", "returncode": returncode, "reason": reason}), flush=True)
            time.sleep(args.sleep_after_failure_seconds)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", choices=sorted(TASKS), required=True)
    parser.add_argument("--lane-id", required=True)
    parser.add_argument("--batch-size", type=int, default=24)
    parser.add_argument("--provider", default="openai-codex")
    parser.add_argument("--model", default="gpt-5.5")
    parser.add_argument("--max-turns", type=int, default=120)
    parser.add_argument("--sleep-empty-seconds", type=int, default=120)
    parser.add_argument("--sleep-after-failure-seconds", type=int, default=30)
    parser.add_argument("--empty-exit-rounds", type=int, default=2)
    args = parser.parse_args()
    config = TASKS[args.task]
    if not config.queue.exists():
        print(f"queue not found: {config.queue}")
        return 2
    return lane_loop(args)


if __name__ == "__main__":
    raise SystemExit(main())
