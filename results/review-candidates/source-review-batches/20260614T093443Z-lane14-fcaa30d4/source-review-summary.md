# Source review summary

- batch id: 20260614T093443Z-lane14-fcaa30d4
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 1
  - merge_existing_surface: 9
  - negative_evidence_candidate: 32
  - needs_named_source_extraction: 17
  - translation_review_needed: 5
  - reject_noise: 36
- boundary statement: Local-only source-surface triage completed. Verdicts reflect only whether each row exposes a bounded reviewable source surface, a negative/absence trace, a translation-sensitive candidate, a dedupe target, or queue noise. No incident, legality, compliance, safety, deployment, prevalence, or ranking conclusions were made.
- next smallest queue-hardening move: Extract one named direct source per `needs_named_source_extraction` row, starting with wrapper rows that already contain a named regulator, register, or official title in local metadata.
