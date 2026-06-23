# Named URL extraction summary: 20260616T112143Z-lane3-d710cda1

- batch id: 20260616T112143Z-lane3-d710cda1
- rows reviewed: 15
- verdict counts:
  - url_extracted: 15
  - source_path_is_snapshot_only: 0
  - wrapper_needs_parent_source: 0
  - duplicate_or_existing_core: 0
  - reject_noise: 0

Boundary statement: This batch used local metadata and local source context only. It recovered explicit public URL strings where present in local source ledgers, sidecar link lists, source refresh files, or nearby records. It does not make incident-truth, legality, compliance, safety, deployment, prevalence, maturity, ranking, or register-completeness claims.

Next smallest hardening move: Backfill these extracted URLs into the named-source/source-ledger rows that lacked URL fields, then run a narrow duplicate-lineage check for repeated Swiss, Belgium, Canada, and AESIA surfaces before any reviewed-core promotion.
