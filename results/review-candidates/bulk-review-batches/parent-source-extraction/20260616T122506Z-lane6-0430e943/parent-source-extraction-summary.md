# Parent-source extraction summary

Batch: 20260616T122506Z-lane6-0430e943
Input rows reviewed: 24
Output rows written: 24
Verification: PASS - output queue_id set and row count match input.tsv; no duplicate queue_id values.

## Verdict counts

- country_gap_no_parent_source: 17
- duplicate_existing_core: 0
- parent_source_wrapper: 5
- reject_noise: 0
- source_surface_only_no_case: 0
- source_url_extracted: 2

## Notes

- Used only local metadata/source files and nearby context.
- Extracted concrete URLs only where explicit in local atlas/source context.
- Country gap/profile/search-target placeholders with no extractable URL were marked country_gap_no_parent_source.
- Source-pack or unresolved source-family wrappers requiring a human parent-source choice were marked parent_source_wrapper.
- No web crawl, publication, upload, portal submission, or promotion action was performed.
