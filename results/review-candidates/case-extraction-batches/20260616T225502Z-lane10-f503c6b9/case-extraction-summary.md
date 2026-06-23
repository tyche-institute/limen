# Case extraction summary — 20260616T225502Z-lane10-f503c6b9

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane10-f503c6b9/input.tsv`
Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane10-f503c6b9/case-extraction-results.tsv`

Reviewed source_cluster_key count: 16
Result row count: 16

Verdict counts:
- closed_noncase_source_surface: 16
- case_candidate_for_hardening: 0
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Extraction decision:
All 16 clusters were closed as noncase source surfaces. The inspected surfaces are policy/guidance/legal/specification/register/product/service-description or local score/accounting rows. None contains, at this extraction stage, a concrete AI edge-case event/action/vulnerability/finding/official record with a bounded case claim suitable for reviewed-core or ObscureAI hardening.

Boundary observed:
No reviewed-core promotion, no ObscureAI addition, no incident-truth claim, no legal/safety/compliance finding, no deployment proof, no prevalence/ranking claim, and no public action were taken.

Verification:
A script compared input and result source_cluster_key sets and row counts after writing; see manifest for completion status.
