# Source review summary

- batch id: 20260614T092044Z-lane15-e3703c47
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 4
  - merge_existing_surface: 14
  - negative_evidence_candidate: 26
  - needs_named_source_extraction: 9
  - translation_review_needed: 2
  - reject_noise: 45
- boundary statement: Local-only source-surface triage. Verdicts describe whether a row exposes a reviewable direct-source surface, duplicates an existing modeled surface, records bounded not-found evidence, or is queue noise; they do not establish incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Promote the four source_reviewed_candidate rows into the next bounded direct-source packet, then deduplicate Helsinki/Amsterdam/Dutch-register repeats against the existing surface ledger before leasing more pack-wrapper rows.
