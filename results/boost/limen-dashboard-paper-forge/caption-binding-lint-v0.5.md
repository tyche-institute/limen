# LIMEN caption binding lint v0.5

Updated UTC: 2026-06-18T18:45:00Z
Lane: `limen-dashboard-paper-forge`

## Purpose

Record the dashboard/article caption-binding patch for the sprint-critical LIMEN figures. This is a paper-readiness artifact, not a new evidence collection pass.

## Inputs

| input | role |
|---|---|
| `results/boost/limen-dashboard-paper-forge/figure2-5-7-denominator-binding-register-v0.4.tsv` | canonical denominator/caption lint register |
| `dashboard/limen-dashboard-spec-v0.1.md` | dashboard view and caption contract |
| `papers/article-architecture-v0.1.md` | manuscript architecture and figure plan |
| `results/dashboard-paper/status.md` | lane status tracker |

## Caption/prose lint results

| figure | required denominator language | patched location | claim ceiling |
|---|---|---|---|
| Figure 2 | live core `39 governed record refs / 29 unique lineages`; extended `44 / 34`; mechanical `35 / 27` provenance-only | dashboard View 2; article Figure 2 | workflow/taxonomy denominator only; not incidence, prevalence, completeness, or legal/security finding |
| Figure 5 | `21` collapsed publication-safe lineages; `15` high-confidence cap; `6` low-confidence cap; `6` translation-dependent | dashboard View 4; article Figure 5 | maturity/confidence ceiling only; not legal truth, prevalence, completeness, or country ranking |
| Figure 7 | default visible `21` lineages; projected sidecar `23` lineages | dashboard View 7; article Figure 7 | sidecar/threshold routing only; not product safety, exploit prevalence, or framework coverage |

## Negative/limitation record

No new collection, incident validation, legal conclusion, compliance conclusion, deployment claim, safety claim, country ranking, or fused GAIA/PALLAS/LIMEN denominator was added. The patch only binds captions and article architecture to the existing v0.4 denominator register.

## Observatory hook

The dashboard should expose the v0.4 denominator register as a tooltip/sidecar source for Figures 2, 5, and 7, with visible/default versus sidecar/projected denominators shown wherever the figure can be exported for manuscript use.

## Next smallest publishability move

Run sentence-level lint over the full manuscript draft/captions and reject or rewrite any sentence that silently upgrades routing counts into validated cases, completeness, prevalence, legal/compliance findings, product safety, deployment, country ranking, or a fused cross-observatory denominator.
