# Dashboard / paper parity note — 2026-06-14

Date: 2026-06-14
Lane: `limen-dashboard-paper-forge`
Scope: bounded stabilization pass using local LIMEN artifacts only

## Purpose

This note freezes the publication-safe parity rule for LIMEN's dashboard-facing and paper-facing surfaces. The dashboard may expose multiple count-bearing surfaces, but the paper must only reuse the denominator that belongs to the specific view being cited.

## Live dashboard views that can feed the paper now

These views are locally materialized and already mapped to paper-safe roles:

1. `results/dashboard/source-family-coverage.tsv`
   - paper role: Figure 1 / source-family saturation map
   - safe use: declared family coverage, blocker visibility, thin-family posture

2. `results/dashboard/taxonomy-heatmap.tsv`
   - paper role: Figure 2 / taxonomy support heatmap
   - safe use: category-support unevenness, zero-seed guardrails, overlay-ready versus queue-only routing
   - count contract: `39 governed record refs / 29 unique lineages` core; `44 / 34` extended

3. `results/dashboard/legal-uncertainty-matrix.tsv`
   - paper role: Figure 3 / legal-uncertainty matrix
   - safe use: stronger-source needs and claim ceilings, not legal conclusions

4. `results/dashboard/duplicate-review-graph.tsv`
   - paper role: Figure 4 / duplicate-governance quality-control graph
   - safe use: join safety and non-recurrence discipline, not prevalence

5. `results/dashboard/evidence-funnel.tsv`
   - paper role: Figure 5 / publication-safe evidence-tier funnel
   - safe use: `21` collapsed publication-safe lineages with confidence overlays

6. `results/dashboard/jurisdiction-language-coverage.tsv`
   - paper role: Figure 6 / jurisdiction-language visibility map
   - safe use: multilingual asymmetry and translation burden, not rankings

7. `results/dashboard/authoritative-document-depth-facet.tsv`
   - paper role: Table A / authoritative document-depth facet
   - safe use: support-depth heterogeneity inside the authoritative package

8. `results/dashboard/public-sector-disclosure-comparison.tsv`
   - paper role: Table B / public-sector disclosure asymmetry comparison
   - safe use: heterogeneous disclosure surfaces, not procurement-proof or transparency ranking

9. `results/dashboard/security-threshold-ladder-panel.tsv`
   - paper role: Figure 8 / security-agentic threshold ladder
   - safe use: publication-bucket asymmetry and explicit gap visibility

10. `results/dashboard/attestation-trust-surface-readiness.tsv`
    - paper role: Figure 9 / attestation trust-surface readiness ladder
    - safe use: local-bundle provenance ceiling only

## Older downstream consumers that are stale or bounded

1. `results/boost/limen-dashboard-paper-forge/taxonomy-heatmap.tsv`
   - status: stale mechanical Figure 2 source
   - old contract: `35 visible rows / 27 lineages`
   - allowed use: only when explicitly labeled as the older mechanical source behind Figure 2
   - not allowed: present-tense dashboard or manuscript denominator

2. Any prose or sidecar that treats Figure 2 as a single refreshed `35 / 27` story
   - status: stale narrative shorthand
   - problem: collapses the live dashboard taxonomy consumer into the older boost-local mechanical source

3. Figure 7 authority-balance reuses that omit the warning stack
   - status: bounded legacy consumer, not a live denominator front door
   - allowed use: legacy single-state `21`-lineage panel only, with explicit warning that validator-backed sidecar states are not the default visible denominator

4. Any downstream consumer that infers paper counts from dashboard screenshots or cross-panel headline numbers
   - status: unsafe
   - problem: LIMEN has multiple parallel count scopes; screenshots are symptoms of surface mismatch, not authority sources

## Denominator-drift prevention rule

Before reusing any count-bearing LIMEN view in manuscript prose, captions, or reviewer response:

1. Name the exact source file.
2. Name the exact denominator class used by that file.
3. State whether the figure is core, extended, bounded sidecar, or legacy mechanical.
4. Do not borrow counts from another panel, screenshot, or boost-local helper artifact.

## Minimal denominator registry for this finish state

- Figure 2 core dashboard taxonomy: `results/dashboard/taxonomy-heatmap.tsv` -> `39 governed record refs / 29 unique lineages`
- Figure 2 extended live taxonomy surface: `results/dashboard/taxonomy-heatmap.tsv` -> `44 / 34`
- Figure 2 older mechanical source: `results/boost/limen-dashboard-paper-forge/taxonomy-heatmap.tsv` -> `35 / 27`
- Figure 5 publication-safe funnel: `results/dashboard/evidence-funnel.tsv` -> `21` publication-safe lineages
- Figure 7 bounded legacy authority-balance panel: `21` publication-safe lineages only; any higher sidecar projection stays non-default until deliberately promoted

## Bottom line

The live dashboard can feed the LIMEN paper now, but only view-by-view. The stable rule is not “one LIMEN count”; it is “one denominator per approved view, with the file path named every time.”
