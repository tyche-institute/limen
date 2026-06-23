# Parent source extraction summary

Batch: 20260617T064340Z-lane14-27627e93
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 1
- parent_source_wrapper: 1
- country_gap_no_parent_source: 22

Verification:
- Reviewed every non-empty input row exactly once.
- Result TSV queue_id set matches input.tsv queue_id set.
- Result TSV row count matches input.tsv row count: 24.
- No duplicate output queue_id values.
- Used local metadata/source files only; no web crawl or external submission.

Notable extraction:
- BPSE-02152: extracted explicit local top_sources I03 URL for Bahrain CBB FinTech & Innovation: https://www.cbb.gov.bh/fintech/

Boundary note:
This batch is processing-state parent-source extraction only. It does not promote reviewed-core records and makes no incident truth, legal, safety, compliance, prevalence, or ranking finding.
