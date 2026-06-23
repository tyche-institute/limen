# Shard-011 downstream drift note

Timestamp (UTC): 2026-06-07T09:00:04Z
Lane: `limen-boost-011`

## What this artifact does

This note records downstream prose and figure-registry surfaces that still lag the current shard-011 scoring contract after the latest confidence normalization.

## Current shard-011 contract to treat as canonical

- Raw normalized rows: 28
- Publication-safe lineages: 21
- Confidence caps: high=15, medium=0, low=6
- Translation dependence: 15 not translation dependent; 6 translation dependent
- Authority balance: authority_anchor=7; technical_authority=7; translation_caution_authority=1; provisional_or_limitations_only=6

## Why the drift matters

- Figure 5 prose that still says `medium=2 low=4` overstates the readiness of weak multilingual rows that were explicitly downgraded in the current shard-011 contract.
- Figure 7 prose that still says `translation_caution_authority=2 provisional_or_limitations_only=5` narratively flattens ORION together with weaker title-gloss rows.
- The stale lane-local `dashboard-hook.md` can mislead future refresh work inside shard 011 itself unless its denominator and count language is updated.

## Paper/thesis use

- Methods/data paper: exact repair register for caption and registry drift after scoring normalization.
- Thesis/evidence-infrastructure chapter: shows how denominator and authority-control contracts can drift across manuscript layers even when source TSVs are already normalized.
- Dashboard package: bounded QA surface for caption inheritance and legend repair.

## Next smallest publishability move

Patch the four downstream shared/proto-shared figure surfaces listed in `downstream-drift-register.tsv` so Figure 5 and Figure 7 inherit the current shard-011 confidence and authority composition counts verbatim.
