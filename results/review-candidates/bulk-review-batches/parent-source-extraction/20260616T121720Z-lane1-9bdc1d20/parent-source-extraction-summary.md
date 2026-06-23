# Parent source extraction summary

Batch: 20260616T121720Z-lane1-9bdc1d20

Reviewed 24 input rows exactly once using local metadata, source-line context, and local source-pack/ledger files only. No web crawling or external submission actions were performed.

## Verdict counts

- country_gap_no_parent_source: 20
- parent_source_wrapper: 4
- source_url_extracted: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

Most rows are country gap/profile/score or generic research-query placeholders with no explicit parent URL in the local row context. Four rows point to wrapper/proxy surfaces where local source packs expose multiple plausible parent sources, so they were left for human selection rather than inventing a URL.

## Verification

Result TSV was generated with one row per input queue_id and no extra queue_ids; final machine verification is recorded in manifest.json.
