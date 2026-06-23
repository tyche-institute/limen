# Source review summary: 20260614T090358Z-lane01-ab4c9257

- batch id: 20260614T090358Z-lane01-ab4c9257
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 16
  - merge_existing_surface: 19
  - negative_evidence_candidate: 23
  - needs_named_source_extraction: 20
  - translation_review_needed: 2
  - reject_noise: 20
- boundary statement: Reviewed each input row exactly once using only local metadata and local files. This is source-surface triage only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Normalize canonical dedupe keys for already-modeled register families (for example NL-ALG-REG and CA-AI-REG) at batch-allocation time so duplicate local registry rows are filtered before entering source review.
