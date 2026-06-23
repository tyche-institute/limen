# Parent source extraction summary

Batch: 20260616T123004Z-lane11-50596658
Task: bounded parent-source-extraction using local metadata and local source context only.

## Review method

- Reviewed each input.tsv row once.
- Inspected the cited local line and nearby context.
- For PALLAS score-delta/profile rows, checked local source_refresh/source-pack rows only when the cited row named a lane/source surface needing URL recovery.
- Extracted a public URL only when it was explicitly present in local JSON/CSV/Markdown context or a local source_refresh/source-pack pointer.
- Did not use broad web crawl or external forms.

## Verdict counts

- source_url_extracted: 8
- parent_source_wrapper: 6
- country_gap_no_parent_source: 5
- source_surface_only_no_case: 5
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

Extracted URLs are processing-state source pointers only. They do not promote any row into reviewed core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking. Rows marked parent_source_wrapper require human choice among multiple local source-pack/source-family candidates or later record-level selection. Rows marked country_gap_no_parent_source are country/profile/gap placeholders with no single extractable parent source at the cited row.

## Verification

The output TSV was written with the required header and one result row for every input queue_id. A machine check was run after writing to verify row count and queue_id set equality.
