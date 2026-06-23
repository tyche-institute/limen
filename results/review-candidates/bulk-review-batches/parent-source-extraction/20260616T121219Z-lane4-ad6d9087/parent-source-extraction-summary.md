# Parent source extraction summary

Batch: 20260616T121219Z-lane4-ad6d9087
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 1
- parent_source_wrapper: 16
- country_gap_no_parent_source: 6
- source_surface_only_no_case: 1
- duplicate_existing_core: 0
- reject_noise: 0

Verification:
- Reviewed every input queue_id exactly once.
- Used local metadata/source files only; no web crawl or portal interaction.
- Result TSV queue_id set and row count match input.tsv.
- Boundary observed: processing-state source recovery only; no reviewed-core promotion or substantive legal/safety/compliance finding.

Notes:
- One explicit public parent URL was recovered: Greece Law 4961/2022 official Gazette PDF from the local sprint-14 source refresh ledger.
- Research-queue rows were kept as parent_source_wrapper because they list multiple topical targets without isolating a parent URL.
- Atlas/country/profile/score rows without a concrete URL at the reviewed row were marked country_gap_no_parent_source.
