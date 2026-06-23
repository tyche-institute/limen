# Source review summary

- batch id: 20260614T090701Z-lane15-9027a707
- rows reviewed: 100
- verdict counts:
  - merge_existing_surface: 19
  - negative_evidence_candidate: 17
  - needs_named_source_extraction: 6
  - reject_noise: 48
  - source_reviewed_candidate: 7
  - translation_review_needed: 3
- boundary statement: Reviewed each queued row exactly once using only local metadata and local source files. This triage classifies source-surface posture only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Add a canonical source_surface_id plus direct_source_url at candidate-generation time so registry-table duplicates, gap summaries, and internal manuscript wrappers can be merged or rejected before entering the direct-source queue.
