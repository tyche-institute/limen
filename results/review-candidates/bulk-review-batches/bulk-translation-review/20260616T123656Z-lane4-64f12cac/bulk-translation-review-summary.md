# Bulk translation review summary

Batch: 20260616T123656Z-lane4-64f12cac
Input rows reviewed: 16
Output rows written: 16

Scope: processing-state translation/source-surface review only. No reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking was made. Review used only local metadata/source rows plus language-aware reading of the captured titles/snippets.

## Verdict counts
- candidate_for_parent_source_extraction: 1
- cross_project_duplicate: 3
- machine_translation_hold: 1
- source_surface_only_no_case: 4
- translation_source_reviewed: 7

## Notes
- Dutch Algorithm Register rows were treated conservatively because local text warns English descriptions are automatically translated; Dutch original remains authoritative.
- Persian Mehr rows are duplicate translation-sensitive state-media policy-report surfaces and require Persian-original capture before bounded extraction.
- Peru's official AI applications catalog is the only row marked for parent source extraction, with a catalog/source-surface ceiling rather than a formal algorithm-register claim.
- Belgium, Argentina, Hamburg, and Saint Pierre and Miquelon rows remain source-surface/negative-context only.

## Verification
- Result TSV header matches the required schema.
- One output row was written for each input queue_id.
- Queue_id set and row count were verified against input.tsv after writing.
