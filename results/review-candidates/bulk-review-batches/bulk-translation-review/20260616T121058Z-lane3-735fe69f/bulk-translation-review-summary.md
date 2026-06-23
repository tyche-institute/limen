# Bulk translation review summary

Batch: 20260616T121058Z-lane3-735fe69f

Reviewed 16 input rows exactly once using local metadata/source files only. No web crawl, portal action, publication, upload, legal finding, safety finding, compliance finding, prevalence claim, ranking, or reviewed-core promotion was made.

Verdict counts:
- candidate_for_parent_source_extraction: 2
- cross_project_duplicate: 4
- machine_translation_hold: 2
- source_surface_only_no_case: 6
- translation_source_reviewed: 2

Boundary notes:
- Concrete non-English parent-source candidates were held to source-surface status pending original-language extraction/review.
- Auto-translated Dutch register samples remain machine-translation holds or duplicates.
- General procurement, policy, and digital-government rows were kept as context/source-surface only when no explicit edge-case claim was present.

Verification:
- Output TSV header matches the required schema.
- Output row count equals input row count: 16.
- Output queue_id set equals input queue_id set; no omissions, extras, or duplicate queue_id values.
