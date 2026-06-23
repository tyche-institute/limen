# Source review batch summary

- batch id: 20260614T093249Z-lane11-9e1fd811
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 2
  - merge_existing_surface: 16
  - negative_evidence_candidate: 23
  - needs_named_source_extraction: 6
  - translation_review_needed: 3
  - reject_noise: 50
- boundary statement: Local metadata and local source files only. This pass triaged source-surface existence/posture, deduplication, translation sensitivity, proxy extraction needs, and negative-evidence notes only; it did not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Extract named titles and canonical URLs first from the remaining proxy/wrapper rows, then send only those materialized direct surfaces back into bounded source review.
