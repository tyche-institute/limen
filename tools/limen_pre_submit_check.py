#!/usr/bin/env python3
"""LIMEN pre-submission self-check.

Automated parity verification for the LIMEN AI Edge-Case Atlas submission
package. Runs all hostile-reviewer residue checks, denominator discipline
verification, SI materialization audit, and cross-surface parity validation.

Usage:
    python3 tools/limen_pre_submit_check.py [--project-root PATH]

Exit codes:
    0 = all checks pass
    1 = one or more checks fail (see report)

This script is part of the LIMEN reproducibility package. It verifies that
the submission surfaces (manuscript, cover letter, submission kit, SI) are
internally consistent and free of pipeline artifacts before upload.

Part of: LIMEN AI Edge-Case Atlas
Author: Anton Sokolov (Tyche Institute)
License: CC-BY-4.0 (code component of data descriptor submission)
"""

import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Denominators that must appear consistently across all surfaces
CANONICAL_DENOMINATORS = {
    "evidence_grade_total": 250,
    "t3_regulator_court": 157,
    "t2_contested_interim": 82,
    "t1_cve_security": 11,
    "media_documented": 46,
    "total_all_classes": 296,
    "jurisdictions": 34,
    "source_links": 233,
    "source_link_pct": "93.2",
    "taxonomy_categories": 15,
    "core_refs": 39,
    "unique_lineages": 29,
    "publication_safe_lineages": 21,
    "duplicate_review_edges": 27,
    "source_family_rows": 15,
    "jurisdiction_language_rows": 12,
    "security_threshold_rows": 4,
    "trust_surface_rows": 4,
}

# Stale denominators that must NOT appear
STALE_DENOMINATORS = [
    r"\b248\s+evidence[- ]grade\b",
    r"\b294\b",
    r"\b\|\s*80\s*\|",
    r"\bcorrected to 32\b",
    r"\b248\s+cases\b",
    r"\b248/80/32\b",
]

# Pipeline residue patterns that must NOT appear in prose
RESIDUE_PATTERNS = [
    (r"results/boost/", "boost-local path"),
    (r"results/security/", "security-local path"),
    (r"\bshard\b", "shard label"),
    (r"\blane\b(?!s?\s+run)", "lane label"),
    (r"\bpipeline\b(?!s?\s+step)", "pipeline jargon"),
]

# SI objects that must have source files
SI_OBJECTS = {
    "S1": "results/dashboard/authoritative-document-depth-facet.tsv",
    "S2": "results/dashboard/security-threshold-ladder-panel.tsv",
    "S3": "results/security/security-agentic-threshold-change-matrix-v0.1.tsv",
    "S4": "results/dashboard/provenance-confusion-publication-cells.tsv",
    "S5": "results/dashboard/security-publication-buckets.tsv",
    "S6": "results/dashboard/security-crosswalk-coverage-panel.tsv",
    "S7": "results/dashboard/supplementary-table-s7-trust-boundary-breadth.tsv",
    "S8": "results/dashboard/supplementary-table-s8-supply-chain-frontier.tsv",
    "S9": "results/dashboard/supplementary-table-s9-peer-review-gap.tsv",
    "S10": "results/dashboard/procedural-contamination-source-depth-panel.tsv",
    "S11": "results/dashboard/supplementary-table-s11-research-integrity.tsv",
    "S12": "results/dashboard/procedural-contamination-source-depth-panel.tsv",
    "S13": "results/dashboard/public-sector-disclosure-comparison.tsv",
    "S14": "results/dashboard/attestation-trust-surface-readiness.tsv",
    "S15": "results/dashboard/supplementary-table-s1-panel-c-jurisdiction-tier.tsv",
    "Figure S1": "results/dashboard-paper/figure-reviewed-core-tier-by-theme.png",
    "Note 1": "results/dashboard-paper/caption-control-register-v0.1.tsv",
}

# Manuscript figure/table slots that must be referenced.
# v0.6 migrated legacy dashboard-internal Table A/B/C labels to formal
# manuscript Tables 3/4/5/6. The dashboard spec may still mention the legacy
# labels as internal control surfaces, but the submission manuscript should not.
REQUIRED_SLOTS = [
    "Figure 1", "Figure 2", "Figure 3", "Figure 4",
    "Figure 5", "Figure 6", "Figure 7", "Figure 8",
    "Table 1", "Table 2", "Table 3", "Table 4", "Table 5", "Table 6",
]

