# Source review summary

- batch id: 20260614T092220Z-lane12-14037f3e
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 1
  - merge_existing_surface: 14
  - negative_evidence_candidate: 22
  - needs_named_source_extraction: 8
  - translation_review_needed: 5
  - reject_noise: 50
- boundary statement: Reviewed each input row exactly once using only local metadata and local files for bounded source-surface triage; no incident-truth, legality, compliance, safety, deployment, prevalence, or ranking inference was made, and no public/portal action was taken.
- next smallest queue-hardening move: Canonicalize duplicate Helsinki/Dutch/Scottish register pointers into one surface table, then extract named official surfaces from the remaining country/profile wrapper rows before any deeper review.
