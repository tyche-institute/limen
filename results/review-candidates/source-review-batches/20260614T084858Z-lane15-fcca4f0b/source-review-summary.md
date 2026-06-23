# Source review summary

- batch id: 20260614T084858Z-lane15-fcca4f0b
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 7
  - merge_existing_surface: 25
  - negative_evidence_candidate: 30
  - needs_named_source_extraction: 8
  - translation_review_needed: 7
  - reject_noise: 23
- boundary statement: Local metadata and local source files only. This pass triaged source-surface existence and queue hygiene; it did not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Deduplicate all rows that point to already-modeled registry surfaces first (especially CA-AI-REG and NL-ALG-REG), then re-run source extraction only for the remaining wrapper rows.
