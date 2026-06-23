# Source review summary

- batch id: 20260614T091506Z-lane04-b28f3389
- rows reviewed: 100
- verdict counts:
  - merge_existing_surface: 17
  - needs_named_source_extraction: 10
  - negative_evidence_candidate: 21
  - reject_noise: 42
  - source_reviewed_candidate: 9
  - translation_review_needed: 1
- boundary statement: Local-only source-surface triage. This pass classifies source-surface posture only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Pre-filter derived drafts/configs and deduplicate known registry families (Helsinki, Scottish, Dutch/Amsterdam) before batching so reviewers spend the next pass only on named direct surfaces and true negative-evidence rows.
