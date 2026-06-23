---
title: "LIMEN Paper Snapshot 20260607"
subtitle: "Route A freeze for LIMEN: A Public-Source Observatory for AI Edge Cases"
date: "2026-06-07"
author: "LIMEN project"
geometry: margin=0.8in
fontsize: 10pt
---

# Executive Summary

This report summarizes the frozen Route A paper package in `results/paper-snapshot-20260607/`.

Working title:

`LIMEN: A Public-Source Observatory for AI Edge Cases`

Central claim:

`LIMEN demonstrates a reproducible public-source method for structuring heterogeneous AI edge-case evidence under explicit claim ceilings.`

The paper is framed as a methods/data-observatory paper, not an incident-prevalence paper. The contribution is the research infrastructure: evidence tiers, source-family saturation, duplicate control, legal uncertainty, translation caution, residual taxonomy, public-link limitations, and dashboard-ready observability.

# Frozen Denominator

The headline paper denominator is frozen on the synchronized `limen-boost-011` publication-safe aggregate.

| Quantity | Value |
|---|---:|
| Publication-safe lineages | 21 |
| Raw normalized rows reviewed before collapse | 29 |
| Derivative queue rows excluded | 7 |
| High confidence-cap lineages | 15 |
| Low confidence-cap lineages | 6 |
| Translation-dependent lineages | 6 |

Later local controls now record a wider live duplicate/taxonomy surface of 35 visible governed rows / 27 unique lineages under the current Figure 2 / Table 2 routing bundle, while Figure 7 separately remains a bounded `21 / 23 / 25` denominator stack rather than a flat live count. This report does not silently adopt those wider live packages. It treats the newer FTC, Springer, Datatilsynet, and later taxonomy-sidecar growth as non-denominator anchors, sidecars, or live-routing context unless a synchronized recomputation is performed.

# Public IDs

The snapshot creates stable public-facing IDs and keeps old local IDs as provenance aliases. This prevents reviewer-visible collision hazards from bare IDs such as `LIMEN-000001`, which are reused across local shards.

Prefix roles:

| Prefix | Role |
|---|---|
| `LIMEN-AUTH` | Authoritative regulator, enforcement, court-facing, or official-source rows |
| `LIMEN-SEC` | Security and agentic-control rows |
| `LIMEN-ML` | Multilingual and language-dependent rows |
| `LIMEN-RI` | Research-integrity source-depth anchors |
| `LIMEN-FTC` | FTC sidecars and complex official candidates |
| `LIMEN-PS` | Public-sector governance anchors |

Core mapping file:

`stable-public-id-alias-map.tsv`

# Dashboard Export Bundle

Core dashboard-consumable files:

| Export | Purpose |
|---|---|
| `exports/cases.tsv` | Case table with public IDs, source families, evidence tiers, confidence caps, and denominator roles |
| `exports/sources.tsv` | Compact source table for paper/dashboard use |
| `exports/authoritative-source-anchors.tsv` | Paper-facing public source anchors |
| `exports/evidence-funnel.tsv` | Evidence-tier and confidence-cap funnel |
| `exports/duplicate-graph.tsv` | Duplicate/collision graph |
| `exports/taxonomy-heatmap.tsv` | Frozen historical taxonomy heatmap from the last synchronized snapshot pass; current live Figure 2 / Table 2 claims should route through `results/boost/limen-boost-046/figure2-question-router.tsv` first, then `results/boost/limen-boost-058/taxonomy-snapshot-currentness-hold-register.tsv` plus `exports/caption-claim-ceiling-registry.tsv:CCR-001..CCR-002` |
| `exports/legal-uncertainty-matrix.tsv` | Stronger-source-needs and legal-caution matrix |
| `exports/public-link-audit.tsv` | Public-link retrieval audit |
| `exports/public-link-source-check-notes.tsv` | Source-check notes for important anchors and barriers |
| `exports/source-depth-ladder.tsv` | Figure-ready ladder showing why T3 is not uniform |
| `exports/caption-claim-ceiling-registry.tsv` | Caption and claim-ceiling controls |

The JSON manifest is `manifest.json`.

# Non-Denominator Anchors

These rows are included for paper value but do not change the headline 21-lineage denominator.

| Public ID | Role | Claim ceiling |
|---|---|---|
| `LIMEN-RI-000001` | Springer direct publisher/editor notice anchor | Notice-bounded statements about unverifiable references, peer-review-policy failure, and author-stated generative-AI reference conversion |
| `LIMEN-RI-000002` | Springer book/chapter direct notice appendix comparator | Notice-bounded reference-validity statements; no generative-AI causation unless directly sourced |
| `LIMEN-FTC-000001` | DoNotPay non-finance official AI-claim sidecar | FTC complaint/final-order posture only; no judicial unauthorized-practice or product-truth conclusion |
| `LIMEN-FTC-000002` | Workado / Content at Scale AI detector-governance sidecar | FTC complaint/final-order posture only; no general detector-validity conclusion |
| `LIMEN-PS-000001` | Danish Datatilsynet SU AI public-sector governance anchor | Governance/source-depth anchor only; not a harm case, legality finding, or compliance/certification proof |
| `LIMEN-FTC-000003` | Rytr complex-posture candidate | Hold for full complaint/order/set-aside chronology |
| `LIMEN-FTC-000004` | Air.ai document-read-pending candidate | Hold until complaint/order reading establishes exact AI role |

# Figure Set

