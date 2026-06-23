# LIMEN Figure 2 / Figure 5 / Figure 7 denominator binding audit v0.4

Generated UTC: 2026-06-18T16:21:39Z
Lane: `limen-dashboard-paper-forge`
Sprint target: patch the methods/data article surfaces from the 2026-06-14 dashboard-paper patch plan, especially Figure 2/Figure 5/Figure 7 denominator discipline and dashboard/paper parity.

## Audit result

This cycle did not reopen crawling or broaden the corpus. It binds the three sprint-critical figure surfaces to exact dashboard sources, row counts, checksums, denominator contracts, and manuscript-safe claim ceilings.

| Figure | Canonical source | Current denominator contract | Manuscript-safe use | Forbidden overread |
|---|---|---|---|---|
| Figure 2 taxonomy heatmap | `results/dashboard/taxonomy-heatmap.tsv` | 15 category rows; live core `39 governed record refs / 29 unique lineages`; live extended `44 / 34`; older mechanical `35 / 27` stays legacy/provenance only. | Category-support unevenness, zero-seed visibility, overlay/boxed-comparator routing, and source-authority fragility. | Incidence, completeness, absence, prevalence, legal/security finding, or a fused live/mechanical denominator. |
| Figure 5 evidence funnel | `results/dashboard/evidence-funnel.tsv` | 21 collapsed publication-safe lineages: T3 authoritative `14`, T3 direct-URL-resolved `1`, T1 single-public-source `6`; confidence cap high `15`, low `6`; translation-dependent `6`. | Publication-safe maturity funnel after lineage-safe joins, with confidence and translation ceilings. | Equal-weight evidence strength, prevalence, completeness, legal truth, or jurisdiction/language counts merged into funnel denominator. |
| Figure 7 security threshold / authority-balance sidecar | `results/dashboard/security-threshold-ladder-panel.tsv` plus `results/dashboard-paper/figure7-sidecar-consumption-matrix-v0.1.tsv` | Threshold ladder has `3` current-ceiling/core rows, `6` appendix-upgrade rows, `1` limitations-upgrade row, `1` explicit gap row; authority-balance consumer remains default visible `21` lineages with projected `23`-lineage sidecar only. | Security/agentic route thresholds and sidecar-visible authority-balance transport. | Treating 23-lineage projection as default live panel, stripping singleton/collision warnings, or claiming product safety/exploit prevalence/framework coverage. |

## Machine-readable companion

`results/boost/limen-dashboard-paper-forge/figure2-5-7-denominator-binding-register-v0.4.tsv`

## Provenance and checksums

| Key | Path | Rows | SHA-256 |
|---|---|---:|---|
| figure2_taxonomy | `results/dashboard/taxonomy-heatmap.tsv` | 15 | `c0c9db0ed86acdf4f9910bd9e78ff03fae52303150bf5b62217954f721fdff75` |
| figure5_funnel | `results/dashboard/evidence-funnel.tsv` | 11 | `866475937cae0d4103b2adb4052be18cf5afac0352b34ec3df1232e9c844b499` |
| figure7_threshold | `results/dashboard/security-threshold-ladder-panel.tsv` | 4 | `c989a5509d9ea6337312231e40ab3f6324608d12aa2c6cd6b4c0aa02794ff2e1` |
| figure7_sidecar | `results/dashboard-paper/figure7-sidecar-consumption-matrix-v0.1.tsv` | 3 | `15860b3ad8cbd2879d586602bd939cc6a1150c051c33dd1827a95c3a51d82859` |
| figure_register | `results/dashboard-paper/figure-table-priority-register-v0.1.tsv` | 16 | `02ac4d9f5bf0529fddcc8fb2c4e134e493aa8d1823f997767096c0fd4ea340e9` |
| patch_plan | `results/dashboard-paper/limen-methods-data-article-patch-plan-2026-06-14.md` | n/a | `f4d2bf66db6cec453b20b898ac4fec547efaf52054170ac74fdd864250cedba5` |
| preprint | `draft/preprint.md` | n/a | `ca123748d75c40339163c64dd6f6884a80173af1ef97cd0fc1915e27739bf059` |


## Observability hooks

- Dashboard should expose a denominator-stack tooltip for each figure rather than only a visible count.
- Figure 2 needs badges for `zero_seed_local_gap`, `overlay_ready_*`, `boxed_*`, and `queue_or_methods_guardrail` rows.
- Figure 5 needs a banner that the denominator is collapsed publication-safe lineages, not raw records or candidate leads.
- Figure 7 needs a visible/default versus sidecar/projected switch, with the 21/23/broader-family split never collapsed into one denominator.

## Paper-readiness delta

The package now has a single reviewer-facing binding note for the three highest-risk denominators named in the active sprint directive. This reduces the chance that manuscript prose, dashboard subtitles, and SI/source exports cite different denominator classes.

## Remaining blocker

The manuscript should still be checked for any count-bearing sentence that cites Figure 2, Figure 5, or Figure 7 without naming the matching denominator class. The next smallest move is a sentence-level caption/prose audit against this v0.4 register.
