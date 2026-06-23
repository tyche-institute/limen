# Parent source extraction summary

Batch: 20260617T073305Z-lane23-d8e18748
Completed at UTC: 2026-06-17T07:35:39Z
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073305Z-lane23-d8e18748/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073305Z-lane23-d8e18748/parent-source-extraction-results.tsv

## Scope

Reviewed every input row exactly once using local metadata and local source-file context only. No web crawl or external portal interaction was used. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim is made.

## Verdict counts

- country_gap_no_parent_source: 24
- source_url_extracted: 0
- parent_source_wrapper: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

All 24 rows were generated research-queue query bundles or derived atlas indicator/profile rows. The cited local rows did not expose an explicit, same-row/same-indicator parent public source URL suitable for extraction. Rows were therefore bounded to `country_gap_no_parent_source`.

## Verification

- Input data rows: 24
- Output data rows: 24
- Queue ID set: matched exactly during post-write verification
- Duplicate output queue IDs: none
