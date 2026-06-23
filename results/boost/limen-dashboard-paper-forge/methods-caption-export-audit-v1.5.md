# LIMEN methods/caption export audit v1.5

Generated UTC: 2026-06-19T03:56:08Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

This bounded cycle moves the v1.4 source-ledger renderer gate into the manuscript Methods/caption export path. It verifies that the paper package can cite dashboard/paper parity without implying per-row access-date, rights/terms, license, source-truth, legal, safety, prevalence, or completeness claims.

No new crawling, network access, upload, deposit, portal action, row promotion, incident validation, legal/compliance assessment, source-truth assessment, denominator change, country ranking, or fused GAIA/PALLAS/LIMEN denominator was performed.

## Audit result

Overall status: `PASS`.

Machine-readable audit table: `results/boost/limen-dashboard-paper-forge/methods-caption-export-audit-v1.5.tsv`.

| audit_id | surface | status | evidence |
|---|---|---:|---|
| MCE-001 | draft_methods_denominator_registry | PASS | v1.4 source-ledger export rule present in Methods denominator section |
| MCE-002 | dashboard_spec_export_rule | PASS | dashboard spec cites v1.5 audit and v1.4 gate as export rule |
| MCE-003 | article_architecture_export_rule | PASS | article architecture records manuscript/caption rule |
| MCE-004 | ui_renderer_gate_v1.4 | PASS | 7/7 UI views PASS |
| MCE-005 | api_renderer_gate_v1.4 | PASS | 7/7 API views PASS with join-action summaries |
| MCE-006 | static_renderer_gate_v1.4 | PASS | 7/7 static views PASS with join-action summaries |
| MCE-007 | row_level_access_rights_badge_block | PASS | 99 join rows; 99 rows carry block-style public_dashboard_action |

## Manuscript patch

`draft/preprint.md` now contains a Methods-level source-ledger export rule: dashboard, API, static-preview, figure-export, and caption-export reuse must pass `results/boost/limen-dashboard-paper-forge/source-ledger-renderer-consumption-v1.4.md` and resolve rows through `results/dashboard/source-ledger-join-v0.1.tsv`. Family-level notes and candidate review links may be exposed; row-level access-date/rights/terms/license badges remain blocked pending file-qualified manual verification.

## Interpretation

Evidence: the existing v1.4 UI/API/static gates remain passing, and the article/draft/spec surfaces now point manuscript and caption export to the executable source-ledger gate.

Interpretation: this is a package-integrity and provenance-label discipline gain. It makes a hostile-reviewer Methods claim safer: dashboard/paper parity is governed by fail-closed render checks rather than by prose convention alone.

## Claim ceiling

This artifact supports reproducibility, dashboard/paper parity, source-ledger action coverage, and provenance-label export controls only. It does not support completeness, prevalence, source-truth, incident truth, legal guilt, compliance, certification, safety assurance, deployment claims, country ranking, official endorsement, or a fused GAIA/PALLAS/LIMEN denominator.

## SHA-256 checksums

```text
fb2da35543f3630b55bcd5796f49d7e64030f63557f29ea8fc1cf1ecf98ce149  draft/preprint.md
cb374e546b17f82b14fdd7465e78930202179a34d089708a567165bde7747458  dashboard/limen-dashboard-spec-v0.1.md
a694935e6f1f81e090df4e22f320231b0bfb55ed8e98c81502e05e0cacb687bb  papers/article-architecture-v0.1.md
6a080e2c85723ad7b6de1e762db6fc9345177e8d4a7a7ce2e7b4464adb401913  results/boost/limen-dashboard-paper-forge/methods-caption-export-audit-v1.5.tsv
277dd1efedf8d5f379b79d86bf2ea48de068f2254d43c39f56540d41975dc294  results/boost/limen-dashboard-paper-forge/source-ledger-renderer-consumption-v1.4.md
2f6de784cc8c3842f075e57bfa7d4014687b281ac874668a055cd7b4193122d5  results/boost/limen-dashboard-paper-forge/dashboard-api-bundle-gate-v1.4.tsv
86a06b23d77fd5666a0f161e6bf16634aca56390fa69e6d03ace8b4b598f515f  results/boost/limen-dashboard-paper-forge/static-dashboard-preview-gate-v1.4.tsv
```

## Next smallest publishability move

Run the same v1.5 audit after any PDF/figure-export script is added or changed. If a reviewer-facing PDF is produced, make the exporter consume `methods-caption-export-audit-v1.5.tsv` and fail closed when any audit row is not `PASS`.
