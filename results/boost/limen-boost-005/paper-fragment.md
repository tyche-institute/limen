# Paper fragment and replacement map — limen-boost-005

Generated: 2026-06-07T05:41:11Z
Project: `limen-ai-edge-case-atlas`
Lane: `limen-boost-005`
Sprint: `20260607-hostile-reviewer-pass`

## Purpose

Provide a reviewer-safe multilingual manuscript/dashboard fragment that matches the current shard-005 package after the Radio Ptuj row was upgraded into a direct-source-resolved Slovenian local-news exemplar.

## Current reviewer-safe multilingual state

- Total multilingual rows in the current lane package: `6`
- Direct-source-resolved rows: `3/6`
  - `1` direct official: `LMWCS-20260606-004` (`Policija - Domov`, Slovenia, `sl`)
  - `2` direct non-official: `LMWCS-20260606-001` (`Yle`, Finland, `fi`); `LMWCS-20260606-005` (`Radio Ptuj`, Slovenia, `sl`)
- Queue-only unresolved rows: `3/6`
  - `LMWCS-20260606-002` (`Kaleva`, Finland, `fi`)
  - `LMWCS-20260606-003` (`15min.lt`, Lithuania, `lt`)
  - `LMWCS-20260606-006` (`tv3.ee`, Estonia, `et`)

Interpretation ceiling:
- The multilingual package now supports three bounded appendix/table rows, not two.
- Only one of the three direct rows is official-source-backed; the other two remain direct non-official media rows with explicit claim ceilings.
- The package is still best used to show language-coverage value, source-resolution bottlenecks, and authority-weighted evidence ceilings, not multilingual prevalence.

## Replacement fragment for manuscript use

Suggested replacement for stale prose that still says the package has only two direct-source-resolved rows:

LIMEN's current multilingual package is useful as an evidence-coverage and source-resolution result rather than as an incident count. The reviewer-safe reading is that three of six non-English leads have now moved into direct-source-resolved status, while three remain queue-only limitations rows. The resolved trio is deliberately heterogeneous: one Slovenian official-police page supports a bounded public-sector border-control project row; one Finnish public-broadcaster article supports a bounded procedural-contamination row naming public institutions and workload effects; and one Slovenian regional-radio article supports a bounded municipal-service-channel / institutional-absurdity row with explicit caution against overreading labor replacement, procurement regularity, legality, or diffusion. This package therefore supports a methods/results argument about multilingual discovery value, authority-weighted evidence ceilings, and direct-source bottlenecks, while still refusing prevalence, legality, compliance, or completeness claims.

## Table/figure-ready rendering

### Suggested appendix/table rows

| queue_id | jurisdiction | language | source class | reviewer-safe use now | forbidden overread |
|---|---|---|---|---|---|
| `LMWCS-20260606-004` | Slovenia | `sl` | direct official police page | bounded substantive row on project existence, stated purpose, pilot framing, and privacy/biometric language | no claims about legality, proportionality, effectiveness, or production deployment |
| `LMWCS-20260606-001` | Finland | `fi` | direct public-broadcaster page | bounded descriptive row on AI-assisted administrative appeals, fabricated-case-reference signals, and official workload burden | no claims about prevalence, abuse intent, or system-wide legal-process contamination |
| `LMWCS-20260606-005` | Slovenia | `sl` | direct local-news page | bounded descriptive row on announced AI-assisted municipal call-routing / secretariat channel | no claims about full human replacement, procurement regularity, vendor stack, legality, effectiveness, or wider diffusion |

### Suggested limitations rows

| queue_id | status | blocker class | paper role |
|---|---|---|---|
| `LMWCS-20260606-002` | queue-only | reachable but terms-sensitive news surface | selective-upgrade candidate / methods limitation |
| `LMWCS-20260606-003` | queue-only | rights-sensitive news plus blocked official target | limitations row |
| `LMWCS-20260606-006` | queue-only | challenge-gated news surface | limitations row |

## Dashboard hook

Recommended multilingual panel subtitle:

Three direct-source-resolved multilingual rows (`1` official, `2` non-official) and three queue-only limitation rows show that LIMEN can recover under-covered-language evidence, but source authority and access friction still sharply limit stronger cross-jurisdiction claims.

Recommended panel split:
- layer 1: `direct official`
- layer 2: `direct non-official`
- layer 3: `queue-only / blocked`

## Replacement targets identified this cycle

These local files still contain stale two-row wording and should be patched in a later manuscript/dashboard consolidation pass:

1. `draft/preprint.md`
   - section: `## Multilingual readiness fragment`
   - stale wording: `two of six non-English leads have moved into direct-source-resolved status`
2. `dashboard/limen-dashboard-spec-v0.1.md`
   - stale wording around lines 31, 42, and 174-175 still understates the current reviewer-safe multilingual package

## Evidence used

- `results/boost/limen-boost-005/language-coverage-matrix.tsv`
- `results/boost/limen-boost-005/multilingual-claim-ceiling-register.tsv`
- `results/boost/limen-boost-005/publication-readiness-matrix.tsv`
- `results/boost/limen-boost-005/source-resolution-log.tsv`
- `draft/preprint.md`
- `dashboard/limen-dashboard-spec-v0.1.md`

## Paper/thesis use

- Direct manuscript patch input for the first LIMEN article package.
- Appendix/table seed for a multilingual evidence-ceiling section.
- Dashboard-language patch note for the jurisdiction/language panel.
- Thesis methods evidence that multilingual recovery should be modeled as authority-weighted and route-sensitive, not as a flat non-English count.
