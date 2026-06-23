# LIMEN row-level provenance label gate v1.2

Generated UTC: 2026-06-19T00:42:00Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

This audit closes the open v1.1 blocker about row-level access-date/rights labels by making it executable as a dashboard/paper gate. It checks the seven release-card dashboard views against `dashboard/release-card-ui-config-v0.1.json` and records whether each count-bearing surface already carries row-level `access_date` and `rights_terms_note` fields.

No new collection, network access, upload, deposit, publication, email, portal action, row promotion, or legal/compliance assessment was performed.

## Verdict

- Surface rows audited: `7` dashboard views.
- Row-level access-date + rights ready now: `0` views.
- Blocked for row-level access-date/rights labels: `7` views.
- Machine-readable gate: `results/boost/limen-dashboard-paper-forge/row-level-provenance-label-gate-v1.2.tsv`.

## Finding

The current dashboard package is still safe for artifact-level provenance because every release-card view carries a local source path, checksum, denominator subtitle, claim ceiling, and prohibited-reading rule through `dashboard/release-card-ui-config-v0.1.json`. It is **not** yet safe to display per-row access-date or rights/terms labels in tooltips: none of the active count-bearing dashboard exports contains both required fields as first-class row columns.

This is a useful negative result: v1.1's "hide row-level access-date/rights labels until source-ledger joins are verified" rule remains correct, now with a row-level gate artifact rather than a prose-only warning.

## Source ledger inventory checked

| ledger | data_rows_estimate | sha256 | header/scope |
|---|---:|---|---|
| `sources/sources.md` | 102 | `b9081d53dd4763270395ca3b21cbf23ceea9d8832c2f48d8fabde37a70ab0a3d` | markdown_table_or_notes |
| `sources/authoritative-source-ledger.tsv` | 38 | `36e8addd9a4501e156778450464bddfa5e8afce137bc0db961a02e992303c16d` | source_id, case_id, record_status, evidence_tier, issuing_body, jurisdiction, language, source_type, authority_level, document_depth_status, published_date, access_date |


## Dashboard gate table

| view | source rows | access_date column | rights/terms column | gate state |
|---|---:|---|---|---|
| `source_family_saturation` | 15 | no | no | `BLOCK_ROW_LEVEL_LABELS_SOURCE_POINTERS_ONLY` |
| `taxonomy_heatmap` | 15 | no | no | `BLOCK_ROW_LEVEL_LABELS_SOURCE_POINTERS_ONLY` |
| `evidence_tier_funnel` | 11 | no | no | `BLOCK_ROW_LEVEL_LABELS_NO_JOIN_KEY_VISIBLE` |
| `jurisdiction_language` | 12 | no | no | `BLOCK_ROW_LEVEL_LABELS_SOURCE_POINTERS_ONLY` |
| `legal_uncertainty` | 15 | no | no | `BLOCK_ROW_LEVEL_LABELS_SOURCE_POINTERS_ONLY` |
| `security_agentic_threshold` | 4 | no | no | `BLOCK_ROW_LEVEL_LABELS_NO_JOIN_KEY_VISIBLE` |
| `duplicate_review_graph` | 27 | no | no | `BLOCK_ROW_LEVEL_LABELS_SOURCE_POINTERS_ONLY` |

## Required renderer rule

For every count-bearing dashboard view:

1. Show artifact-level provenance now: `source_path`, `source_sha256`, row count, denominator subtitle, claim ceiling, and prohibited-reading warning.
2. Do **not** show row-level `access_date`, `rights_terms_note`, license, or terms labels unless the row comes from a materialized join that has both fields as first-class columns.
3. If a surface has only `provenance_inputs`, `local_artifact_anchors`, `files_contributing`, or `linked_review_queue_ids`, render those as source-pointer text, not as verified row-level rights/access metadata.
4. Treat family-level and aggregate rows as rollups. They need a rollup policy (`all_same`, `mixed`, `unknown`, `not_applicable`) before rights/access badges are allowed.

## Paper/dashboard readiness delta

This strengthens hostile-reviewer readiness by separating three provenance layers that a reviewer could otherwise conflate:

- artifact-level reproducibility: currently available and executable through v1.1/v1.2 gates;
- source-pointer provenance: partially available through dashboard row columns;
- row-level access-date/rights labels: blocked until explicit source-ledger joins are materialized.

## Claim ceiling

This audit supports package-integrity, dashboard/paper parity, and provenance-label discipline only. It does not support completeness, prevalence, incident truth, legal guilt, compliance, certification, safety, deployment, country ranking, official endorsement, or a fused GAIA/PALLAS/LIMEN denominator.

## Next smallest move

Create a materialized `results/dashboard/source-ledger-join-v0.1.tsv` that resolves dashboard row keys to `sources/sources.md` and `sources/authoritative-source-ledger.tsv`, with fields: `dashboard_view`, `row_key`, `source_id_or_path`, `access_date`, `rights_terms_note`, `language`, `jurisdiction`, `join_confidence`, `rollup_policy`, and `human_review_needed`.
