# Source review summary

- batch id: 20260614T094354Z-lane15-a935a391
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 10
  - merge_existing_surface: 7
  - negative_evidence_candidate: 26
  - needs_named_source_extraction: 13
  - translation_review_needed: 4
  - reject_noise: 40
- boundary statement: Local-only source-surface triage completed. Verdicts address whether a row exposes a bounded reviewable source surface in local metadata or local source lines. They do not establish incident truth, legality, compliance, safety, deployment status, prevalence, or ranking.
- next smallest queue-hardening move: Extract named source titles/URLs from the needs_named_source_extraction rows first, then route the translation_review_needed rows through a translation-aware pass.
