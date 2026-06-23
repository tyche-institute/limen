# Bulk translation review summary

Batch: 20260616T124841Z-lane3-ed445f72
Task: bulk-translation-review
Input rows reviewed: 16
Output rows written: 16

## Verdict counts
- candidate_for_parent_source_extraction: 6
- cross_project_duplicate: 3
- needs_original_language_source: 1
- source_surface_only_no_case: 4
- translation_source_reviewed: 2

## Boundary notes
- Review used local metadata and local source-file rows only; no broad web crawl or external submission was performed.
- Outputs are processing-state classifications only. No reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking is asserted.
- Rows marked candidate_for_parent_source_extraction require bounded source extraction with the stated claim ceiling.
- Duplicate handling references local prior-batch/current metadata: BTR-00610 duplicates ETDA guidance already reviewed as BTR-00562/BTR-00570; BTR-00614 duplicates Malaysia AIGE already reviewed as BTR-00571/BTR-00576; BTR-00623 duplicates INDOTEL already reviewed as BTR-00563.

## Verification
- Result TSV header matches required schema.
- Result TSV row count matches input row count.
- Result queue_id set matches input queue_id set with no omissions, extras, or duplicates.
