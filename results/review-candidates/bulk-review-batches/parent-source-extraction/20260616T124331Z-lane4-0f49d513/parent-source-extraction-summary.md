# Parent source extraction summary

Batch: 20260616T124331Z-lane4-0f49d513

Reviewed every input row exactly once using local metadata, local source files, and local PALLAS source-pack/source-refresh pointers only. No web crawling or external form interaction was performed.

## Results

- Input rows: 24
- Output rows: 24
- source_url_extracted: 2
- parent_source_wrapper: 9
- country_gap_no_parent_source: 4
- source_surface_only_no_case: 9
- duplicate_existing_core: 0
- reject_noise: 0

## Verification

The result TSV was generated in input order with one row per input queue_id. A post-write verification script checks row count, header, duplicate queue IDs, and exact queue_id set equality.

## Boundary

This is processing-state parent-source extraction only. It does not promote reviewed core records, add ObscureAI entries, or make incident truth, legal, safety, compliance, prevalence, or ranking claims.
