# Parent source extraction summary

Batch: `20260616T121626Z-lane4-0b41a3ac`
Input rows reviewed: 24
Output rows written: 24

## Verdict counts

- source_url_extracted: 3
- parent_source_wrapper: 5
- country_gap_no_parent_source: 16
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

- Used only local source rows, nearby context, and local source-refresh/source-pack pointers.
- Extracted URLs only where a local source-refresh row explicitly carried the URL.
- Country research-queue and country profile/score rows without a direct parent URL were marked `country_gap_no_parent_source`.
- Wrapper/manuscript/source-pack rows requiring a human to choose among multiple parent sources were marked `parent_source_wrapper`.
- No reviewed-core promotion, factual incident/legal/safety finding, publication, upload, portal action, or web crawl was performed.
