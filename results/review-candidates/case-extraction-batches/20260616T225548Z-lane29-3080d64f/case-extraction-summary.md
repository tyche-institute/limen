# Case extraction summary: 20260616T225548Z-lane29-3080d64f

Batch lane: lane29
Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane29-3080d64f/input.tsv`
Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225548Z-lane29-3080d64f/case-extraction-results.tsv`

## Result counts

- Input source_cluster_key rows reviewed: 16
- Output rows written: 16
- case_candidate_for_hardening: 0
- closed_noncase_source_surface: 16
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

## Extraction decision

All 16 clusters resolve to DOI-backed scholarly, conference/session-index, survey, policy-analysis, or book-chapter surfaces. DOI metadata was checked for each exact source URL. None exposed a concrete AI edge-case event/action/vulnerability/finding/official record with a bounded public claim suitable for reviewed-core or ObscureAI hardening.

## Boundary notes

No reviewed-core promotion occurred. No ObscureAI addition occurred. No incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence claim, or ranking claim was made. The rows are closed as source-surface accounting only unless later work isolates a direct case-level public source.

## Verification

The output TSV was verified to contain exactly the same source_cluster_key set and source row count as the input TSV: 16 input rows and 16 output rows, with no omissions, extras, or duplicate source_cluster_key values.
