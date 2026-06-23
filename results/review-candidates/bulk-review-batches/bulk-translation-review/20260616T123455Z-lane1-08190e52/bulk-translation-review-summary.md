# Bulk translation review summary

Batch: 20260616T123455Z-lane1-08190e52
Task: bulk-translation-review
Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T123455Z-lane1-08190e52/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T123455Z-lane1-08190e52/bulk-translation-review-results.tsv`

## Verification

- Input rows reviewed: 16
- Output rows written: 16
- Queue ID set: exact match
- Duplicate queue IDs in output: none
- Allowed verdict values only: yes
- Boundary observed: processing-state review only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
- Sources used: local input TSV plus exact local source lines referenced by each row. No web crawl or external submission was used.

## Verdict counts

- candidate_for_parent_source_extraction: 6
- cross_project_duplicate: 4
- source_surface_only_no_case: 3
- translation_source_reviewed: 3

## Notes

Most rows remain source-surface/context or translation-sensitive parent-source candidates. Duplicate local captures were marked as cross_project_duplicate and routed to the first reviewed queue item in this batch. Infrastructure-only or non-jurisdiction-specific rows were capped at source-surface-only/no-case.
