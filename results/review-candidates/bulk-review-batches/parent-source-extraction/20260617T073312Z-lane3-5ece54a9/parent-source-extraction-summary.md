# Parent source extraction summary

Batch: 20260617T073312Z-lane3-5ece54a9

Reviewed input rows: 24
Result rows written: 24

Verdict counts:
- country_gap_no_parent_source: 10
- parent_source_wrapper: 14

Method:
- Used only local input metadata and local source files.
- Inspected exact source rows and nearby context for atlas indicator/profile entries and jurisdiction source-pack entries.
- Did not web crawl or infer URLs from source names.

Outcome:
- Jurisdiction source-pack rows were marked `parent_source_wrapper` because each local row is a generated jurisdiction/query bundle with multiple possible target source types and no selected parent URL.
- Atlas indicator/profile rows were marked `country_gap_no_parent_source` where the local score/profile row and nearby country metadata did not expose a matching parent URL for the requested indicator.

Verification:
- Result TSV header matches the required schema.
- Result TSV contains one row per input queue_id with no duplicates, omissions, or extras.
