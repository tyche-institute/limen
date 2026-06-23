# Case extraction summary: 20260616T225502Z-lane01-b0985abd

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane01-b0985abd/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane01-b0985abd/case-extraction-results.tsv`

Reviewed source_cluster_key rows: 16

Verdict counts:
- closed_duplicate_existing_core: 2
- closed_noncase_source_surface: 14

Extraction notes:
- Every input source_cluster_key was reviewed exactly once.
- Two rows were closed as exact duplicates of existing reviewed-core source surfaces: Colombian Constitutional Court T-323/24 and CVE-2023-37274.
- Fourteen rows were closed as noncase source surfaces: law/policy text, standards homepage, EPO service/API surface, or patent/IP records.
- No reviewed-core promotion, ObscureAI addition, incident-truth claim, legal finding, safety finding, compliance finding, deployment proof, prevalence claim, or ranking claim was made.

Verification:
- Result TSV header matches the requested schema.
- Result source_cluster_key set equals input source_cluster_key set.
- Result row count equals input row count.
