# Source review summary

- batch id: 20260617T073137Z-lane19-33bbad88
- rows reviewed: 160
- verdict counts:
  - source_reviewed_candidate: 1
  - merge_existing_surface: 106
  - negative_evidence_candidate: 24
  - needs_named_source_extraction: 27
  - translation_review_needed: 2
  - reject_noise: 0
- boundary statement: Reviewed local row metadata and local source-path posture only. No broad web crawl and no public/portal actions were performed. Verdicts do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Add a pre-source-review dedupe/extraction gate that routes already-modeled registry bulk rows to merge_existing_surface, negative/gap rows to negative_evidence_candidate, and country-profile/source-pack labels to named-source extraction before leasing.
