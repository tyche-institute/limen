#!/usr/bin/env python3
"""First-pass review all LIMEN review candidates.

This is a deterministic triage layer. It reviews every materialized candidate
into a first-pass verdict so the queue no longer sits at "pending" while
preserving a strict boundary: first-pass review is not reviewed-core promotion
and is not an incident/legal/compliance finding.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
LEDGER = REVIEW_ROOT / "all-signals-review-candidates.tsv"
OUT = REVIEW_ROOT / "full-first-pass-review.tsv"
QUEUE = REVIEW_ROOT / "direct-source-review-queue.tsv"
ROLLUP_JSON = REVIEW_ROOT / "review-rollup-status.json"
ROLLUP_MD = REVIEW_ROOT / "review-rollup-status.md"
SOURCE_BATCH_ROOT = REVIEW_ROOT / "source-review-batches"
DASHBOARD_PANEL = PROJECT_ROOT / "results" / "dashboard" / "review-candidate-triage-panel.tsv"
JOURNAL = PROJECT_ROOT / "journal.md"

VERDICTS = [
    "promote_to_source_review",
    "merge_with_existing_surface",
    "reject_as_cross_project_noise",
    "hold_needs_direct_source",
    "hold_needs_human_translation",
    "hold_low_relevance",
]

DERIVATIVE_PATH_MARKERS = [
    "/results/",
    "/draft/",
    "/papers/",
    "/prompts/",
    "/logs/",
    "/release/",
    "/snapshots/",
    "/submissions/",
    "/manuscript",
    "/package",
    "/boost/",
]

DIRECT_SOURCE_HINTS = [
    "http://",
    "https://",
    ".gov",
    ".europa.eu",
    "ftc.gov",
    "sec.gov",
    "ico.org",
    "datatilsynet",
    "court",
    "tribunal",
    "register",
    "algorithm register",
    "ai register",
]

LOW_RELEVANCE_HINTS = [
    "preprint",
    "manuscript",
    "paper",
    "article",
    "citation",
    "author",
    "submitted",
    "journal",
    "package",
    "prompt",
]

TRANSLATION_HINTS = [
    "translation",
    "auto-translation",
    "translated",
    "non-english",
    "language",
    " da,",
    " fi,",
    " et,",
    " lt,",
    " sl,",
    " fr,",
]

INTERNAL_BACKUP_OR_SCRIPT_MARKERS = [
    ".bak",
    ".no-egress-gate",
    "/runtime/hermes/",
    "/scripts/",
    "/tools/",
    "/bin/hermes_remote_factory.py",
    "/journal.md",
]

REVIEWED_CORE_RESULT_MARKERS = [
    "/results/security/limen-reviewed-core",
    "/results/security/security-agentic-watch",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def contains_any(text: str, needles: list[str]) -> bool:
    low = text.lower()
    return any(needle in low for needle in needles)


def is_derivative_path(path: str) -> bool:
    low = path.lower()
    if "/results/review-candidates/" in low:
        return True
    return any(marker in low for marker in DERIVATIVE_PATH_MARKERS)


def is_internal_backup_or_script_echo(path: str) -> bool:
    low = path.lower()
    return any(marker in low for marker in INTERNAL_BACKUP_OR_SCRIPT_MARKERS)


def is_reviewed_core_result_echo(path: str) -> bool:
    low = path.lower()
    return any(marker in low for marker in REVIEWED_CORE_RESULT_MARKERS)


def classify(row: dict[str, str]) -> tuple[str, str, str, str]:
    path = row.get("source_path", "")
    snippet = row.get("snippet", "")
    queries = row.get("queries", "")
    priority = row.get("review_priority", "")
    text = f"{path} {snippet} {queries}".lower()

    if is_reviewed_core_result_echo(path):
        return (
            "merge_with_existing_surface",
            "existing_reviewed_core_echo",
            "candidate points to an already-modeled LIMEN reviewed-core/security surface and should not be queued as a new source-review item",
            "traceability to an existing reviewed surface only; no new example, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim",
        )

    if is_internal_backup_or_script_echo(path):
        return (
            "reject_as_cross_project_noise",
            "internal_backup_or_script_echo",
            "candidate points to a local backup, script, or journal/process file rather than a direct reviewable public source surface",
            "process trace only; no source-surface, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim",
        )

    if contains_any(text, TRANSLATION_HINTS) and priority.startswith("P1"):
        return (
            "hold_needs_human_translation",
            "translation_sensitive_candidate",
            "candidate appears to depend on non-English or translated public evidence",
            "translation-safe source review only; no legal or policy conclusion from machine translation",
        )

    if contains_any(text, DIRECT_SOURCE_HINTS) and not is_derivative_path(path):
        return (
            "promote_to_source_review",
            "direct_surface_candidate",
            "candidate points directly to a public or official-looking source surface",
            "direct source review may inspect source posture only; no prevalence, legality, safety, or compliance claim",
        )

    if (
        not is_derivative_path(path)
        and ("/reports/" in path.lower() or "/data/" in path.lower() or path.lower().endswith((".csv", ".json", ".jsonl", ".tsv")))
    ):
        if contains_any(text, DIRECT_SOURCE_HINTS):
            return (
                "hold_needs_direct_source",
                "source_pack_proxy_candidate",
                "candidate is a source-pack/proxy row that appears to name an underlying public source",
                "must resolve the underlying source before any reviewed example or paper claim",
            )

    if is_derivative_path(path):
        if contains_any(text, LOW_RELEVANCE_HINTS) and not contains_any(text, DIRECT_SOURCE_HINTS):
            return (
                "reject_as_cross_project_noise",
                "internal_derivative_noise",
                "candidate is an internal manuscript/log/package/prompt surface without a direct reviewable source",
                "not a LIMEN example; may only inform process diagnostics",
            )
        return (
            "merge_with_existing_surface",
            "derivative_or_existing_surface",
            "candidate is an internal derived artifact and should be merged back to the underlying source family or existing dashboard surface",
            "use only as traceability to an existing surface, not as a new example",
        )

    if priority.startswith("P3"):
        return (
            "hold_low_relevance",
            "low_priority_signal",
            "candidate is a broad lower-priority signal with no direct official/source-review cue",
            "do not promote without a named source and article claim target",
        )

    return (
        "hold_needs_direct_source",
        "needs_source_resolution",
        "candidate is potentially relevant but does not yet expose a direct reviewable source in local metadata",
        "must resolve direct public source before promotion",
    )


def read_rows() -> list[dict[str, str]]:
    with LEDGER.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def source_review_status() -> dict[str, object]:
    verdict_counts: Counter[str] = Counter()
    role_counts: Counter[str] = Counter()
    rows = 0
    batch_paths = sorted(SOURCE_BATCH_ROOT.glob("*/source-review-results.tsv"))
    for path in batch_paths:
        with path.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            for row in reader:
                rows += 1
                verdict_counts[row.get("source_review_verdict", "")] += 1
                role_counts[row.get("source_review_role", "")] += 1
    return {
        "source_review_batch_count": len(batch_paths),
        "source_review_rows": rows,
        "source_review_latest_batch": str(batch_paths[-1].parent) if batch_paths else "",
        "source_review_verdict_counts": dict(sorted(verdict_counts.items())),
        "source_review_role_counts": dict(sorted(role_counts.items())),
    }


def write_dashboard_panel(status: dict[str, object]) -> None:
    DASHBOARD_PANEL.parent.mkdir(parents=True, exist_ok=True)
    boundary = str(status["boundary"])
    rows = [
        {
            "metric_id": "RCT-001",
            "metric_label": "materialized_review_candidates",
            "value": status["candidate_rows"],
            "unit": "candidate_rows",
            "interpretation": "clean mined signals materialized as review candidates",
            "artifact": str(LEDGER),
            "boundary": "not reviewed-core examples",
        },
        {
            "metric_id": "RCT-002",
            "metric_label": "first_pass_reviewed_candidates",
            "value": status["first_pass_reviewed_rows"],
            "unit": "candidate_rows",
            "interpretation": "all materialized review candidates have a deterministic first-pass verdict",
            "artifact": str(OUT),
            "boundary": boundary,
        },
        {
            "metric_id": "RCT-003",
            "metric_label": "direct_source_review_queue",
            "value": status["direct_source_review_queue_rows"],
            "unit": "candidate_rows",
            "interpretation": "rows requiring direct-source, source-pack, or translation-aware review before example promotion",
            "artifact": str(QUEUE),
            "boundary": "queue only; not promotion",
        },
        {
            "metric_id": "RCT-004",
            "metric_label": "source_review_batches_completed",
            "value": status["source_review_batch_count"],
            "unit": "batches",
            "interpretation": "Hermes/Codex source-review batches completed from the direct-source queue",
            "artifact": status["source_review_latest_batch"],
            "boundary": "local metadata and local source files only unless batch states otherwise",
        },
        {
            "metric_id": "RCT-005",
            "metric_label": "source_review_rows_completed",
            "value": status["source_review_rows"],
            "unit": "candidate_rows",
            "interpretation": "candidate rows with source-review batch verdicts",
            "artifact": status["source_review_latest_batch"],
            "boundary": "source-surface review; not incident truth, legality, compliance, safety, prevalence, or rank",
        },
    ]
    for verdict, count in sorted(status["verdict_counts"].items()):
        rows.append(
            {
                "metric_id": f"RCT-FP-{verdict}",
                "metric_label": f"first_pass_{verdict}",
                "value": count,
                "unit": "candidate_rows",
                "interpretation": "first-pass review verdict count",
                "artifact": str(OUT),
                "boundary": boundary,
            }
        )
    for verdict, count in sorted(status["source_review_verdict_counts"].items()):
        rows.append(
            {
                "metric_id": f"RCT-SR-{verdict}",
                "metric_label": f"source_review_{verdict}",
                "value": count,
                "unit": "candidate_rows",
                "interpretation": "source-review batch verdict count",
                "artifact": status["source_review_latest_batch"],
                "boundary": "batch verdict; not reviewed-core promotion unless separately hardened",
            }
        )

    fields = ["metric_id", "metric_label", "value", "unit", "interpretation", "artifact", "boundary"]
    with DASHBOARD_PANEL.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, delimiter="\t", fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_rows(rows: list[dict[str, str]], timestamp: str, write_journal: bool) -> None:
    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    fields = [
        "signal_id",
        "review_state",
        "first_pass_verdict",
        "candidate_role",
        "review_reason",
        "claim_ceiling",
        "next_action",
        "reviewed_at_utc",
        "review_priority",
        "shards",
        "queries",
        "source_path",
        "source_line",
        "snippet_hash",
        "snippet",
    ]
    queue_fields = fields + ["queue_reason"]

    reviewed = []
    queue = []
    for row in rows:
        verdict, role, reason, ceiling = classify(row)
        out = {
            "signal_id": row.get("signal_id", ""),
            "review_state": "first_pass_reviewed",
            "first_pass_verdict": verdict,
            "candidate_role": role,
            "review_reason": reason,
            "claim_ceiling": ceiling,
            "next_action": next_action_for(verdict),
            "reviewed_at_utc": timestamp,
            "review_priority": row.get("review_priority", ""),
            "shards": row.get("shards", ""),
            "queries": row.get("queries", ""),
            "source_path": row.get("source_path", ""),
            "source_line": row.get("source_line", ""),
            "snippet_hash": row.get("snippet_hash", ""),
            "snippet": row.get("snippet", ""),
        }
        reviewed.append(out)
        if verdict in {"promote_to_source_review", "hold_needs_direct_source", "hold_needs_human_translation"}:
            q = dict(out)
            q["queue_reason"] = "needs direct source, source-pack resolution, or translation-aware review before example promotion"
            queue.append(q)

    with OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, delimiter="\t", fieldnames=fields)
        writer.writeheader()
        writer.writerows(reviewed)

    with QUEUE.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, delimiter="\t", fieldnames=queue_fields)
        writer.writeheader()
        writer.writerows(queue)

    verdict_counts = Counter(r["first_pass_verdict"] for r in reviewed)
    role_counts = Counter(r["candidate_role"] for r in reviewed)
    priority_counts = Counter(r["review_priority"] for r in reviewed)
    source_status = source_review_status()
    status = {
        "generated_at_utc": timestamp,
        "policy": "all_materialized_review_candidates_receive_deterministic_first_pass_review",
        "candidate_rows": len(reviewed),
        "first_pass_reviewed_rows": len(reviewed),
        "direct_source_review_queue_rows": len(queue),
        "review_output": str(OUT),
        "direct_source_review_queue": str(QUEUE),
        "verdict_counts": dict(sorted(verdict_counts.items())),
        "candidate_role_counts": dict(sorted(role_counts.items())),
        "priority_counts": dict(sorted(priority_counts.items())),
        "boundary": "first-pass review is triage only; it is not reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, or ranking",
    }
    status.update(source_status)
    with ROLLUP_JSON.open("w", encoding="utf-8") as fh:
        json.dump(status, fh, indent=2, sort_keys=True)
        fh.write("\n")

    with ROLLUP_MD.open("w", encoding="utf-8") as fh:
        fh.write("# LIMEN Candidate Review Rollup\n\n")
        fh.write(f"Generated UTC: {timestamp}\n\n")
        fh.write("Policy: all materialized review candidates receive deterministic first-pass review.\n\n")
        fh.write(f"- Candidate rows: `{len(reviewed)}`\n")
        fh.write(f"- First-pass reviewed rows: `{len(reviewed)}`\n")
        fh.write(f"- Direct-source review queue rows: `{len(queue)}`\n")
        fh.write(f"- Review output: `{OUT}`\n")
        fh.write(f"- Direct-source queue: `{QUEUE}`\n\n")
        fh.write("## Verdict Counts\n\n")
        for key, value in sorted(verdict_counts.items()):
            fh.write(f"- `{key}`: `{value}`\n")
        fh.write("\n## Candidate Role Counts\n\n")
        for key, value in sorted(role_counts.items()):
            fh.write(f"- `{key}`: `{value}`\n")
        fh.write("\n## Source-Review Batches\n\n")
        fh.write(f"- Completed source-review batches: `{status['source_review_batch_count']}`\n")
        fh.write(f"- Source-review rows completed: `{status['source_review_rows']}`\n")
        fh.write(f"- Latest source-review batch: `{status['source_review_latest_batch']}`\n\n")
        fh.write("### Source-Review Verdict Counts\n\n")
        for key, value in sorted(status["source_review_verdict_counts"].items()):
            fh.write(f"- `{key}`: `{value}`\n")
        fh.write("\n## Boundary\n\n")
        fh.write(status["boundary"] + "\n")

    write_dashboard_panel(status)

    if write_journal:
        with JOURNAL.open("a", encoding="utf-8") as fh:
            fh.write(f"\n## {timestamp} - all review candidates first-pass reviewed\n\n")
            fh.write(
                f"First-pass reviewed all `{len(reviewed)}` materialized LIMEN review candidates into "
                f"`results/review-candidates/full-first-pass-review.tsv`; `{len(queue)}` rows remain in "
                "`results/review-candidates/direct-source-review-queue.tsv` for direct-source, source-pack, "
                "or translation-aware review before any reviewed-core promotion. This is triage only, not an "
                "incident truth, legal, compliance, safety, deployment, prevalence, or ranking claim.\n"
            )


def next_action_for(verdict: str) -> str:
    if verdict == "promote_to_source_review":
        return "open direct source review packet"
    if verdict == "hold_needs_direct_source":
        return "resolve underlying direct public source before review"
    if verdict == "hold_needs_human_translation":
        return "route to translation-aware source review"
    if verdict == "merge_with_existing_surface":
        return "merge into existing dashboard/source-family surface"
    if verdict == "reject_as_cross_project_noise":
        return "keep as negative/noise evidence only"
    return "hold unless a named article claim target requires it"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-journal", action="store_true")
    args = parser.parse_args()
    timestamp = utc_now()
    rows = read_rows()
    write_rows(rows, timestamp, write_journal=not args.no_journal)
    print(json.dumps({"timestamp": timestamp, "candidate_rows": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
