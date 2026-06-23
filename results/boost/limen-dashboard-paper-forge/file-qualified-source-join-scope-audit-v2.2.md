# File-qualified source-join scope audit v2.2

Updated UTC: 2026-06-19T09:41:58Z  
Lane: `limen-dashboard-paper-forge`  
Project: `limen-ai-edge-case-atlas`

## Purpose

This audit closes the next bounded dashboard/paper blocker after the v2.1 release-state freeze: whether the existing `results/dashboard/source-ledger-join-v0.1.tsv` is sufficient to enable row-level access-date / rights / terms / license labels in the public dashboard or manuscript-facing exports.

## Result

Short answer: **no row-level badges should be enabled yet**.

The source-ledger join is useful and renderer-consumable as a provenance-control table, but it remains mostly a family, rollup, threshold, or collision-safety join. It supports artifact-level provenance pointers, candidate source links, and a non-count-bearing provenance legend. It does **not** support per-row access-date/rights/terms/license tooltips for the count-bearing dashboard rows.

## Checked surfaces

- Join table: `results/dashboard/source-ledger-join-v0.1.tsv`
- Release UI config: `dashboard/release-card-ui-config-v0.1.json`
- Authoritative ledger: `sources/authoritative-source-ledger.tsv`
- Output TSV: `results/boost/limen-dashboard-paper-forge/file-qualified-source-join-scope-audit-v2.2.tsv`
- Source-ID resolution TSV: `results/boost/limen-dashboard-paper-forge/file-qualified-source-join-source-id-resolution-v2.2.tsv`

## Summary

| audit_id | surface | state | evidence | next action |
|---|---|---|---|---|
| FQSJ-001 | source-ledger join table coverage | PASS_PRESENT | 99 rows in results/dashboard/source-ledger-join-v0.1.tsv across 7 dashboard views. | Keep using source-ledger join as renderer gate before API/static/dashboard export. |
| FQSJ-002 | row-level access/rights badges | BLOCKED | public_dashboard_action distribution: {'show_family_level_reuse_note_only_block_per_source_badges': 15, 'block_row_level_access_rights_labels': 80, 'show_candidate_source_ids_as_review_links_block_access_rights_badges': 4} | Do not enable access_date/rights_terms_note/license tooltips until file-qualified case/source rows are verified. |
| FQSJ-003 | authoritative source-ID resolution inside threshold rollups | PASS_IDS_RESOLVE_BUT_ROLLUP_BLOCKS_BADGES | 27 distinct SRC-AUTH IDs resolve in sources/authoritative-source-ledger.tsv; missing=0. | If UI adds source links for threshold rows, label them candidate authoritative links and keep access/rights badges blocked. |
| FQSJ-004 | view-level badge policy | READY_AS_POLICY_TABLE | duplicate_review_graph=27; evidence_tier_funnel=11; jurisdiction_language=12; legal_uncertainty=15; security_agentic_threshold=4; source_family_saturation=15; taxonomy_heatmap=15 | Add this policy table as a non-count-bearing provenance legend if UI is edited. |
| FQSJ-005 | external action boundary | NO_EXTERNAL_ACTION | No upload, deposit, submission, email, contact, portal action, crawler expansion, or bulk download performed. | Human release decision remains Anton-controlled. |


## View counts from the join table

| dashboard_view | rows |
|---|---:|
| `duplicate_review_graph` | 27 |
| `evidence_tier_funnel` | 11 |
| `jurisdiction_language` | 12 |
| `legal_uncertainty` | 15 |
| `security_agentic_threshold` | 4 |
| `source_family_saturation` | 15 |
| `taxonomy_heatmap` | 15 |


## Public dashboard action distribution

| public_dashboard_action | rows |
|---|---:|
| `block_row_level_access_rights_labels` | 80 |
| `show_candidate_source_ids_as_review_links_block_access_rights_badges` | 4 |
| `show_family_level_reuse_note_only_block_per_source_badges` | 15 |


## Authoritative source-ID resolution note

The only rows with explicit `SRC-AUTH-*` identifiers in the current join table are threshold-style rollups. This audit found 27 distinct authoritative source IDs resolving against `sources/authoritative-source-ledger.tsv` and 0 missing source IDs. Even when IDs resolve, the row posture remains `BLOCK_ROW_LEVEL_BADGES_ROLLUP_ONLY` because threshold rows aggregate/collide across case namespaces.

## Claim ceiling

This audit verifies provenance-label scope and package/dashboard parity only. It does not promote any incident row, validate source truth, establish legal compliance or non-compliance, claim completeness or prevalence, rank countries, certify safety, prove deployment, or fuse GAIA/PALLAS/LIMEN denominators.

## Observatory hook

A dashboard can consume `results/boost/limen-dashboard-paper-forge/file-qualified-source-join-scope-audit-v2.2.tsv` as a `provenance_label_gate` or `package_health` panel. The intended visualization is a small fail-closed badge/legend:

- artifact-level provenance: allowed;
- source-family notes: allowed for family rows;
- candidate authoritative links: allowed for threshold rollups with warnings;
- row-level access-date / rights / terms / license badges: blocked until file-qualified source joins are manually verified.

## Checksums

| artifact | sha256 |
|---|---|
| `results/boost/limen-dashboard-paper-forge/file-qualified-source-join-scope-audit-v2.2.tsv` | `046f4aab9fafdccec2db7bae0aa6c819a322e55cef9a5774c48cb1bbea20b182` |
| `results/boost/limen-dashboard-paper-forge/file-qualified-source-join-source-id-resolution-v2.2.tsv` | `4daecc1e2172b6a818405791738dea43f60e7b35b48f87087324313bb3abe2c1` |
| `results/dashboard/source-ledger-join-v0.1.tsv` | `0a87c7f27f2e8c040258b17c78d6204a4298f8f5e3f117092f5b8e61de41851d` |

