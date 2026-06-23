# LIMEN caption-control denominator rewrite v1.1

Generated UTC: 2026-06-19T00:00:00Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

Resolve the v1.0 renderer blocker by rewriting the two stale taxonomy caption-control rows (`CCR-001`, `CCR-002`) against the current dashboard/API denominator grammar before count-bearing dashboard or manuscript export.

## Inputs

- `results/dashboard-paper/caption-control-register-v0.1.tsv`
- `results/boost/limen-dashboard-paper-forge/caption-currentness-audit-v0.9.tsv`
- `dashboard/release-card-ui-config-v0.1.json`
- `tools/limen_caption_currentness_gate.py`

## Rewrite applied

| Control | Surface | Before gate state | New denominator floor | Safe reuse state |
|---|---|---|---|---|
| `CCR-001` | Figure 2 taxonomy support heatmap | blocked for count-bearing reuse because stale `39/38/28` and mechanical `35/27` wording dominated | core `39 governed record refs / 29 unique lineages`; sidecar `44 / 34`; `35/27` legacy/provenance only | may be reused with current denominator badge and prohibited-reading text |
| `CCR-002` | Table 2 category support matrix | blocked for count-bearing reuse because stale `39/38/28` and mechanical `35/27` wording dominated | core `39 governed record refs / 29 unique lineages`; sidecar `44 / 34`; `35/27` legacy/provenance only | may be reused with current denominator badge and maturity/fragility bands visible |

## Claim boundary

This is a dashboard/paper parity and package-integrity repair only. It does not add records, promote incidents, change taxonomy membership, validate allegations, or support completeness, prevalence, legal/compliance, safety, deployment, country-ranking, source-truth, or fused GAIA/PALLAS/LIMEN denominator claims.

## Observatory hook

The taxonomy heatmap and Table 2 category support matrix can now render with explicit badges: `core 39/29`, `sidecar 44/34`, and `legacy 35/27 provenance only`. Tooltips should keep source path, checksum, claim ceiling, uncertainty/review status, and prohibited-reading warnings visible.

## Verification plan

Rerun:

```bash
python3 tools/limen_dashboard_ui_contract_check.py --project-root . --stamp caption-gated-rerun-v1.1 --write-artifacts
python3 tools/build_limen_dashboard_api_bundle.py --project-root . --output dashboard/limen-dashboard-api-bundle-v0.1.json --write-gate-tsv results/boost/limen-dashboard-paper-forge/dashboard-api-bundle-gate-v1.1.tsv
python3 tools/build_limen_static_dashboard_preview.py --project-root . --output dashboard/static-dashboard-preview-v0.1.html --write-gate-tsv results/boost/limen-dashboard-paper-forge/static-dashboard-preview-gate-v1.1.tsv
```

A pass means all seven dashboard views are locally renderable under caption-currentness, row-count, checksum, tooltip, subtitle, and prohibited-reading gates.
