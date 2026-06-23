# Bulk translation review summary

Batch: `20260616T120907Z-lane4-0d840664`
Input: `input.tsv`
Output: `bulk-translation-review-results.tsv`
Completed: `2026-06-16T12:11:50Z`

## Scope

Reviewed all 16 input rows exactly once using local metadata and local source-file rows only. This is processing-state review only: no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

## Verdict counts

- `cross_project_duplicate`: 6
- `source_surface_only_no_case`: 4
- `translation_source_reviewed`: 2
- `needs_original_language_source`: 2
- `machine_translation_hold`: 1
- `candidate_for_parent_source_extraction`: 1
- `reject_noise`: 0

## Notes

- Dutch Algorithm Register auto-translation rows were kept bounded as machine-translation holds or duplicates requiring Dutch-original review.
- Danish AI sandbox and Argentina TINA rows have concrete source-surface value but remain source-surface/context only.
- Greek and Belarus/Syria legal or regulatory surfaces were not promoted into legal or AI-evidence claims without original-language review and stronger source checks.
- eGovAI developer-doc metadata is a parent-source extraction candidate only as an API/supply-chain issue-spotting surface, not as proof of automated decision-making.

## Verification

Automated verification confirmed that result TSV has the required header, 16 data rows, no duplicate `queue_id`, and exactly the same `queue_id` set as `input.tsv`.
