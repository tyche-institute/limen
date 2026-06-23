# Dashboard/paper taxonomy propagation hook

Generated: 2026-06-07T00:24:42Z
Lane: `limen-boost-010`
Sprint: `20260607-hostile-reviewer-pass`

## Why this cycle

The previous lane-010 audit established that the local LIMEN package now supports 12 of 15 top-level categories, leaving only 3 true zero-seed gaps. Several downstream dashboard/paper artifacts still describe the taxonomy layer with older 8/15 seeded counts taken from the shared legal/normative crosswalk. For hostile-reviewer use, those two states must be separated explicitly:

1. the shared crosswalk still contains 15 rows with older `seed_case_count` values;
2. the current local package now shows wider category support because later shard outputs have not been folded back into that shared layer.

## Safe corrected wording

Use wording like this in manuscript, dashboard, and figure notes:

"In the current local LIMEN package, 12 of 15 top-level categories have at least one local row when authoritative, security, multilingual, and shard-009 candidate artifacts are read together using file-qualified references. Only three categories remain true zero-seed gaps in the present local package: `health_medical_or_mental_health`, `research_integrity`, and `residual_unclassified`. The older shared legal/normative crosswalk understates this support because it has not yet absorbed all later shard outputs."

## What should not be said now

- Do not say the taxonomy layer currently has only 8 seeded categories without noting that this is a stale shared-crosswalk view.
- Do not describe `institutional_absurdity`, `deepfake_or_synthetic_identity`, `finance_insurance_or_market`, or `ai_washing_or_false_ai_claim` as unseeded.
- Do not convert this local count into a prevalence claim, completeness claim, or legal-strength claim.

## Files currently needing refresh or caution labels

See `taxonomy-propagation.tsv` for a structured propagation queue covering:
- `dashboard/limen-dashboard-spec-v0.1.md`
- `papers/article-architecture-v0.1.md`
- `results/boost/limen-boost-012/paper-fragment.md`
- `results/boost/limen-boost-012/status.md`

## Paper/thesis use

- Strengthens hostile-reviewer safety by preventing stale gap rhetoric from surviving into figures or methods prose.
- Supports a more accurate taxonomy heatmap caption: local support is broader than the shared crosswalk currently reports, but some categories remain mixed-tier and provisional.
- Helps the thesis distinguish taxonomy design from synthesis-maintenance lag.

## Visualization hook

Immediate dashboard use:
- add a `crosswalk_lag_flag` or `pressure_status` overlay to the taxonomy heatmap;
- show true zero-seed gaps separately from mixed-tier or crosswalk-stale categories.

## Next smallest publishability move

Patch the shared dashboard/paper prose to use the corrected 12/15 local-support statement, then refresh the shared crosswalk layer or regenerate the taxonomy heatmap from `category-pressure.tsv` instead of relying only on the older `seed_case_count` column.
