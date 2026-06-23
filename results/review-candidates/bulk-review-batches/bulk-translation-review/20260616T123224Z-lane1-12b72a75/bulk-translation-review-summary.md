# Bulk translation review summary

Batch: 20260616T123224Z-lane1-12b72a75
Completed at UTC: 2026-06-16T12:33:26Z
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T123224Z-lane1-12b72a75/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T123224Z-lane1-12b72a75/bulk-translation-review-results.tsv

## Verification

- Input rows: 16
- Output rows: 16
- Queue ID set: exact match
- Duplicate output queue_id values: none
- Output header: exact required header
- Field sanitation: tabs/newlines removed from fields

## Verdict counts

- candidate_for_parent_source_extraction: 5
- cross_project_duplicate: 2
- needs_original_language_source: 1
- reject_noise: 1
- source_surface_only_no_case: 4
- translation_source_reviewed: 3

## Review boundary

This batch is processing-state review only. It does not promote any item to reviewed-core, add anything to ObscureAI, establish incident truth, make legal/safety/compliance findings, or assert prevalence/ranking. Review used local metadata and local source rows only. Machine-translated or non-English surfaces are capped at source-surface/context unless exact original-language extraction is still required.

## Notes

- BTR-00380 duplicates the same ETDA guidance URL handled under BTR-00379.
- BTR-00383 duplicates the same Dutch algorithm-register parent URL handled under BTR-00381.
- BTR-00384 has a local timeout/fetch warning and no cached snippet; it requires original Persian source retrieval before translation-aware content review.
