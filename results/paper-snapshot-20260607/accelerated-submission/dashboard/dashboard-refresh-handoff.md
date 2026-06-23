# Dashboard refresh handoff

Use this accelerated handoff to refresh the public observatory without reopening discovery.

## Source bundle

Frozen source directory:

`results/paper-snapshot-20260607/`

Primary manifest:

`results/paper-snapshot-20260607/manifest.json`

## Tables to load

- `exports/cases.tsv`
- `exports/sources.tsv`
- `exports/authoritative-source-anchors.tsv`
- `exports/category-source-family-counts.tsv`
- `exports/evidence-funnel.tsv`
- `exports/duplicate-graph.tsv`
- `exports/taxonomy-heatmap.tsv` (frozen historical `31 / 23` taxonomy export; if any live Figure 2 / Table 2 narration is shown beside it, route through `results/boost/limen-boost-046/figure2-question-router.tsv` first and pair with `results/boost/limen-boost-058/taxonomy-snapshot-currentness-hold-register.tsv`)
- `exports/legal-uncertainty-matrix.tsv`
- `exports/public-link-source-check-notes.tsv`
- `exports/source-depth-ladder.tsv`
- `review/negative-results-table.tsv`
- `paper/paper-claim-register-v0.1.tsv`

## Required dashboard behavior

- Show 21 headline denominator rows.
- Show 7 non-denominator anchors/candidates separately.
- Never mix the frozen 21-lineage denominator with the live `35 / 27` Figure 2 duplicate/taxonomy routing bundle or the separate Figure 7 `21 / 23 / 25` denominator stack without an explicit recomputation/currentness badge.
- Never present the frozen `exports/taxonomy-heatmap.tsv` as the current local atlas taxonomy state; if live Figure 2 / Table 2 wording is needed, add an explicit currentness badge and cite `results/boost/limen-boost-046/figure2-question-router.tsv`, `results/boost/limen-boost-060/figure2-refresh-bundle-contract.tsv`, and the shard-058 hold register.
- If live Figure 7 wording is needed, keep the visible 21-lineage panel separate from the projected 23-lineage sidecar by routing through `results/dashboard-paper/figure7-sidecar-consumption-matrix-v0.1.tsv` and `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-014` rather than improvising denominator language from the frozen snapshot alone.
- Render confidence cap and claim ceiling beside case title.
- Render source-family and evidence-tier filters independently.
- Show negative results as a first-class table, not as hidden notes.
- Show public-link barriers without encouraging bypass.

## Figure assets

Use the PNG/SVG files in:

`accelerated-submission/figures/`

## Public copy rule

Primary public line:

`LIMEN is a public-source observatory for structuring AI edge-case evidence under explicit claim ceilings.`

Avoid:

- `incident database`
- `prevalence map`
- `AI harm ranking`
- `legal/compliance classifier`
- `complete atlas`