FORBIDDEN_MANUSCRIPT_SLOTS = ["Table A", "Table B", "Table C", "Table D"]

METHODS_CAPTION_EXPORT_AUDIT = (
    "results/boost/limen-dashboard-paper-forge/methods-caption-export-audit-v1.5.tsv"
)
REQUIRED_METHODS_CAPTION_AUDIT_IDS = {
    "MCE-001",
    "MCE-002",
    "MCE-003",
    "MCE-004",
    "MCE-005",
    "MCE-006",
    "MCE-007",
}


# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------

def read_file(path):
    """Read file content, return text or None if missing."""
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except (FileNotFoundError, PermissionError):
        return None


def check_residue(text, label):
    """Check for pipeline residue patterns in text."""
    findings = []
    for pattern, desc in RESIDUE_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            findings.append(f"  FAIL: {desc} found ({len(matches)} occurrences) in {label}")
    return findings


def check_stale_denominators(text, label):
    """Check for stale denominator values."""
    findings = []
    for pattern in STALE_DENOMINATORS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            findings.append(f"  FAIL: stale denominator '{pattern}' found ({len(matches)}x) in {label}")
    return findings


def check_slot_references(text, label):
    """Check that all required figure/table slots are referenced."""
    findings = []
    for slot in REQUIRED_SLOTS:
        if slot not in text:
            findings.append(f"  WARN: {slot} not referenced in {label}")
    for slot in FORBIDDEN_MANUSCRIPT_SLOTS:
        if slot in text:
            findings.append(f"  FAIL: legacy {slot} label still appears in {label}")
    return findings


def check_si_materialization(root):
    """Check that all SI source files exist."""
    findings = []
    for si_id, rel_path in SI_OBJECTS.items():
        full_path = root / rel_path
        if not full_path.exists():
            # Try alternate paths
            alt = root / rel_path.replace("supplementary-table-s15-", "supplementary-table-s1-panel-c-")
            if not alt.exists():
                findings.append(f"  FAIL: {si_id} source file missing: {rel_path}")
        else:
            size = full_path.stat().st_size
            if size == 0:
                findings.append(f"  FAIL: {si_id} source file is empty: {rel_path}")
    return findings


def check_denominator_in_text(text, label, key, expected):
    """Check that a canonical denominator appears in text."""
    findings = []
    expected_str = str(expected)
    # Flexible matching — look for the number in context
    if expected_str not in text:
        findings.append(f"  WARN: denominator {key}={expected} not found verbatim in {label}")
    return findings


def check_cross_surface_parity(root):
    """Check that key denominators match across manuscript, cover letter, kit."""
    findings = []
    surfaces = {
        "preprint": root / "draft" / "preprint.md",
        "f1000_manuscript": root / "draft" / "preprint-v0.3-f1000.md",
        "cover_letter": root / "draft" / "cover-letter-f1000.md",
        "submission_kit": root / "draft" / "f1000-submission-kit.md",
    }

    texts = {}
    for name, path in surfaces.items():
        content = read_file(path)
        if content:
            texts[name] = content
        else:
            findings.append(f"  WARN: {name} file not found at {path}")

    # Check critical denominators — some are surface-specific
    # "250" and "34 jurisdictions" should appear in all surfaces
    universal_patterns = [
        (r"\b250\b", "evidence-grade total (250)"),
        (r"\b34\s+jurisdictions?\b", "jurisdiction count (34)"),
    ]
    # "233" source-link count is F1000-specific (patched into f1000 manuscript + cover letter)
    f1000_only_patterns = [
        (r"\b233\b", "source-link count (233)"),
    ]

    for pattern, desc in universal_patterns:
        for name, text in texts.items():
            if not re.search(pattern, text, re.IGNORECASE):
                findings.append(f"  WARN: {desc} not found in {name}")

    for pattern, desc in f1000_only_patterns:
        for name in ["f1000_manuscript", "cover_letter"]:
            if name in texts and not re.search(pattern, texts[name], re.IGNORECASE):
                findings.append(f"  WARN: {desc} not found in {name}")

    return findings


