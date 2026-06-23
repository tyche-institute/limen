# Parent source extraction summary

Batch: 20260616T122829Z-lane2-ed6fda90

Reviewed every input row exactly once using local metadata/source files only. No web crawl or external portal interaction was performed.

## Counts

- input rows: 24
- output rows: 24
- source_url_extracted: 1
- parent_source_wrapper: 4
- country_gap_no_parent_source: 19
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Verification

- Result TSV header matches the required schema.
- Result TSV queue_id set exactly matches input.tsv.
- Result TSV row count exactly matches input.tsv.
- No duplicate queue_id values were written.

## Notes

Only one concrete original public URL was explicitly present in reviewed local context: BPSE-01089 (`https://www.levelpath.com/`) in `facts.json:16623-16643`. Rows that were country gap/profile/score placeholders with no local URL were marked `country_gap_no_parent_source`. Rows pointing to atlas/source-family/derivation wrappers requiring human selection among or within parent sources were marked `parent_source_wrapper`.
