# Bulk translation review summary: 20260617T064339Z-lane2-212433c1

Status: complete

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260617T064339Z-lane2-212433c1/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260617T064339Z-lane2-212433c1/bulk-translation-review-results.tsv
Rows reviewed: 16

Verification:
- result header matches required schema
- input row count: 16
- result row count: 16
- queue_id set equality: PASS
- duplicate result queue_id values: none
- processing boundary: source-surface/translation review only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim

Verdict counts:
- candidate_for_parent_source_extraction: 4
- source_surface_only_no_case: 5
- translation_source_reviewed: 7

Notes:
- Most rows remain source-surface/context or parent-source extraction candidates.
- Rows with explicit local metadata for AI catalogs, sectoral high-risk AI lists, or sandbox pilots were capped at parent source extraction with caveats.
- Territory rows pointing only to France-level CNIL/data.gouv surfaces were not promoted to territory-specific cases.
