# Source review summary

- batch id: 20260614T094052Z-lane16-0776410c
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 2
  - merge_existing_surface: 11
  - negative_evidence_candidate: 24
  - needs_named_source_extraction: 11
  - translation_review_needed: 5
  - reject_noise: 47
- boundary statement: Reviewed each input row exactly once using only local metadata and local source files; this is bounded source-surface triage only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Deduplicate Dutch/Helsinki registry surfaces into their canonical local records, then extract named authority-owned sources from the remaining proxy and multilingual rows.
