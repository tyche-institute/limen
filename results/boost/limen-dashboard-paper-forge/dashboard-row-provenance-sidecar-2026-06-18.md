# LIMEN dashboard row-level provenance sidecar v0.1

Generated: 2026-06-18T06:04:55Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`
Artifact: `results/boost/limen-dashboard-paper-forge/dashboard-row-provenance-sidecar-2026-06-18.tsv`
SHA-256: `811bd29b1782a7547b35722ae7a5459f1c1d15e12e02647b405e7a0b033c7344`

## Purpose

This sidecar converts the seven dashboard/paper TSV exports into a single row-level control table for a future interactive dashboard. It does not add new evidence, change denominators, or relax any claim ceiling. Its function is to make missing row-level provenance fields explicit before public dashboard release.

## Scope and counts

| Dashboard export | Sidecar rows |
|---|---:|
| `results/dashboard/source-family-coverage.tsv` | 15 |
| `results/dashboard/taxonomy-heatmap.tsv` | 15 |
| `results/dashboard/evidence-funnel.tsv` | 11 |
| `results/dashboard/jurisdiction-language-coverage.tsv` | 12 |
| `results/dashboard/legal-uncertainty-matrix.tsv` | 15 |
| `results/dashboard/security-threshold-ladder-panel.tsv` | 4 |
| `results/dashboard/duplicate-review-graph.tsv` | 27 |

| **Total** | **99** |

## Readiness result

- Rows with direct row-level source/provenance pointers: 88/99.
- Rows still relying on SI/manuscript/companion-text provenance instead of direct row-level pointers: 11/99.
- Rows with row-level language or language-scope values: 27/99.
- Rows with row-level jurisdiction or jurisdiction-scope values: 27/99.
- Access-date and rights/terms fields are intentionally marked as source-ledger joins before public dashboard release, not inferred in this cycle.

## Interpretation

The manuscript package remains internally consistent: `tools/limen_pre_submit_check.py` passes 8/8. This sidecar identifies the remaining dashboard-engineering gap: row-level public-dashboard exports should join `accessed_at`, `rights_terms_note`, direct `source_id`/URL/path, and translation-review status from the source ledger or SI package rather than relying on companion prose.

## Claim boundary

This is a provenance/control artifact only. It supports dashboard API readiness, hostile-reviewer traceability, and reproducibility. It does not support completeness, prevalence, legal guilt, non-compliance, certification, safety assurance, country ranking, or final legal/policy claims from machine translation.

## Observatory hook

The dashboard can load this sidecar as a universal tooltip layer. Recommended tooltip fields: `row_key`, `dashboard_surface`, `manuscript_surface`, `denominator_scope`, `claim_ceiling`, `reviewer_safe_reading`, `source_pointer_status`, `source_id_or_pointer`, `accessed_at_status`, `rights_terms_status`, `translation_status`, and `action_needed_before_public_dashboard`.

## Next smallest move

Join this sidecar to the authoritative source ledger/SI manifest to replace `not_row_level_in_export` and `needs_source_ledger_join` statuses with concrete source IDs, URLs/paths, access dates, and rights/terms notes where those values are available. Do not crawl or expand the corpus unless a named figure/table claim needs it.
