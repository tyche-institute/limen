# Parent source extraction summary

Batch: 20260617T073304Z-lane11-8e6ffddd
Input rows reviewed: 24
Output rows written: 24

## Verdict counts
- source_url_extracted: 1
- parent_source_wrapper: 16
- country_gap_no_parent_source: 7

## Method
- Used only local input metadata and referenced local source files.
- Inspected each referenced source line and nearby/source-context records.
- Extracted a URL only where a same-country, same-indicator top_sources URL was explicit in the local country profile.
- Marked research queue rows as parent_source_wrapper because they expose generated query bundles/source-type targets rather than concrete parent URLs.
- Marked country profile dimension rows without matching same-indicator URL as country_gap_no_parent_source.

## Verification
- Queue-id set matches input: True
- Row count matches input: True (24 rows)
- Duplicate output queue_id values: 0
- Output header exact: True
- Column-count errors: 0
- Errors: none
