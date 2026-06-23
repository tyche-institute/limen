# Parent source extraction summary

Batch: 20260617T073305Z-lane22-f3e2c917
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 3
- parent_source_wrapper: 5
- country_gap_no_parent_source: 16
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Notes:
- Used local input rows, nearby source context, and local PALLAS source-pack/source-refresh ledgers only.
- Research-queue rows were country/query placeholders and were retained as country_gap_no_parent_source.
- Wrapper verdicts indicate multiple same-country/indicator local source rows where a human must choose the parent surface.
- Extracted URLs are processing-state source surfaces only and do not assert incident truth, legal status, safety, compliance, prevalence, or ranking.
