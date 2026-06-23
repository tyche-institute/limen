# LIMEN dashboard ingest readiness audit
Generated: 2026-06-18T04:58:05Z
Lane: `limen-dashboard-paper-forge`
Sprint layer: hostile-reviewer pass / dashboard-paper parity.
## Scope
Bounded local audit of the seven dashboard TSV exports that feed the required dashboard/article surfaces. No new crawling, upload, deposit, publication, or claim-ceiling relaxation was performed. The pre-submission tool was also run after the audit and returned 8/8 PASS.
## Ingest table
| Dashboard export | Rows | Columns | SHA-256 | Manuscript/dashboard surface | Reviewer-safe reading |
|---|---:|---:|---|---|---|
| `results/dashboard/source-family-coverage.tsv` | 15 | 23 | `b1d3a0e616db24d4…` | Source-family saturation map / Figure 1-4 | source-family saturation and uncertainty; not completeness |
| `results/dashboard/taxonomy-heatmap.tsv` | 15 | 21 | `c0c9db0ed86acdf4…` | Taxonomy heatmap / Figure 2 + Table 2 | taxonomy support and residual pressure; not prevalence |
| `results/dashboard/evidence-funnel.tsv` | 11 | 8 | `866475937cae0d41…` | Evidence-tier funnel / Figure 3 and publication-safe lineage surface | evidence maturity and proof ceilings; not truth or legal finding |
| `results/dashboard/jurisdiction-language-coverage.tsv` | 12 | 10 | `8bb99a9b5e4d35bb…` | Jurisdiction/language map / Figure 5 sidecar | visibility burden; not country ranking or readiness |
| `results/dashboard/legal-uncertainty-matrix.tsv` | 15 | 13 | `e7e9859a36b3b874…` | Legal uncertainty matrix / Figure 6 | verification routing; not legal conclusion |
| `results/dashboard/security-threshold-ladder-panel.tsv` | 4 | 8 | `c989a5509d9ea633…` | Security/agentic ladder / Figure 7 | bounded route logic; not security prevalence |
| `results/dashboard/duplicate-review-graph.tsv` | 27 | 12 | `bb36d1fd9ddc2833…` | Duplicate-review graph / Figure 8 | double-counting control; not proof no duplicates remain |

## Conceptual schema readiness
| Export | Identifier | Count/denominator scope | Claim ceiling / safe reading | Dashboard hook | Provenance pointer | Uncertainty/caution semantics |
|---|---|---|---|---|---|---|
| `source-family-coverage.tsv` | yes | yes | yes | yes | yes | yes |
| `taxonomy-heatmap.tsv` | yes | yes | yes | yes | gap | yes |
| `evidence-funnel.tsv` | yes | yes | yes | gap | gap | gap |
| `jurisdiction-language-coverage.tsv` | yes | yes | yes | gap | yes | yes |
| `legal-uncertainty-matrix.tsv` | yes | yes | yes | yes | yes | yes |
| `security-threshold-ladder-panel.tsv` | yes | yes | yes | yes | gap | yes |
| `duplicate-review-graph.tsv` | yes | gap | gap | gap | yes | yes |

## Interpretation and limitations
- The exports are dashboard-ingestable as controlled surfaces, but not yet uniform as a public dashboard API. Every file has a stable identifier or surface key; several files still need explicit row-level fields for denominator scope, provenance, or reviewer-safe interpretation rather than relying on companion manuscript/SI text.
- Provenance is partly direct and partly indirect. `source-family-coverage.tsv`, `duplicate-review-graph.tsv`, and jurisdiction/language rows carry explicit provenance/source pointers; `taxonomy-heatmap.tsv`, `evidence-funnel.tsv`, and `security-threshold-ladder-panel.tsv` rely more on linked queues, source-family files, or SI/manuscript binding. This is acceptable for the current paper package but should be made more uniform before a public interactive dashboard release.
- The strongest next dashboard hardening move is not new collection: add a uniform exported sidecar with `source_id`, `source_url_or_path`, `accessed_at`, `rights_terms_note`, `translation_status`, and `claim_ceiling` for every figure/table row that currently has only indirect pointers.
- No country ranking, prevalence estimate, completeness claim, legal/compliance conclusion, official incident status, certification claim, or safety assurance follows from this audit.

## Observatory hook
Dashboard builder can consume the TSV companion as a route table: each export maps to its figure/dashboard view, row count, checksum, and permitted interpretation. Use it to show source-family saturation and uncertainty bands before any raw-count view.

## Paper-readiness delta
This closes a small dashboard-engineering gap between manuscript parity and future interactive release: the figure/table exports now have an explicit ingest-readiness ledger with checksums, row counts, schema-readiness flags, and hostile-reviewer interpretation boundaries.
