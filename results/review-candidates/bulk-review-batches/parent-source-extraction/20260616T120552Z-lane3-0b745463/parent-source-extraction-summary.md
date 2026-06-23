# Parent source extraction summary — 20260616T120552Z-lane3-0b745463

Processed every input row exactly once using local metadata/source-pack evidence only. No web crawl or external actions were used.

- Input rows: 24
- Output rows: 24
- Unique queue_id values: 24
- Verdict counts:
  - source_url_extracted: 10
  - parent_source_wrapper: 9
  - country_gap_no_parent_source: 4
  - source_surface_only_no_case: 1
  - duplicate_existing_core: 0
  - reject_noise: 0

Verification: output TSV queue_id set and row count match input.tsv. Extracted URLs are limited to URLs explicitly present in local source refresh/source pack/ledger/context files. Wrapper rows were not promoted to source claims.
