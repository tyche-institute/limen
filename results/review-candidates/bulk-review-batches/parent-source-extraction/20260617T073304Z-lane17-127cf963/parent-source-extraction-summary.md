# Parent source extraction summary

Batch: 20260617T073304Z-lane17-127cf963
Input rows reviewed: 24
Output rows written: 24

## Verdict counts
- country_gap_no_parent_source: 24

## Method
- Used local metadata and local source files only.
- Inspected configured source paths and nearby context for each row.
- Did not invent URLs from country/source names; no broad web crawl or external action was used.

## Notes
- All rows were country-level query packs or atlas profile/indicator placeholders without an explicitly tied parent source URL in local row/context.
- Atlas rows with nearby top_sources were checked for matching indicator IDs; no matching parent source URL was present for the target indicator rows.
