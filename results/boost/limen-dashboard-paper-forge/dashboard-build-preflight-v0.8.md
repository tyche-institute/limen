# LIMEN dashboard build preflight v0.8

Lane: `limen-dashboard-paper-forge`  
Generated UTC: 2026-06-18T20:20:00Z  
Scope: fail-closed preflight for local dashboard/API/static-preview rebuild after the v0.7 dashboard surface export contract.

## Verdict

- v0.7 contract canonical surfaces present now: `8/8` PASS, `0` FAIL.
- UI release config fail-closed check: `7` PASS / `0` FAIL.
- API bundle gate: `7` PASS / `0` FAIL; output `dashboard/limen-dashboard-api-bundle-v0.1.json` SHA-256 `b39456396a449bd43aea6ab6b785cbfd478afebdc034df24ee335055f39b18e4`.
- Static preview gate: `7` PASS / `0` FAIL; output `dashboard/static-dashboard-preview-v0.1.html` SHA-256 `1208a7cf48cb84c644cfcab8242c0410e31716374f664b403e8707fb158fe0e8`.
- Machine-readable preflight table: `results/boost/limen-dashboard-paper-forge/dashboard-build-preflight-v0.8.tsv`.

## What changed

Ran the existing local fail-closed dashboard checks and rebuilt the offline API bundle and static preview. This converts the v0.7 resolver into an executable package preflight: canonical exports must exist; renderable views must match configured row counts and SHA-256 hashes; denominator subtitles, claim boundaries, tooltip provenance fields, and prohibited-reading warnings must remain present.

## Surface findings

| Surface | Export state | Binding state | Safe reading |
|---|---|---|---|
| `FIG1_SOURCE_FAMILY` | PASS (`results/dashboard/source-family-coverage.tsv`) | rendered_or_linted | 15-row source-family saturation/claim-ceiling surface; use as map/table hook, not completeness or prevalence. |
| `FIG2_TAXONOMY` | PASS (`results/dashboard/taxonomy-heatmap.tsv`) | rendered_or_linted | 39/29 core and 44/34 extended; legacy 35/27 is provenance only. |
| `FIG3_LEGAL_UNCERTAINTY` | PASS (`results/dashboard/legal-uncertainty-matrix.tsv`) | rendered_or_linted | Claim-ceiling matrix only; no legal compliance/guilt finding. |
| `FIG4_DUPLICATE_REVIEW` | PASS (`results/dashboard/duplicate-review-graph.tsv`) | rendered_or_linted | 27-edge join-safety/QC graph; not recurrence evidence. |
| `FIG5_PUBLICATION_FUNNEL` | PASS (`results/dashboard/evidence-funnel.tsv`) | rendered_or_linted | 21 publication-safe lineages; confidence/translation bands are ceilings. |
| `FIG6_JURISDICTION_LANGUAGE` | PASS (`results/dashboard/jurisdiction-language-coverage.tsv`) | rendered_or_linted | 12-row visibility surface with translation-review requirement; not country ranking. |
| `FIG7_SECURITY_THRESHOLD` | PASS (`results/dashboard/security-threshold-ladder-panel.tsv; results/dashboard-paper/figure7-sidecar-consumption-matrix-v0.1.tsv`) | rendered_or_linted | 4 threshold rows; sidecar default 21 / projected 23 lineages only. |
| `CAPTION_CONTROL` | PASS (`results/dashboard-paper/caption-control-register-v0.1.tsv`) | lint_source_only_not_dashboard_view | Use as preflight lint source before PDF/export changes. |

## Negative evidence / limitation

The v0.7 contract has eight surfaces, while the interactive/static dashboard release config renders seven count-bearing views. `CAPTION_CONTROL` remains a Supplementary Methods lint source, not a dashboard chart. This is acceptable for the current package but should stay explicit so the UI does not silently turn a caption register into a count-bearing visualization.

Legacy aliases remain intentionally unresolved as files: `source-family-coverage-map.tsv`, `jurisdiction-language-map.tsv`, and `duplicate-cluster-graph.tsv` are recorded as missing expected aliases. The safe implementation is visible redirect/logging to canonical exports, not copying or minting new denominators.

## Claim boundary

This preflight verifies local package integrity and dashboard/paper parity only. It performs no new collection, upload, deposit, or public release and supports no completeness, prevalence, legal guilt/compliance/certification, safety, deployment, country-ranking, source-truth, third-party endorsement, or fused GAIA/PALLAS/LIMEN denominator claim.

## Observatory hook

Use `dashboard-build-preflight-v0.8.tsv` as the dashboard build gate summary. A future dashboard renderer should fail closed if any canonical export is missing or if UI/API/static gates report a row-count/SHA/subtitle/claim-boundary/prohibited-reading mismatch. Caption-control remains a lint-only package input.

## Next smallest publishability move

Patch the dashboard spec and article architecture to name this v0.8 preflight as the required build/package gate before any PDF, static preview, or interactive dashboard refresh.
