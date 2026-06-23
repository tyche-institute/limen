# Parent source extraction summary

Batch: 20260616T123212Z-lane8-390ce540
Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T123212Z-lane8-390ce540/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T123212Z-lane8-390ce540/parent-source-extraction-results.tsv`

Reviewed every input row exactly once using local metadata and local source/source-pack context only. No web crawl, portal form, submission, upload, email, registration, payment, reviewed-core promotion, incident finding, legal finding, safety finding, compliance finding, prevalence claim, or ranking was made.

## Verification

- Input data rows: 24
- Output data rows: 24
- Queue ID set: matches input exactly
- Duplicate output queue IDs: none
- Output header: exact required header

## Verdict counts

- source_url_extracted: 7
- parent_source_wrapper: 4
- country_gap_no_parent_source: 6
- source_surface_only_no_case: 5
- duplicate_existing_core: 0
- reject_noise: 2

## Notes

Rows marked `source_url_extracted` expose only source-surface provenance under the stated claim ceiling. Rows marked `parent_source_wrapper` require human selection among multiple locally ledgered parent sources before direct review. Rows marked `country_gap_no_parent_source` or `source_surface_only_no_case` should not be promoted without separate source discovery.
