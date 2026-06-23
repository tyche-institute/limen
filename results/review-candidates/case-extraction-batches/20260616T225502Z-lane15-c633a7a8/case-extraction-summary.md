# Case extraction summary — 20260616T225502Z-lane15-c633a7a8

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane15-c633a7a8/input.tsv`

Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane15-c633a7a8/case-extraction-results.tsv`

Reviewed source clusters: 16

Verdict counts:

- closed_noncase_source_surface: 16
- case_candidate_for_hardening: 0
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Extraction boundary: no reviewed-core promotion, no ObscureAI addition, no incident-truth/legal/safety/compliance/deployment/prevalence/ranking claim was made. Each row is treated as a source-surface disposition only.

Rationale: every input cluster was a register/search/observatory/policy/sandbox/product/use-case/homepage/scholarly-index/legal-document/vendor-story surface without a concrete bounded AI edge-case event, action, vulnerability, official finding, or case-level record in the provided metadata and exact URL checks.

Verification: result TSV was checked for exact source_cluster_key set equality and row-count equality against input.tsv.
