# Translation parent-source extraction summary

Batch: `20260617T065734Z-lane1-cfb98514`
Task: translation-parent-source-extraction
Completed UTC: 2026-06-17T06:58:20Z

## Scope and method

Reviewed every row in `input.tsv` exactly once using only local batch input, local source metadata, and nearby local source lines. No broad web crawl and no external submission/publishing actions were performed.

## Results

- Input rows reviewed: 4
- Output rows written: 4
- `source_url_extracted`: 4
- `parent_source_wrapper`: 0
- `country_gap_no_parent_source`: 0
- `source_surface_only_no_case`: 0
- `duplicate_existing_core`: 0
- `reject_noise`: 0

## Evidence notes

- BTPS-00128: official Ecuador SPDP PDF URL was explicit in `input.tsv:2` and `PALLAS_SECOND_PASS_SPRINT_8_SOURCE_REFRESH.csv:197`.
- BTPS-00129: official BNetzA AI sandbox page URL was explicit in `input.tsv:3` and `PALLAS_SECOND_PASS_SPRINT_14_SOURCE_REFRESH.csv:7`.
- BTPS-00130: ETDA Thai guidance URL was explicit as local JSONL `seed_url` at `southeast-asian-language-history.jsonl:152`.
- BTPS-00131: Dutch government algorithm register URL was explicit as local JSONL `seed_url` at `dutch-belgian-language-history.jsonl:53`.

## Verification

Passed automated verification: result TSV header matches the configured schema; input rows = 4; output rows = 4; queue_id set matches exactly; duplicate queue_id values = 0; verdict values are within the allowed set.
