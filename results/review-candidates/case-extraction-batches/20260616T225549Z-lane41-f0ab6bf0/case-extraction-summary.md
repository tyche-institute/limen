# Case extraction summary: 20260616T225549Z-lane41-f0ab6bf0

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane41-f0ab6bf0/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane41-f0ab6bf0/case-extraction-results.tsv`

## Outcome

- Input source clusters reviewed: 16
- Result rows written: 16
- Verdict counts: closed_noncase_source_surface=16
- Case candidates for hardening: 0
- Reviewed-core promotions: 0
- ObscureAI additions: 0

## Extraction notes

All 16 source_cluster_key values were DOI-backed scholarly, archive, or index/source-family surfaces. Exact URL resolution and available DOI metadata were inspected where possible, alongside the row metadata. None exposed a concrete bounded AI edge-case event/action/vulnerability/finding/official record suitable for reviewed-core/ObscureAI hardening. They were therefore closed as `closed_noncase_source_surface`.

Boundary maintained: no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, ranking, or guilt claim was made.

## Verification

- Header matches required schema: yes
- Result row count equals input row count: 16 == 16
- Result source_cluster_key set equals input set: yes
- Duplicate source_cluster_key values in results: 0
