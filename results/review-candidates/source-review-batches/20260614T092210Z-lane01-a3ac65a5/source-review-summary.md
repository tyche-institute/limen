# Source review summary

- batch id: 20260614T092210Z-lane01-a3ac65a5
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 1
  - translation_review_needed: 1
  - needs_named_source_extraction: 17
  - negative_evidence_candidate: 26
  - merge_existing_surface: 12
  - reject_noise: 43
- boundary statement: Reviewed each input row exactly once using only local metadata and local source files; this is source-surface triage only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: extract named direct-source rows from the remaining source-pack/atlas wrappers first, especially repeated Helsinki/Dutch register duplicates and official-source refresh rows that already encode bounded negative evidence.
