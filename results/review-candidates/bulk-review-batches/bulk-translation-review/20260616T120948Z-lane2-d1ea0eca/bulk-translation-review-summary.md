# Bulk translation review summary

Batch: 20260616T120948Z-lane2-d1ea0eca
Input rows reviewed: 16
Output rows written: 16
Verification: result TSV queue_id set and row count match input.tsv; no duplicate queue_id values.

## Verdict counts
- translation_source_reviewed: 4
- needs_original_language_source: 3
- cross_project_duplicate: 3
- machine_translation_hold: 0
- candidate_for_parent_source_extraction: 1
- source_surface_only_no_case: 5
- reject_noise: 0

## Boundary notes
- This batch is processing-state review only.
- No row was promoted to reviewed core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
- Duplicate Guatemala package copies were routed to the canonical reviewed source-surface row.
- Rows with failed fetches or auto-translation keep original-language/source-specific confirmation requirements.
