# Source review summary

- batch id: 20260614T090548Z-lane03-21b05467
- rows reviewed: 100
- verdict counts:
  - source_reviewed_candidate: 3
  - merge_existing_surface: 11
  - negative_evidence_candidate: 13
  - needs_named_source_extraction: 19
  - translation_review_needed: 7
  - reject_noise: 47
- boundary statement: Boundary: local metadata and local source files only; no broad web crawl and no incident/compliance/safety/prevalence inference.
- next smallest queue-hardening move: Next smallest queue-hardening move: extract named direct sources from the local wrapper/summary rows with verdict needs_named_source_extraction, starting with regulator/sandbox rows that already name an institution.

Verification:
- result rows == input rows: True (100/100)
- signal_id set match: True
- duplicate result ids: 0
