# Bulk translation review summary

Batch: 20260616T124028Z-lane2-b718d607
Task: bulk-translation-review
Input rows reviewed: 16
Output rows written: 16

## Verdict counts
- candidate_for_parent_source_extraction: 2
- cross_project_duplicate: 3
- machine_translation_hold: 1
- needs_original_language_source: 1
- source_surface_only_no_case: 4
- translation_source_reviewed: 5

## Boundary applied
All rows were treated as processing-state review only. No row was promoted to reviewed-core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking. Review used only local TSV metadata and local source-file lines. Machine-translated or non-English surfaces were capped at source-surface/context unless original-language review would be required for any substantive claim.

## Notes
- Duplicate same-source surfaces were marked for deduplication: BTR-00485 duplicates BTR-00484, BTR-00486 duplicates BTR-00482, and BTR-00488 duplicates BTR-00481.
- AU Continental AI Strategy surfaces were kept as parent-source extraction candidates, not case-level evidence.
- Dutch Algorithm Register was held at register-surface level because local metadata warns English descriptions are automatic translations.
