#!/usr/bin/env python3
"""Print a compact LIMEN processing status payload."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from datetime import datetime, timezone


ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW = ROOT / "results" / "review-candidates"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def iv(value: object) -> int:
    try:
        return int(value or 0)
    except Exception:
        return 0


def tmux_sessions() -> list[str]:
    try:
        proc = subprocess.run(["tmux", "ls"], text=True, capture_output=True, timeout=8)
    except Exception:
        return []
    if proc.returncode != 0:
        return []
    return [line.split(":", 1)[0] for line in proc.stdout.splitlines() if line.strip()]


def latest_cpu() -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    base = ROOT / "results" / "cpu-mining"
    for shard in sorted(path for path in base.glob("*") if path.is_dir()):
        summaries = sorted(shard.glob("*/summary.json"), key=lambda path: path.parent.name)
        if not summaries:
            continue
        data = read_json(summaries[-1])
        out.append(
            {
                "shard": shard.name,
                "run_id": summaries[-1].parent.name,
                "matches": iv(data.get("match_count")),
            }
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    candidate = read_json(REVIEW / "review-candidate-status.json")
    rollup = read_json(REVIEW / "review-rollup-status.json")
    direct = read_json(REVIEW / "bulk-source-review-routing-status.json")
    hardening = read_json(REVIEW / "hardening-review-rollup-status.json")
    bulk = read_json(REVIEW / "bulk-review-rollup-status.json")
    packet = read_json(REVIEW / "reviewed-core-promotion-packet-status.json")
    case_extraction = read_json(REVIEW / "reviewed-core-case-extraction-rollup-status.json")
    case_review = read_json(REVIEW / "reviewed-core-case-hardening-review-status.json")
    case_autoreview = read_json(REVIEW / "reviewed-core-case-autoreview-status.json")

    hardening_tasks = hardening.get("tasks", {}) if isinstance(hardening.get("tasks", {}), dict) else {}
    url_task = hardening_tasks.get("named-url-extraction", {}) if isinstance(hardening_tasks.get("named-url-extraction", {}), dict) else {}
    translation_task = (
        hardening_tasks.get("translation-source-review", {})
        if isinstance(hardening_tasks.get("translation-source-review", {}), dict)
        else {}
    )
    bulk_tasks = bulk.get("tasks", {}) if isinstance(bulk.get("tasks", {}), dict) else {}

    sessions = tmux_sessions()
    mining_sessions = sorted(session for session in sessions if session.startswith("limen-cpu-miner-"))
    stop_files = sorted(path.name for path in Path("/srv/tyche").glob("STOP-limen-cpu-miner-*"))

    payload = {
        "generated_at_utc": utc_now(),
        "mining": {
            "running_sessions": mining_sessions,
            "stopped": not mining_sessions,
            "stop_files": stop_files,
        },
        "review": {
            "raw_rows": iv(candidate.get("raw_rows")),
            "self_echo_rows_excluded": iv(candidate.get("self_echo_rows_excluded")),
            "candidate_rows": iv(rollup.get("candidate_rows") or candidate.get("review_candidate_rows")),
            "first_pass_reviewed_rows": iv(rollup.get("first_pass_reviewed_rows")),
            "direct_source_queue_rows": iv(direct.get("current_queue_rows") or rollup.get("direct_source_review_queue_rows")),
            "direct_source_reviewed_rows": iv(direct.get("current_queue_reviewed_rows")),
            "direct_source_missing_rows": iv(direct.get("current_queue_missing_rows")),
        },
        "hardening": {
            "current_output_clean": bool(hardening.get("current_output_clean")),
            "url": {
                "queue_rows": iv(url_task.get("queue_rows")),
                "result_rows": iv(url_task.get("result_rows")),
                "missing_rows": len(url_task.get("missing_row_ids") or []),
                "stale_extra_rows": iv(url_task.get("stale_extra_result_row_count")),
            },
            "translation": {
                "queue_rows": iv(translation_task.get("queue_rows")),
                "result_rows": iv(translation_task.get("result_rows")),
                "missing_rows": len(translation_task.get("missing_row_ids") or []),
                "stale_extra_rows": iv(translation_task.get("stale_extra_result_row_count")),
            },
        },
        "bulk": {
            "current_output_clean": bool(bulk.get("current_output_clean")),
            "tasks": {
                name: {
                    "queue_rows": iv(task.get("queue_rows")),
                    "completed_rows": iv(task.get("completed_unique_queue_ids")),
                    "missing_rows": iv(task.get("missing_queue_ids")),
                }
                for name, task in sorted(bulk_tasks.items())
                if isinstance(task, dict)
            },
        },
        "promotion": {
            "packet_rows": iv(packet.get("packet_rows")),
            "source_clusters": iv(packet.get("unique_source_clusters")),
            "reviewed_core_ready_now": iv(packet.get("reviewed_core_ready_now")),
            "obscure_ai_ready_now": iv(packet.get("obscure_ai_ready_now") or case_review.get("obscure_ai_ready_now")),
        },
        "case_extraction": {
            "queue_rows": iv(case_extraction.get("queue_rows")),
            "completed_rows": iv(case_extraction.get("completed_unique_source_clusters")),
            "missing_rows": iv(case_extraction.get("missing_source_clusters")),
            "current_output_clean": bool(case_extraction.get("current_output_clean")),
            "case_candidate_rows": iv(case_extraction.get("case_candidate_rows")),
        },
        "case_hardening": {
            "review_rows": iv(case_review.get("case_hardening_review_rows")),
            "ready_for_human_acceptance": iv(case_review.get("reviewed_core_ready_for_human_acceptance")),
            "final_adjudication_rows": iv(case_review.get("case_final_adjudication_rows")),
            "final_promoted_rows": iv(case_review.get("case_final_promoted_rows")),
            "final_obscure_ai_promoted_rows": iv(case_review.get("case_final_obscure_ai_promoted_rows")),
        },
        "case_autoreview": {
            "rows": iv(case_autoreview.get("rows")),
            "already_final_adjudicated_rows": iv(case_autoreview.get("already_final_adjudicated_rows")),
            "rows_without_final_adjudication": iv(case_autoreview.get("rows_without_final_adjudication")),
            "paid_token_required_rows": iv(case_autoreview.get("paid_token_required_rows")),
            "human_acceptance_required_rows": iv(case_autoreview.get("human_acceptance_required_rows")),
            "token_free_auto_close_rows": iv(case_autoreview.get("token_free_auto_close_rows")),
            "token_free_promotion_candidate_rows": iv(case_autoreview.get("token_free_promotion_candidate_rows")),
        },
        "latest_cpu": latest_cpu(),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
