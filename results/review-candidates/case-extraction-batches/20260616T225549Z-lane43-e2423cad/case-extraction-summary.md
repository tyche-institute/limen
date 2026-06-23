# Case extraction summary: 20260616T225549Z-lane43-e2423cad

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane43-e2423cad/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane43-e2423cad/case-extraction-results.tsv`

## Outcome

- Input source_cluster_key rows reviewed: 16
- Result rows written: 16
- Verdict counts: {'closed_noncase_source_surface': 16}
- Reviewed-core promotions: 0
- ObscureAI additions: 0

## Extraction decision

All 16 clusters in this batch are DOI/scholarly-index/proxy source surfaces according to the supplied metadata. None exposes a concrete bounded AI edge-case event, vulnerability, official finding, action, or case-level record in the provided source surface metadata. They are therefore closed as `closed_noncase_source_surface` for source-family accounting only.

## Verification

- Exact required TSV header: True
- Input/result row counts match: True
- Input/result source_cluster_key sets match: True
- Duplicate result keys: 0

Boundary respected: no reviewed-core promotion, no ObscureAI addition, no incident-truth/legal/safety/compliance/deployment/prevalence/guilt/ranking claim.
