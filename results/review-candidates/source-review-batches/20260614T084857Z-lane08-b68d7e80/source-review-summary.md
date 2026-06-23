# Source review summary

- batch id: 20260614T084857Z-lane08-b68d7e80
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 14
  - merge_existing_surface: 29
  - negative_evidence_candidate: 22
  - needs_named_source_extraction: 4
  - translation_review_needed: 3
  - reject_noise: 28
- boundary statement: Reviewed each input row exactly once using only local metadata and local source files; this is source-surface triage only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Extract stable named source surfaces and direct local pointers for the 4 wrapper/proxy rows before promoting any additional source-review candidates.
