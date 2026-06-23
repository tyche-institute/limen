# Bulk translation review summary

Batch: 20260616T125240Z-lane3-32f169ad
Task: bulk-translation-review
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T125240Z-lane3-32f169ad/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T125240Z-lane3-32f169ad/bulk-translation-review-results.tsv

## Verification

- Input rows reviewed: 16
- Result rows written: 16
- Queue ID set: exact match
- Duplicate output queue IDs: none
- Header: exact required header
- Boundary: processing-state/source-surface review only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

## Verdict counts

- candidate_for_parent_source_extraction: 5
- cross_project_duplicate: 1
- needs_original_language_source: 1
- source_surface_only_no_case: 6
- translation_source_reviewed: 3

## Notes

- Candidate extraction rows were limited to concrete source-surface claims already explicit in local metadata/source-pack rows.
- Source-surface-only rows remain contextual or negative-check evidence and should not be promoted as cases.
- One Ecuador SPDP resolution row was marked as a duplicate of the other local matrix occurrence.
- One Persian Nezamat row needs original-language content because local retrieval timed out and provided no snippet/content hash.
