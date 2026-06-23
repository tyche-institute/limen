# Case extraction summary: 20260618T140247Z-lane01-2d69daaf

Status: complete

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260618T140247Z-lane01-2d69daaf/input.tsv
Output TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260618T140247Z-lane01-2d69daaf/case-extraction-results.tsv

Verification:
- Input rows reviewed: 1
- Output rows written: 1
- Source_cluster_key set match: yes
- Duplicate output source_cluster_key values: no

Verdict counts:
- closed_noncase_source_surface: 1

Notes:
- Reviewed the single source_cluster_key exactly once.
- Exact public URL was checked only as an allowed source locator; CloudFront/AWS WAF returned HTTP 202 challenge to curl, so the extraction relies on the provided EUR-Lex source metadata and the stable OJ law-text locator rather than broad crawling.
- No reviewed-core promotion, ObscureAI addition, public action, incident truth claim, legal finding, safety finding, compliance finding, deployment proof, prevalence claim, or ranking claim was made.
