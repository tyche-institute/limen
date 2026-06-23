#!/usr/bin/env python3
"""LIMEN dashboard UI contract fail-closed check.

Validates dashboard/release-card-ui-config-v0.1.json against local dashboard
exports before any public interactive dashboard binding. The check is deliberately
conservative: a count-bearing view is renderable only when denominator text,
tooltip requirements, prohibited-reading warning, source row count, and SHA-256
all agree with the local export artifact.

No network access, upload, deposit, or source collection is performed.
"""

import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from limen_caption_currentness_gate import caption_audit_path_for_root, caption_gate_for_view

REQUIRED_VIEWS = {
    "source_family_saturation": {
        "source_path": "results/dashboard/source-family-coverage.tsv",
        "subtitle_tokens": ["saturation", "uncertainty", "not completeness"],
    },
    "taxonomy_heatmap": {
        "source_path": "results/dashboard/taxonomy-heatmap.tsv",
        "subtitle_tokens": ["39/29", "taxonomy support", "not prevalence"],
    },
    "evidence_tier_funnel": {
        "source_path": "results/dashboard/evidence-funnel.tsv",
        "subtitle_tokens": ["296", "250", "46", "21"],
    },
    "jurisdiction_language": {
        "source_path": "results/dashboard/jurisdiction-language-coverage.tsv",
        "subtitle_tokens": ["34", "12", "no country ranking"],
    },
    "legal_uncertainty": {
        "source_path": "results/dashboard/legal-uncertainty-matrix.tsv",
        "subtitle_tokens": ["uncertainty", "no compliance", "liability"],
    },
    "security_agentic_threshold": {
        "source_path": "results/dashboard/security-threshold-ladder-panel.tsv",
        "subtitle_tokens": ["4 threshold", "11 security", "not security prevalence"],
    },
    "duplicate_review_graph": {
        "source_path": "results/dashboard/duplicate-review-graph.tsv",
        "subtitle_tokens": ["27", "0 merge", "not proof"],
    },
}

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

SOURCE_LEDGER_JOIN_PATH = "results/dashboard/source-ledger-join-v0.1.tsv"

