# Parent source extraction summary

Batch: 20260617T073304Z-lane14-5d6f9107
Completed at UTC: 2026-06-17T07:34:22Z

## Scope and method

- Reviewed every row in input.tsv exactly once using local metadata/source files only.
- Inspected the cited local source rows and nearby context in OBSERVABILITY_RESEARCH_QUEUE.csv, PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv, and pallas_atlas_countries.json.
- Did not perform broad web crawling or external submission actions.

## Results

- Input rows: 24
- Output rows: 24
- source_url_extracted: 0
- parent_source_wrapper: 0
- country_gap_no_parent_source: 24
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

All rows in this batch were country-level query/profile/score placeholders without an explicit extractable parent source URL in the inspected local metadata/source context.

## Verification

The result TSV was verified for exact header, row count, unique queue_id values, allowed verdict values, and exact queue_id set equality with input.tsv.
