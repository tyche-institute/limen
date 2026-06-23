# Source review summary

- batch id: 20260614T090245Z-lane15-9726c03b
- rows reviewed: 100
- verdict counts:
  - merge_existing_surface: 19
  - negative_evidence_candidate: 13
  - needs_named_source_extraction: 1
  - reject_noise: 41
  - source_reviewed_candidate: 13
  - translation_review_needed: 13
- boundary statement: Reviewed each queued row exactly once using only local metadata and local source files. This triage classifies source-surface posture only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Add a canonical source_surface_id plus direct_source_url at candidate-generation time so registry-table duplicates and derived wrappers can be merged or rejected before entering the direct-source queue.
