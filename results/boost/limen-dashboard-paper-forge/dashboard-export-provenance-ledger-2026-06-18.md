# LIMEN dashboard export provenance ledger

Generated: 2026-06-18T06-43-05Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`
Scope: existing dashboard exports only; no new collection, upload, publication, or portal action.

## Purpose

This ledger fills the gap exposed by the source-ledger/dashboard join audit: most dashboard rows point to internal dashboard/control artifacts rather than directly to public source-ledger records. The dashboard therefore needs an export-level provenance layer that is separate from row-level public-source provenance.

## Ledger summary

- Export files checked: 7
- Missing exports: 0
- Machine-readable TSV: `results/boost/limen-dashboard-paper-forge/dashboard-export-provenance-ledger-2026-06-18.tsv`
- TSV SHA-256: `8a538a88daf9d7c52649e03b5cc68e28862c77f4dba5a447df18f4382b3c66fe`

| export | rows | dashboard surface | manuscript surface | claim ceiling |
|---|---:|---|---|---|
| `results/dashboard/source-family-coverage.tsv` | 15 | Source-family saturation map | Figure 1 / Figure 4 | source-surface maturity and uncertainty; not completeness |
| `results/dashboard/taxonomy-heatmap.tsv` | 15 | Taxonomy heatmap | Figure 2 / Table 2 | taxonomy support and residual pressure; not prevalence |
| `results/dashboard/evidence-funnel.tsv` | 11 | Evidence-tier funnel | Figure 3 / Figure 5 variant | evidence maturity and publication ceilings; not truth |
| `results/dashboard/jurisdiction-language-coverage.tsv` | 12 | Jurisdiction/language coverage | Figure 5 / S1 Panel C | coverage and language burden; no country ranking |
| `results/dashboard/legal-uncertainty-matrix.tsv` | 15 | Legal uncertainty matrix | Figure 6 | verification routing; not legal conclusion |
| `results/dashboard/security-threshold-ladder-panel.tsv` | 4 | Security/agentic threshold ladder | Figure 7 | bounded threshold route; not security prevalence |
| `results/dashboard/duplicate-review-graph.tsv` | 27 | Duplicate-review graph | Figure 8 | double-counting control; not proof of no duplicates |

## Dashboard implementation rule

- Export-level provenance may show file path, row count, checksum, dashboard surface, manuscript surface, and claim ceiling.
- Row-level source provenance may show access date or rights/terms only when an explicit source-ledger ID/path has been confirmed for that row.
- If `source_id` is absent, the UI should display the provenance blocker rather than silently inheriting source facts from a related artifact.

## Paper-readiness delta

This gives reviewers and dashboard users a visible separation between (a) reproducible dashboard exports and (b) public-source evidence records. That separation protects the manuscript from overclaiming provenance, legality, completeness, or source verification.
