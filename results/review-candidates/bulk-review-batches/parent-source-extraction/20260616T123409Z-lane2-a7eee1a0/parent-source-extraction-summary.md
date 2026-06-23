# Parent source extraction summary

Batch: 20260616T123409Z-lane2-a7eee1a0

Reviewed every input row exactly once using local metadata/source files only. No web crawl or external portal interaction was performed.

## Counts

- input rows: 24
- output rows: 24
- source_url_extracted: 7
- parent_source_wrapper: 6
- country_gap_no_parent_source: 7
- source_surface_only_no_case: 1
- duplicate_existing_core: 0
- reject_noise: 3

## Verification

- Result TSV header matches the required schema.
- Result TSV queue_id set exactly matches input.tsv.
- Result TSV row count exactly matches input.tsv.
- No duplicate queue_id values were written.

## Notes

Concrete original public URLs were extracted only where local source context or an explicit local source-refresh/seed/guide ledger provided the URL. Country gap/profile/score placeholders without an extractable URL were marked `country_gap_no_parent_source`. Rows pointing to aggregate/source-family/project wrappers requiring human selection among parent sources were marked `parent_source_wrapper`. Internal submission/gate/status notes with no reviewable parent surface were marked `reject_noise`.
