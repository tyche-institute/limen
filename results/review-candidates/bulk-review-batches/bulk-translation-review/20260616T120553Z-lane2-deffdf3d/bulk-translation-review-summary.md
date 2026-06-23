# Bulk translation review summary

Batch: 20260616T120553Z-lane2-deffdf3d
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T120553Z-lane2-deffdf3d/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T120553Z-lane2-deffdf3d/bulk-translation-review-results.tsv

Reviewed 16 input rows exactly once. This batch is processing-state review only: no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking was made.

## Verdict counts
- candidate_for_parent_source_extraction: 5
- cross_project_duplicate: 2
- machine_translation_hold: 1
- needs_original_language_source: 2
- source_surface_only_no_case: 5
- translation_source_reviewed: 1

## Notes
- Most rows were held at source-surface/context level because the local evidence was metadata, digest text, auto-translation, blocked capture, or negative comparator context.
- Concrete source-extraction candidates were limited to rows where local metadata explicitly named a public AI system, register, or institution/source surface.
- Duplicates were marked for BTR-00038 (same PretorIA digest surface as BTR-00035) and BTR-00047 (same Datamask/NL register sample family as BTR-00045).

## Verification
- Input data rows: 16
- Output data rows: 16
- Output queue_id set matches input queue_id set: yes
- Duplicate output queue_id values: none
