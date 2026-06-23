# LIMEN source-ledger join materialization v1.3

Generated UTC: 2026-06-19T01:20:00Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

This cycle materialized the v1.2 blocker into `results/dashboard/source-ledger-join-v0.1.tsv`. The output is a dashboard/paper provenance-control table that resolves each active release-card row to the safest available local source-ledger relation: exact family-level ledger rows where possible, candidate authoritative-source review links where bounded, and explicit blocked states for aggregate/control rows.

No new crawling, network access, upload, deposit, portal action, row promotion, incident validation, legal/compliance assessment, or denominator relaxation was performed.

## Machine-readable artifacts

- `results/dashboard/source-ledger-join-v0.1.tsv`
- `results/boost/limen-dashboard-paper-forge/source-ledger-join-v0.1.tsv`
- SHA-256: `0a87c7f27f2e8c040258b17c78d6204a4298f8f5e3f117092f5b8e61de41851d`
- Rows: `99`

## Join result

| class | rows | dashboard implication |
|---|---:|---|
| family ledger exact ID, not per-source row | 15 | show family-level reuse/access note only; block per-source badges |
| candidate authoritative case-ID rollup with collision risk | 3 | show candidate source IDs as review links only; block access/rights badges |
| all other aggregate/control/provenance-pointer rows | 81 | artifact-level provenance only; no row-level access-date/rights labels |

Per-view row counts:

- `duplicate_review_graph`: 27
- `evidence_tier_funnel`: 11
- `jurisdiction_language`: 12
- `legal_uncertainty`: 15
- `security_agentic_threshold`: 4
- `source_family_saturation`: 15
- `taxonomy_heatmap`: 15

## Interpretation

Evidence: the package now has a concrete join table for every active dashboard release-card row. Fifteen source-family rows can be connected to `sources/source-family-ledger.tsv` by `family_id`, but these remain family-level rollups; they do not license per-source access-date or rights badges. Security-threshold rows can expose candidate authoritative source IDs as review links, but the rows are threshold rollups and the duplicate graph already documents LIMEN ID collision risk.

Interpretation: the v1.2 rule remains correct but is now more operational. A renderer can consume `join_confidence`, `rollup_policy`, `human_review_needed`, and `public_dashboard_action` to decide whether to show artifact-level provenance, family-level notes, candidate review links, or blocked row-level badges.

## Renderer rule

1. For `family_ledger_exact_id_not_row_source`, show `source_id_or_path`, family-level `access_date`/`rights_terms_note` as ledger-scope notes only; do not label them as row-level source facts.
2. For `candidate_case_id_join_rollup_collision_risk`, show `source_id_or_path` as review-link candidates; do not show access-date/rights badges until a file-qualified source join is reviewed.
3. For `aggregate_no_source_ledger_key`, `file_aggregate_no_source_ledger_key`, `denominator_stage_no_source_ledger_key`, and `provenance_pointer_only_collision_blocker`, keep artifact-level provenance only.

## Claim ceiling

This supports dashboard/paper parity, provenance-label discipline, hostile-reviewer traceability, and a reproducible source-join gate. It does not support completeness, prevalence, incident truth, legal guilt, compliance, certification, safety assurance, deployment claims, country ranking, official endorsement, or a fused GAIA/PALLAS/LIMEN denominator.

## Next smallest publishability move

Patch the dashboard renderer/API bundle to consume `results/dashboard/source-ledger-join-v0.1.tsv` for tooltip state. Keep row-level access-date/rights labels hidden by default; expose only artifact-level provenance, family-level notes, and candidate review links until a file-qualified source ledger join is manually verified.


## v1.3 verification rerun (2026-06-19T01:28:00Z)

After materializing `results/dashboard/source-ledger-join-v0.1.tsv`, the existing fail-closed package checks were rerun:

- `python3 -m json.tool manifest.json`: PASS.
- `source-ledger-join-v0.1.tsv` structural check: PASS, 99 rows, seven dashboard views, `public_dashboard_action` populated for every row.
- `tools/limen_dashboard_ui_contract_check.py --write-artifacts`: PASS 7/7; new report `results/boost/limen-dashboard-paper-forge/dashboard-ui-contract-fail-closed-check-2026-06-19T00-11-11Z.md`.
- `tools/build_limen_dashboard_api_bundle.py`: PASS 7/7; rebuilt `dashboard/limen-dashboard-api-bundle-v0.1.json`.
- `tools/build_limen_static_dashboard_preview.py`: PASS 7/7; rebuilt `dashboard/static-dashboard-preview-v0.1.html`.

Important limitation: these checks confirm that the prior caption/dashboard gates still pass after adding the join table. They do not yet prove that the renderer consumes `source-ledger-join-v0.1.tsv`; that remains the next code patch.
