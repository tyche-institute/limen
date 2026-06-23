#!/usr/bin/env python3
"""Build a local static LIMEN dashboard preview from the fail-closed UI config.

This is a bounded, offline renderer for reviewer/dashboard parity checks. It
renders only configured count-bearing views whose local TSV export still matches
row-count and SHA-256 values declared in dashboard/release-card-ui-config-v0.1.json.
No network access, upload, deposit, or source collection is performed.
"""

import argparse
import csv
import hashlib
import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from limen_caption_currentness_gate import caption_audit_path_for_root, caption_gate_for_view

MAX_PREVIEW_ROWS = 5
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


def count_rows(path: Path) -> int:
    return len(read_tsv(path))


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
    failures = []
    for row in rows:
        key = (row.get("dashboard_view", ""), row.get("row_key", ""))
        if key in mapping:
            failures.append("duplicate source-ledger join key: " + "|".join(key))
        mapping[key] = row
        if not row.get("public_dashboard_action", "").strip():
            failures.append("source-ledger join row missing public_dashboard_action: " + "|".join(key))
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
            join_payload = {"row_key": row_key, "public_dashboard_action": "block_row_level_access_rights_labels", "join_confidence": "missing_join_row"}
        else:
            join_payload = {
                "row_key": row_key,
                "source_id_or_path": join.get("source_id_or_path", ""),
                "join_confidence": join.get("join_confidence", ""),
                "rollup_policy": join.get("rollup_policy", ""),
                "human_review_needed": join.get("human_review_needed", ""),
                "public_dashboard_action": join.get("public_dashboard_action", ""),
            }
        action = join_payload.get("public_dashboard_action", "")
        actions[action] = actions.get(action, 0) + 1
        enriched_row = dict(row)
        enriched_row["_source_ledger_join"] = join_payload
        enriched.append(enriched_row)
    return enriched, missing, actions


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
    actual_rows = None
    actual_sha = ""
    rows = []
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


def compact_columns(rows):
    if not rows:
        return []
    preferred = [
        "source_family", "saturation_state", "dashboard_readiness", "safe_claim_posture_now",
        "category_code", "category_label", "support_state", "paper_safe_role_now",
        "stage_code", "stage_label", "lineage_count", "publication_confidence_note",
        "jurisdiction", "language", "record_count", "translation_review_needed_count",
        "review_priority", "legal_conclusion_limit", "minimum_stronger_source_needed",
        "threshold_class", "member_count", "reviewer_safe_reading",
        "edge_id", "edge_type", "cross_source_overlap", "evidence_tier_ceiling",
    ]
    available = rows[0].keys()
    cols = [c for c in preferred if c in available]
    if cols:
        return cols[:6]
    return list(available)[:6]


def render_table(rows):
    if not rows:
        return "<p class='muted'>No rows in source export.</p>"
    cols = compact_columns(rows)
    head = "".join(f"<th>{html.escape(c)}</th>" for c in cols)
    body = []
    for row in rows[:MAX_PREVIEW_ROWS]:
        body.append("<tr>" + "".join(f"<td>{html.escape(str(row.get(c, '')))}</td>" for c in cols) + "</tr>")
    note = "" if len(rows) <= MAX_PREVIEW_ROWS else f"<p class='muted'>Showing first {MAX_PREVIEW_ROWS} of {len(rows)} rows; full source remains in TSV.</p>"
    return f"<table><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table>{note}"


