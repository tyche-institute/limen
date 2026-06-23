# Source review summary

- batch id: 20260614T093617Z-lane05-4b06354f
- rows reviewed: 100
- verdict counts:
  - merge_existing_surface: 17
  - needs_named_source_extraction: 15
  - negative_evidence_candidate: 21
  - reject_noise: 39
  - source_reviewed_candidate: 7
  - translation_review_needed: 1
- boundary statement: Local-only source-surface triage using row metadata and selected local source context. No web crawl, no incident-truth inference, no legality/compliance/safety/deployment/prevalence/ranking claims, and no public/portal actions.
- next smallest queue-hardening move: Deduplicate known Helsinki, Scottish, Dutch, and Kela register surfaces before the next batch, then auto-route country-queue wrappers and weak-source warnings into extraction vs bounded-negative lanes.
