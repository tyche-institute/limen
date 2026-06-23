# Source review summary

- batch id: 20260614T084857Z-lane12-5d7000be
- rows reviewed: 100
- verdict counts:
  - merge_existing_surface: 27
  - negative_evidence_candidate: 22
  - needs_named_source_extraction: 12
  - reject_noise: 21
  - source_reviewed_candidate: 5
  - translation_review_needed: 13
- boundary statement: Local-only source-surface triage. These verdicts address whether each row exposes a reviewable direct source surface, a bounded negative/gap note, a translation-sensitive official source, an already-modeled local surface, or queue noise. They do not resolve incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Extract named official source URLs/pages from the remaining proxy/synthesis rows first, especially local country/profile summaries and archived snapshot wrappers, so the next pass can shrink the direct-source queue without re-promoting already-modeled registry surfaces.
