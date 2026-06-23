# Source review summary

- batch id: 20260614T085548Z-lane13-d6161a71
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 14
  - merge_existing_surface: 23
  - negative_evidence_candidate: 30
  - needs_named_source_extraction: 9
  - translation_review_needed: 4
  - reject_noise: 20
- boundary statement: Local metadata and local source files only; no broad web crawl and no incident, legality, compliance, safety, deployment, prevalence, or ranking inferences were made.
- next smallest queue-hardening move: materialize a normalized allowlist of already-modeled registry surfaces (for example CA-AI-REG, NL-ALG-REG, UK-ATRS, SCOT-AI-REG) so future source-review batches can auto-deduplicate them before leasing.
