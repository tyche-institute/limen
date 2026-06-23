# Source review summary

- batch id: 20260614T090101Z-lane13-3ac69280
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 8
  - merge_existing_surface: 16
  - negative_evidence_candidate: 35
  - needs_named_source_extraction: 5
  - translation_review_needed: 10
  - reject_noise: 26
- boundary statement: Reviewed each input row exactly once using only local metadata and local source files. This is source-surface triage only; no incident-truth, legality, compliance, safety, deployment, prevalence, or ranking claims were inferred.
- next smallest queue-hardening move: Extract named direct-source rows for the few remaining wrappers/proxies, starting with MAS sandbox, the unnamed government API/developer-doc surface, and the curated wrapper rows.
