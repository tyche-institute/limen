# Shard 011 paper fragment: discrepancy-gated aggregate wording

Timestamp (UTC): 2026-06-07T04:27:00Z
Lane: `limen-boost-011`

## Why this fragment exists

The hostile-reviewer pass now needs a narrower wording checkpoint for shared LIMEN aggregate prose. Current local artifacts no longer agree on the safe denominator: the normalized join ledger has 23 raw normalized rows, but the current materialized publication-safe aggregate matrix exposes 17 lineages, not the 18 lineages stated in `results/dashboard-paper/status.md`. The current cluster ledger is also ahead of `draft/preprint.md`: it now contains 14 review rows, not the 11 review edges still named in the preprint framing fragment.

## Reviewer-safe wording to reuse

LIMEN's current join-safety package should be described as a provisional, materialized checkpoint rather than as a settled atlas-wide count. The present lane-011 ledger spans 23 normalized record rows, while the currently materialized publication-safe aggregate matrix exposes 17 lineages after duplicate collapse and queue-copy exclusion. Five derivative queue rows are intentionally excluded from lineage counts, and one additional authoritative singleton (`data/cases/authoritative-candidates.jsonl:LIMEN-000005`) is visible in the normalization ledger but not yet represented in the current aggregate refresh. The safe interpretation is methodological: LIMEN can show how duplicate control, confidence caps, and translation cautions shape publishable evidence surfaces, but aggregate prose must stay tied to the exact materialized export being cited.

The duplicate-control graph should likewise be described as an active quality-control layer with heterogeneous edge types rather than as a flat legacy count. The current local cluster ledger contains 14 review rows: 5 `identifier_collision_blocker`, 5 `stable_duplicate_cluster`, and 4 `reviewed_not_duplicate`. This supports a stronger methods claim about reviewer-visible join discipline, but only if the manuscript distinguishes collision blockers, lineage-collapse rows, and explicit non-merges instead of freezing an older 11-edge summary.

## Paper/thesis use

- Methods/data paper: gives a reviewer-safe denominator paragraph for figures/tables that depend on duplicate collapse and normalized join rules.
- Thesis chapter on evidence infrastructure: concrete example of why upstream ledgers and downstream materialized aggregates must be versioned and cited separately.
- Dashboard package: supports a build-health or figure-gating note that blocks stronger geography/count rhetoric until the shared exports consume the lane-local safe artifacts.

## Visualization/dashboard hook

- Build a small discrepancy panel with three fields: `raw_normalized_rows`, `materialized_safe_lineages`, and `cluster_review_rows_current`.
- Show a warning state whenever shared prose cites a denominator that does not match the current materialized aggregate file.

## Next smallest publishability move

Refresh the shared dashboard-paper status and preprint figure prose so they cite the current materialized lane-011 exports explicitly, or regenerate the aggregate matrix to include the omitted authoritative singleton before shared counts are narrated as stable.
