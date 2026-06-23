# translation-parent-source-extraction summary

Batch: 20260616T130035Z-lane7-613828a8
Input rows reviewed: 16
Output rows written: 16

Verdict counts:
- source_url_extracted: 15
- parent_source_wrapper: 1
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Notes:
- Every input queue_id was reviewed exactly once against local metadata/source context only.
- Concrete URLs were extracted only where explicitly present in local rows, JSONL metadata, or source-refresh rows.
- BTPS-00106 was marked parent_source_wrapper because the score-change row points to multiple Icelandic official sandbox parent-source rows (PALLAS_SECOND_PASS_SPRINT_13_SOURCE_REFRESH.csv:109-110), requiring human source choice.
- Territorial rows for French Guiana and Reunion retain national/negative-context caveats and are not promoted to territorial claims.

Verification:
- Result TSV header matches configured schema.
- Result TSV has one row per input queue_id, with no omissions, extras, or duplicate queue_id values.
- Internal field sanitation removed tabs/newlines from result fields.
