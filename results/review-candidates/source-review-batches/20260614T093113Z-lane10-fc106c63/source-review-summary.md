# Source review summary

- batch id: 20260614T093113Z-lane10-fc106c63
- rows reviewed: 100
- verdict counts:
  - merge_existing_surface: 14
  - needs_named_source_extraction: 10
  - negative_evidence_candidate: 25
  - reject_noise: 42
  - source_reviewed_candidate: 7
  - translation_review_needed: 2
- boundary statement: Reviewed each input row exactly once using only local row metadata and local files. This pass classifies source-surface posture only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Pull the needs_named_source_extraction rows into a tiny follow-on resolver pass that extracts one canonical named direct surface per row before any further promotion.