GLOBAL_RULE_TOKENS = [
    "denominator label",
    "Do not substitute denominators",
    "saturation and uncertainty",
    "Do not infer legal compliance",
    "row-level access-date/rights labels require a verified source-ledger join",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def count_tsv_data_rows(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return 0
    return max(0, len(lines) - 1)


def has_all_tokens(text: str, tokens) -> bool:
    low = text.lower()
    return all(token.lower() in low for token in tokens)


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


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
        return {}, [f"source-ledger join missing: {SOURCE_LEDGER_JOIN_PATH}"]
    mapping = {}
    failures = []
    for row in read_tsv(path):
        key = (row.get("dashboard_view", ""), row.get("row_key", ""))
        if key in mapping:
            failures.append("duplicate source-ledger join key: " + "|".join(key))
        mapping[key] = row
        if not row.get("public_dashboard_action", "").strip():
            failures.append("source-ledger join row missing public_dashboard_action: " + "|".join(key))
    return mapping, failures


def validate(root: Path):
    cfg_path = root / "dashboard/release-card-ui-config-v0.1.json"
    rows = []
    failures = []
    warnings = []

    if not cfg_path.exists():
        return [{
            "dashboard_view": "__config__",
            "allowed_to_render": "false",
            "status": "FAIL",
            "reason": "config_missing",
            "source_path": str(cfg_path),
            "configured_rows": "",
            "actual_rows": "",
            "configured_sha256": "",
            "actual_sha256": "",
            "subtitle": "",
            "claim_boundary": "",
        }], ["Config missing: dashboard/release-card-ui-config-v0.1.json"], warnings

    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    caption_audit_path = caption_audit_path_for_root(root)
    source_join_map, source_join_failures = read_source_ledger_join(root)
    failures.extend(source_join_failures)
    if cfg.get("schema") != "limen_dashboard_release_ui_config_v0_1":
        failures.append("Unexpected or missing schema")
    if cfg.get("lane_id") != "limen-dashboard-paper-forge":
        failures.append("Unexpected or missing lane_id")

    global_rules = "\n".join(cfg.get("global_rules", []))
    missing_global = [tok for tok in GLOBAL_RULE_TOKENS if tok.lower() not in global_rules.lower()]
    if missing_global:
        failures.append("Missing global guardrail token(s): " + "; ".join(missing_global))

    views = cfg.get("views", [])
    seen = set()
    if len(views) != len(REQUIRED_VIEWS):
        failures.append(f"Expected {len(REQUIRED_VIEWS)} views, found {len(views)}")

    for view in views:
        name = view.get("dashboard_view", "")
        status_bits = []
        view_fail = False
        if not name:
            name = "__missing_view_name__"
            view_fail = True
            status_bits.append("missing dashboard_view")
        if name in seen:
            view_fail = True
            status_bits.append("duplicate dashboard_view")
        seen.add(name)

        expected = REQUIRED_VIEWS.get(name)
        if not expected:
            view_fail = True
            status_bits.append("unexpected view")
            expected_path = view.get("source_path", "")
            subtitle_tokens = []
        else:
            expected_path = expected["source_path"]
            subtitle_tokens = expected["subtitle_tokens"]

        configured_path = view.get("source_path", "")
        if configured_path != expected_path:
            view_fail = True
            status_bits.append("source_path mismatch")

        src = root / configured_path if configured_path else root / "__missing__"
        actual_rows = ""
        actual_sha = ""
        source_join_action_summary = {}
        if not src.exists():
            view_fail = True
            status_bits.append("source file missing")
        else:
            data_rows = read_tsv(src)
            actual_rows = len(data_rows)
            actual_sha = sha256_file(src)
            if actual_rows != view.get("source_data_rows"):
                view_fail = True
                status_bits.append("row count mismatch")
            if actual_sha != view.get("source_sha256"):
                view_fail = True
                status_bits.append("sha256 mismatch")
            missing_join_keys = []
            for data_row in data_rows:
                row_key = row_key_for_view(name, data_row)
                join = source_join_map.get((name, row_key))
                if not join:
                    missing_join_keys.append(row_key or "__blank__")
                else:
                    action = join.get("public_dashboard_action", "")
                    source_join_action_summary[action] = source_join_action_summary.get(action, 0) + 1
            if missing_join_keys:
                view_fail = True
                status_bits.append("source-ledger join missing row keys: " + ",".join(missing_join_keys[:10]))

        tooltip = set(view.get("tooltip_must_include", []))
        if not REQUIRED_TOOLTIP_FIELDS.issubset(tooltip):
            view_fail = True
            missing = sorted(REQUIRED_TOOLTIP_FIELDS - tooltip)
            status_bits.append("missing tooltip fields: " + ",".join(missing))

        subtitle = view.get("subtitle", "")
        if subtitle_tokens and not has_all_tokens(subtitle, subtitle_tokens):
            view_fail = True
            status_bits.append("subtitle denominator/guardrail token mismatch")

        prohibited = view.get("prohibited_reading", "")
        missing_prohibited = [tok for tok in PROHIBITED_TOKENS if tok.lower() not in prohibited.lower()]
        if missing_prohibited:
            view_fail = True
            status_bits.append("missing prohibited-reading token(s): " + ",".join(missing_prohibited))

        claim_boundary = view.get("claim_boundary", "")
        if not claim_boundary or any(tok.lower() not in claim_boundary.lower() for tok in ["public-source", "no completeness", "no" ]):
            view_fail = True
            status_bits.append("claim boundary too weak or missing")

        caption_gate = caption_gate_for_view(name, caption_audit_path)
        if not caption_gate["allowed"]:
            view_fail = True
            status_bits.append("caption currentness gate failed: " + str(caption_gate["reason"]))

        allowed = not view_fail
        if not allowed:
            failures.append(f"{name}: " + "; ".join(status_bits))

        rows.append({
            "dashboard_view": name,
            "allowed_to_render": str(allowed).lower(),
            "status": "PASS" if allowed else "FAIL",
            "reason": "all_required_ui_guards_present" if allowed else "; ".join(status_bits),
            "source_path": configured_path,
            "configured_rows": view.get("source_data_rows", ""),
            "actual_rows": actual_rows,
            "configured_sha256": view.get("source_sha256", ""),
            "actual_sha256": actual_sha,
            "subtitle": subtitle,
            "claim_boundary": claim_boundary,
            "source_ledger_join_actions": json.dumps(source_join_action_summary, sort_keys=True),
            "caption_currentness_status": caption_gate["status"],
            "caption_currentness_reason": caption_gate["reason"],
        })

    missing_views = sorted(set(REQUIRED_VIEWS) - seen)
    for name in missing_views:
        failures.append(f"{name}: missing required view")
        rows.append({
            "dashboard_view": name,
            "allowed_to_render": "false",
            "status": "FAIL",
            "reason": "missing required view",
            "source_path": REQUIRED_VIEWS[name]["source_path"],
            "configured_rows": "",
            "actual_rows": "",
            "configured_sha256": "",
            "actual_sha256": "",
            "subtitle": "",
            "claim_boundary": "",
        })

    return rows, failures, warnings


def write_outputs(root: Path, rows, failures, warnings, stamp: str):
    out_dir = root / "results/boost/limen-dashboard-paper-forge"
    out_dir.mkdir(parents=True, exist_ok=True)
    tsv_path = out_dir / f"dashboard-ui-contract-fail-closed-check-{stamp}.tsv"
    md_path = out_dir / f"dashboard-ui-contract-fail-closed-check-{stamp}.md"

    fields = [
        "dashboard_view", "allowed_to_render", "status", "reason", "source_path",
        "configured_rows", "actual_rows", "configured_sha256", "actual_sha256",
        "subtitle", "claim_boundary", "caption_currentness_status", "caption_currentness_reason",
    ]
    with tsv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    pass_count = sum(1 for r in rows if r["status"] == "PASS")
    fail_count = sum(1 for r in rows if r["status"] == "FAIL")
    verdict = "PASS" if fail_count == 0 and not failures else "FAIL"

    lines = [
        "# LIMEN dashboard UI contract fail-closed check",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "Lane: `limen-dashboard-paper-forge`",
        "Project: `limen-ai-edge-case-atlas`",
        "",
        "## Purpose",
        "",
        "This bounded check validates `dashboard/release-card-ui-config-v0.1.json` as a fail-closed renderer contract for future count-bearing dashboard views. A view is marked renderable only if its local export exists, row count and SHA-256 match the config, denominator/subtitle text is present, tooltip fields include provenance and claim-ceiling requirements, every rendered row has a `results/dashboard/source-ledger-join-v0.1.tsv` action row, and prohibited readings remain visible.",
        "",
        "No new collection, network access, upload, deposit, or public release was performed.",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{verdict}`",
        f"- PASS rows: {pass_count}",
        f"- FAIL rows: {fail_count}",
        f"- Machine-readable TSV: `{tsv_path.relative_to(root)}`",
        "",
        "## View gate table",
        "",
        "| Dashboard view | Allowed to render | Status | Reason | Source rows |",
        "|---|---:|---|---|---:|",
    ]
    for r in rows:
        lines.append(
            f"| `{r['dashboard_view']}` | {r['allowed_to_render']} | {r['status']} | {r['reason']} | {r['actual_rows']} |"
        )

    lines.extend([
        "",
        "## Failures / warnings",
        "",
    ])
    if failures:
        lines.extend([f"- FAIL: {f}" for f in failures])
    else:
        lines.append("- No failures detected.")
    if warnings:
        lines.extend([f"- WARN: {w}" for w in warnings])
    else:
        lines.append("- No warnings detected.")

    lines.extend([
        "",
        "## Paper/dashboard readiness delta",
        "",
        "This adds a durable hostile-reviewer control proving that dashboard UI binding can fail closed rather than silently rendering count-bearing charts without denominator labels, claim ceilings, provenance pointers, or prohibited-reading warnings. It strengthens dashboard/paper parity without changing any data denominator.",
        "",
        "## Claim boundary",
        "",
        "This artifact verifies local UI-contract integrity only. It does not support completeness, prevalence, legal liability, compliance, certification, safety assurance, official incident status, country ranking, third-party endorsement, or source-truth claims.",
        "",
        "## Next smallest move",
        "",
        "If/when a concrete dashboard app is edited, make the renderer import this config and refuse to mount a count-bearing chart unless its `allowed_to_render` gate would pass; keep row-level access-date/rights labels hidden until source-ledger joins are verified.",
    ])
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return md_path, tsv_path, verdict, pass_count, fail_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--stamp", default=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ"))
    parser.add_argument("--write-artifacts", action="store_true")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    rows, failures, warnings = validate(root)
    fail_count = sum(1 for r in rows if r["status"] == "FAIL")
    verdict = "PASS" if fail_count == 0 and not failures else "FAIL"

    if args.write_artifacts:
        md_path, tsv_path, verdict, pass_count, fail_count = write_outputs(root, rows, failures, warnings, args.stamp)
        print(f"VERDICT: {verdict}")
        print(f"PASS rows: {pass_count}")
        print(f"FAIL rows: {fail_count}")
        print(f"Markdown: {md_path}")
        print(f"TSV: {tsv_path}")
    else:
        print(json.dumps({"verdict": verdict, "rows": rows, "failures": failures, "warnings": warnings}, indent=2))

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

