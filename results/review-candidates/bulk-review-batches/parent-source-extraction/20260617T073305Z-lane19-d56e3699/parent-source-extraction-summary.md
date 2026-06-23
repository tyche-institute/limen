# Parent source extraction summary

Batch: 20260617T073305Z-lane19-d56e3699
Task: parent-source-extraction
Input rows reviewed: 24
Output rows written: 24

## Verdict counts

- country_gap_no_parent_source: 24

## Method

Reviewed each input row once against the configured local source path and source_line, using nearby local context only. No web crawling, form submission, upload, publication, registration, payment, or external portal interaction was performed.

## Result

All rows in this batch are country/query search-pack rows or Atlas country-profile indicator placeholders. The inspected local rows expose country/query or indicator label/score metadata, but no explicit concrete public parent source URL. Therefore all rows were marked country_gap_no_parent_source.

## Verification

- Result TSV header matches the configured schema.
- Result row count equals input row count: 24.
- Result queue_id set equals input queue_id set.
- Duplicate output queue_id count: 0.
