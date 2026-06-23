# Source review summary

- batch id: 20260614T084857Z-lane10-13f07521
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 15
  - merge_existing_surface: 18
  - negative_evidence_candidate: 31
  - needs_named_source_extraction: 4
  - translation_review_needed: 5
  - reject_noise: 27
- boundary statement: Local-only source-surface triage. Reviewed each input row exactly once using local row metadata and local file references only; no web crawl and no claims about incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Resolve the needs_named_source_extraction rows into named direct surfaces first, then dedupe remaining register clones against existing modeled Canada/Dutch/Scottish/UK surfaces.
