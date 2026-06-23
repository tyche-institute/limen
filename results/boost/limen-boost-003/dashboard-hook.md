# Shard 003 dashboard hook

Primary artifacts:
- `results/boost/limen-boost-003/regulator-court-lead-board.tsv`
- `results/boost/limen-boost-003/shared-consumer-currentness-audit.tsv`

Suggested dashboard/table views
- Threshold front-door panel: separate the shared `11`-row authoritative core from the two threshold-changing court/public-record blockers (`LIMEN-000002`, `LIMEN-000005`).
- Explicit-gap badge: show `QUEUE-HUMAN-AS-AI-001` as a package-level final-authority gap rather than as a case row.
- Bounded-sidecar strip: keep `LIMEN-000013` (FTC reversibility chronology) and `LIMEN-000014` (FTC court-settlement sidecar) visible as reusable but denominator-neutral/threshold-neutral support.
- Non-U.S./non-UK authority-depth ladder: show the distinct ceilings for France warning-page depth (`LIMEN-000015`), Denmark governance-companion depth (`LIMEN-000012`), and Slovenia official follow-through depth (`LIMEN-000009_plus_non_us_follow_through`).
- Blocker-class matrix: court-text absence vs exact-caption normalization vs hidden-human final-authority gap vs governance-only companion gap.

Fields already suitable for visualization
- `scope_or_case_id`
- `lead_class`
- `jurisdiction`
- `language`
- `current_authority_posture`
- `threshold_changing_target`
- `paper_or_thesis_use`
- `dashboard_hook`
- `uncertainty_or_caution`
- `next_smallest_move`

Interpretation supported
The view should help a reviewer see that shard-003 is now a route-state panel rather than a backlog. Some rows are already reusable as core authoritative package state, some are genuine threshold blockers whose exact next document type is known, some are bounded sidecars that strengthen chronology or settlement comparison without moving the denominator, and some widen language/jurisdiction coverage while still falling short of document-grade enforcement or court depth.
