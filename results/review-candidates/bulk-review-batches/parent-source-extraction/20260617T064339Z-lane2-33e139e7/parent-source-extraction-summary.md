# Parent source extraction summary — 20260617T064339Z-lane2-33e139e7

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064339Z-lane2-33e139e7/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064339Z-lane2-33e139e7/parent-source-extraction-results.tsv

Processed rows: 24
Output rows: 24

Verdict counts:
- source_url_extracted: 1
- parent_source_wrapper: 1
- country_gap_no_parent_source: 22
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Method:
- Reviewed each input row exactly once against the referenced local file and nearby/local atlas metadata.
- Used only local metadata and local source context; no web crawling or external source invention.
- Extracted a URL only when a single concrete matching parent source URL was explicitly present in local atlas top_sources.
- Marked country/research queue placeholders with no explicit matching parent URL as country_gap_no_parent_source.
- Marked local wrappers with multiple matching parent URLs as parent_source_wrapper.

Boundary:
Processing-state source extraction only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, ranking, or publication claim.
