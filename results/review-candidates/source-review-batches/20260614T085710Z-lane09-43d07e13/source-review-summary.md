# Source review summary

- batch id: 20260614T085710Z-lane09-43d07e13
- rows reviewed: 100
- verdict counts:
  - merge_existing_surface: 10
  - needs_named_source_extraction: 9
  - negative_evidence_candidate: 31
  - reject_noise: 28
  - source_reviewed_candidate: 11
  - translation_review_needed: 11
- boundary statement: Local-only source-surface triage. This batch classifies named direct surfaces, wrappers, negative/gap signals, translation-sensitive rows, duplicate existing surfaces, and internal noise without inferring incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Extract named direct-source targets from wrapper/proxy rows first, then deduplicate already-modeled registry surfaces before sending any remainder to translation-aware review.
