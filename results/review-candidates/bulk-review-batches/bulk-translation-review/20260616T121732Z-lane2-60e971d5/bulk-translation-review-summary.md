# Bulk translation review summary

Batch: 20260616T121732Z-lane2-60e971d5
Completed UTC: 2026-06-16T12:19:45Z
Input rows reviewed: 16
Output rows written: 16

## Verdict counts
- candidate_for_parent_source_extraction: 3
- cross_project_duplicate: 4
- machine_translation_hold: 3
- needs_original_language_source: 1
- source_surface_only_no_case: 3
- translation_source_reviewed: 2

## Boundary applied
This batch is processing-state review only. The review used local metadata and local source-file surfaces only. Machine-translated rows were kept at source-surface, duplicate-routing, or original-language-review ceilings; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking was made.

## Verification
- Result TSV header matches the required schema.
- One output row was written for each input queue_id.
- Queue_id set and row count were verified against input.tsv.
