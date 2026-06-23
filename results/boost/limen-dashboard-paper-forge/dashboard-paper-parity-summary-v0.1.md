# LIMEN Dashboard/Paper Parity Pack v0.1

Generated UTC: 2026-06-18T13:48:24Z
Lane: `limen-dashboard-paper-forge`

## What changed

This pass converts the current review-candidate ledger into manuscript/dashboard-ready denominator surfaces. The input ledger contains `55725` non-self CPU-mined public-source review candidates. The outputs are deliberately cautious: they show review routing, source-family proxy coverage, query/taxonomy proxy coverage, and claim ceilings; they do not assert incident truth, legal status, compliance, safety, deployment, or prevalence.

## Outputs

- `evidence-tier-funnel-v0.1.tsv` — Figure 2 denominator/routing funnel.
- `source-family-coverage-map-v0.1.tsv` — Figure 1 source-family saturation proxy.
- `review-priority-routing-v0.1.tsv` — priority counts and sample IDs for review planning.
- `claim-ceiling-summary-v0.1.tsv` — limitation/caption grammar for hostile-reviewer pass.
- `taxonomy-query-proxy-heatmap-v0.1.tsv` — query-level proxy for taxonomy heatmap; not final taxonomy mapping.
- `dashboard-paper-parity-manifest-v0.1.json` — checksums and ingestion metadata.

## Paper-readiness delta

The prior dashboard and article specs defined views but did not provide first view data. This pack gives the dashboard and paper a shared denominator surface for Figure 1 and Figure 2 and makes the review ceiling explicit. It directly supports the sprint directive to patch Figure 2/Figure 5/Figure 7 denominator discipline and dashboard/paper parity.

## Reviewer-safe interpretation

- Counts are counts of review candidates, not verified incidents.
- `P1_official_or_regulator_review`, `P2_article_relevance_review`, and `P3_candidate_review` are routing priorities, not confidence grades.
- Source-family labels are proxies inferred from paths/shards/queries and should be replaced or validated by a final source taxonomy before strong claims.
- The current review-candidate ledger yields `0` validated/publishable claims by itself; promotion must link to reviewed-core hardening/adjudication artifacts.

## Observatory hook

Dashboard panels can consume the TSV files directly:

1. Funnel/Sankey: `stage`, `count`, `claim_ceiling`, `uncertainty_flags`.
2. Source-family saturation: `source_family_proxy`, `count`, `share_of_review_candidates`.
3. Query heatmap: `query_or_taxonomy_proxy`, `count`, `share`.
4. Limitation panel: `claim_ceiling`, `count`, `reviewer_safe_use`.

## Next smallest publishability move

Link these denominator surfaces to reviewed-core hardening artifacts and produce a second funnel that separates: review candidates → source-reviewed rows → hardened core cases → final adjudication rows → manuscript examples.
