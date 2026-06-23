# Source review summary

- batch id: 20260614T092756Z-lane06-99f4ca02
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 3
  - merge_existing_surface: 12
  - negative_evidence_candidate: 18
  - needs_named_source_extraction: 31
  - translation_review_needed: 2
  - reject_noise: 34
- boundary statement: Local metadata and local source files only; this pass classified source-surface posture and bounded existence cues only, with no claim about incident truth, legality, compliance, safety, deployment, prevalence, completeness, or ranking.
- next smallest queue-hardening move: Pull the needs_named_source_extraction rows through one narrow local packet-extraction pass to promote only rows that expose a named official source URL/title and demote the rest to duplicate/negative/noise buckets.
