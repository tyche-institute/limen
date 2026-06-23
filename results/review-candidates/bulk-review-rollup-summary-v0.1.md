# LIMEN Bulk Review Rollup

Generated UTC: 2026-06-23T19:58:28Z

- All queues complete: `True`
- Current output clean: `False`
- Blocking integrity issue: `True`
- Duplicate queue IDs: `False`
- Duplicate queue IDs in queues: `False`
- Extra queue IDs: `True`
- Signal mismatch queue IDs: `True`
- Superseded historical result queue IDs: `1907`
- Failed batches: `True`

## parent_source_extraction

- Queue rows: `1832`
- Completed unique queue IDs: `1832`
- Missing queue IDs: `0`
- Result files: `164`
- Verdict counts: `{"country_gap_no_parent_source": 817, "duplicate_existing_core": 1, "parent_source_wrapper": 465, "reject_noise": 28, "source_surface_only_no_case": 181, "source_url_extracted": 340}`

## bulk_translation_review

- Queue rows: `751`
- Completed unique queue IDs: `751`
- Missing queue IDs: `0`
- Result files: `53`
- Verdict counts: `{"candidate_for_parent_source_extraction": 116, "cross_project_duplicate": 163, "machine_translation_hold": 40, "needs_original_language_source": 57, "reject_noise": 12, "source_surface_only_no_case": 222, "translation_source_reviewed": 141}`

## translation_parent_source_extraction

- Queue rows: `116`
- Completed unique queue IDs: `116`
- Missing queue IDs: `0`
- Result files: `16`
- Verdict counts: `{"parent_source_wrapper": 6, "source_surface_only_no_case": 1, "source_url_extracted": 109}`

## Boundary

Bulk rollup is processing-state only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
