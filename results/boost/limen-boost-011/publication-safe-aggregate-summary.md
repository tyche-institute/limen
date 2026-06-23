# Publication-safe aggregate summary v0.1

Timestamp (UTC): 2026-06-07T08:15:15Z
Lane: `limen-boost-011`

## Core counts

- Raw normalized-record rows reviewed: 29
- Publication-safe unique lineages after stable-duplicate collapse: 21
- Stable-duplicate derivative queue rows excluded from lineage counts: 7
- Identifier-collision-blocker lineages requiring normalized keys: 5
- Reviewed-not-duplicate separate lineages retained: 8

## Confidence-cap distribution across unique lineages

- `high`: 15
- `medium`: 0
- `low`: 6

## Translation dependence

- `not_translation_dependent`: 15
- `translation_dependent`: 6

## Interpretation

- The current local package still exposes 30 normalized rows and 21 collapsed lineages after stable-duplicate control, so earlier 23-row / 17-lineage shard-011 checkpoints remain stale.
- The refresh now keeps unresolved multilingual title-gloss rows out of the medium-cap band: the aggregate contract no longer implies that Lithuanian and Kaleva queue rows are as publication-ready as direct-source-resolved multilingual exemplars.
- The LangChain `LIMEN-000008` row is now synchronized with the duplicate ledger as a reviewed non-merge rather than an unreviewed singleton, reducing drift between duplicate-control and aggregate-safe exports.
- Low-cap rows remain unsuitable for stronger comparative or prevalence-style prose; high-cap rows are bounded exemplars, not a completeness claim.
- Identifier collisions remain a schema-control problem rather than an event-duplication problem, so any bare `case_id` aggregation remains unsafe.

## Dashboard and paper hook

- Feed figure-caption discipline for the provisional evidence funnel and jurisdiction/language map.
- Provide a machine-readable inclusion/exclusion contract for downstream refresh of shared dashboard and manuscript exports.
- Support a reviewer-facing methods paragraph that separates duplicate collapse, join safety, and confidence-cap handling into three distinct quality controls.
