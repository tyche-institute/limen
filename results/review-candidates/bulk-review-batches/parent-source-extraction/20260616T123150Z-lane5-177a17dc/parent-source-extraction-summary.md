# Parent source extraction summary

Batch: 20260616T123150Z-lane5-177a17dc
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 4
- parent_source_wrapper: 8
- country_gap_no_parent_source: 8
- source_surface_only_no_case: 4
- duplicate_existing_core: 0
- reject_noise: 0

Method boundary:
- Used local metadata and local source files only.
- Extracted concrete public URLs only where an explicit local row/source-pack pointer contained the URL.
- Did not make reviewed-core promotions, incident truth claims, legal/safety/compliance findings, prevalence claims, or rankings.

Verification:
- Result TSV header matches required schema.
- One output row per input queue_id.
- Queue_id set and row count verified against input.tsv.
