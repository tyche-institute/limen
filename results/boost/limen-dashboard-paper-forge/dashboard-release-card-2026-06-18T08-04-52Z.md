# LIMEN dashboard release card v0.1

Generated: 2026-06-18T08:04:52.660952+00:00
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`
Sprint: hostile-reviewer pass / dashboard-paper parity

## Purpose

This artifact turns the existing dashboard/paper parity package into a reviewer-safe public-dashboard release card. It does not publish or upload anything. It records the exact source export, row count, checksum, visible denominator label, tooltip rule, and prohibited reading for each dashboard view before any interactive UI copies counts into a public surface.

## Release-card table

| Dashboard view | Manuscript surface | Source export | Rows | Visible denominator / claim ceiling | UI status |
|---|---|---|---:|---|---|
| `source_family_saturation` | Figure 1 / Figure 4 | `results/dashboard/source-family-coverage.tsv` | 15 | source-family rows; saturation/uncertainty, not completeness | ready_as_bounded_control_surface |
| `taxonomy_heatmap` | Figure 2 + Table 2 | `results/dashboard/taxonomy-heatmap.tsv` | 15 | core 39/29; sidecar 44/34; taxonomy support, not prevalence | ready_as_bounded_control_surface |
| `evidence_tier_funnel` | Figure 3 / Figure 5 variant | `results/dashboard/evidence-funnel.tsv` | 11 | 296 catalogued / 250 evidence-grade / 46 excluded / 21 publication-safe lineages where used | ready_as_bounded_control_surface |
| `jurisdiction_language` | Figure 5 / S1 Panel C | `results/dashboard/jurisdiction-language-coverage.tsv` | 12 | 34 jurisdictions broad; 12 reviewed-core non-English rows where panel used; no country ranking | ready_as_bounded_control_surface |
| `legal_uncertainty` | Figure 6 | `results/dashboard/legal-uncertainty-matrix.tsv` | 15 | uncertainty routing only; no compliance/liability conclusion | ready_as_bounded_control_surface |
| `security_agentic_threshold` | Figure 7 | `results/dashboard/security-threshold-ladder-panel.tsv` | 4 | 4 threshold rows; 11 security rows where described; not security prevalence | ready_as_bounded_control_surface |
| `duplicate_review_graph` | Figure 8 | `results/dashboard/duplicate-review-graph.tsv` | 27 | 27 duplicate-review edges; 0 merge decisions; not proof all duplicates are absent | ready_as_bounded_control_surface |

## Reviewer-safe UI requirements

1. Show denominator labels before or next to every count-bearing chart.
2. Keep Figure 2, Figure 5, and Figure 7 denominators separate: 39/29 taxonomy support, 21 publication-safe lineages, and 4 security threshold rows respectively.
3. Tooltips must expose denominator scope, claim ceiling, uncertainty/provenance status, and source artifact path/checksum.
4. The dashboard may show source-family saturation and uncertainty, but must not market LIMEN as complete.
5. Legal/normative/security labels are routing and proof-ceiling labels, not findings of law, compliance, certification, safety, guilt, or prevalence.
6. Jurisdiction/language views are coverage and review-burden surfaces only; they must not rank countries or infer deployment readiness.
7. Row-level source provenance remains bounded by the source-ledger join audit: export-level checksums are available, but row-level access-date/rights labels should not be implied where no ledger match exists.

## Validation

- Pre-submit checker command: `python3 tools/limen_pre_submit_check.py`
- Exit code: `0`
- Output summary: `VERDICT: ALL CHECKS PASS — submission package is internally consistent.`

## Paper-readiness delta

The dashboard now has a compact release gate linking seven count-bearing views to manuscript surfaces, checksums, denominator captions, and prohibited interpretations. This strengthens hostile-reviewer readiness by preventing an interactive dashboard from silently weakening the article's denominator discipline or source-provenance cautions.

## Claim boundary

No new collection, upload, deposit, publication, denominator change, legal/compliance/certification/safety/prevalence claim, or country ranking was made.

## Next smallest move

If Anton proceeds toward a public dashboard, wire these seven release-card rows into the UI configuration so chart subtitles and tooltips inherit the exact denominator and prohibited-reading language from the TSV.