def check_no_fused_denominator(text, label):
    """Check that the text explicitly rejects a fused denominator."""
    findings = []
    if "fused" not in text.lower() and "not one" not in text.lower():
        findings.append(f"  WARN: {label} may lack explicit fused-denominator rejection")
    return findings


def check_figure_files(root):
    """Check that figure files exist."""
    findings = []
    fig_dir = root / "results" / "boost" / "limen-dashboard-paper-forge" / "figures"
    if not fig_dir.exists():
        findings.append("  WARN: figures directory not found")
        return findings

    png_files = list(fig_dir.glob("*.png"))
    svg_files = list(fig_dir.glob("*.svg"))

    if len(png_files) < 7:
        findings.append(f"  WARN: expected ≥7 PNG figures, found {len(png_files)}")
    if len(svg_files) < 7:
        findings.append(f"  WARN: expected ≥7 SVG figures, found {len(svg_files)}")

    return findings


def check_methods_caption_export_audit(root):
    """Fail closed unless the v1.5 methods/caption export audit is current and all rows pass.

    This bridges the dashboard/paper parity lane into the pre-submission package
    gate. It verifies package-integrity/provenance-label export controls only;
    it does not promote rows or validate incident/legal/source-truth claims.
    """
    findings = []
    audit_path = root / METHODS_CAPTION_EXPORT_AUDIT
    if not audit_path.exists():
        return [f"  FAIL: methods/caption export audit missing: {METHODS_CAPTION_EXPORT_AUDIT}"]

    try:
        with audit_path.open(newline="", encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        return [f"  FAIL: methods/caption export audit unreadable: {exc}"]

    if not rows:
        return [f"  FAIL: methods/caption export audit has no rows: {METHODS_CAPTION_EXPORT_AUDIT}"]

    seen_ids = set()
    for idx, row in enumerate(rows, start=2):
        audit_id = (row.get("audit_id") or "").strip()
        status = (row.get("status") or "").strip().upper()
        evidence = (row.get("evidence") or "").strip()
        claim_ceiling = (row.get("claim_ceiling") or "").strip()
        blocked_overread = (row.get("blocked_overread") or "").strip()
        if audit_id:
            seen_ids.add(audit_id)
        if status != "PASS":
            findings.append(f"  FAIL: {audit_id or 'row ' + str(idx)} status is {status or 'blank'}, expected PASS")
        if not evidence:
            findings.append(f"  FAIL: {audit_id or 'row ' + str(idx)} lacks evidence text")
        if not claim_ceiling:
            findings.append(f"  FAIL: {audit_id or 'row ' + str(idx)} lacks claim_ceiling text")
        if not blocked_overread:
            findings.append(f"  FAIL: {audit_id or 'row ' + str(idx)} lacks blocked_overread text")

    missing = sorted(REQUIRED_METHODS_CAPTION_AUDIT_IDS - seen_ids)
    if missing:
        findings.append(f"  FAIL: methods/caption export audit missing required rows: {', '.join(missing)}")

    return findings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="LIMEN pre-submission self-check")
    parser.add_argument(
        "--project-root",
        default="/srv/tyche/projects/limen-ai-edge-case-atlas",
        help="Project root directory",
    )
    args = parser.parse_args()
    root = Path(args.project_root).resolve()

    print("=" * 70)
    print("LIMEN Pre-Submission Self-Check")
    print(f"Time: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    print(f"Project root: {root}")
    print("=" * 70)

    all_findings = []
    pass_count = 0
    fail_count = 0
    warn_count = 0

    # --- Check 1: Residue in preprint ---
    print("\n[1/8] Pipeline residue check (preprint v0.5)...")
    preprint = read_file(root / "draft" / "preprint.md")
    if preprint:
        findings = check_residue(preprint, "preprint.md")
        if not findings:
            print("  PASS: 0 residue patterns found")
            pass_count += 1
        else:
            for f in findings:
                print(f)
                if "FAIL" in f:
                    fail_count += 1
                else:
                    warn_count += 1
            all_findings.extend(findings)
    else:
        print("  FAIL: preprint.md not found")
        fail_count += 1

    # --- Check 2: Stale denominators ---
    print("\n[2/8] Stale denominator check...")
    surfaces_to_check = [
        ("preprint.md", root / "draft" / "preprint.md"),
        ("f1000 manuscript", root / "draft" / "preprint-v0.3-f1000.md"),
        ("cover letter", root / "draft" / "cover-letter-f1000.md"),
        ("submission kit", root / "draft" / "f1000-submission-kit.md"),
    ]
    stale_found = False
    for label, path in surfaces_to_check:
        text = read_file(path)
        if text:
            findings = check_stale_denominators(text, label)
            if findings:
                stale_found = True
                for f in findings:
                    print(f)
                    fail_count += 1
                all_findings.extend(findings)
    if not stale_found:
        print("  PASS: 0 stale denominators across all surfaces")
        pass_count += 1

    # --- Check 3: SI materialization ---
    print("\n[3/8] SI materialization audit (S1-S15 + Figure S1 + Note 1)...")
    findings = check_si_materialization(root)
    if not findings:
        print(f"  PASS: all {len(SI_OBJECTS)} SI objects have source files")
        pass_count += 1
    else:
        for f in findings:
            print(f)
            if "FAIL" in f:
                fail_count += 1
            else:
                warn_count += 1
        all_findings.extend(findings)

    # --- Check 4: Figure/table slot references ---
    print("\n[4/8] Figure/table slot registration...")
    if preprint:
        findings = check_slot_references(preprint, "preprint.md")
        if not findings:
            print(f"  PASS: all {len(REQUIRED_SLOTS)} slots referenced")
            pass_count += 1
        else:
            for f in findings:
                print(f)
                warn_count += 1
            all_findings.extend(findings)

    # --- Check 5: Cross-surface parity ---
    print("\n[5/8] Cross-surface denominator parity...")
    findings = check_cross_surface_parity(root)
    if not findings:
        print("  PASS: key denominators consistent across submission surfaces")
        pass_count += 1
    else:
        for f in findings:
            print(f)
            warn_count += 1
        all_findings.extend(findings)

    # --- Check 6: Fused-denominator rejection ---
    print("\n[6/8] Fused-denominator rejection...")
    if preprint:
        findings = check_no_fused_denominator(preprint, "preprint.md")
        if not findings:
            print("  PASS: explicit fused-denominator rejection present")
            pass_count += 1
        else:
            for f in findings:
                print(f)
                warn_count += 1
            all_findings.extend(findings)

    # --- Check 7: Figure files ---
    print("\n[7/8] Figure file presence...")
    findings = check_figure_files(root)
    if not findings:
        print("  PASS: figure files present (PNG + SVG)")
        pass_count += 1
    else:
        for f in findings:
            print(f)
            warn_count += 1
        all_findings.extend(findings)

    # --- Check 8: Claim-boundary language ---
    print("\n[8/9] Claim-boundary language check...")
    if preprint:
        boundary_phrases = [
            "does not claim",
            "not claim",
            "does not support",
            "bounded",
            "ceiling",
        ]
        found_boundaries = sum(1 for p in boundary_phrases if p.lower() in preprint.lower())
        if found_boundaries >= 3:
            print(f"  PASS: {found_boundaries}/{len(boundary_phrases)} claim-boundary phrases present")
            pass_count += 1
        else:
            print(f"  WARN: only {found_boundaries}/{len(boundary_phrases)} claim-boundary phrases found")
            warn_count += 1

    # --- Check 9: Methods/caption export audit ---
    print("\n[9/9] Methods/caption export audit gate (v1.5)...")
    findings = check_methods_caption_export_audit(root)
    if not findings:
        print("  PASS: v1.5 methods/caption export audit rows present and PASS")
        pass_count += 1
    else:
        for f in findings:
            print(f)
            if "FAIL" in f:
                fail_count += 1
            else:
                warn_count += 1
        all_findings.extend(findings)

    # --- Summary ---
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  PASS: {pass_count}")
    print(f"  FAIL: {fail_count}")
    print(f"  WARN: {warn_count}")
    print()

    if fail_count == 0 and warn_count == 0:
        print("VERDICT: ALL CHECKS PASS — submission package is internally consistent.")
        print("Remaining external blockers: Zenodo deposit, F1000Research upload (Anton).")
    elif fail_count == 0:
        print(f"VERDICT: PASS WITH WARNINGS ({warn_count}) — review warnings above before submission.")
    else:
        print(f"VERDICT: FAIL ({fail_count} failures) — fix before submission.")

    print()
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
