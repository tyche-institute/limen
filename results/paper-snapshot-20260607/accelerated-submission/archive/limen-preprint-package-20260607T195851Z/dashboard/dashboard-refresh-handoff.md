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
- `exports/taxonomy-heatmap.tsv`
- `exports/legal-uncertainty-matrix.tsv`
- `exports/public-link-source-check-notes.tsv`
- `exports/source-depth-ladder.tsv`
- `review/negative-results-table.tsv`
- `paper/paper-claim-register-v0.1.tsv`

## Required dashboard behavior

- Show 21 headline denominator rows.
- Show 7 non-denominator anchors/candidates separately.
- Never mix the frozen 21-lineage denominator with the live 33 / 25 post-FTC drift without a recomputation badge.
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
