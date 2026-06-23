# LIMEN release-card UI config v0.1

Generated: 2026-06-18T08:45:33Z
Lane: `limen-dashboard-paper-forge`

## Purpose

This artifact wires the existing dashboard release-card gate into a machine-readable UI contract. It is not a publication, upload, or dataset expansion. It tells a future dashboard renderer which subtitle, tooltip rule, checksum, and prohibited-reading warning must travel with each count-bearing chart.

## Source

- Release-card TSV: `results/boost/limen-dashboard-paper-forge/dashboard-release-card-2026-06-18T08-04-52Z.tsv`
- Release-card SHA-256: `47fe077ac1f923b3ac73589c91ee9d75222ad68bdc5ecbc9517eea7a3a6af096`

## View contract

| Dashboard view | Source rows | Subtitle / denominator label | Tooltip rule | Prohibited reading |
|---|---:|---|---|---|
| `source_family_saturation` | 15 | source-family rows; saturation/uncertainty, not completeness | Expose denominator, claim ceiling, uncertainty flag, and provenance pointer before any count is shown. | completeness, prevalence, legal guilt, compliance/certification/safety assurance, country ranking, or third-party endorsement |
| `taxonomy_heatmap` | 15 | core 39/29; sidecar 44/34; taxonomy support, not prevalence | Expose denominator, claim ceiling, uncertainty flag, and provenance pointer before any count is shown. | completeness, prevalence, legal guilt, compliance/certification/safety assurance, country ranking, or third-party endorsement |
| `evidence_tier_funnel` | 11 | 296 catalogued / 250 evidence-grade / 46 excluded / 21 publication-safe lineages where used | Expose denominator, claim ceiling, uncertainty flag, and provenance pointer before any count is shown. | completeness, prevalence, legal guilt, compliance/certification/safety assurance, country ranking, or third-party endorsement |
| `jurisdiction_language` | 12 | 34 jurisdictions broad; 12 reviewed-core non-English rows where panel used; no country ranking | Expose denominator, claim ceiling, uncertainty flag, and provenance pointer before any count is shown. | completeness, prevalence, legal guilt, compliance/certification/safety assurance, country ranking, or third-party endorsement |
| `legal_uncertainty` | 15 | uncertainty routing only; no compliance/liability conclusion | Expose denominator, claim ceiling, uncertainty flag, and provenance pointer before any count is shown. | completeness, prevalence, legal guilt, compliance/certification/safety assurance, country ranking, or third-party endorsement |
| `security_agentic_threshold` | 4 | 4 threshold rows; 11 security rows where described; not security prevalence | Expose denominator, claim ceiling, uncertainty flag, and provenance pointer before any count is shown. | completeness, prevalence, legal guilt, compliance/certification/safety assurance, country ranking, or third-party endorsement |
| `duplicate_review_graph` | 27 | 27 duplicate-review edges; 0 merge decisions; not proof all duplicates are absent | Expose denominator, claim ceiling, uncertainty flag, and provenance pointer before any count is shown. | completeness, prevalence, legal guilt, compliance/certification/safety assurance, country ranking, or third-party endorsement |

## Reviewer-safe implementation notes

- Show the subtitle/denominator label before or next to every count-bearing view.
- Do not substitute denominators across Figure 2, Figure 5, and Figure 7: 39/29 taxonomy support, 21 publication-safe lineages, and 4 threshold rows are distinct.
- Display source-family saturation and uncertainty, not completeness.
- Do not infer legal compliance, liability, official incident status, certification, safety assurance, prevalence, or country ranking from these views.
- Export-level checksums may be shown; row-level access-date/rights labels require a verified source-ledger join before display.

## Paper-readiness delta

The dashboard can now consume a versioned JSON contract rather than manually copying denominator and tooltip language. This reduces drift between the manuscript, SI exports, and any future interactive dashboard release.

## Claim boundary

No new collection, no upload/deposit/submission, no denominator change, no legal/compliance/certification/safety/prevalence claim, and no country ranking was made.
