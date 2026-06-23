# Source review summary

- batch id: 20260614T093530Z-lane16-56ab11de
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 5
  - merge_existing_surface: 9
  - negative_evidence_candidate: 20
  - needs_named_source_extraction: 29
  - translation_review_needed: 3
  - reject_noise: 34
- boundary statement: Reviewed each input row exactly once using only local metadata and selectively inspected local source lines; this remains source-surface triage only and does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Extract named direct-source targets from the remaining wrapper/proxy rows, starting with high-signal country/profile rows and multilingual official-source records that already carry stable source URLs or titles.
