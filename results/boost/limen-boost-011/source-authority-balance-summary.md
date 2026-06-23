# Source authority balance summary for limen-boost-011

Timestamp (UTC): 2026-06-07T08:15:15Z
Lane: `limen-boost-011`

## What this artifact adds

This refresh converts the current 21-lineage publication-safe aggregate into a reviewer-visible authority and confidence composition table. The point is not completeness, but to show which lineages are safe as bounded main-text exemplars, which remain translation-caution material, and which still require denominator controls.

## Current composition

- Total current lineages in `publication-safe-aggregate-matrix.tsv`: 21
- Confidence caps: high=15, medium=0, low=6
- Translation-dependent lineages: 6; non-translation-dependent: 15
- Duplicate-control states: identifier_collision_blocker=5, reviewed_not_duplicate=8, stable_duplicate_cluster=7, no_cluster_review_row=1

## Reviewer-safe interpretation

- Authority anchors safe for bounded main-text or figure exemplars: 7 lineages.
- Technical-authority security exemplars safe for bounded hazard description: 7 lineages.
- Translation-caution authority exemplars: 1 lineages.
- Provisional/limitations-only rows: 6 lineages (5 translation-dependent provisional rows plus 1 low-cap security singleton).
- All low-cap rows should stay out of prevalence or cross-country ranking rhetoric.
- All identifier-collision-blocker lineages remain unsafe for joins on bare local `case_id`; manuscript and dashboard text should cite file-qualified or normalized keys only.

## Dashboard/paper hook

- Build a stacked bar or waffle chart with three bands: `authority_anchor`, `technical_authority`, and `provisional/translation-caution`.
- Add a denominator-warning overlay keyed to `join_hazard` so counts are not narrated without the duplicate-control state.
- Use `reviewer_safe_paper_use` to gate which rows can appear in headline figure captions versus limitations notes.

## Remaining blocker

- The multilingual package still has five translation-dependent rows that remain provisional or queue-only because they are title-gloss-only, unresolved, or non-official direct-source surfaces.
- Only one translation-dependent lineage currently qualifies as an authority-backed exemplar (`LMWCS-20260606-004` / ORION), and even that row remains translation-qualified and below deployment/compliance rhetoric.

## Next smallest publishability move

- Patch shared manuscript/dashboard prose so headline counts cite the current 30-normalized-row / 21-lineage authority-balance mix and keep translation-dependent single-source rows in provisional or limitations-only views while allowing ORION to appear as a bounded official-source exemplar with explicit translation caution.
