# Figure File Generation and SI Packaging Verification

Generated: 2026-06-19T00:00:00Z
Lane: `limen-dashboard-paper-forge`

## What was done

Generated 7 publication figures (Figures 2–8) from live dashboard TSVs and
packaged all 17 supplementary information objects plus figure files into a
submission-ready bundle.

## Figures generated

| Figure | Title | Source TSV | PNG (KB) | SVG (KB) |
|--------|-------|------------|----------|----------|
| 2 | Taxonomy Heatmap | taxonomy-heatmap.tsv | 266.6 | 114.6 |
| 3 | Evidence-Tier Funnel and Confidence Cap | evidence-funnel.tsv | 183.2 | 58.3 |
| 4 | Source-Family Saturation Map | source-family-coverage.tsv | 279.1 | 113.2 |
| 5 | Jurisdiction and Language Coverage | jurisdiction-language-coverage.tsv | 147.3 | 78.7 |
| 6 | Legal Uncertainty Matrix | legal-uncertainty-matrix.tsv | 235.4 | 104.9 |
| 7 | Security Threshold Ladder | security-threshold-ladder-panel.tsv | 154.3 | 80.1 |
| 8 | Duplicate-Review Graph | duplicate-review-graph.tsv | 163.3 | 47.7 |

All figures include:
- Explicit denominator annotation in title or subtitle
- Claim-ceiling disclaimer (does not represent prevalence/completeness)
- Colorblind-friendly palette
- 300 dpi PNG + vector SVG
- Review-priority or evidence-tier encoding

## Denominator discipline in figures

| Figure | Denominator class | Value |
|--------|-------------------|-------|
| 2 | Taxonomy core | 39 governed record refs / 29 unique lineages |
| 2 | Taxonomy extended sidecar | 44 / 34 |
| 3 | Publication-safe lineages | 21 |
| 5 | Jurisdiction/language rows | 12 (reviewed-core) |
| 7 | Security threshold classes | 4 (11 total security rows) |
| 8 | Duplicate-review edges | 27 |

## SI package contents

Location: `results/boost/limen-dashboard-paper-forge/si-package/`

| Object | Filename | Source | Size |
|--------|----------|--------|------|
| S1 | supplementary-s1.tsv | authoritative-document-depth-facet.tsv | 8.0 KB |
| S2 | supplementary-s2.tsv | security-threshold-ladder-panel.tsv | 1.2 KB |
| S3 | supplementary-s3.tsv | security-authority-balance-panel.tsv | 0.9 KB |
| S4 | supplementary-s4.tsv | provenance-confusion-publication-cells.tsv | 6.2 KB |
| S5 | supplementary-s5.tsv | security-publication-buckets.tsv | 7.5 KB |
| S6 | supplementary-s6.tsv | security-crosswalk-coverage-panel.tsv | 1.3 KB |
| S7 | supplementary-s7.tsv | supplementary-table-s7-trust-boundary-breadth.tsv | 2.4 KB |
| S8 | supplementary-s8.tsv | supplementary-table-s8-supply-chain-frontier.tsv | 3.5 KB |
| S9 | supplementary-s9.tsv | supplementary-table-s9-peer-review-gap.tsv | 0.3 KB |
| S10 | supplementary-s10.tsv | procedural-contamination-source-depth-panel.tsv | 9.5 KB |
| S11 | supplementary-s11.tsv | supplementary-table-s11-research-integrity.tsv | 7.0 KB |
| S12 | supplementary-s12.tsv | procedural-contamination-source-depth-panel.tsv | 9.5 KB |
| S13 | supplementary-s13.tsv | public-sector-disclosure-comparison.tsv | 9.0 KB |
| S14 | supplementary-s14.tsv | public-sector-proof-ceilings.tsv | 8.1 KB |
| S15 | supplementary-s15.tsv | supplementary-table-s1-panel-c-jurisdiction-tier.tsv | 4.5 KB |
| Figure S1 | supplementary-figure-s1.svg | figure-reviewed-core-tier-by-theme.svg | 7.9 KB |
| Note 1 | supplementary-note-1.tsv | caption-control-register-v0.1.tsv | 37.6 KB |
| Figures 2–8 | figure-*.png / .svg | Generated from dashboard TSVs | 1,733.2 KB |

Total: 32 files, 2,152.6 KB

## Hostile-reviewer defenses

1. Every figure carries its own denominator in the title/subtitle.
2. No figure implies prevalence, completeness, or legal conclusion.
3. Zero-count rows in Figures 2 and 6 are labeled as methods guardrails.
4. Figure 7 explicitly states it is a bounded companion, not a core count surface.
5. Figure 8 shows 0 merge decisions — all 27 edges reviewed as distinct.
6. SI TSV files are verbatim copies of verified dashboard exports.
7. Figure files generated with matplotlib 3.x, DejaVu Sans, 300 dpi PNG + SVG.

## Remaining blockers (after this cycle)

1. ✅ Figure file generation — RESOLVED
2. ✅ SI file packaging — RESOLVED
3. Source-link exact count: D-12 states "≥232" conservatively; exact count needs dataset refresh.
4. sf08/sf09/sf11 gaps remain documented (not fixable from this lane).
5. Zenodo deposit update — needs upload infrastructure.
6. F1000Research upload — needs Anton's approval and action.

## Paper-readiness delta

**Before this cycle:**
- 0 figure PNG/SVG files for Figures 2–8
- SI TSV files scattered across results/dashboard/ and results/dashboard-paper/
- No submission bundle

**After this cycle:**
- 7 figures × 2 formats = 14 figure files
- 17 SI objects + 14 figure files in one package directory
- Manifest file with provenance chain
- Reproducible generation script at scripts/generate-figures.py

## Submission-readiness update

| Item | Status |
|------|--------|
| F1000 v0.4 manuscript | ✅ COMPLETE |
| Denominator synchronization | ✅ COMPLETE |
| Figure/Table references in prose | ✅ COMPLETE |
| SI references in prose | ✅ COMPLETE |
| Reference list (14 citations) | ✅ COMPLETE |
| Caption discipline | ✅ COMPLETE |
| Figure file generation (PNG/SVG) | ✅ COMPLETE (this cycle) |
| SI TSV file packaging | ✅ COMPLETE (this cycle) |
| Zenodo deposit update | ⏳ REMAINING |
| F1000Research upload | ⏳ REMAINING (needs Anton) |

## Reproducibility

```bash
cd /srv/tyche/projects/limen-ai-edge-case-atlas
python3 scripts/generate-figures.py
```

Dependencies: matplotlib >= 3.5, numpy, csv (stdlib).
