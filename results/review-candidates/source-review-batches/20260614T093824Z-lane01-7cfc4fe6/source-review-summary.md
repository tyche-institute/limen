# Source review summary

- batch id: 20260614T093824Z-lane01-7cfc4fe6
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 6
  - merge_existing_surface: 9
  - negative_evidence_candidate: 33
  - needs_named_source_extraction: 21
  - translation_review_needed: 3
  - reject_noise: 28
- boundary statement: Review used only local metadata and local source files for bounded source-surface triage. These verdicts do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Add an upstream splitter that diverts matrix/summary/manuscript/script/config artifacts into reject_noise, auto-dedupes already-modeled Helsinki/Dutch/algorithmregister surface families, and peels search-target or atlas-wrapper rows into named-source-extraction packets.
