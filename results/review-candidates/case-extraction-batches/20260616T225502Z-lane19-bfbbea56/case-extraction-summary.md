# Case extraction summary: 20260616T225502Z-lane19-bfbbea56

Completed at UTC: 2026-06-16T22:55:28Z

## Scope
- Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane19-bfbbea56/input.tsv`
- Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane19-bfbbea56/case-extraction-results.tsv`
- Rows reviewed: 16
- Unique source_cluster_key values reviewed: 16

## Verdict counts
- closed_noncase_source_surface: 16

## Extraction result
All input source clusters were closed as noncase source surfaces for this extraction pass. The rows are registers, transparency inventories/records, policy/guidance surfaces, search/discovery surfaces, or product/news/source-family surfaces. They may be useful provenance, but the provided metadata does not isolate a concrete AI edge-case event, vulnerability, finding, authority action, official adverse record, or harm claim suitable for reviewed-core/ObscureAI hardening.

## Boundary retained
No reviewed-core promotion, ObscureAI addition, incident truth claim, legal finding, safety finding, compliance finding, deployment proof, prevalence claim, or ranking claim was made.

## Verification
A post-write script verified that the output TSV has the exact same source_cluster_key set as the input TSV, with no omissions, extras, or duplicate output keys.
