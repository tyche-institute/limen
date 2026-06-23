# Case extraction summary: 20260617T065736Z-lane02-90a09dcb

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T065736Z-lane02-90a09dcb/input.tsv`
Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T065736Z-lane02-90a09dcb/case-extraction-results.tsv`

## Result

- Input source_cluster_key rows reviewed: 1
- Output result rows written: 1
- case_candidate_for_hardening: 0
- closed_noncase_source_surface: 1

## Reviewed cluster

1. `https://open.canada.ca/data/en/dataset/fcbc0200-79ba-4fa4-94a6-00e32facea6b`
   - Verdict: `closed_noncase_source_surface`
   - Reason: Open Canada hosts the Government of Canada AI Register MVP dataset. The inspected package/API/CSV expose registry rows for Parliamentary Machine Translation and Echo - Transcription/Translation, but this is an official transparency/register inventory surface rather than a concrete edge-case event, finding, vulnerability, harm record, or authority action.
   - Boundary retained: no reviewed-core promotion, no ObscureAI addition, and no legality, safety, compliance, deployment-scope, prevalence, or guilt claim.

## Verification

A post-write script verified that the output TSV has the same source_cluster_key set and row count as `input.tsv`: 1 key in, 1 key out, 0 missing, 0 extra, 0 duplicates.
