# Source review summary

- batch id: 20260614T093855Z-lane14-362ca5ae
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 3
  - merge_existing_surface: 12
  - negative_evidence_candidate: 25
  - needs_named_source_extraction: 10
  - translation_review_needed: 1
  - reject_noise: 49
- boundary statement: Reviewed each queued row exactly once using only local row metadata and local source files where needed. This is source-surface triage only and does not assert incident truth, legality, compliance, safety, deployment status, prevalence, or ranking.
- next smallest queue-hardening move: Deduplicate already-modeled Helsinki/Dutch/Scottish/atlas surfaces first, then run a narrow named-source extraction pass over the remaining country-profile and wrapper rows.
