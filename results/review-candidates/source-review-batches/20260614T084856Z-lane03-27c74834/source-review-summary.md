# Source review summary

- batch id: 20260614T084856Z-lane03-27c74834
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 16
  - merge_existing_surface: 25
  - negative_evidence_candidate: 23
  - needs_named_source_extraction: 21
  - translation_review_needed: 2
  - reject_noise: 13
- boundary statement: Local-only source-surface triage using row metadata and local files. Verdicts classify only whether a row exposes a reviewable source surface, duplicate, bounded negative-evidence signal, translation dependency, or queue noise. No incident truth, legality, compliance, safety, deployment, prevalence, or ranking inference is made.
- next smallest queue-hardening move: Pre-filter rows that already name NL-ALG-REG/CA-AI-REG/SCOT-AI-REG/UK-ATRS surfaces and auto-drop internal queue/digest/manuscript artifacts before leasing future source-review batches.
