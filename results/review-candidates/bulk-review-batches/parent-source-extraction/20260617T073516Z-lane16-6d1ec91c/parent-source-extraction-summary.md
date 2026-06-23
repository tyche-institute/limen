# Parent source extraction summary

Batch: `20260617T073516Z-lane16-6d1ec91c`
Completed at UTC: `2026-06-17T07:36:26Z`

## Scope

Reviewed every row in `input.tsv` exactly once using only local metadata and local source-file context. No broad web crawl or external portal action was performed.

## Results

- Input rows reviewed: 13
- Output rows written: 13
- `source_url_extracted`: 0
- `parent_source_wrapper`: 10
- `country_gap_no_parent_source`: 3
- Other verdicts: 0

## Notes

- Research queue rows were generic country/query wrappers listing acceptable source classes but no concrete parent URL; these were marked `parent_source_wrapper`.
- Country profile rows for Republic of the Congo I03, Mauritania I03, and Palestine I05 were score/label/gap placeholders without an exposed matching parent URL in nearby local profile context; these were marked `country_gap_no_parent_source`.
- No URL was inferred from source names or country/query text.

## Verification

The result TSV was checked for exact header, allowed verdicts, duplicate queue IDs, row count, and queue_id set equality against `input.tsv`.
