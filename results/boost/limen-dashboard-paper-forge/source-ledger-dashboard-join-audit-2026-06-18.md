# LIMEN source-ledger/dashboard join audit

Generated: 2026-06-18T06-41-37Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`
Source scope: local `sources/sources.md`, existing dashboard exports, and existing row-level provenance sidecar only. No new crawling, upload, portal action, or claim-ceiling relaxation.

## Why this artifact exists

The previous dashboard sidecar deliberately marked many rows as needing a source-ledger join before a public interactive dashboard. This audit tests whether the current row pointers can be mechanically connected to existing source-ledger access dates and rights/terms notes. It is a dashboard/tooling readiness artifact, not a new evidence collection pass.

## Result

- Sidecar rows checked: 99
- Candidate source-ledger matches: 0
- Artifact-pointer-only rows without a source-ledger match: 88
- Rows with no source-ledger match: 11
- Machine-readable TSV: `results/boost/limen-dashboard-paper-forge/source-ledger-dashboard-join-audit-2026-06-18.tsv`
- TSV SHA-256: `b8c062031a663a5d8892d1b06b5626262a4675eca5ba83f0500ecc8e5672f4ae`

## Per-export join readiness

| dashboard_export | rows | candidate_matches | artifact_pointer_only | no_match | dashboard implication |
|---|---:|---:|---:|---:|---|
| `results/dashboard/duplicate-review-graph.tsv` | 27 | 0 | 27 | 0 | do not present row as source-ledger enriched; keep artifact/proof-ceiling tooltip only |
| `results/dashboard/evidence-funnel.tsv` | 11 | 0 | 0 | 11 | do not present row as source-ledger enriched; keep artifact/proof-ceiling tooltip only |
| `results/dashboard/jurisdiction-language-coverage.tsv` | 12 | 0 | 12 | 0 | do not present row as source-ledger enriched; keep artifact/proof-ceiling tooltip only |
| `results/dashboard/legal-uncertainty-matrix.tsv` | 15 | 0 | 15 | 0 | do not present row as source-ledger enriched; keep artifact/proof-ceiling tooltip only |
| `results/dashboard/security-threshold-ladder-panel.tsv` | 4 | 0 | 4 | 0 | do not present row as source-ledger enriched; keep artifact/proof-ceiling tooltip only |
| `results/dashboard/source-family-coverage.tsv` | 15 | 0 | 15 | 0 | do not present row as source-ledger enriched; keep artifact/proof-ceiling tooltip only |
| `results/dashboard/taxonomy-heatmap.tsv` | 15 | 0 | 15 | 0 | do not present row as source-ledger enriched; keep artifact/proof-ceiling tooltip only |

## Interpretation for paper/dashboard parity

- Evidence: the dashboard can already expose record-level or row-level proof ceilings, denominator scopes, and reviewer-safe readings from the sidecar.
- Interpretation: access-date and rights/terms fields should not be shown as row-level source facts unless a source-ledger candidate has been spot-checked; unmatched rows should remain labeled as dashboard artifact pointers.
- Claim ceiling: this audit supports provenance UI readiness and hostile-reviewer transparency only. It does not strengthen completeness, prevalence, legality, compliance, certification, safety, country-ranking, or official-incident claims.
- Observatory hook: dashboard tooltips should use `join_status`, `candidate_source_id`, `candidate_access_date`, `candidate_rights_terms_note`, and `public_dashboard_action` from the TSV. Red/yellow states should remain visible instead of being hidden.

## Next smallest publishability move

Because this mechanical pass found zero candidate source-ledger matches, do not copy access-date or rights/terms fields into public row tooltips from inference alone. The next bounded move is to create an explicit export-level provenance ledger for dashboard artifacts, then manually attach source-ledger IDs only where a row truly points to a public source rather than to an internal dashboard/control artifact.
