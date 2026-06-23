# Bulk translation review summary: 20260616T124143Z-lane1-aaf40b7c

Reviewed every row in `input.tsv` exactly once using local metadata and local source files only.

## Counts

- input rows: 16
- output rows: 16
- candidate_for_parent_source_extraction: 3
- cross_project_duplicate: 2
- needs_original_language_source: 2
- source_surface_only_no_case: 5
- translation_source_reviewed: 4

## Boundary applied

This batch is processing-state review only. No row was promoted to reviewed core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking. Translation-sensitive rows were capped at source-surface/context unless the local source text explicitly exposed bounded edge-case vocabulary.

## Notes

- BTR-00533 duplicates the Italian Garante source reviewed at BTR-00532.
- BTR-00544 duplicates the ANPD sandbox source reviewed at BTR-00531.
- BTR-00530 and BTR-00538 require original/primary language source resolution before substantive use.
- BTR-00540 is the only row with explicit edge-case vocabulary in local source text; it remains a bounded guidance-text extraction candidate only.
