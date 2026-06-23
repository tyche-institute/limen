# Named URL extraction summary

- batch id: 20260616T111210Z-lane8-e2092942
- rows reviewed: 15
- verdict counts:
  - url_extracted: 15

## Boundary statement

Reviewed each input row exactly once using only local metadata, local source-cache manifests, cached HTML source context, and local PALLAS source-refresh/rollup files. No broad web crawl or public/portal action was performed. Output recovers explicit public URLs only where locally present and preserves a source-surface-only claim ceiling; it does not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.

## Next smallest hardening move

Run a bounded direct-source posture review for the extracted URLs, prioritizing rows whose recovered URL came from source-refresh rollups rather than the row's immediate source line, and preserve negative/sectoral caveats in the source ledger.

## Verification

Input row count: 15. Result row count: 15. Row_id set matches input exactly; no duplicate row_id values.
