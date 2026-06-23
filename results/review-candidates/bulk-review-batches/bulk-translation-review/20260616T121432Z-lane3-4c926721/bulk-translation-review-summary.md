# Bulk translation review summary

Batch: 20260616T121432Z-lane3-4c926721
Completed at UTC: 2026-06-16T12:16:33Z
Input rows reviewed: 16
Result rows written: 16

Scope: processing-state translation/source-surface review only. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking was made.

Verdict counts:
- translation_source_reviewed: 4
- needs_original_language_source: 3
- cross_project_duplicate: 1
- machine_translation_hold: 1
- candidate_for_parent_source_extraction: 2
- source_surface_only_no_case: 5

Review notes:
- Strongest bounded candidates for later parent-source extraction: BTR-00163 (Chinese deep-synthesis provisions) and BTR-00171 (Malaysia AISHAH public-sector chatbot).
- BTR-00176 is held because local evidence is explicitly English auto-translation from Dutch with unresolved reuse terms.
- BTR-00169, BTR-00170, and BTR-00175 need accessible original/source text before substantive review.
- BTR-00174 duplicates the BTR-00162 AgID Italian consultation source surface across local Pallas packs.

Verification:
- Output header matches required schema.
- Output queue_id set and row count were checked against input.tsv before manifest update.
