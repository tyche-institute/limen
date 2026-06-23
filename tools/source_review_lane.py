#!/usr/bin/env python3
"""Drain LIMEN direct-source review queue batches through Hermes/Codex lanes."""

from __future__ import annotations

import argparse
import csv
import fcntl
import json
import os
import subprocess
import sys
import time
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
DEFAULT_QUEUE = REVIEW_ROOT / "direct-source-review-queue.tsv"
BATCH_ROOT = REVIEW_ROOT / "source-review-batches"
LOCK_PATH = BATCH_ROOT / ".source-review-lease.lock"
VALID_VERDICTS = {
    "source_reviewed_candidate",
    "merge_existing_surface",
    "negative_evidence_candidate",
    "needs_named_source_extraction",
    "translation_review_needed",
    "reject_noise",
}
RESULT_FIELDS = [
    "signal_id",
    "source_review_verdict",
    "source_review_role",
    "reason",
    "claim_ceiling",
    "next_action",
    "source_path",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, delimiter="\t", fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    tmp.replace(path)


def completed_ids() -> set[str]:
    ids: set[str] = set()
    for path in sorted(BATCH_ROOT.glob("*/source-review-results.tsv")):
        try:
            for row in load_tsv(path):
                signal_id = row.get("signal_id", "")
                if signal_id:
                    ids.add(signal_id)
        except Exception:
            continue
    return ids


def active_ids() -> set[str]:
    ids: set[str] = set()
    for manifest_path in sorted(BATCH_ROOT.glob("*/manifest.json")):
        result_path = manifest_path.parent / "source-review-results.tsv"
        if result_path.exists():
            continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if manifest.get("status") not in {"leased", "running"}:
            continue
        input_path = manifest_path.parent / "source-review-input.tsv"
        if not input_path.exists():
            continue
        try:
            for row in load_tsv(input_path):
                signal_id = row.get("signal_id", "")
                if signal_id:
                    ids.add(signal_id)
        except Exception:
            continue
    return ids


def allocate_batch(queue: Path, lane_id: str, batch_size: int) -> Path | None:
    BATCH_ROOT.mkdir(parents=True, exist_ok=True)
    with LOCK_PATH.open("a+", encoding="utf-8") as lock_fh:
        fcntl.flock(lock_fh, fcntl.LOCK_EX)
        queue_rows = load_tsv(queue)
        done = completed_ids()
        active = active_ids()
        selected = [
            row
            for row in queue_rows
            if row.get("signal_id", "") and row.get("signal_id", "") not in done and row.get("signal_id", "") not in active
        ][:batch_size]
        if not selected:
            return None

        batch_id = f"{stamp()}-{lane_id}-{uuid.uuid4().hex[:8]}"
        batch_dir = BATCH_ROOT / batch_id
        input_path = batch_dir / "source-review-input.tsv"
        manifest_path = batch_dir / "manifest.json"
        fields = list(selected[0].keys())
        write_tsv(input_path, selected, fields)
        manifest = {
            "batch_id": batch_id,
            "batch_size": batch_size,
            "created_at_utc": utc_now(),
            "input": str(input_path),
            "input_rows": len(selected),
            "lane_id": lane_id,
            "queue": str(queue),
            "queue_rows": len(queue_rows),
            "remaining_unleased_at_allocation": sum(
                1
                for row in queue_rows
                if row.get("signal_id", "") and row.get("signal_id", "") not in done and row.get("signal_id", "") not in active
            ),
            "status": "leased",
            "updated_at_utc": utc_now(),
        }
        write_json(manifest_path, manifest)
        return batch_dir


def prompt_for_batch(batch_dir: Path) -> str:
    input_path = batch_dir / "source-review-input.tsv"
    result_path = batch_dir / "source-review-results.tsv"
    summary_path = batch_dir / "source-review-summary.md"
    manifest_path = batch_dir / "manifest.json"
    return f"""You are Hermes/Codex performing a bounded LIMEN source-review batch.

Input TSV:
{input_path}

Required outputs:
{result_path}
{summary_path}

Update this manifest status/details when complete:
{manifest_path}

Task:
- Review every row in source-review-input.tsv exactly once.
- Use local metadata and local source files only. Do not broad web crawl. Do not email, upload, submit, publish, register, pay, deploy, or take public/portal actions.
- This is source-surface triage only. Do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- If a local source_path exists and the needed evidence is local, you may inspect only the relevant local lines/nearby context. If it is too large or unavailable, classify from the local row metadata and say so in the reason.

Write source-review-results.tsv with exactly this header:
signal_id	source_review_verdict	source_review_role	reason	claim_ceiling	next_action	source_path

Allowed source_review_verdict values:
- source_reviewed_candidate
- merge_existing_surface
- negative_evidence_candidate
- needs_named_source_extraction
- translation_review_needed
- reject_noise

Rubric:
- source_reviewed_candidate: row names a concrete official, regulator, institutional, vendor/advisory, court, register, procurement, notice, or other direct source surface sufficient for bounded source-surface existence review.
- translation_review_needed: row names a plausible direct source surface but the local evidence is materially non-English or translation-sensitive.
- needs_named_source_extraction: row is a source-pack, country profile, index row, wrapper, or adjacent artifact that points toward a source but does not expose a named reviewable source surface yet.
- negative_evidence_candidate: row records a search-negative, gap warning, weak-source warning, or absence/evidence-limit result.
- merge_existing_surface: row duplicates or points to an already-modeled local registry/dashboard/atlas surface and should be deduplicated rather than promoted again.
- reject_noise: row is internal manuscript/prose/script/config/log/package noise or another derived artifact that should not remain in the direct-source queue.

Keep reasons concise. Replace tabs and newlines inside fields with spaces.
Write one output row per input signal_id, no omissions, no extras, no duplicate signal_id values.

Write source-review-summary.md with:
- batch id
- rows reviewed
- verdict counts
- boundary statement
- next smallest queue-hardening move

Before stopping, verify that source-review-results.tsv has exactly the same signal_id set and row count as source-review-input.tsv.
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


def run_hermes(batch_dir: Path, provider: str, model: str, max_turns: int) -> int:
    update_manifest(batch_dir, status="running", started_at_utc=utc_now())
    prompt_path = batch_dir / "source-review-prompt.md"
    prompt = prompt_for_batch(batch_dir)
    prompt_path.write_text(prompt, encoding="utf-8")
    log_path = batch_dir / "hermes.log"
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
        "limen-source-review",
        "--yolo",
        "--quiet",
        "--query",
        prompt,
    ]
    with log_path.open("w", encoding="utf-8") as log_fh:
        proc = subprocess.run(
            cmd,
            cwd=str(PROJECT_ROOT),
            text=True,
            stdout=log_fh,
            stderr=subprocess.STDOUT,
        )
    return proc.returncode


def validate_batch(batch_dir: Path) -> tuple[bool, str, Counter[str]]:
    input_rows = load_tsv(batch_dir / "source-review-input.tsv")
    result_path = batch_dir / "source-review-results.tsv"
    if not result_path.exists():
        return False, "missing source-review-results.tsv", Counter()
    with result_path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != RESULT_FIELDS:
            return False, f"unexpected result header: {reader.fieldnames}", Counter()
    result_rows = load_tsv(result_path)
    if len(result_rows) != len(input_rows):
        return False, f"row count mismatch: input={len(input_rows)} result={len(result_rows)}", Counter()
    input_ids = [row["signal_id"] for row in input_rows]
    result_ids = [row.get("signal_id", "") for row in result_rows]
    if set(input_ids) != set(result_ids):
        return False, "signal_id set mismatch", Counter()
    if len(result_ids) != len(set(result_ids)):
        return False, "duplicate signal_id in result", Counter()
    for row in result_rows:
        if None in row:
            return False, "extra TSV columns detected, likely embedded tab", Counter()
        verdict = row.get("source_review_verdict", "")
        if verdict not in VALID_VERDICTS:
            return False, f"invalid verdict: {verdict}", Counter()
        for field in RESULT_FIELDS:
            if field not in row:
                return False, f"missing field: {field}", Counter()
    return True, "ok", Counter(row["source_review_verdict"] for row in result_rows)


def lane_loop(args: argparse.Namespace) -> int:
    empty_rounds = 0
    while True:
        batch_dir = allocate_batch(args.queue, args.lane_id, args.batch_size)
        if batch_dir is None:
            empty_rounds += 1
            if empty_rounds >= args.empty_exit_rounds:
                print(json.dumps({"lane_id": args.lane_id, "status": "empty", "timestamp": utc_now()}), flush=True)
                return 0
            time.sleep(args.sleep_empty_seconds)
            continue
        empty_rounds = 0
        print(json.dumps({"lane_id": args.lane_id, "batch": str(batch_dir), "status": "allocated"}), flush=True)
        returncode = run_hermes(batch_dir, args.provider, args.model, args.max_turns)
        ok, reason, counts = validate_batch(batch_dir)
        if ok and returncode == 0:
            update_manifest(
                batch_dir,
                status="complete",
                completed_at_utc=utc_now(),
                hermes_returncode=returncode,
                verdict_counts=dict(sorted(counts.items())),
            )
            print(
                json.dumps(
                    {
                        "lane_id": args.lane_id,
                        "batch": str(batch_dir),
                        "status": "complete",
                        "verdict_counts": dict(sorted(counts.items())),
                    }
                ),
                flush=True,
            )
        else:
            update_manifest(
                batch_dir,
                status="failed",
                failed_at_utc=utc_now(),
                hermes_returncode=returncode,
                failure_reason=reason,
            )
            print(
                json.dumps(
                    {
                        "lane_id": args.lane_id,
                        "batch": str(batch_dir),
                        "status": "failed",
                        "returncode": returncode,
                        "reason": reason,
                    }
                ),
                flush=True,
            )
            time.sleep(args.sleep_after_failure_seconds)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lane-id", required=True)
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--provider", default="openai-codex")
    parser.add_argument("--model", default="gpt-5.4")
    parser.add_argument("--max-turns", type=int, default=140)
    parser.add_argument("--sleep-empty-seconds", type=int, default=120)
    parser.add_argument("--sleep-after-failure-seconds", type=int, default=30)
    parser.add_argument("--empty-exit-rounds", type=int, default=2)
    args = parser.parse_args()
    if not args.queue.exists():
        print(f"queue not found: {args.queue}", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(lane_loop(args))


if __name__ == "__main__":
    main()
