# Case extraction summary: 20260616T225548Z-lane27-d99e5c2a

Completed at UTC: 2026-06-16T22:56:39Z

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane27-d99e5c2a/input.tsv
Results TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane27-d99e5c2a/case-extraction-results.tsv

Reviewed source_cluster_key count: 16
Output row count: 16

Verdict counts:
- closed_noncase_source_surface: 16

Extraction decision:
All 16 clusters are API bibliographic/index source surfaces (Crossref or OpenAlex query URLs). The input metadata already marked them as scholarly/index/source-family surfaces, and exact locator inspection where reachable showed bibliographic result lists, zero-result index responses, or malformed index-query responses rather than a direct concrete AI edge-case event/action/vulnerability/finding/official record.

Boundary honored:
- No reviewed-core promotion.
- No ObscureAI addition.
- No incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, ranking, or guilt claim.
- No broad web crawling or invented URLs; only provided locators and input metadata were used.

Before any later reviewed-core consideration, each closed surface would need an original direct public source or precise local locator containing a concrete bounded case record.
