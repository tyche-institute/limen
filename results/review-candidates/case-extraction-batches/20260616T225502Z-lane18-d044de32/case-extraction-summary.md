# Case extraction summary — 20260616T225502Z-lane18-d044de32

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane18-d044de32/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane18-d044de32/case-extraction-results.tsv`

## Verification

- Input source_cluster_key rows: 16
- Output source_cluster_key rows: 16
- Duplicate output keys: 0
- Missing output keys: 0
- Extra output keys: 0
- Boundary honored: extraction only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, or ranking claim.

## Verdict counts

- closed_noncase_source_surface: 16
- case_candidate_for_hardening: 0
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

## Extraction rationale

All 16 clusters resolve to source surfaces such as AI registers/transparency pages, policy or law text, public-service chatbot/product pages, vendor/product pages, or reporting channels. The batch metadata did not expose a concrete AI edge-case event, action, vulnerability, finding, or official adverse record with a bounded claim. Each row is therefore closed as a noncase source surface while preserving the public locator for future lead tracing.
