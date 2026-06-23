# LIMEN lifecycle live-coverage note

Updated: 2026-06-07T09:29:39Z
Lane: `limen-attestation-receipt-profile`

This note turns lifecycle-state coverage into one reviewer-facing surface.

Key delta:
- `observed` is no longer example-only. The package now includes a live observed receipt over `sources/sources.md#LIMEN-S-041`.
- `extracted` is no longer example-only. The package now includes a live extracted receipt linking `LIMEN-S-041` to `data/cases/security-agentic-candidates.jsonl#LIMEN-000008`.

Remaining live-coverage gaps:
- none at the lifecycle-action level in profile v0.1.

Interpretation:
- The profile now demonstrates live coverage for observation, extraction, classification, review, clustering, publication, and bounded supersession.
- The remaining hostile-reviewer objection is narrower than before: the package still lacks external trust wiring such as detached signatures, verified transparency inclusion proofs, issued credentials, or a shared release workflow beyond local project artifacts.
