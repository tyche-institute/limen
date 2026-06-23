# Parent source extraction summary

Batch: 20260617T073304Z-lane10-6cbab326
Completed at UTC: 2026-06-17T07:35:19Z

## Verification

- Input rows reviewed: 24
- Output rows written: 24
- Queue ID set parity: verified
- Duplicate output queue IDs: none
- Boundary: processing-state parent-source extraction only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claims.

## Verdict counts

- source_url_extracted: 3
- parent_source_wrapper: 17
- country_gap_no_parent_source: 4
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

- Used local metadata and local source files only.
- Extracted concrete URLs only where a matching indicator-specific URL was explicitly present in local country-profile `top_sources`.
- Research queue rows were marked `parent_source_wrapper` because their local rows are generated query bundles requiring a human/source-selection step.
- Country-profile dimension labels without a matching local indicator URL were marked `country_gap_no_parent_source`.
