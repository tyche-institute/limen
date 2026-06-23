# Parent source extraction summary

Batch: 20260617T064340Z-lane18-e00cd5f2
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane18-e00cd5f2/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane18-e00cd5f2/parent-source-extraction-results.tsv

Reviewed rows: 24
Output rows: 24

Verdict counts:
- source_url_extracted: 3
- parent_source_wrapper: 2
- country_gap_no_parent_source: 19

Notes:
- Local metadata/source files only; no web crawl or external submission was used.
- Extracted URLs were only used where local source-refresh/source-pack rows explicitly named a concrete public URL.
- Query-pack, country-profile, matrix, and score/gap rows without direct URL evidence were left as country_gap_no_parent_source.
- Wrapper rows with multiple possible parent sources or only target evidence categories were marked parent_source_wrapper.
- Boundary preserved: processing-state source extraction only; no reviewed-core promotion or factual/legal/safety/compliance finding.
