# Source review summary

- batch id: 20260614T090941Z-lane13-de1c341d
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 4
  - merge_existing_surface: 12
  - negative_evidence_candidate: 19
  - needs_named_source_extraction: 11
  - translation_review_needed: 2
  - reject_noise: 52
- boundary statement: Reviewed each input row exactly once using only local metadata and local source files. This is source-surface triage only; no incident-truth, legality, compliance, safety, deployment, prevalence, or ranking claims were inferred.
- next smallest queue-hardening move: Extract named direct-source rows from the remaining local wrappers/claim-support proxies, starting with prior-batch wrapper rows and vendor/legal metadata that already point toward specific source families.
