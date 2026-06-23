# Source review summary

- batch id: 20260614T093104Z-lane02-8fdc7260
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 6
  - merge_existing_surface: 10
  - negative_evidence_candidate: 24
  - needs_named_source_extraction: 19
  - translation_review_needed: 2
  - reject_noise: 39
- boundary statement: Review used only local metadata and local source files for bounded source-surface triage. These verdicts do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Add an upstream splitter that diverts matrix/summary/manuscript/script/config artifacts into reject_noise before batching, auto-dedupes already-modeled Helsinki/Dutch/Kela register families, and peels research-queue rows into named-source-extraction packets.