def build(root: Path, out_path: Path):
    cfg_path = root / "dashboard/release-card-ui-config-v0.1.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    caption_audit_path = caption_audit_path_for_root(root)
    source_join_path, source_join_map, source_join_failures = read_source_ledger_join(root)
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")

    sections = []
    gate_rows = []
    for view in cfg.get("views", []):
        gate = view_gate(root, view, caption_audit_path, source_join_map)
        if source_join_failures:
            gate["allowed"] = False
            gate["reasons"].extend(source_join_failures)
        caption_gate = caption_gate_for_view(view.get("dashboard_view", ""), caption_audit_path)
        status = "PASS" if gate["allowed"] else "FAIL"
        gate_rows.append({
            "dashboard_view": view.get("dashboard_view", ""),
            "status": status,
            "allowed_to_render": str(gate["allowed"]).lower(),
            "configured_rows": view.get("source_data_rows", ""),
            "actual_rows": gate["actual_rows"] if gate["actual_rows"] is not None else "",
            "configured_sha256": view.get("source_sha256", ""),
            "actual_sha256": gate["actual_sha"],
            "source_ledger_join_actions": json.dumps(gate["source_join_actions"], sort_keys=True),
            "caption_currentness_status": caption_gate["status"],
            "caption_currentness_reason": caption_gate["reason"],
            "reason": "all guards present" if gate["allowed"] else "; ".join(gate["reasons"]),
        })
        if gate["allowed"]:
            preview = render_table(gate["rows"])
        else:
            preview = "<p class='fail'>Fail-closed: preview not rendered because guard checks failed.</p>"
        sections.append(f"""
<section class='card {status.lower()}'>
  <h2>{html.escape(view.get('dashboard_view', 'unnamed_view'))}</h2>
  <p><strong>Manuscript surface:</strong> {html.escape(view.get('manuscript_surface', ''))}</p>
  <p><strong>Denominator / subtitle:</strong> {html.escape(view.get('subtitle', ''))}</p>
  <p><strong>Claim boundary:</strong> {html.escape(view.get('claim_boundary', ''))}</p>
  <p><strong>Prohibited reading:</strong> {html.escape(view.get('prohibited_reading', ''))}</p>
  <p><strong>Source:</strong> <code>{html.escape(view.get('source_path', ''))}</code> · rows {html.escape(str(gate['actual_rows']))} · SHA-256 <code>{html.escape(gate['actual_sha'][:16])}</code></p>
  <p><strong>Source-ledger join actions:</strong> <code>{html.escape(json.dumps(gate["source_join_actions"], sort_keys=True))}</code></p>
  <p><strong>Caption-currentness gate:</strong> <span class='{caption_gate['status'].lower()}'>{html.escape(str(caption_gate['status']))}</span> — {html.escape(str(caption_gate['reason']))}</p>
  <p><strong>Gate:</strong> <span class='{status.lower()}'>{status}</span> — {html.escape('all guards present' if gate['allowed'] else '; '.join(gate['reasons']))}</p>
  {preview}
</section>
""")

    pass_count = sum(1 for r in gate_rows if r["status"] == "PASS")
    fail_count = sum(1 for r in gate_rows if r["status"] == "FAIL")
    verdict = "PASS" if fail_count == 0 else "FAIL"
    global_rules = "".join(f"<li>{html.escape(rule)}</li>" for rule in cfg.get("global_rules", []))

    html_doc = f"""<!doctype html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<title>LIMEN static dashboard preview v0.1</title>
<style>
body {{ font-family: system-ui, -apple-system, Segoe UI, sans-serif; margin: 2rem; line-height: 1.45; color: #1f2937; background: #f8fafc; }}
header, .card {{ background: white; border: 1px solid #d8dee9; border-radius: 12px; padding: 1rem 1.25rem; margin: 1rem 0; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.06); }}
h1 {{ margin-top: 0; }}
.card.pass {{ border-left: 6px solid #15803d; }}
.card.fail {{ border-left: 6px solid #b91c1c; }}
.pass {{ color: #15803d; font-weight: 700; }}
.fail {{ color: #b91c1c; font-weight: 700; }}
.muted {{ color: #64748b; font-size: 0.93rem; }}
table {{ border-collapse: collapse; width: 100%; margin-top: 0.75rem; font-size: 0.9rem; }}
th, td {{ border: 1px solid #d8dee9; padding: 0.45rem; vertical-align: top; }}
th {{ background: #eef2ff; text-align: left; }}
code {{ background: #eef2f7; padding: 0.1rem 0.25rem; border-radius: 4px; }}
</style>
</head>
<body>
<header>
  <h1>LIMEN static dashboard preview v0.1</h1>
  <p><strong>Generated:</strong> {html.escape(generated)}</p>
  <p><strong>Lane:</strong> limen-dashboard-paper-forge · <strong>Project:</strong> limen-ai-edge-case-atlas</p>
  <p><strong>Verdict:</strong> <span class='{verdict.lower()}'>{verdict}</span> ({pass_count} pass / {fail_count} fail)</p>
  <p>This offline preview renders dashboard surfaces only when the release-card UI config, local TSV row counts, SHA-256 hashes, denominator labels, tooltip requirements, source-ledger join rows, and prohibited-reading warnings agree. It consumes <code>results/dashboard/source-ledger-join-v0.1.tsv</code> for tooltip action state. It is not a public release and performs no collection, upload, deposit, or submission.</p>
  <h2>Global reviewer-safe rules</h2>
  <ul>{global_rules}</ul>
</header>
{''.join(sections)}
</body>
</html>
"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_doc, encoding="utf-8")
    return verdict, pass_count, fail_count, gate_rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--output", default="dashboard/static-dashboard-preview-v0.1.html")
    parser.add_argument("--write-gate-tsv", default="")
    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    out_path = root / args.output
    verdict, pass_count, fail_count, gate_rows = build(root, out_path)
    if args.write_gate_tsv:
        gate_path = root / args.write_gate_tsv
        gate_path.parent.mkdir(parents=True, exist_ok=True)
        fields = ["dashboard_view", "status", "allowed_to_render", "configured_rows", "actual_rows", "configured_sha256", "actual_sha256", "source_ledger_join_actions", "caption_currentness_status", "caption_currentness_reason", "reason"]
        with gate_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            writer.writerows(gate_rows)
    print(f"VERDICT: {verdict}")
    print(f"PASS rows: {pass_count}")
    print(f"FAIL rows: {fail_count}")
    print(f"HTML: {out_path}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

