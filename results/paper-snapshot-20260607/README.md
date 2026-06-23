# LIMEN paper snapshot 20260607

This directory freezes the Route A paper package for:

`LIMEN: A Public-Source Observatory for AI Edge Cases`

The paper claim is deliberately narrow:

> LIMEN demonstrates a reproducible public-source method for structuring heterogeneous AI edge-case evidence under explicit claim ceilings.

This is a methods/data-observatory snapshot, not an incident-prevalence, country-ranking, illegality, compliance, or certification dataset.

## Frozen denominator

The headline denominator is the synchronized `limen-boost-011` publication-safe aggregate:

- 21 publication-safe lineages
- 29 reviewed normalized rows before stable duplicate collapse
- 7 derivative queue rows excluded from lineage counts
- 15 high confidence-cap lineages
- 6 low confidence-cap lineages
- 6 translation-dependent lineages

Later local controls now expose a wider live duplicate/taxonomy surface after DoNotPay and Workado authoritative-candidate additions. This snapshot preserves those rows as non-denominator anchor additions and records the drift explicitly in `provenance/taxonomy-post-ftc-drift-register.tsv`.

## Core exports

- `exports/cases.tsv`: dashboard-ready case table with public IDs and denominator role.
- `stable-public-id-alias-map.tsv`: public-facing IDs with old local IDs as aliases.
- `exports/sources.tsv`: compact source table for the paper artifact.
- `exports/evidence-funnel.tsv`: frozen evidence-tier/confidence funnel.
- `exports/duplicate-graph.tsv`: duplicate/collision graph.
- `exports/taxonomy-heatmap.tsv`: frozen historical taxonomy heatmap from the last synchronized dashboard-paper forge pass. Current live Figure 2 / Table 2 claims should route through `results/boost/limen-boost-046/figure2-question-router.tsv` first, then `results/boost/limen-boost-058/taxonomy-snapshot-currentness-hold-register.tsv` and `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-001..CCR-002`, rather than treating this snapshot export as the latest local atlas state.
- `exports/legal-uncertainty-matrix.tsv`: legal uncertainty/caution matrix.
- `exports/public-link-audit.tsv`: public retrieval audit copied into the snapshot.
- `exports/caption-claim-ceiling-registry.tsv`: caption and claim-ceiling controls.

## Additions held outside the headline denominator

- `LIMEN-RI-000001`: Springer / Intensive Care Medicine direct retraction notice about unverifiable references and author-stated generative-AI reference conversion.
- `LIMEN-FTC-000001`: FTC DoNotPay complaint/final-order package, official-text candidate, sidecar-first.
- `LIMEN-FTC-000002`: FTC Workado / Content at Scale AI detector-accuracy package, official-text candidate, detector-governance sidecar.
- `LIMEN-PS-000001`: Danish Datatilsynet SU AI decision page, public-sector governance anchor, not a harm case.

These rows may be used for methods, source-depth, appendix, or dashboard-sidecar discussion. They do not silently change the main 21-lineage paper denominator.

## Boundary

Use public sources only. Do not bypass paywalls, access controls, robots exclusions, 403s, or rate limits. Do not state legal conclusions, illegality findings, prevalence claims, compliance/certification claims, or unbounded product-effectiveness claims. Separate complaint allegations, final orders, settlement posture, regulator summaries, court-facing records, publisher notices, and media leads.
