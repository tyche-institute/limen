# Source review summary

- batch id: 20260617T072935Z-lane10-1953bc8f
- rows reviewed: 160
- verdict counts:
  - source_reviewed_candidate: 6
  - merge_existing_surface: 13
  - negative_evidence_candidate: 12
  - needs_named_source_extraction: 129
  - translation_review_needed: 0
  - reject_noise: 0
- boundary statement: Reviewed each input row exactly once using local row metadata and local source-path context only. This is source-surface triage only; it does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Split country/query-pack and atlas-dimension rows before batching so only rows with an explicit named source title, issuer, URL, register, notice, or instrument enter direct source review; route weak-source/gap warnings into a separate negative-evidence queue.
