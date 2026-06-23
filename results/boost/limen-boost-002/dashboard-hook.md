# Shard 002 dashboard hook

Primary artifact: `results/boost/limen-boost-002/comparator-claim-ceiling-matrix.tsv`

Suggested dashboard/table views
- Comparator role ladder: structured seed import vs bounded public comparator vs taxonomy bridge vs manual citation overlay.
- Overread guardrail table: exact identifier verified, metadata-first only, concept-only, and manual-only rows shown as different interoperability classes.
- Methods appendix panel: pair the new matrix with `field-map-appendix-v0.1.tsv` to show why crosswalk slots exist for all six sources but machine use differs sharply.
- Security-focused inset: link the matrix to `results/crosswalks/atlas-technique-context-appendix-v0.1.tsv` so reviewers can see that structured interoperability is concentrated in the security slice and split cleanly between generalized case context, technique-only rows, and cautious-context-only rows.

Fields already suitable for visualization
- `source_id`
- `source_name`
- `reviewer_control_class_now`
- `verification_status`
- `exact_identifier_surface_now`
- `structured_payload_readiness_now`
- `safe_role_now`
- `reviewer_safe_claim_now`
- `forbidden_overread_now`
- `dashboard_hook`

Interpretation supported
The view should help a reviewer see that LIMEN's external crosswalk package is intentionally non-uniform. Some comparators are precise enough for machine-readable appendix or dashboard joins, some are safe only for bounded metadata-first comparison, and some are useful only as concept or citation overlays. That asymmetry is a quality-control feature, not a weakness to hide.
