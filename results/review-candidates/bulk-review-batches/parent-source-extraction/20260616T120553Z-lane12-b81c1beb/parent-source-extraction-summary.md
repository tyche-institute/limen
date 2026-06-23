# Parent source extraction summary

- Batch: 20260616T120553Z-lane12-b81c1beb
- Input rows reviewed exactly once: 24
- Output rows written: 24
- Verification: result TSV queue_id set and row count match input.tsv
- Boundary: processing-state parent-source triage only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

## Verdict counts
- source_url_extracted: 7
- parent_source_wrapper: 1
- country_gap_no_parent_source: 16

## Notes
- Country research queues, country hardening summaries, matrix rows, and country profile rows were marked country_gap_no_parent_source when no concrete URL was present in the local row/context.
- Extracted URLs came from local GAIA source-resolution appendices or exported source-document/fact ledgers tied to the named local manifest/gap-sprint rows.
- BOSCO was marked parent_source_wrapper because the local case study is a bundle of BOS-001..BOS-016 references, not one selected parent source.
