#!/usr/bin/env python3
"""Run Hermes/Codex lanes for LIMEN source-surface case extraction."""

from __future__ import annotations

import argparse
import csv
import fcntl
import json
import subprocess
import time
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
QUEUE = REVIEW_ROOT / "reviewed-core-source-surface-disposition-v0.1.tsv"
BATCH_ROOT = REVIEW_ROOT / "case-extraction-batches"

RESULT_FILE = "case-extraction-results.tsv"
SUMMARY_FILE = "case-extraction-summary.md"
PROMPT_FILE = "case-extraction-prompt.md"
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
VALID_VERDICTS = {
    "case_candidate_for_hardening",
    "closed_duplicate_existing_core",
    "closed_noncase_source_surface",
    "blocked_no_public_source",
    "needs_original_source_text",
    "reject_noise",
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


def completed_ids() -> set[str]:
    ids: set[str] = set()
    for path in sorted(BATCH_ROOT.glob(f"*/{RESULT_FILE}")):
        try:
            for row in load_tsv(path):
                key = row.get("source_cluster_key", "")
                if key:
                    ids.add(key)
        except Exception:
            continue
    return ids


def active_ids() -> set[str]:
    ids: set[str] = set()
    for manifest_path in sorted(BATCH_ROOT.glob("*/manifest.json")):
        if (manifest_path.parent / RESULT_FILE).exists():
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
                key = row.get("source_cluster_key", "")
                if key:
                    ids.add(key)
        except Exception:
            continue
    return ids


def allocate_batch(lane_id: str, batch_size: int) -> Path | None:
    BATCH_ROOT.mkdir(parents=True, exist_ok=True)
    lock_path = BATCH_ROOT / ".lease.lock"
    with lock_path.open("a+", encoding="utf-8") as lock_fh:
        fcntl.flock(lock_fh, fcntl.LOCK_EX)
        queue_rows = load_tsv(QUEUE)
        done = completed_ids()
        active = active_ids()
        selected = [
            row
            for row in queue_rows
            if row.get("source_cluster_key") and row["source_cluster_key"] not in done and row["source_cluster_key"] not in active
        ][:batch_size]
        if not selected:
            return None
        batch_id = f"{stamp()}-{lane_id}-{uuid.uuid4().hex[:8]}"
        batch_dir = BATCH_ROOT / batch_id
        write_tsv(batch_dir / "input.tsv", selected, list(selected[0].keys()))
        write_json(
            batch_dir / "manifest.json",
            {
                "batch_id": batch_id,
                "task": "source-surface-case-extraction",
                "batch_size": batch_size,
                "created_at_utc": utc_now(),
                "input": str(batch_dir / "input.tsv"),
                "input_rows": len(selected),
                "lane_id": lane_id,
                "queue": str(QUEUE),
                "queue_rows": len(queue_rows),
                "remaining_unleased_at_allocation": sum(
                    1
                    for row in queue_rows
                    if row.get("source_cluster_key") and row["source_cluster_key"] not in done and row["source_cluster_key"] not in active
                ),
                "status": "leased",
                "updated_at_utc": utc_now(),
            },
        )
        return batch_dir


def prompt_for_batch(batch_dir: Path) -> str:
    input_path = batch_dir / "input.tsv"
    result_path = batch_dir / RESULT_FILE
    summary_path = batch_dir / SUMMARY_FILE
    manifest_path = batch_dir / "manifest.json"
    return f"""You are Hermes/Codex performing LIMEN source-surface case extraction.

Input TSV:
{input_path}

Required outputs:
{result_path}
{summary_path}

Update this manifest when complete:
{manifest_path}

Task:
- Review every source_cluster_key in input.tsv exactly once.
- Your goal is to decide whether the cluster contains a concrete AI edge-case suitable for later reviewed-core/ObscureAI hardening, or whether it is finally a noncase source surface.
- Use the input row metadata. You may inspect exact local file locators and exact public URLs present in source_url_or_locator. Do not broad crawl, search the web generally, or invent URLs.
- Do not submit, publish, email, upload, register, pay, log into portals, or take public actions.
- Do not promote anything. This is extraction only.
- A case candidate must have a concrete event/action/vulnerability/finding/official record, a public source URL or precise locator, and a bounded claim that does not overread legality, safety, compliance, deployment, prevalence, or guilt.
- Scholarly DOI/index pages, algorithm registers, policy/guidance/law text, patents, vendor docs, product pages, and generic source-family surfaces are usually closed_noncase_source_surface unless they explicitly contain a concrete edge-case event/finding.

Write case-extraction-results.tsv with exactly this header:
source_cluster_key	case_extraction_verdict	source_url_or_locator	source_name	source_host	proposed_case_title	proposed_evidence_tier	proposed_limen_categories	source_record_date	jurisdiction	bounded_claim_candidate	claim_ceiling	forbidden_overread	rationale	required_before_reviewed_core	required_before_obscure_ai	next_action

Allowed case_extraction_verdict values:
- case_candidate_for_hardening
- closed_duplicate_existing_core
- closed_noncase_source_surface
- blocked_no_public_source
- needs_original_source_text
- reject_noise

Use one row per input source_cluster_key, no omissions, no extras, no duplicate source_cluster_key values.
Keep fields concise. Replace tabs/newlines inside fields with spaces.
Before stopping, verify that the result TSV has exactly the same source_cluster_key set and row count as input.tsv.
Boundary: no reviewed-core promotion, no ObscureAI addition, no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, or ranking claim.
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
    prompt = prompt_for_batch(batch_dir)
    (batch_dir / PROMPT_FILE).write_text(prompt, encoding="utf-8")
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
        "limen-source-surface-case-extraction",
        "--yolo",
        "--quiet",
        "--query",
        prompt,
    ]
    with (batch_dir / "hermes.log").open("w", encoding="utf-8") as log_fh:
        proc = subprocess.run(cmd, cwd=str(PROJECT_ROOT), text=True, stdout=log_fh, stderr=subprocess.STDOUT)
    return proc.returncode


def validate_batch(batch_dir: Path) -> tuple[bool, str, Counter[str]]:
    input_rows = load_tsv(batch_dir / "input.tsv")
    result_path = batch_dir / RESULT_FILE
    if not result_path.exists():
        return False, f"missing {RESULT_FILE}", Counter()
    with result_path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != RESULT_FIELDS:
            return False, f"unexpected result header: {reader.fieldnames}", Counter()
    result_rows = load_tsv(result_path)
    if len(result_rows) != len(input_rows):
        return False, f"row count mismatch: input={len(input_rows)} result={len(result_rows)}", Counter()
    input_ids = [row["source_cluster_key"] for row in input_rows]
    result_ids = [row.get("source_cluster_key", "") for row in result_rows]
    if set(input_ids) != set(result_ids):
        return False, "source_cluster_key set mismatch", Counter()
    if len(result_ids) != len(set(result_ids)):
        return False, "duplicate source_cluster_key in result", Counter()
    for row in result_rows:
        if None in row:
            return False, "extra TSV columns detected, likely embedded tab", Counter()
        verdict = row.get("case_extraction_verdict", "")
        if verdict not in VALID_VERDICTS:
            return False, f"invalid verdict: {verdict}", Counter()
        if verdict == "case_candidate_for_hardening" and not row.get("bounded_claim_candidate", "").strip():
            return False, "case candidate missing bounded_claim_candidate", Counter()
    return True, "ok", Counter(row["case_extraction_verdict"] for row in result_rows)


def lane_loop(args: argparse.Namespace) -> int:
    empty_rounds = 0
    while True:
        batch_dir = allocate_batch(args.lane_id, args.batch_size)
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
            update_manifest(batch_dir, status="complete", completed_at_utc=utc_now(), hermes_returncode=returncode, verdict_counts=dict(sorted(counts.items())))
            print(json.dumps({"lane_id": args.lane_id, "batch": str(batch_dir), "status": "complete", "verdict_counts": dict(sorted(counts.items()))}), flush=True)
        else:
            update_manifest(batch_dir, status="failed", failed_at_utc=utc_now(), hermes_returncode=returncode, failure_reason=reason)
            print(json.dumps({"lane_id": args.lane_id, "batch": str(batch_dir), "status": "failed", "returncode": returncode, "reason": reason}), flush=True)
            time.sleep(args.sleep_after_failure_seconds)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lane-id", required=True)
    parser.add_argument("--batch-size", type=int, default=24)
    parser.add_argument("--provider", default="openai-codex")
    parser.add_argument("--model", default="gpt-5.5")
    parser.add_argument("--max-turns", type=int, default=160)
    parser.add_argument("--sleep-empty-seconds", type=int, default=120)
    parser.add_argument("--sleep-after-failure-seconds", type=int, default=30)
    parser.add_argument("--empty-exit-rounds", type=int, default=2)
    args = parser.parse_args()
    if not QUEUE.exists():
        print(f"queue not found: {QUEUE}")
        return 2
    return lane_loop(args)


if __name__ == "__main__":
    raise SystemExit(main())
