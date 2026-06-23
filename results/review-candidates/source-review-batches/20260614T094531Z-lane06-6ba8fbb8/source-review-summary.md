# Source review summary

- batch id: 20260614T094531Z-lane06-6ba8fbb8
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 3
  - merge_existing_surface: 15
  - negative_evidence_candidate: 25
  - needs_named_source_extraction: 11
  - translation_review_needed: 2
  - reject_noise: 44
- boundary statement: Local metadata and local source files only; this pass triaged source-surface existence posture only and did not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Pull the needs_named_source_extraction rows into a tiny follow-on pass that extracts one canonical named source page or notice per wrapper row before any further promotion.
