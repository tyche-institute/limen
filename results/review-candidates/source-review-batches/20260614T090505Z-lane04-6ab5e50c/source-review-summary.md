# Source review summary

- batch id: 20260614T090505Z-lane04-6ab5e50c
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 22
  - merge_existing_surface: 13
  - negative_evidence_candidate: 21
  - needs_named_source_extraction: 17
  - translation_review_needed: 6
  - reject_noise: 21
- boundary statement: Local metadata and local source files only; this pass triages source-surface existence and queue hygiene only, and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Extract named underlying source surfaces from wrapper/summary artifacts first, especially country summaries, review queues, and metadata rows that currently stop at unresolved source references.
