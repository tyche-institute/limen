# LIMEN Candidate Review Rollup

Generated UTC: 2026-06-23T19:57:04Z

Policy: all materialized review candidates receive deterministic first-pass review.

- Candidate rows: `55725`
- First-pass reviewed rows: `55725`
- Direct-source review queue rows: `13918`
- Review output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/full-first-pass-review.tsv`
- Direct-source queue: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/direct-source-review-queue.tsv`

## Verdict Counts

- `hold_low_relevance`: `1773`
- `hold_needs_direct_source`: `5761`
- `hold_needs_human_translation`: `554`
- `merge_with_existing_surface`: `21572`
- `promote_to_source_review`: `7603`
- `reject_as_cross_project_noise`: `18462`

## Candidate Role Counts

- `derivative_or_existing_surface`: `21501`
- `direct_surface_candidate`: `7603`
- `existing_reviewed_core_echo`: `71`
- `internal_backup_or_script_echo`: `1707`
- `internal_derivative_noise`: `16755`
- `low_priority_signal`: `1773`
- `needs_source_resolution`: `5761`
- `translation_sensitive_candidate`: `554`

## Source-Review Batches

- Completed source-review batches: `239`
- Source-review rows completed: `24880`
- Latest source-review batch: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/source-review-batches/20260618T132100Z-lane02-19a87176`

### Source-Review Verdict Counts

- `merge_existing_surface`: `3932`
- `needs_named_source_extraction`: `6846`
- `negative_evidence_candidate`: `5074`
- `reject_noise`: `6535`
- `source_reviewed_candidate`: `1646`
- `translation_review_needed`: `847`

## Boundary

first-pass review is triage only; it is not reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, or ranking
