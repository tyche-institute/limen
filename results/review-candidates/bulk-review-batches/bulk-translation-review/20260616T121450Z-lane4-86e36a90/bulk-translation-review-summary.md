# Bulk translation review summary — 20260616T121450Z-lane4-86e36a90

Status: complete
Completed at UTC: 2026-06-16T12:16:52Z
Input rows reviewed: 16
Output rows written: 16

## Verdict counts
- candidate_for_parent_source_extraction: 2
- cross_project_duplicate: 4
- machine_translation_hold: 1
- needs_original_language_source: 3
- source_surface_only_no_case: 6

## Scope notes
- Reviewed each input queue_id exactly once using only the input TSV plus referenced local source rows.
- Kept this as processing-state review only: no reviewed-core promotion, legal finding, safety finding, compliance finding, prevalence claim, or ranking.
- Dutch auto-translated register rows were held for original-language review or marked duplicate where the same locator recurred in-batch.
- Non-English official pages were generally retained at source-surface/context ceiling unless they were plausible parent sources for later original-language extraction.

## Verification
- Result TSV header matches the required nine columns.
- Result TSV has one data row per input row.
- Queue_id set equality was checked after writing; see manifest verification fields.
