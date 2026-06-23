# Case extraction summary: 20260616T225549Z-lane38-7b1c2cc1

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane38-7b1c2cc1/input.tsv`
Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane38-7b1c2cc1/case-extraction-results.tsv`

## Result

- Input source_cluster_key rows reviewed: 16
- Output rows written: 16
- Unique source_cluster_key values: 16
- Verdict counts:
  - closed_noncase_source_surface: 16

## Extraction note

All rows in this batch are DOI/scholarly-index source surfaces from `doi.org`. The input metadata characterizes them as scholarly/index wrappers or local aggregate/proxy rows that do not expose a standalone concrete AI edge-case event/action/vulnerability/finding/official record. Under the extraction boundary, these are closed as noncase source surfaces and are not promoted to reviewed-core or ObscureAI.

## Verification

- Result TSV header matches the required schema.
- Result TSV row count equals input row count: 16 == 16.
- Result TSV source_cluster_key set exactly equals input source_cluster_key set.
- No duplicate output source_cluster_key values.

## Boundary kept

No broad web crawl, publishing, submission, portal login, public action, reviewed-core promotion, ObscureAI addition, incident truth claim, legal/safety/compliance finding, deployment proof, prevalence claim, or ranking claim was made.
