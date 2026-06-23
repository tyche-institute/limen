# Case extraction summary: 20260616T225549Z-lane42-050c8a7c

Completed: 2026-06-16T22:56:16Z

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane42-050c8a7c/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane42-050c8a7c/case-extraction-results.tsv`

## Verification

- Input rows: 16
- Result rows: 16
- Header matches required schema: yes
- Source cluster key set matches input exactly: yes
- Duplicate source_cluster_key values in results: none
- Omissions/extras: none

## Verdict counts

- closed_noncase_source_surface: 16

## Extraction notes

All 16 clusters are DOI/scholarly/index wrapper surfaces according to the batch metadata. None exposes, in the row itself, a standalone concrete event/action/vulnerability/finding/official record suitable for reviewed-core or ObscureAI hardening. Each is therefore closed as a noncase source surface with a disposition-only claim ceiling.

Boundary observed: no reviewed-core promotion, no ObscureAI addition, no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, or ranking claim.
