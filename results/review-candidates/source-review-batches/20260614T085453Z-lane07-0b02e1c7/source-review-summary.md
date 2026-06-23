# Source review summary

- batch id: 20260614T085453Z-lane07-0b02e1c7
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 15
  - merge_existing_surface: 26
  - negative_evidence_candidate: 14
  - needs_named_source_extraction: 17
  - translation_review_needed: 5
  - reject_noise: 23
- boundary statement: Local metadata and local source files only. This pass classifies source surfaces, bounded negative evidence, translation-sensitive surfaces, wrapper rows, and internal noise; it does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Extract one named direct source for the highest-yield wrapper bucket first, starting with matrix/summary rows that already expose an official publisher or URL family but not a clean source surface in the queue.
