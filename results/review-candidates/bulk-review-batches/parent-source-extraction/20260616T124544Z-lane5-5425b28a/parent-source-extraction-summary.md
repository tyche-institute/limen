# Parent source extraction summary

Batch: 20260616T124544Z-lane5-5425b28a
Completed UTC: 2026-06-16T12:51:17Z

## Scope

Reviewed every row in `input.tsv` exactly once using local metadata and local source/source-pack context only. No web crawl, forms, submission, upload, or promotion action was performed. This is processing-state review only.

## Counts

- input rows: 24
- output rows: 24
- country_gap_no_parent_source: 1
- parent_source_wrapper: 10
- reject_noise: 2
- source_surface_only_no_case: 7
- source_url_extracted: 4

## Notes

- Extracted URLs only where a concrete URL was explicitly present in local source-pack/ledger metadata.
- Rows bundling multiple local parent surfaces were marked `parent_source_wrapper`.
- Country/profile/seed/method/status rows without an extractable parent URL were not promoted beyond source-surface processing state.
