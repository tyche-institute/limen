# Parent source extraction summary

Batch: 20260617T064340Z-lane23-5afd4449
Completed at UTC: 2026-06-17T06:46:42Z
Input rows reviewed exactly once: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 1
- parent_source_wrapper: 1
- country_gap_no_parent_source: 22
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Method notes:
- Used local metadata and local source files only.
- Inspected cited source rows and nearby local context.
- Extracted a concrete URL only where a local source-pack/ledger row explicitly provided it.
- Did not crawl the web or make any promotion/truth/legal/safety/compliance finding.

Verification:
- Result TSV header matches the required schema.
- Result TSV contains one row per input queue_id, with no omissions, extras, or duplicate queue_id values.
