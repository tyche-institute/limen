# LIMEN token-free review audit

- Generated: `2026-06-23T15:39:55Z`
- Current paid-token-required rows: `2`
- Current human-required rows: `0`
- Current missing review rows: `2`
- Incomplete layers: `bulk_parent_source_extraction`

| Layer | Mode | Complete | Rows | Missing | Paid-token rows | Human rows |
|---|---:|---:|---:|---:|---:|---:|
| candidate_materialization | deterministic_no_tokens | True | 55725 | 0 | 0 | 0 |
| first_pass_candidate_review | deterministic_no_tokens | True | 55725 | 0 | 0 | 0 |
| direct_source_review | hermes_or_human_when_backlog_exists | True | 13918 | 0 | 0 | 0 |
| translation_hold_board | deterministic_no_tokens_for_board_only | True | 554 | 0 | 0 | 0 |
| hardening_named-url-extraction | hermes_or_human_when_backlog_exists | True | 208 | 0 | 0 | 0 |
| hardening_translation-source-review | hermes_or_human_when_backlog_exists | True | 554 | 0 | 0 | 0 |
| bulk_bulk_translation_review | hermes_or_human_when_backlog_exists | True | 751 | 0 | 0 | 0 |
| bulk_parent_source_extraction | hermes_or_human_when_backlog_exists | False | 1826 | 2 | 2 | 0 |
| bulk_translation_parent_source_extraction | hermes_or_human_when_backlog_exists | True | 116 | 0 | 0 | 0 |
| source_review_promotion_hardening | deterministic_no_tokens | True | 1646 | 0 | 0 | 0 |
| source_review_completion_ledger | deterministic_no_tokens | True | 1646 | 0 | 0 | 0 |
| reviewed_core_promotion_packet | deterministic_no_tokens | True | 2003 | 0 | 0 | 0 |
| case_extraction_rollup | hermes_or_human_when_backlog_exists | True | 974 | 0 | 0 | 0 |
| case_hardening_review | deterministic_fetch_no_model_tokens | True | 13 | 0 | 0 | 0 |
| case_autoreview | deterministic_no_tokens | True | 13 | 0 | 0 | 0 |

Audit only. It does not mine, call models, promote reviewed-core rows, add ObscureAI cases, or deploy.
