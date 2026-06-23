# LIMEN dashboard surface export contract v0.7

Lane: `limen-dashboard-paper-forge`  
Created UTC: 2026-06-18T19:45:00Z  
Scope: dashboard/paper parity preflight for canonical export paths after Figure 2/Figure 5/Figure 7 denominator lint.

## Why this artifact exists

The previous sprint passes fixed denominator grammar, but several dashboard/article surfaces still had path-name ambiguity: prose used map/cluster-style names while live exports use shorter canonical names. This contract converts that ambiguity into an explicit, machine-readable resolver table before any dashboard build or PDF export consumes the wrong file.

## Result

- Surfaces audited: 8.
- Canonical export surfaces ready: 8/8.
- Ambiguous/missing legacy aliases identified: 3.
- New collection performed: none.
- Claim promotion performed: none.

## Canonical resolver findings

| Surface | Canonical export | Legacy/ambiguous path state | Safe dashboard/paper reading |
| --- | --- | --- | --- |
| Figure 1 — Source-family coverage map | `results/dashboard/source-family-coverage.tsv` | missing_expected_alias_only | 15-row source-family saturation/claim-ceiling surface; use as map/table hook, not completeness or prevalence. |
| Figure 2 / Table 2 — Taxonomy heatmap | `results/dashboard/taxonomy-heatmap.tsv` | n/a | 39/29 core and 44/34 extended; legacy 35/27 is provenance only. |
| Figure 3 / Table 2 — Legal uncertainty matrix | `results/dashboard/legal-uncertainty-matrix.tsv` | n/a | Claim-ceiling matrix only; no legal compliance/guilt finding. |
| Figure 4 / Figure 7 related — Duplicate-review graph | `results/dashboard/duplicate-review-graph.tsv` | missing_expected_alias_only | 27-edge join-safety/QC graph; not recurrence evidence. |
| Figure 5 — Publication-safe evidence funnel | `results/dashboard/evidence-funnel.tsv` | n/a | 21 publication-safe lineages; confidence/translation bands are ceilings. |
| Figure 6 — Jurisdiction/language visibility map | `results/dashboard/jurisdiction-language-coverage.tsv` | missing_expected_alias_only | 12-row visibility surface with translation-review requirement; not country ranking. |
| Figure 7 — Security/agentic threshold ladder plus sidecar | `results/dashboard/security-threshold-ladder-panel.tsv; results/dashboard-paper/figure7-sidecar-consumption-matrix-v0.1.tsv` | n/a | 4 threshold rows; sidecar default 21 / projected 23 lineages only. |
| Supplementary Methods — Caption control register | `results/dashboard-paper/caption-control-register-v0.1.tsv` | n/a | Use as preflight lint source before PDF/export changes. |


## Observatory hook

Dashboard code and article export scripts should treat `dashboard-surface-export-contract-v0.7.tsv` as the resolver layer between view names and files. If a component asks for `results/dashboard/source-family-coverage-map.tsv`, `results/dashboard/jurisdiction-language-map.tsv`, or `results/dashboard/duplicate-cluster-graph.tsv`, the UI should redirect to the canonical export named in the contract and display the alias state as a data-quality note rather than silently failing or minting a new denominator.

## Reviewer-safe interpretation

This pass improves reproducibility and dashboard/paper parity only. It does not add incidents, promote rows, validate legal claims, or change denominator totals. The useful paper claim is methodological: LIMEN now distinguishes denominator grammar from export-path resolution, reducing the chance that a dashboard implementation or manuscript packager will accidentally consume a stale or missing surface.

## Next smallest publishability move

Use this contract as the preflight input for a static dashboard build or figure-export script. The build should fail closed when `canonical_exists != yes` and should warn, not infer, when an ambiguous legacy path is requested.
