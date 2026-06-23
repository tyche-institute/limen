# Bulk translation review summary

Batch: 20260616T121358Z-lane2-edecfa53
Completed at UTC: 2026-06-16T12:15:39Z
Input rows reviewed: 16
Result rows written: 16

## Verdict counts
- candidate_for_parent_source_extraction: 1
- machine_translation_hold: 1
- needs_original_language_source: 5
- source_surface_only_no_case: 2
- translation_source_reviewed: 7

## Boundary applied
- Processing-state review only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
- Local metadata and local source files only; rows with failed local capture were held for original-source acquisition.
- Source-surface/context outcomes were kept distinct from case-level promotion.

## Verification
- Result TSV header matches required schema.
- One result row was written per input queue_id.
- Queue_id set equality and row count equality were verified by script before manifest completion.
