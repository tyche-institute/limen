# Source review summary

- batch id: 20260614T094346Z-lane04-184a11d5
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 6
  - merge_existing_surface: 7
  - negative_evidence_candidate: 24
  - needs_named_source_extraction: 16
  - translation_review_needed: 2
  - reject_noise: 45
- boundary statement: Reviewed each input row exactly once using only local row metadata and local source files; this is bounded source-surface triage only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Promote the named official surfaces, dedupe the already-modeled Helsinki/Amsterdam registry surfaces, and run a narrow follow-up pass to extract named sources from research-queue and country-wrapper rows.
