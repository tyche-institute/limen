#!/usr/bin/env python3
"""Caption-currentness fail-closed gate for LIMEN dashboard renderers.

The gate consumes the lane-local caption audit produced by the dashboard-paper
forge lane. It prevents count-bearing dashboard/API/static exports from silently
reusing stale manuscript caption-control rows. This is a package-integrity check
only; it does not change denominators or promote evidence rows.
"""

from __future__ import annotations

import csv
from pathlib import Path

DEFAULT_AUDIT_PATH = Path("results/boost/limen-dashboard-paper-forge/caption-currentness-audit-v0.9.tsv")

VIEW_TO_CONTROL_IDS = {
    "taxonomy_heatmap": {"CCR-001", "CCR-002"},
    "evidence_tier_funnel": {"CCR-005"},
    "security_agentic_threshold": {"CCR-014", "CCR-017"},
}

PASS_STATES = {
    "PASS_WITH_CURRENT_DENOMINATOR_LANGUAGE",
    "PASS_SCOPE_ONLY_NO_EXPLICIT_COUNT_FOUND",
}

BLOCK_STATES = {
    "BLOCK_FOR_COUNT_BEARING_REUSE",
}


def _read_audit_rows(audit_path: Path) -> list[dict[str, str]]:
    with audit_path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def caption_gate_for_view(dashboard_view: str, audit_path: str | Path) -> dict[str, object]:
    """Return a fail-closed caption-currentness gate for a dashboard view.

    Views not mapped to a caption-control ID are allowed but marked not_applicable.
    Mapped views fail when any linked control row is absent or carries a block
    state. This deliberately treats stale caption controls as an export blocker
    for count-bearing surfaces.
    """
    audit_path = Path(audit_path)
    control_ids = VIEW_TO_CONTROL_IDS.get(dashboard_view, set())
    if not control_ids:
        return {
            "allowed": True,
            "status": "PASS",
            "reason": "caption currentness audit not applicable to this view",
            "source": str(audit_path),
            "control_ids": "",
            "audit_states": "not_applicable",
        }

    if not audit_path.exists():
        return {
            "allowed": False,
            "status": "FAIL",
            "reason": f"caption currentness audit missing: {audit_path}",
            "source": str(audit_path),
            "control_ids": ",".join(sorted(control_ids)),
            "audit_states": "missing_audit",
        }

    rows = _read_audit_rows(audit_path)
    by_id = {row.get("control_id", ""): row for row in rows}
    failures: list[str] = []
    states: list[str] = []
    for control_id in sorted(control_ids):
        row = by_id.get(control_id)
        if row is None:
            failures.append(f"{control_id}:missing_caption_audit_row")
            states.append(f"{control_id}=missing")
            continue
        state = row.get("audit_state", "")
        states.append(f"{control_id}={state}")
        if state in BLOCK_STATES:
            action = row.get("safe_reuse_action", "rewrite before export")
            failures.append(f"{control_id}:{state}:{action}")
        elif state not in PASS_STATES:
            failures.append(f"{control_id}:unknown_or_nonpass_state:{state}")

    if failures:
        return {
            "allowed": False,
            "status": "FAIL",
            "reason": "; ".join(failures),
            "source": str(audit_path),
            "control_ids": ",".join(sorted(control_ids)),
            "audit_states": ";".join(states),
        }

    return {
        "allowed": True,
        "status": "PASS",
        "reason": "caption currentness audit permits count-bearing reuse",
        "source": str(audit_path),
        "control_ids": ",".join(sorted(control_ids)),
        "audit_states": ";".join(states),
    }


def caption_audit_path_for_root(root: Path, audit_path: str | Path = DEFAULT_AUDIT_PATH) -> Path:
    audit_path = Path(audit_path)
    if audit_path.is_absolute():
        return audit_path
    return root / audit_path
