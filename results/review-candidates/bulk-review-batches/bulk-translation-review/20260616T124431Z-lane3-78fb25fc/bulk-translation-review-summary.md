# Bulk translation review summary

Batch: 20260616T124431Z-lane3-78fb25fc
Task: bulk-translation-review
Input rows reviewed: 16
Output rows written: 16

## Verdict counts
- candidate_for_parent_source_extraction: 4
- cross_project_duplicate: 2
- needs_original_language_source: 1
- source_surface_only_no_case: 5
- translation_source_reviewed: 4

## Boundary notes
- Review used local metadata and local source-file rows only; no broad web crawl or external submission was performed.
- Outputs are processing-state classifications only. No reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking is asserted.
- Rows marked candidate_for_parent_source_extraction still require bounded original-source extraction with the stated claim ceiling.
- Duplicate handling is source-level within this batch: BTR-00570 duplicates BTR-00562; BTR-00576 duplicates BTR-00571.

## Verification
- Result TSV header matches required schema.
- Result TSV row count matches input row count.
- Result queue_id set matches input queue_id set with no omissions, extras, or duplicates.
