# Case extraction summary: 20260616T225548Z-lane33-d2d6e91a

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane33-d2d6e91a/input.tsv`
Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane33-d2d6e91a/case-extraction-results.tsv`

Reviewed source_cluster_key rows: 16
Verdicts:
- closed_noncase_source_surface: 16
- case_candidate_for_hardening: 0
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Scope notes:
- Extraction only; no reviewed-core promotion and no ObscureAI addition.
- Inspected only input metadata and exact DOI/public locator metadata for the listed source surfaces.
- All rows were DOI/indexed scholarly, book/chapter, or registry-style source surfaces lacking a concrete AI edge-case event/action/vulnerability/finding/official case record with a bounded claim.

Verification:
- Result TSV header matches the required schema.
- Result row count equals input row count: 16.
- Result source_cluster_key set exactly matches input source_cluster_key set.
- No duplicate result source_cluster_key values.
