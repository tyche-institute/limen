# Parent source extraction summary — 20260617T064340Z-lane13-1787ca74

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane13-1787ca74/input.tsv`

Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane13-1787ca74/parent-source-extraction-results.tsv`

Rows reviewed: 24

Verdict counts:

- source_url_extracted: 1
- parent_source_wrapper: 3
- country_gap_no_parent_source: 20
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Notes:

- Used local metadata and local source files only.
- Query-pack country rows were treated as country/query gap placeholders unless a concrete local URL was present.
- Atlas profile score placeholders without matching local `top_sources` were treated as country/profile gaps.
- Rows with multiple candidate parent URLs in local `top_sources` were marked `parent_source_wrapper` rather than forcing a choice.

Verification:

- Result TSV header matches the configured schema exactly.
- Result TSV row count equals input row count: 24.
- Queue ID set matches input exactly; no omissions, extras, or duplicate queue IDs.
- Allowed verdict vocabulary check passed.
