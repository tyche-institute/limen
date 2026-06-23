# LIMEN preprint slot-normalization audit

Cycle timestamp (UTC): 2026-06-17T10:12:17Z
Lane id: `limen-dashboard-paper-forge`
Project root: `/srv/tyche/projects/limen-ai-edge-case-atlas`
Sprint posture: harvest-only hostile-reviewer manuscript-assembly pass; no new collection; normalize front-door manuscript surfaces against the live Figure 1-8 / Table A-C contract.

## Inputs checked

- `draft/preprint.md`
- `dashboard/limen-dashboard-spec-v0.1.md`
- `papers/article-architecture-v0.1.md`
- `results/dashboard-paper/status.md`
- `results/dashboard-paper/dashboard-paper-figure-route-registry-2026-06-16T23-33-03Z.tsv`
- `results/dashboard-paper/caption-control-register-v0.1.tsv`
- `results/dashboard-paper/live-export-audit-2026-06-17T08-56-03Z.tsv`
- `/etc/tyche-factory/current-publication-sprint.md`
- `publication-goal-card-current.md`
- `/srv/tyche/athena/memory-transfer/20260608-athena-codex-memory/ATHENA-CODEX-MEMORY-TRANSFER-2026-06-08.md`
- `/srv/tyche/shared/status/gaia-pallas-limen-stabilization.md`

STOP check:
- no `/srv/tyche/STOP`
- no project `STOP`

## Verified front-door drift counts in `draft/preprint.md`

- legacy `Table 1*` references: `15`
  - `Table 1`: `1`
  - `Table 1A`: `1`
  - `Table 1B`: `3`
  - `Table 1C`: `2`
  - `Table 1D`: `2`
  - `Table 1E`: `4`
  - `Table 1F`: `2`
- legacy `Table 6*` references: `3`
  - `Table 6`: `2`
  - `Table 6A`: `1`
- top-level shard-fragment headings: `6`
  - `Shard 003`, `004`, `007`, `008`, `009`, `010`
- boost-local path mentions: `55` total mentions across `47` unique `results/boost/...` paths
- live shared figure references remain present and bounded:
  - `Figure 1`: `2`
  - `Figure 2`: `10`
  - `Figure 3`: `1`
  - `Figure 4`: `1`
  - `Figure 5`: `3`
  - `Figure 6`: `2`
  - `Figure 7`: `3`
  - `Figure 8`: `2`

Interpretation:
- the manuscript front door is current on shared figure numbering and live denominator language;
- the remaining drift is structural packaging drift from shard-era staging labels and boost-local travel kits;
- this is a manuscript normalization blocker, not an evidence-collection blocker.

## Route-safe normalization board

| Legacy surface in `draft/preprint.md` | Current use state | Route-safe action now | Current authority / replacement surface |
| --- | --- | --- | --- |
| `Table 1` generic family bundle | legacy front-door staging label | Replace with explicit surface names; do not leave `Table 1` as a manuscript slot label. | `Figure 1` source-family map plus the live denominator registry in `dashboard/limen-dashboard-spec-v0.1.md` |
| `Table 1A` authority prose | direct live analog exists | Normalize to `Table A`; keep authority-depth wording tied to the live shared table rather than shard-local slot memory. | `results/dashboard/authoritative-document-depth-facet.tsv` |
| `Table 1B` public-sector disclosure asymmetry | direct live analog exists | Normalize to `Table B`; keep procurement/deployment overread blocked. | `results/dashboard/public-sector-disclosure-comparison.tsv` |
| `Table 1C` AI-washing posture ladder | no direct live slot in the current Figure 1-8 / Table A-C bundle | Quarantine as appendix or shard-local sidecar until a shared slot is formally registered; do not present as a live core table label. | no current direct live slot in `dashboard-paper-figure-route-registry-2026-06-16T23-33-03Z.tsv` |
| `Table 1D` multilingual ladder | only partial live analog exists | Rewrite front-door multilingual prose around `Figure 6`; keep ladder detail as bounded sidecar or appendix prose only. | `results/dashboard/jurisdiction-language-coverage.tsv` |
| `Table 1E` procedural-contamination source-depth panel | no direct live Route A slot | Quarantine from front-door route unless formally promoted; keep as appendix/shared sidecar rather than a live main-slot label. | no current direct live slot in the Route A bundle |
| `Table 1F` provenance-confusion publication cells | only partial live analog exists | Rewrite provenance front-door prose around `Figure 8`; keep provenance-confusion cells as bounded appendix/sidecar material. | `results/dashboard/attestation-trust-surface-readiness.tsv` |
| `Table 6` security/comparator legacy label | no direct live slot | Replace with explicit live surface names or quarantine; do not leave `Table 6` as a manuscript slot. | depends on sentence scope; use `Table C`, `Figure 7`, or comparator appendix prose explicitly |
| `Table 6A` comparator publication cells | no direct live slot in the current shared bundle | Quarantine as comparator appendix/control note; do not imply it is part of the live Route A front door. | no current direct live slot in the live Figure 1-8 / Table A-C contract |
| `Shard 003/004/007/008/009/010` top-level headings | staging headings still exposed in the main draft | Demote to appendix-fragment or integration-note status; the main manuscript should surface route-safe section headings instead of shard IDs. | `papers/article-architecture-v0.1.md` section structure |

## Manuscript-safe normalization rules

1. Front-door manuscript prose should use only the live shared slots: `Figure 1-8` and `Table A-C`.
2. Legacy `Table 1*` and `Table 6*` labels are staging artifacts unless they have an explicit live replacement in the board above.
3. `results/boost/...` paths may remain in internal control notes, but should not dominate the front-door preprint prose once a live shared dashboard surface exists.
4. Shard IDs are valid provenance markers, not final article section names.
5. Any retained sidecar material must keep the same claim ceilings already enforced by the dashboard spec and article architecture: no completeness, prevalence, procurement-proof, legal/compliance, or external-assurance overread.

## Paper-readiness delta

This cycle adds a reviewer-safe negative result with exact counts and a route board: the manuscript drift is now localized to legacy slot labels, shard headings, and boost-local bundle spillover rather than to the live denominator registry or the shared Figure 1-8 / Table A-C contract. That makes the next edit pass narrower and safer.

## Next smallest publishability move

Patch `dashboard/limen-dashboard-spec-v0.1.md`, `papers/article-architecture-v0.1.md`, and `results/dashboard-paper/status.md` so the lane's front door explicitly treats this audit as the normalization authority. Then rewrite or quarantine legacy `Table 1*`, `Table 6*`, and shard-heading usage in `draft/preprint.md` without reopening collection or denominator scope.
