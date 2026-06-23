# Source review summary

- batch id: 20260614T092220Z-lane11-9cb89784
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 0
  - merge_existing_surface: 21
  - negative_evidence_candidate: 16
  - needs_named_source_extraction: 14
  - translation_review_needed: 6
  - reject_noise: 43
- boundary statement: Reviewed only local row metadata and limited local source context where already embedded; no web crawling or public/portal actions; verdicts cover source-surface triage only and do not assert incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: materialize named direct-source extraction from wrapper rows first, then deduplicate atlas/registry repeats before sending any new rows into source review.
