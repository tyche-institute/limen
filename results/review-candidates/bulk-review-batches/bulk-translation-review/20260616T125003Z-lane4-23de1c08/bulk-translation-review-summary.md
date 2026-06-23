# Bulk translation review summary — 20260616T125003Z-lane4-23de1c08

Completed: 2026-06-16T12:55:56Z
Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T125003Z-lane4-23de1c08/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T125003Z-lane4-23de1c08/bulk-translation-review-results.tsv`

## Verification

- Input data rows: 16
- Output data rows: 16
- Queue ID set: exact match
- Duplicate output queue IDs: 0
- Extra output queue IDs: 0
- Missing output queue IDs: 0
- Field sanitation: no tabs/newlines inside output fields

## Verdict counts

- candidate_for_parent_source_extraction: 2
- cross_project_duplicate: 5
- machine_translation_hold: 1
- needs_original_language_source: 1
- source_surface_only_no_case: 4
- translation_source_reviewed: 3

## Review boundary

This batch is processing-state review only. Rows were evaluated against local metadata and local source rows. No row is promoted to reviewed core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

## Notes

- Several rows are duplicate source surfaces already present in this batch or prior translation-review batches (ANPD, Garante, Dutch Algorithm Register, Nezamat).
- Timeout-only Persian Nezamat rows remain original-language-source holds.
- Dutch Algorithm Register landing-page rows remain machine-translation holds because local evidence explicitly warns that English descriptions are automatically translated.
