# Parent source extraction summary — 20260617T073306Z-lane31-e17cb182

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073306Z-lane31-e17cb182/input.tsv`
Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073306Z-lane31-e17cb182/parent-source-extraction-results.tsv`
Rows reviewed: 24

Verdict counts:
- country_gap_no_parent_source: 5
- parent_source_wrapper: 18
- source_url_extracted: 1

Verification:
- Result TSV header matches the configured schema.
- One output row was written per input queue_id.
- Queue-id set and row count were verified against input.tsv.
- Review used local metadata/source files only.

Notes:
- Jurisdiction research-queue rows were treated as parent source wrappers because they list query/source-type packs rather than concrete source URLs.
- Atlas indicator/profile rows without a matching local top_sources URL were marked country_gap_no_parent_source.
- One local top_sources URL was extracted for Mozambique I03 regulatory sandbox.
