# Source review summary

- batch id: 20260614T085249Z-lane09-7eee9661
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 16
  - merge_existing_surface: 14
  - negative_evidence_candidate: 13
  - needs_named_source_extraction: 27
  - translation_review_needed: 6
  - reject_noise: 24
- boundary statement: Local-only source-surface triage. Reviewed local metadata and local files only. No web crawl or public/portal action. Verdicts classify source-surface posture only and do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: materialize a local named-source extraction pass for proxy/queue rows and auto-dedupe known registry families such as NL-ALG-REG and CA-AI-REG before future source-review batching.
