# Bulk translation review summary

Batch: 20260616T125642Z-lane1-cc233af5
Input rows reviewed: 15
Output rows written: 15

## Verdict counts
- translation_source_reviewed: 3
- needs_original_language_source: 1
- cross_project_duplicate: 2
- machine_translation_hold: 0
- candidate_for_parent_source_extraction: 2
- source_surface_only_no_case: 4
- reject_noise: 3

## Boundary notes
- Review used local batch input, local metadata rows, and local source-file records only.
- No web crawl, portal interaction, upload, publication, email, payment, or registration was performed.
- All decisions are processing-state/source-surface decisions only. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking is made.
- Duplicate handling is limited to duplicate DOI/source surfaces inside this batch.

## Verification
- Result TSV header matches the required schema.
- Result TSV contains one row per input queue_id.
- Queue_id set and row count were verified against input.tsv after writing.
