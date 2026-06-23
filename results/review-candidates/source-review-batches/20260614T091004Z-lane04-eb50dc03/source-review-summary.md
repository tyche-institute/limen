# Source review summary

- batch id: 20260614T091004Z-lane04-eb50dc03
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 4
  - merge_existing_surface: 13
  - negative_evidence_candidate: 26
  - needs_named_source_extraction: 21
  - translation_review_needed: 2
  - reject_noise: 34
- boundary statement: Local metadata and local source files only. This pass triaged source-surface existence and reviewability only; it did not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Route already-modeled Helsinki/Dutch/ANPD/Scottish duplicates to dedupe, and siphon matrix/summary negative-evidence rows into a separate negative-evidence queue before the next source-review batch.