This frozen Route A snapshot still preserves the older five-figure package below, but live manuscript, dashboard, reviewer-response, or thesis reuse should now route through the current shared visual spine rather than treating the frozen numbering as authoritative. The current live spine is described in `results/paper-snapshot-20260607/paper/figure-plan-v0.1.md`, `results/dashboard-paper/figure-table-priority-register-v0.1.tsv`, and `results/dashboard-paper/caption-control-register-v0.1.tsv`.

Frozen Route A figure package:

| Figure | Title | Input |
|---|---|---|
| 1 | Source-family observability map | `exports/source-families.tsv`, `exports/category-source-family-counts.tsv` |
| 2 | Evidence-tier funnel with confidence caps | `exports/evidence-funnel.tsv`, `exports/cases.tsv` |
| 3 | Duplicate/collision graph | `exports/duplicate-graph.tsv`, `stable-public-id-alias-map.tsv` |
| 4 | Taxonomy heatmap with residual and zero-seed rows | `exports/taxonomy-heatmap.tsv`, `exports/legal-uncertainty-matrix.tsv`, `results/boost/limen-boost-046/figure2-question-router.tsv`, `results/boost/limen-boost-058/taxonomy-snapshot-currentness-hold-register.tsv` |
| 5 | Source-depth ladder showing why T3 is not uniform | `exports/source-depth-ladder.tsv`, `exports/authoritative-source-anchors.tsv` |

Current live shared-package figure order for bounded reuse:

| Live figure | Title | Required routing/control bundle |
|---|---|---|
| 1 | Source-family saturation map | `results/source-map/source-family-figure1-register-v0.1.tsv`; `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-008` |
| 2 | Taxonomy heatmap | `results/boost/limen-boost-046/figure2-question-router.tsv`; `results/boost/limen-boost-060/figure2-refresh-bundle-contract.tsv`; `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-001..CCR-002` |
| 3 | Legal uncertainty matrix | `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-019` |
| 4 | Duplicate-review quality-control graph | `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-018` |
| 5 | Publication-safe evidence-tier funnel | `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-005` |
| 6 | Jurisdiction/language visibility map | `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-016`; `results/multilingual/multilingual-publication-routing-matrix-v0.1.tsv` |
| 7 | Authority-balance composition panel | `results/dashboard-paper/figure7-sidecar-consumption-matrix-v0.1.tsv`; `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-014` |
| 8 | Authority-geography concentration panel | `results/dashboard-paper/caption-control-register-v0.1.tsv:CCR-011` |

Each figure needs a paired "forbidden overread" caption note. Counts are observability counts, not prevalence estimates.

# Negative Results

The negative-results table is central, not decorative. It shows that public evidence sometimes supports only a bounded claim ceiling.

Selected negative results:

| Record | Visible | Not safe to infer |
|---|---|---|
| EEOC iTutorGroup | EEOC lawsuit and settlement summaries | Open court-originating complaint/decree text or judicial merits finding |
| Nate | DOJ charging-stage page and indictment PDF | Guilt, liability, disposition, or hidden-human prevalence |
| NEJM | DOI/retraction metadata | Retraction rationale from blocked publisher notice |
| SEC Delphia/Global Predictions | Prior captured order metadata and press release | Current shell retrieval from this host; no bypass |
| FTC DoNotPay/Workado | Public pages and locally represented PDFs | Frictionless source surface or generalized sector claims |
| Helsinki/Amsterdam public-sector traces | Register/procurement signals | Exact contract proof, deployment impact, legality, or completeness |
| Datatilsynet SU AI | Official Danish decision page | Harm, illegality, compliance, certification, or failed deployment |

Full table:

`review/negative-results-table.tsv`

# Reliability Status

The snapshot includes a coding protocol and an internal two-pass dry-run:

- `review/coding-protocol-v0.1.md`
- `review/reliability-audit-v0.1.tsv`

The dry-run is not inter-rater reliability. A submission-ready reliability section should either add a true second-coder audit or report the current file as a single-team adjudication audit without kappa or alpha statistics.

# Claim Boundary

Allowed:

- LIMEN structures heterogeneous public-source evidence under explicit claim ceilings.
- The frozen package contains 21 publication-safe lineages.
- The dashboard exports make evidence limits inspectable.
- Source family and document depth shape what claims can responsibly be made.

Not allowed:

- AI harms are increasing.
- The atlas is complete.
- A country, company, sector, or source family is worse.
- Complaint allegations are final findings.
- Official records automatically support legal conclusions.
- A row proves compliance, certification, legality, safety, efficacy, or prevalence.

# Main Source Links

- FTC DoNotPay: <https://www.ftc.gov/legal-library/browse/cases-proceedings/donotpay>
- FTC Workado / Content at Scale AI: <https://www.ftc.gov/legal-library/browse/cases-proceedings/2323092-content-scale-ai>
- Springer ICM retraction notice: <https://link.springer.com/article/10.1007/s00134-024-07752-6>
- Springer book/chapter notice PDF: <https://link.springer.com/content/pdf/10.1007/978-981-97-9914-5_1.pdf>
- Danish Datatilsynet SU AI decision: <https://www.datatilsynet.dk/afgoerelser/afgoerelser/2024/jun/udvikling-af-ai-loesning-til-sagsbehandling-paa-su-omraadet>

# Next Submission Steps

1. Run a true second-coder audit or keep the reliability dry-run labeled as non-inter-rater.
2. Decide whether DoNotPay remains sidecar-only or triggers a synchronized denominator recomputation.
3. Keep Workado appendix/detector-governance unless a bounded detector branch is deliberately opened.
4. Add one non-Springer direct research-integrity notice only if publisher-diversity language is needed.
5. Draft the paper around the five figures and the negative-results table.
