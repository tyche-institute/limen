# Source review summary

- batch id: 20260614T085717Z-lane14-fa1d04c2
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 8
  - merge_existing_surface: 17
  - negative_evidence_candidate: 27
  - needs_named_source_extraction: 11
  - translation_review_needed: 6
  - reject_noise: 31
- boundary statement: Local-only source-surface triage was applied to each row exactly once. Verdicts stay at source-surface existence, dedupe, translation sensitivity, wrapper extraction, negative-evidence handling, or queue-noise removal only; no incident-truth, legality, compliance, safety, deployment, prevalence, or ranking inference was made.
- next smallest queue-hardening move: Extract named direct-source surfaces from the remaining proxy/wrapper rows first, then deduplicate any newly resolved surfaces against the already-modeled Dutch, UK, and Canada registry surfaces before promotion.
