# Named URL extraction summary: 20260616T111210Z-lane4-bf2e2ece

- batch id: 20260616T111210Z-lane4-bf2e2ece
- rows reviewed: 15

## Verdict counts

- url_extracted: 14
- wrapper_needs_parent_source: 1
- source_path_is_snapshot_only: 0
- duplicate_or_existing_core: 0
- reject_noise: 0

## Boundary statement

Used local metadata, local source files, and nearby relevant context only. No broad web crawl and no public/portal action. URL extraction is source-surface hardening only; it does not infer incident truth, legality, compliance, safety, deployment, prevalence, ranking, or sandbox effectiveness.

## Next smallest hardening move

Split the one wrapper row (SRPH-00951) into parent source-record extractions for src-001, src-002, and src-003, then assign one direct URL per parent source instead of one URL for the readiness-table wrapper.
