# Source review summary

- batch id: 20260614T092802Z-lane07-23eb854e
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 14
  - merge_existing_surface: 12
  - negative_evidence_candidate: 23
  - needs_named_source_extraction: 2
  - translation_review_needed: 0
  - reject_noise: 49
- boundary statement: Local-only source-surface triage. These verdicts classify named surfaces, duplicates, negatives, extraction needs, and noise from local metadata/files only; they do not establish incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Add a pre-triage rule that auto-merges known Helsinki/Kela/Scottish register rows, auto-routes weak-warning and not-found matrix rows to bounded negative evidence, and promotes exact source_title/source_url facts rows straight into source-surface review.
