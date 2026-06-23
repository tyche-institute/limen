# sf09 source-family ledger alignment note

Timestamp (UTC): 2026-06-07T03:50:20Z
Lane: `limen-continuous-experiments`
Sprint: `20260607-hostile-reviewer-pass`

## Why this artifact exists

The canonical source-family ledger still described `sf09` as if LIMEN only had the first Slovenian ORION official-page resolution. That had become stale. The shared package already contained a stronger bounded public-sector comparison: one Dutch public register row, one Slovenian official project-page row, and two UK regulator-document anchors, plus an explicit freeze note stating that the family still lacks buyer-side procurement traceability.

## What was synchronized

The `sf09` row in `sources/source-family-ledger.tsv` now matches the already existing local evidence package:

- `results/boost/limen-continuous-experiments/public-sector-disclosure-field-completeness-v0.1.tsv`
- `results/boost/limen-continuous-experiments/orion-disclosure-schema-probe-v0.1.tsv`
- `results/boost/limen-boost-006/comparator-freeze-matrix.tsv`
- `results/dashboard-paper/public-sector-disclosure-asymmetry-v0.1.md`

## Reviewer-safe family statement now reflected canonically

`sf09` currently supports a frozen disclosure-surface comparison across:

1. one Dutch public AI register exemplar;
2. one Slovenian official police project-page exemplar;
3. two UK regulator-document anchors.

This is enough for methods/results language about disclosure-surface heterogeneity and reconstruction ceilings. It is not enough for broader claims about buyer-side procurement traceability, contract transparency, operational deployment proof, or public-sector compliance.

## Paper/thesis use

- hostile-reviewer consistency control between the source-family ledger and the shared public-sector comparison package;
- methods table row for `sf09` without stale undercounting;
- dashboard caption guardrail for the register-vs-project-page-vs-regulator panel.

## Dashboard/observatory hook

Use the canonical `sf09` row for:

- source-family saturation map text;
- disclosure-field completeness panel captions;
- hover/help text that distinguishes `register`, `project_page`, and `regulator_document` surfaces without implying buyer-side procurement visibility.

## Remaining blocker

A second non-Dutch positive register/procurement/buyer-side comparator is still needed before stronger comparative public-sector transparency language is justified.
