# LIMEN dashboard UI contract fail-closed check

Generated: 2026-06-18T20:09:31+00:00
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

This bounded check validates `dashboard/release-card-ui-config-v0.1.json` as a fail-closed renderer contract for future count-bearing dashboard views. A view is marked renderable only if its local export exists, row count and SHA-256 match the config, denominator/subtitle text is present, tooltip fields include provenance and claim-ceiling requirements, and prohibited readings remain visible.

No new collection, network access, upload, deposit, or public release was performed.

## Verdict

- Verdict: `FAIL`
- PASS rows: 6
- FAIL rows: 1
- Machine-readable TSV: `results/boost/limen-dashboard-paper-forge/dashboard-ui-contract-fail-closed-check-v1.0-caption-gated-rerun.tsv`

## View gate table

| Dashboard view | Allowed to render | Status | Reason | Source rows |
|---|---:|---|---|---:|
| `source_family_saturation` | true | PASS | all_required_ui_guards_present | 15 |
| `taxonomy_heatmap` | false | FAIL | caption currentness gate failed: CCR-001:BLOCK_FOR_COUNT_BEARING_REUSE:rewrite caption/control text before PDF, dashboard, or manuscript export; keep as historical lint source only until patched; CCR-002:BLOCK_FOR_COUNT_BEARING_REUSE:rewrite caption/control text before PDF, dashboard, or manuscript export; keep as historical lint source only until patched | 15 |
| `evidence_tier_funnel` | true | PASS | all_required_ui_guards_present | 11 |
| `jurisdiction_language` | true | PASS | all_required_ui_guards_present | 12 |
| `legal_uncertainty` | true | PASS | all_required_ui_guards_present | 15 |
| `security_agentic_threshold` | true | PASS | all_required_ui_guards_present | 4 |
| `duplicate_review_graph` | true | PASS | all_required_ui_guards_present | 27 |

## Failures / warnings

- FAIL: taxonomy_heatmap: caption currentness gate failed: CCR-001:BLOCK_FOR_COUNT_BEARING_REUSE:rewrite caption/control text before PDF, dashboard, or manuscript export; keep as historical lint source only until patched; CCR-002:BLOCK_FOR_COUNT_BEARING_REUSE:rewrite caption/control text before PDF, dashboard, or manuscript export; keep as historical lint source only until patched
- No warnings detected.

## Paper/dashboard readiness delta

This adds a durable hostile-reviewer control proving that dashboard UI binding can fail closed rather than silently rendering count-bearing charts without denominator labels, claim ceilings, provenance pointers, or prohibited-reading warnings. It strengthens dashboard/paper parity without changing any data denominator.

## Claim boundary

This artifact verifies local UI-contract integrity only. It does not support completeness, prevalence, legal liability, compliance, certification, safety assurance, official incident status, country ranking, third-party endorsement, or source-truth claims.

## Next smallest move

If/when a concrete dashboard app is edited, make the renderer import this config and refuse to mount a count-bearing chart unless its `allowed_to_render` gate would pass; keep row-level access-date/rights labels hidden until source-ledger joins are verified.
