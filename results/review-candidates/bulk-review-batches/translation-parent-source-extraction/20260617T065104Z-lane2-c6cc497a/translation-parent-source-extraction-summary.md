# translation-parent-source-extraction summary

Batch: 20260617T065104Z-lane2-c6cc497a
Task: translation-parent-source-extraction
Input rows reviewed: 1
Output rows written: 1

Verdict counts:
- source_url_extracted: 1
- parent_source_wrapper: 0
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Notes:
- Reviewed BTPS-00123 / LIMEN-SIGNAL-CCACC40DBF8AE9A9 exactly once.
- Local source context at PALLAS_READINESS_WORLD_SOURCE_PACK.csv:2145 explicitly supplies the CNIL public URL.
- Claim ceiling remains source-surface only: France/CNIL sandbox context, not French Guiana-specific AI Act sandbox implementation, legal/compliance/safety/prevalence/ranking evidence.

Verification:
- Result TSV header matches required schema.
- Result TSV has one data row for one input data row.
- Queue_id set matches input exactly: BTPS-00123.
