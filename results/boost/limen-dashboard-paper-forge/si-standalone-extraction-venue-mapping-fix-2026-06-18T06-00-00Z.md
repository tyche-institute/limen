# SI standalone TSV extraction + venue-adaptation SI mapping correction

**Date:** 2026-06-18T06:00:00Z
**Lane:** `limen-dashboard-paper-forge`
**Cycle type:** editorial / submission-packaging

## What was done

### 1. Extracted four standalone TSV files

Prior status (blocker #3 from 2026-06-17T22:00 cycle):
> "S7, S8, S9, S11 are currently referenced as slices/branches of parent
> tables, not yet exported as standalone TSV files."

| SI table | Standalone file | Rows | Parent source |
|---|---|---|---|
| S7 | `results/dashboard/supplementary-table-s7-trust-boundary-breadth.tsv` | 3 | `security-publication-buckets.tsv` (LIMEN-000009, -000012, -000016) |
| S8 | `results/dashboard/supplementary-table-s8-supply-chain-frontier.tsv` | 5 | `security-publication-buckets.tsv` (supply-chain-adjacent rows) |
| S9 | `results/dashboard/supplementary-table-s9-peer-review-gap.tsv` | 1 | `security-authority-balance-panel.tsv` (SEC-AUTH-PANEL-001) |
| S11 | `results/dashboard/supplementary-table-s11-research-integrity.tsv` | 5 | `procedural-contamination-source-depth-panel.tsv` (SCPANEL-008-003..007) |

All four files carry the original parent header and exact row content.
No rows were added, modified, or removed from parent tables.

### 2. Corrected venue-adaptation SI mapping

**Before:** `venue-adaptation-scientific-data-2026-06-17.md` had only 3 S-tables
mapped (S1 = reviewed-core, S2 = source-family, S3 = taxonomy-heatmap) plus
Figure S1 and two Notes. This was stale and did not match the preprint's
S1–S14 references or the SI document's definitions.

**After:** Full 14-table + Figure S1 + Note 1 mapping, corrected to match
`draft/supplementary-information.md` and `draft/preprint.md`. Each S-table
now names its canonical source artifact path and row count.

### 3. Updated supplementary-information.md source paths

S7, S8, S9, S11 entries now reference the new standalone TSV paths instead
of "Derived from ..." prose.

## Verification

| Check | Result |
|---|---|
| S7 row count matches SI spec (3) | ✓ |
| S8 row count matches SI spec (≤5) | ✓ (5) |
| S9 row count matches SI spec (1) | ✓ |
| S11 row count matches SI spec (≤5) | ✓ (5) |
| All row IDs match parent source | ✓ |
| Headers match parent source | ✓ |
| Venue-adaptation S1 matches SI doc (authoritative-document-depth-facet.tsv) | ✓ |
| Venue-adaptation S2 matches SI doc (security-threshold-ladder-panel.tsv) | ✓ |
| Venue-adaptation S3 matches SI doc (threshold-change matrix) | ✓ |
| Venue-adaptation S4–S14 all mapped | ✓ |

## Denominator discipline

- No denominator was changed.
- No new data was collected.
- No claim ceiling was relaxed.
- All extractions are editorial-only row subsets of existing verified parents.

## Remaining blockers (updated)

1. sf08 court-depth, sf09 buyer-side, sf11 peer-reviewed gaps remain
   (documented, not fixable from this lane).
2. Route C remains local-bundle provenance only.
3. Panel C (jurisdiction × tier) for S1 still needs extraction from
   reviewed-core case data.
4. S4 source artifact (`publication-cell-geometry-v0.1.tsv`) needs
   verification that it exists at the stated path.

## Paper-readiness delta

**Before:** 4 of 14 SI tables were only described as slices/branches;
venue-adaptation SI mapping covered 3 of 14 tables with stale definitions.

**After:** All 14 SI tables have either a direct source path or a standalone
extracted TSV; venue-adaptation SI mapping covers all 14 tables with
corrected definitions matching the preprint and SI document. A hostile
reviewer or submission system can now locate every S-table's data file.

## Next smallest publishability move

Verify S4 source artifact path exists; extract Panel C for S1 from
reviewed-core case data; then the SI package is fully materialized and
the manuscript passes the "every S-reference has a verifiable file" gate.
