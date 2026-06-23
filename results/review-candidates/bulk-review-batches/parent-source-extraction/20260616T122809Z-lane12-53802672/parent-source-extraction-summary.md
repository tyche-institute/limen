# Parent source extraction summary

Batch: `20260616T122809Z-lane12-53802672`
Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122809Z-lane12-53802672/input.tsv`
Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122809Z-lane12-53802672/parent-source-extraction-results.tsv`
Completed UTC: `2026-06-16T12:32:38Z`

## Scope

Bounded processing-state parent-source extraction. Used local metadata, local source files, and local source-pack/ledger pointers only. No broad web crawl, promotion, publication, upload, or portal action was performed.

## Results

- Input rows reviewed: 24
- Output rows written: 24
- `source_url_extracted`: 5
- `parent_source_wrapper`: 2
- `country_gap_no_parent_source`: 17
- Other verdicts: 0

## Extracted URLs

- BPSE-01033: Luxembourg I03 sandbox provisions in bill 8476 PDF.
- BPSE-01042: Slovakia AI Watch public-sector AI strategy page.
- BPSE-01045: Philippines BSP Circular No. 1153 regulatory sandbox PDF.
- BPSE-01053: Estonia/Kratid mapping AI and algorithms page.
- BPSE-01056: Åland AI supervision draft bill PDF, sandbox chapter.

## Wrapper rows requiring human source choice

- BPSE-01046: Botswana Bank of Botswana sandbox cluster has multiple candidate parent URLs.
- BPSE-01050: Jersey I10 evidence summarizes multiple laws/service-manual sources.

## Verification

Verified before completion:

- Output header exactly matches required schema.
- Output row count equals input row count: 24.
- Output queue_id set equals input queue_id set.
- No missing, extra, or duplicate queue_id values.
- Every output row has exactly 9 TSV columns.

Claim boundary preserved: processing-state/source-surface review only; no reviewed-core promotion, incident truth, legal/safety/compliance finding, prevalence claim, or ranking claim.
