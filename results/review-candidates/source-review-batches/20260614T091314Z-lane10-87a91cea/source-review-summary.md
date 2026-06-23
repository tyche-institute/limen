# Source review summary

- batch id: 20260614T091314Z-lane10-87a91cea
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 7
  - merge_existing_surface: 13
  - negative_evidence_candidate: 27
  - needs_named_source_extraction: 8
  - translation_review_needed: 0
  - reject_noise: 45
- boundary statement: Reviewed each row exactly once using only local metadata and local source files. These verdicts are bounded source-surface triage only and do not assert incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Split future batches upstream into three streams before review: explicit negative-search/gap rows, already-modeled register duplicates, and true named-source candidates. That should shrink manual source-surface triage immediately.
