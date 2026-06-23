#!/usr/bin/env python3
"""Run Hermes/Codex lanes for LIMEN hardening-review queues."""

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
QUEUE_ROOT = REVIEW_ROOT / "hardening-review-queues"
BATCH_ROOT = REVIEW_ROOT / "hardening-review-batches"


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
    valid_verdicts: set[str]


TASKS = {
    "url": TaskConfig(
        task="named-url-extraction",
        queue=QUEUE_ROOT / "named-url-extraction-queue.tsv",
        batch_subdir="named-url-extraction",
        result_file="named-url-extraction-results.tsv",
        summary_file="named-url-extraction-summary.md",
        prompt_file="named-url-extraction-prompt.md",
        source_tag="limen-named-url-extraction",
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
        valid_verdicts={
            "url_extracted",
            "source_path_is_snapshot_only",
            "wrapper_needs_parent_source",
            "duplicate_or_existing_core",
            "reject_noise",
        },
    ),
    "translation": TaskConfig(
        task="translation-source-review",
        queue=QUEUE_ROOT / "translation-source-review-queue.tsv",
        batch_subdir="translation-source-review",
        result_file="translation-source-review-results.tsv",
        summary_file="translation-source-review-summary.md",
        prompt_file="translation-source-review-prompt.md",
        source_tag="limen-translation-source-review",
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
        valid_verdicts={
            "translation_source_reviewed",
            "needs_original_language_source",
            "cross_project_duplicate",
            "machine_translation_hold",
            "candidate_for_url_extraction",
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


def completed_ids(config: TaskConfig) -> set[str]:
    ids: set[str] = set()
    for path in sorted(task_root(config).glob(f"*/{config.result_file}")):
        try:
            for row in load_tsv(path):
                row_id = row.get("row_id", "")
                if row_id:
                    ids.add(row_id)
        except Exception:
            continue
    return ids


def active_ids(config: TaskConfig) -> set[str]:
    ids: set[str] = set()
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
        try:
            for row in load_tsv(input_path):
                row_id = row.get("row_id", "")
                if row_id:
                    ids.add(row_id)
        except Exception:
            continue
    return ids


def allocate_batch(config: TaskConfig, lane_id: str, batch_size: int) -> Path | None:
    root = task_root(config)
    root.mkdir(parents=True, exist_ok=True)
    lock_path = root / ".lease.lock"
    with lock_path.open("a+", encoding="utf-8") as lock_fh:
        fcntl.flock(lock_fh, fcntl.LOCK_EX)
        queue_rows = load_tsv(config.queue)
        done = completed_ids(config)
        active = active_ids(config)
        selected = [
            row
            for row in queue_rows
            if row.get("row_id", "") and row.get("row_id", "") not in done and row.get("row_id", "") not in active
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
                    if row.get("row_id", "") and row.get("row_id", "") not in done and row.get("row_id", "") not in active
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
    if config.task == "named-url-extraction":
        task_body = """Task:
- Review every row in input.tsv exactly once.
- Use local metadata and local source files only. Inspect only relevant local lines/nearby context.
- Recover a concrete original public URL only when it is explicitly present in local metadata, local source context, or a cache/snapshot locator. Do not invent URLs from hostnames.
- Do not broad web crawl. Do not email, upload, submit, publish, register, pay, deploy, or take public/portal actions.
- This is URL/source-surface hardening only. Do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.

Write named-url-extraction-results.tsv with exactly this header:
row_id	signal_id	url_extraction_verdict	extracted_source_url	source_name	evidence_location	reason	claim_ceiling	next_action

Allowed url_extraction_verdict values:
- url_extracted: an explicit http(s) source URL was recovered locally; extracted_source_url must contain it.
- source_path_is_snapshot_only: local cache/snapshot confirms a source surface but no original URL is locally recoverable.
- wrapper_needs_parent_source: row points to a wrapper/source pack/index that needs parent source extraction first.
- duplicate_or_existing_core: row is already resolved by reviewed-core/source-ledger lineage.
- reject_noise: internal, derivative, or irrelevant noise.
"""
    else:
        task_body = """Task:
- Review every row in input.tsv exactly once.
- Use local metadata and local source files only. You may use multilingual understanding, but do not turn machine translation into a factual/legal claim.
- Do not broad web crawl. Do not email, upload, submit, publish, register, pay, deploy, or take public/portal actions.
- This is translation-aware source review only. Do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.

Write translation-source-review-results.tsv with exactly this header:
row_id	signal_id	translation_review_verdict	language_reviewed	source_url_or_locator	source_name	reason	claim_ceiling	next_action

Allowed translation_review_verdict values:
- translation_source_reviewed: the row has enough original-language or translated local context plus a named source/locator for bounded source-surface review.
- needs_original_language_source: plausible lead, but original-language source/URL is missing or insufficient.
- cross_project_duplicate: derived GAIA/Pallas/Atlas/public-registry artifact that should be routed upstream or deduplicated, not promoted here.
- machine_translation_hold: only machine-translated summary/gloss is present; keep held.
- candidate_for_url_extraction: source clues exist, but the next move is named URL extraction.
- reject_noise: internal, derivative, or irrelevant noise.
"""
    return f"""You are Hermes/Codex performing a bounded LIMEN {config.task} batch.

Input TSV:
{input_path}

Required outputs:
{result_path}
{summary_path}

Update this manifest status/details when complete:
{manifest_path}

{task_body}
Keep reasons concise. Replace tabs and newlines inside fields with spaces.
Write one output row per input row_id, no omissions, no extras, no duplicate row_id values.

Write the summary markdown with:
- batch id
- rows reviewed
- verdict counts
- boundary statement
- next smallest hardening move

Before stopping, verify that the result TSV has exactly the same row_id set and row count as input.tsv.
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
    input_ids = [row["row_id"] for row in input_rows]
    result_ids = [row.get("row_id", "") for row in result_rows]
    if set(input_ids) != set(result_ids):
        return False, "row_id set mismatch", Counter()
    if len(result_ids) != len(set(result_ids)):
        return False, "duplicate row_id in result", Counter()
    verdict_field = "url_extraction_verdict" if config.task == "named-url-extraction" else "translation_review_verdict"
    for row in result_rows:
        if None in row:
            return False, "extra TSV columns detected, likely embedded tab", Counter()
        verdict = row.get(verdict_field, "")
        if verdict not in config.valid_verdicts:
            return False, f"invalid verdict: {verdict}", Counter()
        if config.task == "named-url-extraction" and verdict == "url_extracted" and not row.get("extracted_source_url", "").startswith(("http://", "https://")):
            return False, "url_extracted without http(s) extracted_source_url", Counter()
    return True, "ok", Counter(row[verdict_field] for row in result_rows)


def failure_reason_for(batch_dir: Path, validation_reason: str, returncode: int) -> str:
    log_path = batch_dir / "hermes.log"
    if log_path.exists():
        text = log_path.read_text(encoding="utf-8", errors="replace")
        tail = text[-4000:]
        low = tail.lower()
        if "http 429" in low or "usage limit has been reached" in low:
            return "quota_429: OpenAI Codex usage limit reached"
        for line in tail.splitlines():
            if "API call failed" in line:
                return f"hermes_failed: {line[:220]}; validation={validation_reason}"
    if returncode != 0:
        return f"hermes_returncode_{returncode}: {validation_reason}"
    return validation_reason


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
            update_manifest(
                batch_dir,
                status="complete",
                completed_at_utc=utc_now(),
                hermes_returncode=returncode,
                verdict_counts=dict(sorted(counts.items())),
            )
            print(json.dumps({"lane_id": args.lane_id, "task": config.task, "batch": str(batch_dir), "status": "complete", "verdict_counts": dict(sorted(counts.items()))}), flush=True)
        else:
            failure_reason = failure_reason_for(batch_dir, reason, returncode)
            update_manifest(batch_dir, status="failed", failed_at_utc=utc_now(), hermes_returncode=returncode, failure_reason=failure_reason)
            print(json.dumps({"lane_id": args.lane_id, "task": config.task, "batch": str(batch_dir), "status": "failed", "returncode": returncode, "reason": failure_reason}), flush=True)
            if failure_reason.startswith("quota_429"):
                return 75
            time.sleep(args.sleep_after_failure_seconds)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", choices=sorted(TASKS), required=True)
    parser.add_argument("--lane-id", required=True)
    parser.add_argument("--batch-size", type=int, default=32)
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
