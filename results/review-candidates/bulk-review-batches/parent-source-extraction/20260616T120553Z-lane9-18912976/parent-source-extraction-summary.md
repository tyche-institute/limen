# Parent source extraction summary

Batch: 20260616T120553Z-lane9-18912976
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T120553Z-lane9-18912976/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T120553Z-lane9-18912976/parent-source-extraction-results.tsv

Reviewed input rows exactly once: 24
Output rows written: 24

## Verdict counts
- source_url_extracted: 3
- source_surface_only_no_case: 1
- parent_source_wrapper: 4
- country_gap_no_parent_source: 16
- duplicate_existing_core: 0
- reject_noise: 0

## Notes
- Used local metadata and local source/source-refresh files only.
- No web crawl, promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking was performed.
- Placeholder research-queue/country-profile rows were left as country_gap_no_parent_source unless a concrete local source pointer resolved to a bounded surface.
- Wrapper rows that exposed multiple possible parent sources were marked parent_source_wrapper rather than forcing a single URL.
