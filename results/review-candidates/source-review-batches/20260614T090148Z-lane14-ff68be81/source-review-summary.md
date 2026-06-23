# Source review summary

- batch id: 20260614T090148Z-lane14-ff68be81
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 12
  - merge_existing_surface: 26
  - negative_evidence_candidate: 30
  - needs_named_source_extraction: 5
  - translation_review_needed: 3
  - reject_noise: 24
- boundary statement: Reviewed each input row exactly once using only local metadata and local files for bounded source-surface triage; no web crawl, no incident-truth inference, and no legality/compliance/safety/prevalence/ranking claims.
- next smallest queue-hardening move: Pre-dedupe already-modeled NL-ALG-REG and CA-AI-REG rows before leasing future source-review batches so reviewers spend fewer slots on duplicate registry surfaces.
