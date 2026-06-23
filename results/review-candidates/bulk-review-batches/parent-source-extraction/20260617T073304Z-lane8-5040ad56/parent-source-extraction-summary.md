# Parent-source extraction summary

- Batch: `20260617T073304Z-lane8-5040ad56`
- Input rows reviewed: 24
- Output rows written: 24
- Method: local-only review of input rows, nearby JSON/CSV context, and `top_sources` metadata; no web crawl or external submission.
- Boundary: processing-state source-surface triage only; no reviewed-core promotion or substantive incident/legal/safety/compliance/prevalence/ranking claim.

## Verdict counts
- source_url_extracted: 5
- parent_source_wrapper: 7
- country_gap_no_parent_source: 12
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Verification
- Verified result TSV row count and queue_id set match input.tsv exactly (24 rows); no duplicate queue_id values; header and verdict vocabulary valid.

## Notes
- `source_url_extracted` was used only where exactly one requested-indicator URL was explicitly present in local `top_sources`.
- `parent_source_wrapper` was used where multiple explicit local requested-indicator parent URLs were present and require a human choice.
- `country_gap_no_parent_source` was used for country/profile/score or research-queue placeholders without an extractable requested parent URL.
