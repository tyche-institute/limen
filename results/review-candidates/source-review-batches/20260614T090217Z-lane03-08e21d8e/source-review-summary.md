# Source review summary

- batch id: 20260614T090217Z-lane03-08e21d8e
- rows reviewed: 100
- verdict counts:
  - merge_existing_surface: 18
  - negative_evidence_candidate: 31
  - needs_named_source_extraction: 8
  - reject_noise: 15
  - source_reviewed_candidate: 18
  - translation_review_needed: 10
- boundary statement: Reviewed each input row exactly once using only local metadata and local files; this triage covers source-surface existence/posture only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Split future queueing earlier between already-modeled registry duplicates, translation-sensitive foreign-language surfaces, and negative/gap evidence so those rows do not re-enter the same direct-source batch.
