# Bulk translation review summary

- Batch: 20260616T123346Z-lane3-8b615968
- Input rows reviewed: 16
- Output rows written: 16
- Boundary: processing-state source-surface review only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
- Verification: result queue_id set and row count match input.tsv; no duplicate output queue_id values.

## Verdict counts
- candidate_for_parent_source_extraction: 4
- cross_project_duplicate: 1
- source_surface_only_no_case: 9
- translation_source_reviewed: 2

## Notes
- Most rows were retained at source-surface/context ceiling because local metadata did not expose an explicit case-level edge-case claim.
- Candidate parent-source extraction rows: BTR-00385, BTR-00387, BTR-00397, BTR-00399.
- BTR-00388 is a cross-project duplicate of the ANPD source reviewed at BTR-00385.
- BTR-00393 should be resolved through local source-refresh lines before any downstream extraction because the input locator is a score-delta row rather than the source row itself.
