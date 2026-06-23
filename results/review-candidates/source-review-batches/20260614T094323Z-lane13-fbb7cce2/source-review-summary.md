# Source review summary

- batch id: 20260614T094323Z-lane13-fbb7cce2
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 10
  - merge_existing_surface: 7
  - negative_evidence_candidate: 20
  - needs_named_source_extraction: 15
  - translation_review_needed: 1
  - reject_noise: 47
- boundary statement: Local-only source-surface triage. Verdicts address whether a row exposes a reviewable source surface, duplicate, wrapper, translation-sensitive item, negative-evidence record, or noise artifact. They do not adjudicate incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Extract named official/regulator/procurement URLs from the remaining wrapper/source-pack rows so the next batch shrinks the needs_named_source_extraction bucket.
