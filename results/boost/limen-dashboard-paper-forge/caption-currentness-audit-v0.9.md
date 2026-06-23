# LIMEN caption currentness audit v0.9

Lane: `limen-dashboard-paper-forge`  
Generated UTC: 2026-06-18T20:55:00Z  
Patched/rerun UTC: 2026-06-19T00:00:00Z  
Scope: fail-closed audit of `results/dashboard-paper/caption-control-register-v0.1.tsv` against the current v0.8 dashboard/API denominator contract.

## Verdict

- Caption/control rows audited: 5.
- Blocked for count-bearing reuse until rewritten: 0.
- Passed with current denominator language: 3.
- Passed only as scope/control text, requiring pairing with the v0.8 API subtitle before reuse: 2.
- Machine-readable audit: `results/boost/limen-dashboard-paper-forge/caption-currentness-audit-v0.9.tsv`.
- TSV SHA-256 after patch: `e0481c8934685ec1dd5a9273d2341191146ed08a745c0818e40627fc5d9e6f06`.
- Source caption register SHA-256 after patch: `b8c56bb2eefc2d2679a5a0ffac15892676b10832c819dcdcba9d8aa9c7ad7126`.

## Why this artifact exists

The v0.8 dashboard preflight showed that `CAPTION_CONTROL` is a lint source, not a dashboard chart. This audit adds the missing hostile-reviewer guard: old caption-control prose must not silently override current dashboard denominators when figures are exported to a manuscript, PDF, or static dashboard.

## Current denominator floors enforced here

| Domain | Current safe caption floor |
|---|---|
| Taxonomy / Figure 2 / Table 2 | `39/29 core; 44/34 extended; legacy 35/27 provenance only` |
| Publication-safe funnel / Figure 5 | `21 publication-safe lineages; confidence/translation bands are ceilings` |
| Security threshold / Figure 7 | `4 threshold rows; sidecar default 21 / projected 23 lineages only` |

## Patched controls

| control_id | slot | current terms found | safe reuse action |
|---|---|---|---|
| `CCR-001` | Figure 2 taxonomy support heatmap | `39/29 core`; `44/34 extended`; `35/27` legacy/provenance only | may be reused with current denominator badge and claim-boundary/prohibited-reading text intact |
| `CCR-002` | Table 2 category support matrix | `39/29 core`; `44/34 extended`; `35/27` legacy/provenance only | may be reused with current denominator badge and claim-boundary/prohibited-reading text intact |

## Negative evidence / limitation

The initial audit blocked `CCR-001` and `CCR-002`; the 2026-06-19 patch rewrote those caption-control rows in place and updated the TSV audit to PASS them under the current denominator grammar. This remains a caption-currentness/package-integrity artifact only. No new collection, row promotion, legal conclusion, prevalence estimate, country ranking, public release, or completeness claim was made.

## Observatory hook

Dashboard, article-export, and PDF-build scripts should load `results/boost/limen-dashboard-paper-forge/caption-currentness-audit-v0.9.tsv` before consuming `results/dashboard-paper/caption-control-register-v0.1.tsv`. If `audit_state == BLOCK_FOR_COUNT_BEARING_REUSE`, the renderer should stop or display a build error rather than exporting the stale caption. If `audit_state == PASS_SCOPE_ONLY_NO_EXPLICIT_COUNT_FOUND`, the renderer should require the current API bundle subtitle for the relevant view.

## Paper/thesis use

This artifact strengthens the methods/data-paper claim that LIMEN separates denominator truth, caption grammar, and dashboard rendering. It is directly usable in Supplementary Methods as a reproducibility and hostile-reviewer safeguard.

## Next smallest publishability move

Keep the renderer-side preflight active and rerun it after any caption-control, dashboard TSV, API bundle, static preview, figure, or PDF export change. Do not make `CAPTION_CONTROL` itself a count-bearing dashboard view.
