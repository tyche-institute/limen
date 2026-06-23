# Source review summary

- batch id: 20260614T085839Z-lane16-639256ba
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 17
  - merge_existing_surface: 18
  - negative_evidence_candidate: 24
  - needs_named_source_extraction: 2
  - translation_review_needed: 8
  - reject_noise: 31
- boundary statement: Local metadata and local source files only. This pass triaged source-surface existence and queue hygiene; it did not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Deduplicate every CA-AI-REG and NL-ALG-REG duplicate first, then extract concrete named sources only from the small remainder of wrapper or translation-sensitive rows.
