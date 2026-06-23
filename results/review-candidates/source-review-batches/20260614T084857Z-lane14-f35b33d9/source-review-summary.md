# Source review summary

- batch id: 20260614T084857Z-lane14-f35b33d9
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 12
  - merge_existing_surface: 20
  - negative_evidence_candidate: 20
  - needs_named_source_extraction: 9
  - translation_review_needed: 13
  - reject_noise: 26
- boundary statement: Reviewed every input row exactly once using only local metadata and local source files. This is source-surface triage only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Extract named direct-source surfaces from the remaining local source-pack/summary proxies, then rerun bounded dedupe against already-modeled registry surfaces before any new promotion.
