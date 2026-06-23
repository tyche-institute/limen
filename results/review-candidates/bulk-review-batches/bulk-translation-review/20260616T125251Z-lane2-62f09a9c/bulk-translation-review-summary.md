# Bulk translation review summary

Batch: 20260616T125251Z-lane2-62f09a9c
Task: bulk-translation-review
Input rows reviewed: 16
Output: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T125251Z-lane2-62f09a9c/bulk-translation-review-results.tsv

## Verdict counts
- translation_source_reviewed: 5
- needs_original_language_source: 1
- cross_project_duplicate: 2
- machine_translation_hold: 0
- candidate_for_parent_source_extraction: 4
- source_surface_only_no_case: 4
- reject_noise: 0

## Boundary notes
- All rows were treated as processing-state/source-surface review only.
- No row was promoted to reviewed core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
- Duplicate handling was limited to repeated local source surfaces inside this batch: ETDA guideline and ETDA AIGC.
- Rows with summarized or access-restricted surfaces were capped at context or original-source retrieval.

## Verification
- Result TSV row count and queue_id set were verified against input.tsv after writing.
