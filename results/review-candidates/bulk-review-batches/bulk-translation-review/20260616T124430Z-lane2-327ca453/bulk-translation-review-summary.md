# Bulk translation review summary

Batch: 20260616T124430Z-lane2-327ca453
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T124430Z-lane2-327ca453/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T124430Z-lane2-327ca453/bulk-translation-review-results.tsv

Reviewed 16 input rows exactly once using local metadata/source files only. No reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking was made.

Verdict counts:
- candidate_for_parent_source_extraction: 4
- cross_project_duplicate: 1
- needs_original_language_source: 1
- source_surface_only_no_case: 7
- translation_source_reviewed: 3

Notes:
- Most rows remain source-surface or context-only because the local evidence names portals, guidelines, procurement pages, transparency portals, or adjacent legal-publication infrastructure rather than explicit edge-case facts.
- BTR-00551 and BTR-00556 are duplicate Malaysia AIGE locators and should be merged before extraction.
- Parent-source extraction candidates are bounded to original-language/source-surface extraction, not case-level promotion.
