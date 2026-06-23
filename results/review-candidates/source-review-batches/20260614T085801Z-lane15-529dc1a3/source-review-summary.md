# Source review summary

- batch id: 20260614T085801Z-lane15-529dc1a3
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 15
  - merge_existing_surface: 24
  - negative_evidence_candidate: 17
  - needs_named_source_extraction: 14
  - translation_review_needed: 8
  - reject_noise: 22
- boundary statement: This batch was limited to local metadata and local source files for source-surface triage only. Verdicts address whether a row exposes a reviewable source surface, duplicate surface, negative-evidence surface, translation-sensitive surface, wrapper/proxy, or queue noise. They do not assess incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: normalize and collapse already-modeled Canada AI Register and Dutch Algorithm Register duplicates upstream so future batches emit one canonical surface row plus explicit wrapper links instead of repeated derivative rows.
