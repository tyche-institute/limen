import csv
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from limen_caption_currentness_gate import caption_gate_for_view


def write_audit(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        {
            "as_of_utc": "2026-06-18T20:55:00Z",
            "control_id": "CCR-001",
            "shared_slot": "Figure 2 taxonomy support heatmap",
            "domain": "taxonomy",
            "audit_state": "BLOCK_FOR_COUNT_BEARING_REUSE",
            "stale_denominator_terms_found": "39 review rows / 38 governed records / 28",
            "current_terms_found": "",
            "required_current_caption_floor": "39/29 core; 44/34 extended; legacy 35/27 provenance only",
            "source_caption_register": "results/dashboard-paper/caption-control-register-v0.1.tsv",
            "safe_reuse_action": "rewrite caption/control text before PDF, dashboard, or manuscript export",
            "claim_boundary": "caption-currentness/parity audit only",
        },
        {
            "as_of_utc": "2026-06-18T20:55:00Z",
            "control_id": "CCR-005",
            "shared_slot": "Figure 5 publication-safe evidence-tier funnel",
            "domain": "publication_funnel",
            "audit_state": "PASS_WITH_CURRENT_DENOMINATOR_LANGUAGE",
            "stale_denominator_terms_found": "",
            "current_terms_found": "21 publication-safe",
            "required_current_caption_floor": "21 publication-safe lineages; confidence/translation bands are ceilings",
            "source_caption_register": "results/dashboard-paper/caption-control-register-v0.1.tsv",
            "safe_reuse_action": "may be reused",
            "claim_boundary": "caption-currentness/parity audit only",
        },
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def test_taxonomy_view_fails_closed_when_caption_audit_blocks_control(tmp_path):
    audit = tmp_path / "caption-currentness-audit-v0.9.tsv"
    write_audit(audit)

    gate = caption_gate_for_view("taxonomy_heatmap", audit)

    assert gate["allowed"] is False
    assert gate["status"] == "FAIL"
    assert "CCR-001" in gate["reason"]
    assert "BLOCK_FOR_COUNT_BEARING_REUSE" in gate["reason"]


def test_unblocked_view_passes_with_caption_audit_source(tmp_path):
    audit = tmp_path / "caption-currentness-audit-v0.9.tsv"
    write_audit(audit)

    gate = caption_gate_for_view("evidence_tier_funnel", audit)

    assert gate["allowed"] is True
    assert gate["status"] == "PASS"
    assert gate["reason"] == "caption currentness audit permits count-bearing reuse"
    assert gate["source"] == str(audit)
