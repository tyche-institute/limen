# Bulk translation review summary

Batch: 20260616T122744Z-lane1-7fafad99
Task: bulk-translation-review
Input rows reviewed: 16
Result rows written: 16

## Verdict counts
- cross_project_duplicate: 6
- needs_original_language_source: 4
- reject_noise: 1
- source_surface_only_no_case: 4
- translation_source_reviewed: 1

## Boundary applied
This batch performed processing-state/source-surface review only. It made no reviewed-core promotion, ObscureAI addition, incident truth claim, legal finding, safety finding, compliance finding, prevalence claim, or ranking. Machine-translated Dutch register records were held to source-surface field/existence status pending original Dutch review. Metadata-only hits were kept as source/context or rejected as queue noise.

## Verification
- Result TSV header matches the required schema.
- Result TSV queue_id set equals input.tsv queue_id set.
- Result TSV data-row count equals input.tsv data-row count (16).
- No duplicate queue_id values in results.
