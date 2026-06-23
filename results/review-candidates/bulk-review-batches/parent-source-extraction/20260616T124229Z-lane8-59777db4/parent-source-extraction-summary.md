# Parent source extraction summary

Batch: `20260616T124229Z-lane8-59777db4`
Input rows reviewed: 24
Output rows written: 24

## Verdict counts

- country_gap_no_parent_source: 5
- parent_source_wrapper: 2
- reject_noise: 6
- source_url_extracted: 11

## Method

Reviewed each `input.tsv` row exactly once against local cited lines plus nearby local PALLAS source-pack/source-refresh ledger entries where available. No web crawl, submission, publication, upload, email, registration, payment, or portal-form action was performed.

## Verification

- Result TSV header matches the required schema.
- Result row count equals input row count: 24.
- Queue ID set equality verified in the final validation step.
- Boundary preserved: processing-state/source-surface extraction only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
