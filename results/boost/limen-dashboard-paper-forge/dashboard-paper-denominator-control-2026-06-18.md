# LIMEN Dashboard/Paper Denominator Control — hostile reviewer artifact

Generated: 2026-06-18T03:52:36Z
Lane: `limen-dashboard-paper-forge`
Project root: `/srv/tyche/projects/limen-ai-edge-case-atlas`

## Why this artifact exists

The current sprint asks LIMEN to patch methods/data article surfaces from the 2026-06-14 dashboard-paper patch plan, especially Figure 2/Figure 5/Figure 7 denominator discipline and dashboard/paper parity. This file records the reconciliation without changing the dataset or reopening crawling.

## Provenance used

| Local artifact | Role |
|---|---|
| `/etc/tyche-factory/current-publication-sprint.md` | Sprint authority and LIMEN-specific patch target. |
| `publication-goal-card-current.md` | Project win condition and claim boundaries. |
| `results/boost/limen-dashboard-paper-forge/dashboard-paper-parity-audit-2026-06-19.md` | Existing parity audit and exact denominator list. |
| `results/boost/limen-dashboard-paper-forge/figure-generation-si-packaging-2026-06-19.md` | Generated figure/SI package verification. |
| `results/boost/limen-dashboard-paper-forge/si-package/si-package-manifest.json` | SI bundle source-file manifest. |
| `draft/preprint-v0.3-f1000.md` and `draft/preprint.md` | Manuscript surfaces carrying caption discipline. |

No external collection was performed in this cycle.

## Denominator map

| Surface | Denominator | Correct use | Reviewer risk if mishandled |
|---|---:|---|---|
| Evidence-grade records | 250 | analysis base after exclusions | mistaken for total universe |
| Total catalogued | 296 | gross catalogue including excluded media-only records | mixed with evidence-grade base |
| Media-only/excluded | 46 | exclusion transparency | accidentally cited as claim support |
| Source-link coverage | 233/250 (93.2%) | source-link availability | mistaken for full verification |
| Evidence tiers | 157 T3 / 82 T2 / 11 T1 | authority/evidence balance | treated as truth hierarchy or legal finding |
| Figure 2 taxonomy core | 39 record refs / 29 lineages | taxonomy support | mistaken for case prevalence |
| Figure 2 extended sidecar | 44/34 | labeled sidecar only | silently replacing core denominator |
| Figure 5 publication-safe lineages | 21 | evidence maturity / publication ceiling | summed with taxonomy rows |
| Jurisdiction/language broad surface | 34 jurisdictions | coverage burden | country ranking |
| Reviewed-core non-English rows/leads | 12 | language review burden | legal/policy claim from MT alone |
| Figure 7 security threshold ladder | 4 rows | bounded threshold logic | security prevalence claim |
| Security seed | 11 rows | public security seed breadth where explicitly named | fused with Figure 7 ladder |
| Figure 8 duplicate review | 27 edges / 0 merges | dedupe transparency | proof no duplicates remain |

## Required caption/control text

Figure 2, Figure 5, and Figure 7 carry different denominators — 39/29 taxonomy support, 21 publication-safe lineages, and 4 threshold rows respectively — and these counts are not interchangeable.

## Dashboard implementation hook

Every count-bearing dashboard card should expose:

- denominator class;
- source export path;
- record/lineage/source IDs where applicable;
- evidence tier or authority class;
- uncertainty flag;
- claim ceiling;
- manuscript surface consuming the card.

## Article use

This artifact strengthens:

- Methods: dashboard/paper parity and evidence-tiered processing.
- Results: taxonomy heatmap, evidence funnel, jurisdiction/language visibility, security threshold ladder.
- Limitations: public-source-only scope, legal uncertainty, source-family gaps, duplicate-review incompleteness.
- SI/reproducibility: trace from dashboard TSVs to SI package and figure files.

## Negative result / caution

No new source-family gap was closed in this cycle. The useful result is control-layer hardening: fewer ways for a hostile reviewer to accuse LIMEN of denominator drift, fused denominators, or dashboard/manuscript mismatch.
