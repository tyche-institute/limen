# LIMEN Dashboard/Paper Parity Pack v0.2

Generated UTC: 2026-06-18T14:31:07Z
Lane: `limen-dashboard-paper-forge`

## What changed

This pass upgrades the earlier proxy-denominator pack with a source-level audit surface derived from `sources/sources.md` and selected bridge artifacts. It creates source-level Figure 1 rows and an evidence-tier Figure 2 branch while keeping the claim ceiling explicit: the audit supports source/readiness routing, not validated incidents, legality, compliance, deployment, safety, or prevalence.

## Outputs

- `corpus-audit-v0.1.tsv` — 102 audited source rows plus header; built from `sources.md` with explicit gap notes.
- `source-family-coverage-map-v0.2.tsv` — source-level Figure 1 coverage rows with access date, jurisdiction/language, inferred tier, centroid/geocode basis, uncertainty flags, and claim ceiling.
- `evidence-tier-funnel-v0.2.tsv` — Figure 2 audit funnel from source ledger rows through inferred tiers, bridge references, uncertainty flags, and zero audit-alone claim promotion.
- `review-priority-routing-v0.2.tsv` — P1/P2/P3 review queue labels for hardening; labels are not confidence grades.
- `claim-ceiling-summary-v0.2.tsv` — caption/limitation grammar for hostile-reviewer control.
- `dashboard-paper-parity-manifest-v0.2.json` — checksums and ingestion metadata.

## Key counts

| Measure | Count |
|---|---:|
| Audited source rows | 102 |
| Distinct source families | 60 |
| Distinct jurisdiction labels | 11 |
| Distinct language labels | 5 |
| Rows referenced by selected bridge artifacts | 11 |
| Rows with inferred uncertainty flags | 63 |
| Validated/publishable claims from this audit alone | 0 |

## Reviewer-safe interpretation

- `evidence_tier` and `uncertainty_flags` are inferred because `sources.md` does not yet expose those fields as first-class columns.
- Latitude/longitude are country or region centroids where possible; they are dashboard placement aids, not exact source locations.
- The requested file `results/boost/limen-boost-009/ai-washing-posture-table-v0.1.tsv` was absent; the likely live artifact is under `results/dashboard-paper/ai-washing-posture-table-v0.1.tsv`, but this pass did not silently substitute it.
- The audit is a paper-readiness surface for Figure 1/Figure 2 and methods limitations, not an adjudication result.

## Next smallest publishability move

Correct the boost-009 input pointer, rerun the audit with the dashboard-paper AI-washing posture artifact, and build the second-stage funnel: source-reviewed rows → hardened core cases → final adjudication rows → manuscript examples.
