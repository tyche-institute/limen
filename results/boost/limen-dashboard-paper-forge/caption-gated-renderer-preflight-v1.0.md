# LIMEN caption-gated renderer preflight v1.0

Generated UTC: 2026-06-18T21:25:00Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

Convert the v0.9 caption-currentness audit from a passive lint artifact into an executable fail-closed renderer gate for dashboard/API/static-preview exports. This protects dashboard/paper parity by preventing count-bearing surfaces from silently reusing stale caption-control denominators.

No new collection, network access, upload, deposit, public release, legal/compliance finding, safety claim, prevalence claim, or row promotion was performed.

## Code/artifact changes

| Path | Role |
|---|---|
| `tools/limen_caption_currentness_gate.py` | New shared caption-currentness gate. Maps dashboard views to caption-control IDs and fails mapped views when v0.9 audit rows are blocked, missing, or non-pass. |
| `tests/test_limen_caption_currentness_gate.py` | Regression tests for blocked taxonomy reuse and permitted funnel reuse. |
| `tools/limen_dashboard_ui_contract_check.py` | UI contract check now consumes `caption-currentness-audit-v0.9.tsv`. |
| `tools/build_limen_dashboard_api_bundle.py` | API bundle now exposes caption-currentness status and fails closed on blocked mapped views. |
| `tools/build_limen_static_dashboard_preview.py` | Static preview now exposes caption-currentness status and refuses blocked mapped views. |

## Preflight result

| Gate | Artifact | Verdict | PASS | FAIL | Interpretation |
|---|---|---:|---:|---:|---|
| UI contract | `results/boost/limen-dashboard-paper-forge/dashboard-ui-contract-fail-closed-check-v1.0-caption-gated.tsv` | FAIL | 6 | 1 | Expected negative result: `taxonomy_heatmap` is blocked because CCR-001 and CCR-002 still carry stale denominator control text. |
| API bundle | `results/boost/limen-dashboard-paper-forge/dashboard-api-bundle-gate-v1.0-caption-gated.tsv` | FAIL | 6 | 1 | API export refuses the same blocked taxonomy surface and records the caption-currentness reason. |
| Static preview | `results/boost/limen-dashboard-paper-forge/static-dashboard-preview-gate-v1.0-caption-gated.tsv` | FAIL | 6 | 1 | Static renderer refuses the same blocked taxonomy surface. |

The failing row is useful negative evidence: `results/dashboard/taxonomy-heatmap.tsv` still passes row-count and checksum guards, but the renderer now correctly blocks count-bearing export because the linked caption-control rows (`CCR-001`, `CCR-002`) remain stale according to `results/boost/limen-dashboard-paper-forge/caption-currentness-audit-v0.9.tsv`.

## Claim boundary

This artifact supports a methods/data-paper claim about fail-closed dashboard/paper parity and stale-caption prevention. It does not support completeness, prevalence, legal guilt/liability, compliance, certification, safety assurance, official incident status, country ranking, source-truth, third-party endorsement, or a fused GAIA/PALLAS/LIMEN denominator.

## Observatory hook

Dashboard/API/static renderers can consume the new fields:

- `caption_currentness_status`
- `caption_currentness_reason`
- `source_caption_currentness_audit`

Interpretation supported: show a red package-integrity badge for blocked count-bearing surfaces even when source TSV checksums are valid. This makes stale manuscript captions visible at the dashboard layer before export.

## Next smallest publishability move

Patch or supersede the stale caption-control rows `CCR-001` and `CCR-002` with current Figure 2/Table 2 denominator language (`39/29 core`, `44/34 extended`, legacy `35/27` as provenance only), then rerun the v1.0 gated preflight. Until then, `taxonomy_heatmap` should remain blocked for count-bearing PDF, dashboard, API, or manuscript export.
