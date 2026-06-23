# Case extraction summary: 20260616T225548Z-lane34-c91967b1

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane34-c91967b1/input.tsv`
Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane34-c91967b1/case-extraction-results.tsv`

Reviewed 16 source_cluster_key values exactly once. Inspection was limited to input metadata and exact DOI URLs listed in `source_url_or_locator` via DOI content negotiation; no broad crawling/searching or public actions were performed.

Verdict counts:

- closed_noncase_source_surface: 16
- case_candidate_for_hardening: 0
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Finding: all clusters are DOI/report/article/index/source-family surfaces. None exposes a concrete AI edge-case event, action, vulnerability, finding, or official case record with a bounded claim suitable for reviewed-core/ObscureAI hardening.

Boundary retained: no reviewed-core promotion, no ObscureAI addition, no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, ranking, or culpability claim.
