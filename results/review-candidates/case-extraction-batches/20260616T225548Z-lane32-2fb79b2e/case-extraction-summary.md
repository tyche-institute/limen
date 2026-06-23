# Case extraction summary: 20260616T225548Z-lane32-2fb79b2e

Status: complete
Updated UTC: 2026-06-16T22:56:21Z

Input rows reviewed: 16
Result rows written: 16
Unique source_cluster_key values: 16

Verdict counts:
- closed_noncase_source_surface: 16
- case_candidate_for_hardening: 0
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Extraction notes:
- Reviewed every source_cluster_key in input.tsv exactly once.
- The batch consists of DOI/scholarly/index/proxy source-surface rows whose metadata does not expose a concrete AI edge-case event, action, vulnerability, finding, or official record.
- No reviewed-core promotion, ObscureAI addition, incident-truth claim, legal/safety/compliance finding, deployment proof, prevalence claim, or ranking claim was made.

Verification:
- Result TSV header matches the required schema.
- Result row count equals input row count: 16.
- Result source_cluster_key set equals input source_cluster_key set.
- No duplicate result source_cluster_key values.

Outputs:
- /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane32-2fb79b2e/case-extraction-results.tsv
- /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane32-2fb79b2e/case-extraction-summary.md
