# Figure 2 denominator stabilization — 2026-06-14

Date: 2026-06-14
Lane: `limen-dashboard-paper-forge`
Status: stale-data warning plus authoritative denominator freeze

## Visible issue being stabilized

The dashboard or other public-facing LIMEN surfaces can show larger high-level counts than the manuscript-facing Figure 2 or Table 2 consumers. This is not, by itself, an error. It reflects different allowed denominator classes.

The problem appears when later prose silently treats those larger dashboard-facing counts as if they were the same thing as the manuscript-facing Figure 2 taxonomy denominator.

## Authoritative denominators and where each is allowed

| Consumer | Authority file | Authoritative denominator | Allowed use | Not allowed |
|---|---|---:|---|---|
| Figure 2 / Table 2 live dashboard taxonomy core | `results/dashboard/taxonomy-heatmap.tsv` | `39 governed record refs / 29 unique lineages` | Main manuscript routing language for taxonomy support | Prevalence or completeness claims |
| Figure 2 / Table 2 live dashboard taxonomy extended surface | `results/dashboard/taxonomy-heatmap.tsv` | `44 governed record refs / 34 unique lineages` | Explicitly labeled extended dashboard surface or sidecar explanation | Default manuscript denominator without label |
| Figure 2 older mechanical source | `results/boost/limen-dashboard-paper-forge/taxonomy-heatmap.tsv` | `35 visible rows / 27 lineages` | Historical/mechanical figure provenance only | Present-tense “current Figure 2 count” |
| Figure 5 publication-safe funnel | `results/dashboard/evidence-funnel.tsv` | `21 publication-safe lineages` | Evidence-maturity and publication-ceiling discussion | Taxonomy denominator or public-surface headline substitute |
| Figure 7 bounded legacy authority-balance panel | bounded legacy panel family | `21 publication-safe lineages` | Legacy authority-balance panel with explicit warning stack | Replacement for Figure 2 or proof of a larger stable core |

## Stabilization decision

1. Figure 2 for manuscript and reviewer-facing prose is frozen to the live dashboard taxonomy consumer in `results/dashboard/taxonomy-heatmap.tsv`.
2. The older boost-local `35 / 27` file is not repaired into a new current count here. It remains a mechanical source with an explicit stale-data warning.
3. The larger `44 / 34` live surface may be mentioned only as an extended dashboard state, not as the unqualified paper denominator.
4. The `21` publication-safe lineage denominator belongs to Figure 5 and related publication-safe discussion, not to Figure 2.

## Safe wording rule

Use wording like this:

- “Under the live dashboard taxonomy contract, Figure 2 is grounded in `39 governed record refs / 29 unique lineages`, with a larger `44 / 34` extended live surface kept separate.”
- “The older mechanical Figure 2 source still materializes `35 visible rows / 27 lineages` and should be treated as legacy figure provenance, not as the current manuscript denominator.”

Avoid wording like this:

- “LIMEN has X taxonomy cases” without naming the surface.
- “Figure 2 now shows the larger dashboard count” unless the exact extended surface is named and bounded.
- Any claim inferred from screenshot numerals alone.

## Why the public surface can look larger

Some LIMEN surfaces count governed record references or extended reviewed/dashboard states, while the manuscript uses a narrower figure-specific consumer. A bigger dashboard headline therefore does not automatically mean the paper is stale; it means the paper and dashboard are doing different jobs.

## Required warning to keep with Figure 2

Whenever Figure 2 or Table 2 is reused, keep this warning visible in some form:

“Figure 2 uses the live dashboard taxonomy consumer (`39 / 29` core; `44 / 34` extended) while the older mechanical heatmap source still materializes `35 / 27`. These scopes are not interchangeable.”

## Finish-state conclusion

Figure 2 is stabilized for publication by freezing the manuscript denominator to the live dashboard taxonomy consumer and quarantining the older mechanical file as legacy/stale provenance rather than silently upgrading or silently discarding it.
