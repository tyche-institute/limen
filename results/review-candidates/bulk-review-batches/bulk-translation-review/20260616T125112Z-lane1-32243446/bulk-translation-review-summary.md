# Bulk translation review summary: 20260616T125112Z-lane1-32243446

Reviewed every row in `input.tsv` exactly once using local metadata and local source files only.

## Counts

- input rows: 16
- output rows: 16
- candidate_for_parent_source_extraction: 1
- cross_project_duplicate: 4
- machine_translation_hold: 1
- needs_original_language_source: 1
- source_surface_only_no_case: 5
- translation_source_reviewed: 4

## Boundary applied

This batch is processing-state review only. No row was promoted to reviewed core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking. Translation-sensitive rows were capped at source-surface/context unless local source metadata supported only a bounded extraction candidate.

## Notes

- BTR-00644 and BTR-00652 are the Dutch Algorithm Register surface; English descriptions are machine-translated, so entry-level use requires Dutch originals.
- BTR-00643, BTR-00646, and BTR-00655 duplicate source surfaces already reviewed in local bulk-translation batches.
- BTR-00642 is only a local case-study reference label and needs the original Spanish Civio source before substantive use.
- BTR-00650 and BTR-00651 are explicit non-AI-specific/negative-context surfaces and should not be promoted as AI sandbox or algorithm-register evidence.
