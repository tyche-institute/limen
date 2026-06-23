# Translation parent-source extraction summary

Batch: `20260616T130035Z-lane8-f5455c93`
Task: `translation-parent-source-extraction`
Completed UTC: `2026-06-16T13:02:45Z`

## Scope

Reviewed every non-empty row in `input.tsv` exactly once using local metadata and local source files only. No web crawling, portal interaction, upload, publication, registration, payment, email, or reviewed-core promotion was performed.

## Results

- Input rows reviewed: 3
- Output rows written: 3
- `source_url_extracted`: 2
- `source_surface_only_no_case`: 1
- `parent_source_wrapper`: 0
- `country_gap_no_parent_source`: 0
- `duplicate_existing_core`: 0
- `reject_noise`: 0

## Row notes

- `BTPS-00113`: explicit Malaysia government AIGE URL found in local JSONL fields `seed_url`/`source_url`/`url` at line 41; marked `source_surface_only_no_case` because local context is portal/guidance surface only.
- `BTPS-00114`: explicit NAIH-hosted WP251 guidance URL found in local source-pack row 290; extracted as parent guidance candidate only, not a Hungarian register/case.
- `BTPS-00115`: explicit DOI URL found in local Crossref JSONL record at line 183; extracted as technical parent-source context only.

## Verification

Final verification was run after writing outputs: result TSV has the exact same non-empty `queue_id` set and row count as `input.tsv`, with no duplicate output `queue_id` values.
