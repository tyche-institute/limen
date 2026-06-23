# Source review summary

- batch id: 20260614T094359Z-lane02-9b86b938
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 6
  - merge_existing_surface: 10
  - negative_evidence_candidate: 15
  - needs_named_source_extraction: 8
  - translation_review_needed: 4
  - reject_noise: 57
- boundary statement: Local-only source-surface triage. These verdicts classify source posture and queue fitness only; they do not establish incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Promote the six source_reviewed_candidate rows plus the four translation_review_needed rows into a small canonical-surface ledger, then collapse the ten merge_existing_surface duplicates against those canonicals before further queueing.
