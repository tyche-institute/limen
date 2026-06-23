#!/usr/bin/env python3
"""Build a fail-closed LIMEN dashboard API bundle from release-card UI config.

The bundle is a local, offline JSON contract for a future interactive dashboard.
It only includes count-bearing views whose TSV export still matches the
release-card row count and SHA-256. Row-level source access dates/rights labels
are deliberately not promoted here; the bundle exposes export-level provenance
and a row-level-provenance status field until source-ledger joins are verified.

No network access, upload, deposit, submission, or source collection is performed.
"""

import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from limen_caption_currentness_gate import caption_audit_path_for_root, caption_gate_for_view

MAX_SAMPLE_ROWS = 3
MAX_SAMPLE_VALUE_LEN = 120
SOURCE_LEDGER_JOIN_PATH = "results/dashboard/source-ledger-join-v0.1.tsv"


REQUIRED_TOOLTIP_FIELDS = {
    "denominator_scope",
    "claim_ceiling",
    "uncertainty_flag_or_review_status",
    "source_artifact_path",
    "source_artifact_sha256",
    "row_level_provenance_status_when_available",
}

PROHIBITED_TOKENS = [
    "completeness",
    "prevalence",
    "legal",
    "compliance",
    "certification",
    "safety",
    "country ranking",
    "third-party endorsement",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def truncate(value: str) -> str:
    value = str(value or "").replace("\n", " ").strip()
    if len(value) <= MAX_SAMPLE_VALUE_LEN:
        return value
    return value[: MAX_SAMPLE_VALUE_LEN - 1] + "…"


def row_key_for_view(view_name: str, row: dict) -> str:
    if view_name == "source_family_saturation":
        return row.get("family_id", "")
    if view_name in {"taxonomy_heatmap", "legal_uncertainty"}:
        return row.get("category_code", "")
    if view_name == "evidence_tier_funnel":
        return row.get("stage_code") or row.get("review_priority") or row.get("row_type", "")
    if view_name == "jurisdiction_language":
        return f"{row.get('jurisdiction', '')}|{row.get('language', '')}"
    if view_name == "security_agentic_threshold":
        return row.get("panel_id", "")
    if view_name == "duplicate_review_graph":
        return row.get("edge_id", "")
    return ""


def read_source_ledger_join(root: Path):
    path = root / SOURCE_LEDGER_JOIN_PATH
    if not path.exists():
        return path, {}, [f"source-ledger join missing: {SOURCE_LEDGER_JOIN_PATH}"]
    rows = read_tsv(path)
    mapping = {}
    duplicates = []
    for row in rows:
        key = (row.get("dashboard_view", ""), row.get("row_key", ""))
        if key in mapping:
            duplicates.append("|".join(key))
        mapping[key] = row
    failures = []
    if duplicates:
        failures.append("duplicate source-ledger join keys: " + ", ".join(sorted(duplicates)[:10]))
    for idx, row in enumerate(rows, start=2):
        if not row.get("public_dashboard_action", "").strip():
            failures.append(f"source-ledger join row {idx} missing public_dashboard_action")
    return path, mapping, failures


def attach_source_ledger_join(view_name: str, rows, join_map):
    enriched = []
    missing = []
    actions = {}
    for row in rows:
        row_key = row_key_for_view(view_name, row)
        join = join_map.get((view_name, row_key))
        if not join:
            missing.append(row_key or "__blank__")
            join_payload = {
                "row_key": row_key,
                "join_status": "missing_join_row",
                "public_dashboard_action": "block_row_level_access_rights_labels",
                "human_review_needed": "yes",
                "claim_ceiling": "provenance-label discipline only; source-ledger join missing",
            }
        else:
            join_payload = {
                "row_key": row_key,
                "source_id_or_path": truncate(join.get("source_id_or_path", "")),
                "join_confidence": join.get("join_confidence", ""),
                "rollup_policy": join.get("rollup_policy", ""),
                "human_review_needed": join.get("human_review_needed", ""),
                "public_dashboard_action": join.get("public_dashboard_action", ""),
                "claim_ceiling": join.get("claim_ceiling", ""),
                "access_date_scope_note": "family/access date is ledger-scope only unless action explicitly permits row-level badges",
            }
        action = join_payload.get("public_dashboard_action", "")
        actions[action] = actions.get(action, 0) + 1
        enriched_row = dict(row)
        enriched_row["_source_ledger_join"] = join_payload
        enriched.append(enriched_row)
    return enriched, missing, actions


def column_profile(rows):
    if not rows:
        return []
    fields = list(rows[0].keys())
    profiles = []
    for field in fields:
        values = [str(row.get(field, "")).strip() for row in rows]
        non_empty = [v for v in values if v]
        distinct = sorted(set(non_empty))
        profiles.append({
            "name": field,
            "non_empty_rows": len(non_empty),
            "distinct_count": len(distinct),
            "sample_values": [truncate(v) for v in distinct[:3]],
        })
    return profiles


def view_gate(root: Path, view: dict, caption_audit_path: Path | None = None, source_join_map=None):
    reasons = []
    source_join_map = source_join_map or {}
    source_join_missing = []
    source_join_actions = {}
    if caption_audit_path is not None:
        caption_gate = caption_gate_for_view(view.get("dashboard_view", ""), caption_audit_path)
        if not caption_gate["allowed"]:
            reasons.append("caption currentness gate failed: " + str(caption_gate["reason"]))
    source_path = view.get("source_path", "")
    src = root / source_path if source_path else root / "__missing__"
    rows = []
    actual_rows = None
    actual_sha = ""
    if not src.exists():
        reasons.append("source file missing")
    else:
        rows = read_tsv(src)
        actual_rows = len(rows)
        actual_sha = sha256_file(src)
        if actual_rows != view.get("source_data_rows"):
            reasons.append("row count mismatch")
        if actual_sha != view.get("source_sha256"):
            reasons.append("sha256 mismatch")
        rows, source_join_missing, source_join_actions = attach_source_ledger_join(view.get("dashboard_view", ""), rows, source_join_map)
        if source_join_missing:
            reasons.append("source-ledger join missing row keys: " + ", ".join(source_join_missing[:10]))

    tooltip = set(view.get("tooltip_must_include", []))
    missing_tooltip = sorted(REQUIRED_TOOLTIP_FIELDS - tooltip)
    if missing_tooltip:
        reasons.append("missing tooltip fields: " + ", ".join(missing_tooltip))

    prohibited = view.get("prohibited_reading", "")
    missing_prohibited = [tok for tok in PROHIBITED_TOKENS if tok.lower() not in prohibited.lower()]
    if missing_prohibited:
        reasons.append("missing prohibited-reading tokens: " + ", ".join(missing_prohibited))

    if not view.get("subtitle"):
        reasons.append("missing denominator subtitle")
    if not view.get("claim_boundary"):
        reasons.append("missing claim boundary")

    return {
        "allowed": not reasons,
        "reasons": reasons,
        "actual_rows": actual_rows,
        "actual_sha": actual_sha,
        "rows": rows,
        "source_join_missing": source_join_missing,
        "source_join_actions": source_join_actions,
    }


def build(root: Path, output: Path, gate_tsv: Path | None):
    cfg_path = root / "dashboard/release-card-ui-config-v0.1.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    caption_audit_path = caption_audit_path_for_root(root)
    source_join_path, source_join_map, source_join_failures = read_source_ledger_join(root)
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

    bundle = {
        "schema": "limen_dashboard_api_bundle_v0_1",
        "generated_at_utc": generated,
        "lane_id": "limen-dashboard-paper-forge",
        "project_id": "limen-ai-edge-case-atlas",
        "source_ui_config": "dashboard/release-card-ui-config-v0.1.json",
        "source_ui_config_sha256": sha256_file(cfg_path),
        "source_caption_currentness_audit": str(caption_audit_path.relative_to(root)) if caption_audit_path.exists() else str(caption_audit_path),
        "source_ledger_join": str(source_join_path.relative_to(root)) if source_join_path.exists() else str(source_join_path),
        "source_ledger_join_sha256": sha256_file(source_join_path) if source_join_path.exists() else "",
        "purpose": "Fail-closed local JSON bundle for reviewer-safe interactive dashboard/API prototyping.",
        "claim_boundary": "Public-source evidence visibility and dashboard/paper parity only; no completeness, prevalence, legal guilt, compliance, certification, safety assurance, country ranking, source-truth, or third-party endorsement claim.",
        "row_level_provenance_policy": "Consume source-ledger-join-v0.1.tsv for tooltip state. Show family-level notes or candidate review links only where public_dashboard_action permits; keep row-level access-date/rights badges blocked unless a file-qualified source join is manually verified.",
        "global_rules": cfg.get("global_rules", []),
        "views": [],
    }
    gate_rows = []
    for view in cfg.get("views", []):
        gate = view_gate(root, view, caption_audit_path, source_join_map)
        if source_join_failures:
            gate["allowed"] = False
            gate["reasons"].extend(source_join_failures)
        caption_gate = caption_gate_for_view(view.get("dashboard_view", ""), caption_audit_path)
        status = "PASS" if gate["allowed"] else "FAIL"
        source_path = view.get("source_path", "")
        rendered_rows = gate["rows"] if gate["allowed"] else []
        sample_rows = [
            {key: truncate(value) for key, value in row.items()}
            for row in rendered_rows[:MAX_SAMPLE_ROWS]
        ]
        bundle["views"].append({
            "dashboard_view": view.get("dashboard_view", ""),
            "manuscript_surface": view.get("manuscript_surface", ""),
            "render_status": status,
            "render_allowed": gate["allowed"],
            "fail_closed_reason": "all guards present" if gate["allowed"] else "; ".join(gate["reasons"]),
            "source_path": source_path,
            "configured_source_rows": view.get("source_data_rows"),
            "actual_source_rows": gate["actual_rows"],
            "configured_source_sha256": view.get("source_sha256", ""),
            "actual_source_sha256": gate["actual_sha"],
            "subtitle": view.get("subtitle", ""),
            "claim_boundary": view.get("claim_boundary", ""),
            "prohibited_reading": view.get("prohibited_reading", ""),
            "tooltip_must_include": view.get("tooltip_must_include", []),
            "row_level_provenance_status": "controlled_by_source_ledger_join_action",
            "source_ledger_join_actions": gate["source_join_actions"],
            "caption_currentness_status": caption_gate["status"],
            "caption_currentness_reason": caption_gate["reason"],
            "caption_currentness_audit_source": caption_gate["source"],
            "columns": column_profile(rendered_rows),
            "sample_rows": sample_rows,
        })
        gate_rows.append({
            "dashboard_view": view.get("dashboard_view", ""),
            "status": status,
            "render_allowed": str(gate["allowed"]).lower(),
            "configured_rows": view.get("source_data_rows", ""),
            "actual_rows": gate["actual_rows"] if gate["actual_rows"] is not None else "",
            "configured_sha256": view.get("source_sha256", ""),
            "actual_sha256": gate["actual_sha"],
            "row_level_provenance_status": "controlled_by_source_ledger_join_action",
            "source_ledger_join_actions": gate["source_join_actions"],
            "caption_currentness_status": caption_gate["status"],
            "caption_currentness_reason": caption_gate["reason"],
            "reason": "all guards present" if gate["allowed"] else "; ".join(gate["reasons"]),
        })

    pass_count = sum(1 for r in gate_rows if r["status"] == "PASS")
    fail_count = sum(1 for r in gate_rows if r["status"] == "FAIL")
    bundle["verdict"] = "PASS" if fail_count == 0 else "FAIL"
    bundle["pass_count"] = pass_count
    bundle["fail_count"] = fail_count

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if gate_tsv:
        gate_tsv.parent.mkdir(parents=True, exist_ok=True)
        fields = ["dashboard_view", "status", "render_allowed", "configured_rows", "actual_rows", "configured_sha256", "actual_sha256", "row_level_provenance_status", "source_ledger_join_actions", "caption_currentness_status", "caption_currentness_reason", "reason"]
        with gate_tsv.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            writer.writerows(gate_rows)

    return bundle, gate_rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--output", default="dashboard/limen-dashboard-api-bundle-v0.1.json")
    parser.add_argument("--write-gate-tsv", default="")
    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    gate_path = root / args.write_gate_tsv if args.write_gate_tsv else None
    bundle, _ = build(root, root / args.output, gate_path)
    print(f"VERDICT: {bundle['verdict']}")
    print(f"PASS views: {bundle['pass_count']}")
    print(f"FAIL views: {bundle['fail_count']}")
    print(f"JSON: {root / args.output}")
    if gate_path:
        print(f"Gate TSV: {gate_path}")
    return 0 if bundle["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

