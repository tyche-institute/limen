# Translation parent-source extraction summary

Batch: 20260617T093723Z-lane1-6bdf1983
Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260617T093723Z-lane1-6bdf1983/input.tsv`
Result TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260617T093723Z-lane1-6bdf1983/translation-parent-source-extraction-results.tsv`

## Scope

Reviewed every input row exactly once using local metadata and local source files only. No broad web crawl, submission, publication, upload, email, registration, payment, portal form use, reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking claim.

## Verdict counts

- source_url_extracted: 4
- parent_source_wrapper: 0
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Verification

- Input data rows: 4
- Output data rows: 4
- Queue ID set equality: PASS
- Duplicate output queue_id values: none
- Header matches configured 9-column schema: PASS
- Field sanitation: tabs/newlines removed from field values

## Notes

All four rows had a concrete original public URL explicitly present in local metadata/source context, so each was marked `source_url_extracted` with a bounded source-surface claim ceiling.
