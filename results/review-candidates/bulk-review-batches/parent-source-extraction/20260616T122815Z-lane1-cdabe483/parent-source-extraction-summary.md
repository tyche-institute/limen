# Parent source extraction summary

Batch: 20260616T122815Z-lane1-cdabe483
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122815Z-lane1-cdabe483/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122815Z-lane1-cdabe483/parent-source-extraction-results.tsv

Reviewed rows: 24
Output rows: 24

Verdict counts:
- source_url_extracted: 0
- parent_source_wrapper: 3
- country_gap_no_parent_source: 21
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Notes:
- No broad web crawl was used.
- No rows were promoted to reviewed core or treated as incident/legal/safety/compliance findings.
- Local matrix/research-queue rows were treated as processing-state gaps where no concrete URL was present.
- Derived Estonia/Finland I05 rows were marked parent_source_wrapper because local context/source-pack pointers expose multiple possible parent sources requiring human scope selection.
