# Named URL extraction summary

- Batch id: 20260616T112020Z-lane5-9a675284
- Rows reviewed: 15

## Verdict counts

- url_extracted: 13
- source_path_is_snapshot_only: 0
- wrapper_needs_parent_source: 1
- duplicate_or_existing_core: 1
- reject_noise: 0

## Boundary statement

Reviewed each input row exactly once using local metadata, local source files, and nearby relevant context only. No broad web crawl and no public/portal action was performed. URLs were recovered only where an explicit local URL or local source-pack locator was present; otherwise the row was kept as wrapper/lineage status. No incident truth, legality, compliance, safety, deployment, prevalence, or ranking inference is made.

## Next smallest hardening move

Resolve the single paired wrapper row (`SRPH-01101`) against its parent source-ledger IDs (`src-014`, `src-008`, `src-026`) and choose one route-specific URL per downstream claim surface before any reviewed-core promotion.
