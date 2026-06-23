# Source review summary: 20260614T090830Z-lane06-b5ce6182

- batch id: 20260614T090830Z-lane06-b5ce6182
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 6
  - merge_existing_surface: 16
  - negative_evidence_candidate: 22
  - needs_named_source_extraction: 18
  - translation_review_needed: 1
  - reject_noise: 37
- boundary statement: Reviewed each queued row exactly once using local metadata and local files only; this is source-surface triage and does not assert incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: pre-deduplicate known modeled surfaces (for example Helsinki, Dutch Algorithm Register, and Scottish AI Register families) before lease allocation so future source-review batches spend more rows on newly named surfaces.
