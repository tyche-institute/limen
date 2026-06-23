# Supplementary Information binding verification

Date (UTC): 2026-06-17T22:00:00Z
Lane: `limen-dashboard-paper-forge`
Artifact: `draft/supplementary-information.md` (v0.1, 500 lines)

## Binding verification

All 11 primary source artifacts confirmed present and non-empty:

| SI ref | Source path | Lines (incl. header) | Status |
|---|---|---|---|
| S1 | `results/dashboard/authoritative-document-depth-facet.tsv` | 10 | OK |
| S2 | `results/dashboard/security-threshold-ladder-panel.tsv` | 5 | OK |
| S3 | `results/dashboard/security-authority-balance-panel.tsv` | 7 | OK |
| S4 | `results/dashboard/provenance-confusion-publication-cells.tsv` | 7 | OK |
| S5 | `results/dashboard/security-publication-buckets.tsv` | 13 | OK |
| S6 | `results/dashboard/security-crosswalk-coverage-panel.tsv` | 7 | OK |
| S7 | Derived from S5 (trust-boundary slice: LIMEN-000009, 000012, 000016) | 3 rows | OK |
| S8 | Derived from S5 (supply-chain mechanism slice) | ≤5 rows | OK |
| S9 | `results/dashboard/security-authority-balance-panel.tsv` row 1 (gap) | 1 row | OK |
| S10 | `results/dashboard/procedural-contamination-source-depth-panel.tsv` | 8 | OK |
| S11 | S10 research_integrity branch (SCPANEL-008-003..007) | ≤5 rows | OK |
| S12 | S10 reformatted as sidecar control | 7 rows | OK |
| S13 | `results/dashboard/public-sector-disclosure-comparison.tsv` | 7 | OK |
| S14 | `results/dashboard/public-sector-proof-ceilings.tsv` | 7 | OK |
| Fig S1 | `results/dashboard-paper/figure-reviewed-core-tier-by-theme.svg` | 103 lines | OK |
| Note 1 | `results/dashboard-paper/caption-control-register-v0.1.tsv` | 20 | OK |

## Denominator discipline check

- No SI table claims corpus completeness or prevalence.
- No SI table merges GAIA/PALLAS/LIMEN denominators.
- Security tables (S2–S9) are explicitly marked as not part of the Route A denominator.
- Procedural-contamination tables (S10–S12) carry separate denominator from governed-core.
- Public-sector tables (S13–S14) carry separate denominator from governed-core.
- All captions include "does not support" language.

## Venue-adaptation note reconciliation

The venue-adaptation note (`results/dashboard-paper/venue-adaptation-scientific-data-2026-06-17.md`)
mapped S1–S3 differently from the preprint's own prose. The SI binding follows
the preprint prose as the authoritative reference:

| SI ref | Preprint prose binding | Venue-note mapping | Resolution |
|---|---|---|---|
| S1 | Authoritative-document routing (§4.1) | Reviewed-core 248-case | Preprint wins; S1 = authoritative-document-depth |
| S2 | Route B threshold contract (§4.3) | Source-family coverage | Preprint wins; S2 = security threshold ladder |
| S3 | Threshold-change matrix (§4.3) | Taxonomy heatmap | Preprint wins; S3 = authority-balance panel |

The venue-adaptation note's SI mapping should be updated in a future editorial
pass to match the preprint's actual S-number references.

## Remaining work

1. Extract S7, S8, S9, S11 as standalone TSV files from their parent tables
   (currently referenced as slices/branches, not yet exported separately).
2. Update the venue-adaptation note's SI mapping to match preprint prose.
3. Produce Panel C (jurisdiction × tier) TSV for S1 from reviewed-core case data.
4. Convert all SI tables to submission-ready format (per venue template).
