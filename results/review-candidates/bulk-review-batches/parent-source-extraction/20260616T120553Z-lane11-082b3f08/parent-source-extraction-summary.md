# Parent source extraction summary

Batch: `20260616T120553Z-lane11-082b3f08`

Input rows reviewed exactly once: 24
Output rows written: 24

Verdict counts:
- `country_gap_no_parent_source`: 11
- `parent_source_wrapper`: 5
- `source_surface_only_no_case`: 1
- `source_url_extracted`: 7

Verification:
- Result TSV header matches required schema.
- Queue-id set and row count were verified against input.tsv.
- Used local metadata/source-pack/ledger pointers only; no web crawl or external submission actions.
- Claim ceilings are limited to processing-state parent-source extraction.
