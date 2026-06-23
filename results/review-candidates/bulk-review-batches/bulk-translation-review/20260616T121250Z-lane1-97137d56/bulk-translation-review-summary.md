# Bulk translation review summary

- batch_id: 20260616T121250Z-lane1-97137d56
- task: bulk-translation-review
- input_rows_reviewed: 16
- output_rows_written: 16
- boundary: processing-state/source-surface review only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

## Verdict counts
- candidate_for_parent_source_extraction: 1
- cross_project_duplicate: 5
- source_surface_only_no_case: 4
- translation_source_reviewed: 6

## Notes
- Dutch Algorithm Register auto-translation rows were kept as cross-project duplicates rather than promoted.
- Pakistan MOITT PDF rows were deduplicated because local metadata names the official PDF but fetch failed and no local source body is available.
- Iceland, Serbia, Aruba, and Cabo Verde rows remain source-surface/context only because local metadata negates the queried sandbox/register claim.
- Chinese, Colombian, Norwegian, Romanian, and Turkish rows were reviewed only at source-surface level with original-language/source-extraction limits.
