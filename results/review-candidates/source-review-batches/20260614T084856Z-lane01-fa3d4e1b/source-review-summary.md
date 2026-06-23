# Source review summary

- batch id: 20260614T084856Z-lane01-fa3d4e1b
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 6
  - merge_existing_surface: 34
  - negative_evidence_candidate: 19
  - needs_named_source_extraction: 18
  - translation_review_needed: 7
  - reject_noise: 16
- boundary statement: Reviewed each input row exactly once using local metadata/local files only for bounded source-surface triage. No web crawl or public/portal actions were taken, and verdicts do not assert incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- next smallest queue-hardening move: Split wrapper/aggregate rows into dedicated named-source rows first, then deduplicate already-modeled Dutch/Canada/Helsinki/FCC/GAIA surfaces before sending any remaining direct-source candidates forward.
