#!/usr/bin/env python3
"""Close the source-reviewed promotion-hardening layer with final dispositions.

This is not reviewed-core promotion. It marks every source-reviewed candidate as
resolved for the current layer: existing core, source-surface anchor only,
wrapper/source extraction residual, or not an ObscureAI case.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
HARDENING = REVIEW_ROOT / "source-reviewed-promotion-hardening-v0.1.tsv"
URL_RESULTS = REVIEW_ROOT / "named-url-extraction-results-v0.1.tsv"
OUT = REVIEW_ROOT / "source-reviewed-completion-ledger-v0.1.tsv"
STATUS = REVIEW_ROOT / "source-reviewed-completion-ledger-status.json"
SUMMARY = REVIEW_ROOT / "source-reviewed-completion-ledger-summary-v0.1.md"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "source-reviewed-completion-ledger.tsv"

FIELDS = [
    "row_id",
    "signal_id",
    "completion_disposition",
    "completion_state",
    "obscure_ai_posture",
    "promotion_gate",
    "promotion_priority",
    "url_extraction_verdict",
    "source_url",
    "source_host",
    "source_surface_class",
    "source_review_role",
    "dedupe_key",
    "cluster_size",
    "title_or_snippet",
    "claim_ceiling",
    "completion_reason",
    "next_bulk_action",
    "forbidden_overread",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def clean(value: str, limit: int = 420) -> str:
    return " ".join((value or "").split())[:limit].rstrip()


def disposition(row: dict[str, str], url_verdict: str) -> tuple[str, str, str, str, str]:
    gate = row.get("promotion_gate", "")
    if gate == "already_reviewed_core_lineage" or url_verdict == "duplicate_or_existing_core":
        return (
            "closed_existing_reviewed_core_or_duplicate",
            "complete_no_new_case",
            "do_not_add_duplicate",
            "Already linked to reviewed core or duplicate lineage; keep only as dedupe/source-lineage evidence.",
            "none",
        )
    if gate == "source_surface_anchor_only":
        return (
            "closed_source_surface_anchor_only",
            "complete_no_case_claim",
            "not_obscure_ai_case",
            "Reviewed public/official source surface, registry, policy, sandbox, or context anchor only; no concrete edge-case record extracted.",
            "move_to_next_bulk_queue",
        )
    if gate == "possible_case_hardening_after_context":
        return (
            "closed_policy_surface_false_positive",
            "complete_no_case_claim",
            "not_obscure_ai_case",
            "Manual context check shows an EU AI Act sandbox/legal text surface, not a concrete edge-case case record.",
            "move_to_next_bulk_queue",
        )
    if gate == "needs_named_url_extraction":
        if url_verdict == "wrapper_needs_parent_source":
            return (
                "residual_parent_source_wrapper",
                "complete_for_current_layer_parent_needed",
                "not_obscure_ai_case",
                "URL extraction reviewed this as a wrapper/source-pack row; parent source selection is required before any case work.",
                "parent_source_extraction_queue",
            )
        if url_verdict == "source_path_is_snapshot_only":
            return (
                "closed_snapshot_only_no_original_url",
                "complete_no_case_claim",
                "not_obscure_ai_case",
                "URL extraction reviewed this as snapshot/local-source only with no original public URL locally recoverable.",
                "move_to_next_bulk_queue",
            )
        return (
            "residual_no_named_url_reviewed",
            "complete_for_current_layer_parent_needed",
            "not_obscure_ai_case",
            "No named URL remains after extraction review; keep out of reviewed core until a parent/original source is resolved.",
            "parent_source_extraction_queue",
        )
    return (
        "closed_other_non_case",
        "complete_no_case_claim",
        "not_obscure_ai_case",
        "No case-level promotion gate remains after hardening.",
        "move_to_next_bulk_queue",
    )


def build() -> dict[str, object]:
    hardening_rows = read_tsv(HARDENING)
    url_by_signal = {row.get("signal_id", ""): row for row in read_tsv(URL_RESULTS)}
    cluster_counts = Counter(row.get("dedupe_key", "") for row in hardening_rows)
    out_rows: list[dict[str, str]] = []

    for row in hardening_rows:
        url_verdict = url_by_signal.get(row.get("signal_id", ""), {}).get("url_extraction_verdict", "")
        disp, state, posture, reason, action = disposition(row, url_verdict)
        out_rows.append(
            {
                "row_id": row.get("row_id", ""),
                "signal_id": row.get("signal_id", ""),
                "completion_disposition": disp,
                "completion_state": state,
                "obscure_ai_posture": posture,
                "promotion_gate": row.get("promotion_gate", ""),
                "promotion_priority": row.get("promotion_priority", ""),
                "url_extraction_verdict": url_verdict,
                "source_url": row.get("source_url", ""),
                "source_host": row.get("source_host", ""),
                "source_surface_class": row.get("source_surface_class", ""),
                "source_review_role": row.get("source_review_role", ""),
                "dedupe_key": row.get("dedupe_key", ""),
                "cluster_size": str(cluster_counts[row.get("dedupe_key", "")]),
                "title_or_snippet": clean(row.get("title_or_snippet", "")),
                "claim_ceiling": clean(row.get("claim_ceiling", ""), 300),
                "completion_reason": reason,
                "next_bulk_action": action,
                "forbidden_overread": "Completion closes source-surface routing only; it is not reviewed-core promotion, incident truth, legality, safety, compliance, prevalence, or ranking.",
            }
        )

    out_rows.sort(key=lambda row: (row["completion_disposition"], row["source_host"], row["signal_id"]))
    write_tsv(OUT, out_rows)
    write_tsv(DASHBOARD_COPY, out_rows[:250])

    disposition_counts = Counter(row["completion_disposition"] for row in out_rows)
    state_counts = Counter(row["completion_state"] for row in out_rows)
    posture_counts = Counter(row["obscure_ai_posture"] for row in out_rows)
    action_counts = Counter(row["next_bulk_action"] for row in out_rows)
    status = {
        "generated_at_utc": utc_now(),
        "input": str(HARDENING),
        "output": str(OUT),
        "dashboard_copy": str(DASHBOARD_COPY),
        "source_reviewed_rows": len(out_rows),
        "completed_rows": len(out_rows),
        "obscure_ai_ready_now": posture_counts.get("case_candidate_needs_human_claim_ceiling", 0),
        "completion_disposition_counts": dict(sorted(disposition_counts.items())),
        "completion_state_counts": dict(sorted(state_counts.items())),
        "obscure_ai_posture_counts": dict(sorted(posture_counts.items())),
        "next_bulk_action_counts": dict(sorted(action_counts.items())),
        "unique_dedupe_clusters": len(cluster_counts),
        "boundary": "Completion ledger closes the 1,432 source-reviewed candidates as a processing layer only; no reviewed-core or ObscureAI addition occurred.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY.write_text(
        "\n".join(
            [
                "# Source-reviewed completion ledger",
                "",
                f"- Generated: {status['generated_at_utc']}",
                f"- Source-reviewed rows completed: `{status['completed_rows']}`",
                f"- Unique dedupe clusters: `{status['unique_dedupe_clusters']}`",
                f"- ObscureAI ready now: `{status['obscure_ai_ready_now']}`",
                f"- Completion dispositions: `{json.dumps(status['completion_disposition_counts'], sort_keys=True)}`",
                f"- Next bulk actions: `{json.dumps(status['next_bulk_action_counts'], sort_keys=True)}`",
                "",
                status["boundary"],
                "",
            ]
        ),
        encoding="utf-8",
    )
    return status


def main() -> int:
    print(json.dumps(build(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
