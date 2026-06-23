# Parent source extraction summary

Batch: 20260617T073306Z-lane29-1a00528b
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073306Z-lane29-1a00528b/input.tsv
Output: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073306Z-lane29-1a00528b/parent-source-extraction-results.tsv

Reviewed rows: 24
Output rows: 24

Verdict counts:
- source_url_extracted: 1
- parent_source_wrapper: 18
- country_gap_no_parent_source: 5

Method:
- Used only local input metadata and local source files referenced by source_path/source_line.
- Inspected exact source rows and nearby JSON top_sources context for atlas indicator/profile rows.
- Did not infer URLs from source names and did not perform broad web crawling.
- Source-pack rows were treated as wrappers because they enumerate multiple query/source-type targets rather than one public URL.

Extracted URL:
- BPSE-03468: https://www.rbf.gov.fj/fintech-regulatory-sandbox-guideline/ from pallas_atlas_countries.json lines 34584 and 34689-34692.

Boundary:
Processing-state review only. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim made.
