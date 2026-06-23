# Parent source extraction summary

Batch: 20260616T123628Z-lane3-e08183e4
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 4
- parent_source_wrapper: 2
- country_gap_no_parent_source: 12
- source_surface_only_no_case: 6
- duplicate_existing_core: 0
- reject_noise: 0

Method boundary:
- Used local metadata, local source files, and local source-refresh/ledger pointers only.
- Extracted concrete public URLs only where explicit local rows or source-pack/ledger entries contained the URL.
- Did not make reviewed-core promotions, incident truth claims, legal/safety/compliance findings, prevalence claims, or rankings.

Verification:
- Result TSV header matches required schema.
- One output row per input queue_id.
- Queue_id set and row count verified against input.tsv.
