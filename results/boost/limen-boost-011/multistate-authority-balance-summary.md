# limen-boost-011 multistate authority projection

- Source: `multistate-export-validator.tsv`
- Projected lineage total if multistate transport is allowed: 23
- Newly restored omitted rows: 2
- State transport split: multistate=17, single_state=6

## Projected visualization-band counts

- authority_anchor: 8
- provisional_security: 1
- technical_authority: 8
- translation_caution_authority: 1
- translation_caution_provisional: 5

## Primary review-state counts

- identifier_collision_blocker: 5
- no_cluster_review_row: 3
- reviewed_not_duplicate: 8
- stable_duplicate_cluster: 7

## Additional join-hazard state counts

- identifier_collision_blocker: 17
- none: 6

## Restored omitted rows

- `data/cases/authoritative-candidates.jsonl:LIMEN-000008` -> `authority_anchor` with `no_cluster_review_row` + `identifier_collision_blocker`
- `data/cases/security-agentic-candidates.jsonl:LIMEN-000009` -> `technical_authority` with `no_cluster_review_row` + `identifier_collision_blocker`

## Interpretation

- This file is a projection contract for figure/table refresh, not a new legal or incident-strength claim.
- Every restored row still requires normalized record keys and explicit collision badges where `identifier_collision_blocker` travels alongside the primary review state.
- The highest-value use is a shared export patch that separates `primary_review_state` from `additional_join_hazard_state`.
