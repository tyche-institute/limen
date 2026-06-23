#!/usr/bin/env python3
"""Audit which LIMEN review layers can run without paid model tokens.

The output is intentionally operational: it separates deterministic local
closure from source-text interpretation layers that still need Hermes, Codex,
or human review when new backlog appears.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
OUT = PROJECT_ROOT / "runtime" / "limen-token-free-review-audit-latest.json"
SUMMARY = REVIEW_ROOT / "token-free-review-audit-summary-v0.1.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def iv(value: Any) -> int:
    try:
        return int(value or 0)
    except Exception:
        return 0


def truthy(value: Any) -> bool:
    if isinstance(value, (dict, list, tuple, set)):
        return bool(value)
    return bool(value) and value not in {"0", "false", "False", "no", "No"}


def layer(
    name: str,
    mode: str,
    complete: bool,
    rows: int = 0,
    missing: int = 0,
    paid_token_need: int = 0,
    human_need: int = 0,
    note: str = "",
) -> dict[str, Any]:
    return {
        "name": name,
        "mode": mode,
        "complete": bool(complete),
        "rows": rows,
        "missing_rows": missing,
        "paid_token_required_rows": paid_token_need,
        "human_required_rows": human_need,
        "note": note,
    }


def build(project_root: Path) -> dict[str, Any]:
    review_root = project_root / "results" / "review-candidates"
    candidate = read_json(review_root / "review-candidate-status.json")
    first_pass = read_json(review_root / "review-rollup-status.json")
    direct = read_json(review_root / "bulk-source-review-routing-status.json")
    source_hardening = read_json(review_root / "source-reviewed-promotion-hardening-status.json")
    completion = read_json(review_root / "source-reviewed-completion-ledger-status.json")
    hardening_rollup = read_json(review_root / "hardening-review-rollup-status.json")
    bulk = read_json(review_root / "bulk-review-rollup-status.json")
    promotion = read_json(review_root / "reviewed-core-promotion-packet-status.json")
    case_extraction = read_json(review_root / "reviewed-core-case-extraction-rollup-status.json")
    case_hardening = read_json(review_root / "reviewed-core-case-hardening-review-status.json")
    case_autoreview = read_json(review_root / "reviewed-core-case-autoreview-status.json")
    translation_hold = read_json(review_root / "translation-held-review-status.json")

    hardening_tasks = hardening_rollup.get("tasks", {}) if isinstance(hardening_rollup.get("tasks"), dict) else {}
    bulk_tasks = bulk.get("tasks", {}) if isinstance(bulk.get("tasks"), dict) else {}

    layers: list[dict[str, Any]] = []
    layers.append(
        layer(
            "candidate_materialization",
            "deterministic_no_tokens",
            iv(candidate.get("review_candidate_rows")) == iv(first_pass.get("candidate_rows")),
            rows=iv(candidate.get("review_candidate_rows")),
            note="Materializes non-self mined rows as review candidates; no model call.",
        )
    )
    layers.append(
        layer(
            "first_pass_candidate_review",
            "deterministic_no_tokens",
            iv(first_pass.get("candidate_rows")) == iv(first_pass.get("first_pass_reviewed_rows")),
            rows=iv(first_pass.get("first_pass_reviewed_rows")),
            missing=max(0, iv(first_pass.get("candidate_rows")) - iv(first_pass.get("first_pass_reviewed_rows"))),
            note="Rule-based triage only; not reviewed-core promotion.",
        )
    )
    layers.append(
        layer(
            "direct_source_review",
            "hermes_or_human_when_backlog_exists",
            iv(direct.get("current_queue_rows")) == iv(direct.get("current_queue_reviewed_rows"))
            and iv(direct.get("current_queue_missing_rows")) == 0,
            rows=iv(direct.get("current_queue_reviewed_rows")),
            missing=iv(direct.get("current_queue_missing_rows")),
            paid_token_need=iv(direct.get("current_queue_missing_rows")),
            note="Current queue is closed; future new rows need source interpretation unless deterministic rules close them first.",
        )
    )
    translation_task = (
        hardening_tasks.get("translation-source-review", {})
        if isinstance(hardening_tasks.get("translation-source-review", {}), dict)
        else {}
    )
    translation_downstream_complete = bool(translation_task.get("complete")) and not translation_task.get("missing_row_ids")
    layers.append(
        layer(
            "translation_hold_board",
            "deterministic_no_tokens_for_board_only",
            truthy(translation_hold),
            rows=iv(translation_hold.get("translation_hold_rows")),
            human_need=0 if translation_downstream_complete else iv(translation_hold.get("translation_hold_rows")),
            note="Board creation is free; downstream translation-source review is separately tracked before any promotion.",
        )
    )
    for task_name, task in sorted(hardening_tasks.items()):
        if not isinstance(task, dict):
            continue
        layers.append(
            layer(
                f"hardening_{task_name}",
                "hermes_or_human_when_backlog_exists",
                bool(task.get("complete")) and not task.get("missing_row_ids"),
                rows=iv(task.get("result_rows") or task.get("queue_rows")),
                missing=len(task.get("missing_row_ids") or []),
                paid_token_need=len(task.get("missing_row_ids") or []),
                note="Bounded source-review aid; not reviewed-core promotion.",
            )
        )
    for task_name, task in sorted(bulk_tasks.items()):
        if not isinstance(task, dict):
            continue
        layers.append(
            layer(
                f"bulk_{task_name}",
                "hermes_or_human_when_backlog_exists",
                iv(task.get("missing_queue_ids")) == 0 and not task.get("failed_batches"),
                rows=iv(task.get("completed_unique_queue_ids")),
                missing=iv(task.get("missing_queue_ids")),
                paid_token_need=iv(task.get("missing_queue_ids")),
                note="Bulk semantic lanes are already drained; rollup itself is local.",
            )
        )
    layers.extend(
        [
            layer(
                "source_review_promotion_hardening",
                "deterministic_no_tokens",
                truthy(source_hardening),
                rows=iv(source_hardening.get("source_reviewed_candidate_rows")),
                note="Classifies reviewed source surfaces into bounded promotion gates.",
            ),
            layer(
                "source_review_completion_ledger",
                "deterministic_no_tokens",
                iv(completion.get("source_reviewed_rows")) == iv(completion.get("completed_rows")),
                rows=iv(completion.get("completed_rows")),
                note="Closes the source-reviewed layer without adding reviewed-core or ObscureAI rows.",
            ),
            layer(
                "reviewed_core_promotion_packet",
                "deterministic_no_tokens",
                iv(promotion.get("direct_source_queue_rows")) == iv(promotion.get("direct_source_queue_reviewed_rows")),
                rows=iv(promotion.get("packet_rows")),
                note="Builds bounded source-linked packet; no promotion by itself.",
            ),
            layer(
                "case_extraction_rollup",
                "hermes_or_human_when_backlog_exists",
                bool(case_extraction.get("all_complete")) and iv(case_extraction.get("missing_source_clusters")) == 0,
                rows=iv(case_extraction.get("completed_unique_source_clusters")),
                missing=iv(case_extraction.get("missing_source_clusters")),
                paid_token_need=iv(case_extraction.get("missing_source_clusters")),
                note="Current case extraction is complete; future clusters may need semantic extraction lanes.",
            ),
            layer(
                "case_hardening_review",
                "deterministic_fetch_no_model_tokens",
                truthy(case_hardening),
                rows=iv(case_hardening.get("case_hardening_review_rows")),
                human_need=iv(case_hardening.get("reviewed_core_ready_for_human_acceptance")),
                note="Fetches/checks public sources and drafts bounded claims; human acceptance remains the boundary.",
            ),
            layer(
                "case_autoreview",
                "deterministic_no_tokens",
                truthy(case_autoreview),
                rows=iv(case_autoreview.get("rows")),
                paid_token_need=iv(case_autoreview.get("paid_token_required_rows")),
                human_need=iv(case_autoreview.get("human_acceptance_required_rows")),
                note="Creates deterministic final recommendations/draft adjudication; never calls an LLM.",
            ),
        ]
    )

    paid_rows = sum(iv(item.get("paid_token_required_rows")) for item in layers)
    human_rows = sum(iv(item.get("human_required_rows")) for item in layers)
    missing_rows = sum(iv(item.get("missing_rows")) for item in layers)
    incomplete_layers = [item["name"] for item in layers if not item["complete"]]
    current_blockers: list[dict[str, Any]] = []
    if missing_rows:
        current_blockers.append({"code": "missing_review_rows", "rows": missing_rows})
    if paid_rows:
        current_blockers.append({"code": "paid_token_review_rows", "rows": paid_rows})

    return {
        "generated_at_utc": utc_now(),
        "ok": not current_blockers,
        "current_paid_token_required_rows": paid_rows,
        "current_human_required_rows": human_rows,
        "current_missing_review_rows": missing_rows,
        "incomplete_layers": incomplete_layers,
        "layers": layers,
        "recommended_no_token_command": "tools/limen_case_review_no_tokens.sh --refresh-frontends",
        "recommended_health_command": "tools/limen_doctor.py --pretty",
        "blockers": current_blockers,
        "boundary": "Audit only. It does not mine, call models, promote reviewed-core rows, add ObscureAI cases, or deploy.",
    }


def write_outputs(payload: dict[str, Any], out: Path, summary: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "# LIMEN token-free review audit",
        "",
        f"- Generated: `{payload['generated_at_utc']}`",
        f"- Current paid-token-required rows: `{payload['current_paid_token_required_rows']}`",
        f"- Current human-required rows: `{payload['current_human_required_rows']}`",
        f"- Current missing review rows: `{payload['current_missing_review_rows']}`",
        f"- Incomplete layers: `{', '.join(payload['incomplete_layers']) if payload['incomplete_layers'] else 'none'}`",
        "",
        "| Layer | Mode | Complete | Rows | Missing | Paid-token rows | Human rows |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for item in payload["layers"]:
        lines.append(
            "| {name} | {mode} | {complete} | {rows} | {missing_rows} | {paid_token_required_rows} | {human_required_rows} |".format(
                **item
            )
        )
    lines.extend(["", str(payload["boundary"]), ""])
    summary.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(PROJECT_ROOT))
    parser.add_argument("--out", default=str(OUT))
    parser.add_argument("--summary", default=str(SUMMARY))
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    payload = build(Path(args.project_root))
    write_outputs(payload, Path(args.out), Path(args.summary))
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
