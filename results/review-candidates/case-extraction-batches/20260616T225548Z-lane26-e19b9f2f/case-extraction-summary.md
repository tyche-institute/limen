# Case extraction summary: 20260616T225548Z-lane26-e19b9f2f

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane26-e19b9f2f/input.tsv`
Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane26-e19b9f2f/case-extraction-results.tsv`

Reviewed source_cluster_key rows: 16

Verdict counts:
- case_candidate_for_hardening: 1
- closed_noncase_source_surface: 15
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Case candidate retained for hardening:
- https://arxiv.org/abs/2603.26983 — bounded as a scholarly preprint claim about provenance-tracking constraints for AI-generated content transparency workflows. It is not promoted to reviewed-core or ObscureAI.

Closure rationale:
Most rows are OpenAlex/DOI scholarly index surfaces, book/chapter metadata, policy/regulatory-sandbox literature, or a blockchain trust architecture preprint. They do not by themselves expose a concrete AI edge-case event/action/vulnerability/finding with a bounded claim suitable for hardening.

Boundary observed: no reviewed-core promotion, no ObscureAI addition, no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, or ranking claim.
