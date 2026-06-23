# Case extraction summary: 20260616T225549Z-lane35-3bd96b7b

- Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane35-3bd96b7b/input.tsv`
- Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane35-3bd96b7b/case-extraction-results.tsv`
- Input source_cluster_key rows reviewed: 16
- Output rows written: 16
- Verdict counts:
  - closed_noncase_source_surface: 16

## Extraction decision

All 16 input clusters are DOI/index or scholarly/wrapper source surfaces according to the supplied metadata. No row exposed a concrete public event/action/vulnerability/finding/official record with a bounded AI edge-case claim suitable for reviewed-core or ObscureAI hardening. Each cluster was therefore closed as `closed_noncase_source_surface`.

## Boundary applied

No reviewed-core promotion, ObscureAI addition, incident-truth claim, legal finding, safety finding, compliance finding, deployment proof, prevalence claim, guilt claim, or ranking claim was made.

## Verification

The output TSV was generated with one row per input `source_cluster_key`; final key-set and row-count verification is recorded in `manifest.json`.
