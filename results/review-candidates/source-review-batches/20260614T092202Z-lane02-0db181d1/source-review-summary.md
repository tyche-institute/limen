# Source review summary

- batch id: 20260614T092202Z-lane02-0db181d1
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 2
  - merge_existing_surface: 11
  - negative_evidence_candidate: 25
  - needs_named_source_extraction: 12
  - translation_review_needed: 8
  - reject_noise: 42
- boundary statement: Review used only local metadata and local source files for bounded source-surface triage. These verdicts do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Add an upstream filter that diverts queue/matrix/summary/warning/config/manuscript artifacts into reject_noise before source-review batch allocation, and auto-merge already-modeled registry families such as Helsinki/Scottish register surfaces.
