# Source review summary

- batch id: 20260617T063958Z-lane08-b4ecfc82
- rows reviewed: 160
- verdict counts:
  - source_reviewed_candidate: 8
  - merge_existing_surface: 2
  - negative_evidence_candidate: 39
  - needs_named_source_extraction: 105
  - translation_review_needed: 6
  - reject_noise: 0
- boundary statement: Used local row metadata and local source-surface snippets only. This was source-surface triage only; no incident truth, legality, compliance, safety, deployment, prevalence, or ranking claims were inferred.
- next smallest queue-hardening move: Split generic research-queue/profile rows from named source-pack rows before batching, and add a pre-batch flag for negative/gap evidence so direct-source review queues contain only named reviewable surfaces.
