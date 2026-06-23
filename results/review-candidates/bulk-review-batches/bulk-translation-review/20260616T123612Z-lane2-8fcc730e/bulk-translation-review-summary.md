# Bulk translation review summary

Batch: `20260616T123612Z-lane2-8fcc730e`

Scope: bounded processing-state review using only local metadata and local source rows. No reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence claim, ranking, publication, upload, or portal interaction was performed.

## Results

- Input rows reviewed: 16
- Output rows written: 16
- Queue IDs: `BTR-00417` through `BTR-00432`

## Verdict counts

- `candidate_for_parent_source_extraction`: 3
- `cross_project_duplicate`: 3
- `source_surface_only_no_case`: 7
- `translation_source_reviewed`: 3

## Review notes

- Most rows remain source-surface/context because the local evidence names official pages, policy pages, searches, or sectoral surfaces without an explicit LIMEN edge-case claim.
- Duplicate surfaces were marked for Garante Privacy (`BTR-00430` duplicate of `BTR-00417`), Strategy.bg (`BTR-00427` duplicate of `BTR-00426`), and AU Continental AI Strategy (`BTR-00432` duplicate of `BTR-00429`).
- Candidate parent-source extraction is limited to source/provenance extraction for official English strategy/framework sources; it is not reviewed-core promotion.
- Translation-sensitive rows were reviewed only at the source-surface level; machine translation was not used to create factual, legal, policy, safety, compliance, prevalence, or ranking claims.

## Verification

- Result TSV header matches required schema.
- Result TSV contains one row per input `queue_id`, with no omissions, extras, or duplicate `queue_id` values.
