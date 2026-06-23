# Source review summary

- batch id: 20260614T090334Z-lane05-043d7fb9
- rows reviewed: 100
- verdict counts:
  - merge_existing_surface: 27
  - negative_evidence_candidate: 28
  - needs_named_source_extraction: 6
  - reject_noise: 18
  - source_reviewed_candidate: 10
  - translation_review_needed: 11
- boundary statement: Reviewed each input row exactly once using only local metadata and local files; this triage covers source-surface existence/posture only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Add a pre-lease split that routes already-modeled registry families, translation-sensitive foreign-language rows, and recurring internal digest/script artifacts out of the direct-source queue before batching.
