# Dashboard hook: publication-safe aggregate refresh

Timestamp (UTC): 2026-06-07T09:00:04Z
Lane: `limen-boost-011`

## What changed

- Re-centered the lane-local dashboard note on the current 30-normalized-row / 21-lineage shard-011 contract rather than the earlier 17-lineage checkpoint.
- Preserved the post-normalization confidence split: high=15, medium=0, low=6.
- Preserved the current authority-balance split: authority_anchor=7; technical_authority=7; translation_caution_authority=1; provisional_or_limitations_only=6.
- Kept the translation-dependent denominator explicit: 6 of 21 lineages remain translation dependent, but only one currently qualifies as an authority-backed exemplar.

## Output artifacts

- `results/boost/limen-boost-011/refreshed-evidence-funnel-safe.tsv`
- `results/boost/limen-boost-011/publication-safe-aggregate-summary.md`
- `results/boost/limen-boost-011/source-authority-balance.tsv`
- `results/boost/limen-boost-011/source-authority-balance-summary.md`
- `results/boost/limen-boost-011/downstream-drift-register.tsv`

## Reviewer-visible deltas

- Safe funnel denominator is 21 collapsed lineages from 30 normalized rows, not the older 17-lineage checkpoint.
- Confidence-cap split is explicit: high=15, medium=0, low=6.
- Translation-dependent lineages remain explicit: 6 of 21.
- `T3_authoritative_source` / `T3_authoritative_source_direct_url_resolved` together cover 15 of 21 lineages.
- Only one translation-dependent lineage currently qualifies as an authority-backed exemplar: ORION (`LMWCS-20260606-004`), and even that row remains translation-qualified and bounded to narrow existence/scope language.

## Paper/thesis use

- Methods/data paper: supports a hostile-reviewer-safe funnel and authority panel with current denominator and confidence semantics.
- Thesis chapter on evidence infrastructure: concrete example of how duplicate collapse, confidence caps, translation flags, and authority bands alter interpretability without inventing new facts.
- Dashboard build: gives a lane-local control note for verifying downstream caption inheritance against the current shard-011 contract.

## Cautions

- These are lane-local reviewer-safe control semantics, not a claim that shared dashboard or manuscript surfaces are already synchronized.
- Low-cap rows remain unsuitable for prevalence claims, country ranking, or flat comparative rhetoric.
- Translation-dependent rows still need bounded wording and, where weak, stronger direct sources or human review.

## Next smallest publishability move

Patch shared/proto-shared Figure 5 and Figure 7 caption surfaces to inherit the current `high=15 / medium=0 / low=6` funnel contract and the current `7 / 7 / 1 / 6` authority-balance split verbatim.
