# Bulk translation review summary

Batch: 20260617T064627Z-lane4-dd67dc8c
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260617T064627Z-lane4-dd67dc8c/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260617T064627Z-lane4-dd67dc8c/bulk-translation-review-results.tsv

Reviewed rows: 6

Verdict counts:
- candidate_for_parent_source_extraction: 2
- cross_project_duplicate: 1
- source_surface_only_no_case: 1
- translation_source_reviewed: 2

Boundary applied: processing-state review only. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking was made.

Notes:
- GAIA cross-project rows were kept at source-surface/context level; one release-freeze row was marked duplicate of the active GAIA parent row.
- The France Pallas row is a research-query surface, not a concrete case.
- Canada AI Register rows are official-register accession surfaces and were routed to parent-source extraction rather than promoted.

Verification:
- Output header matches the required schema.
- Output has one data row per input queue_id.
- Output queue_id set equals input queue_id set.
