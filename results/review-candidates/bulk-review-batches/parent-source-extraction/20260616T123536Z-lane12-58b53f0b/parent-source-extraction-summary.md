# Parent-source extraction summary

Batch: 20260616T123536Z-lane12-58b53f0b
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- parent_source_wrapper: 9
- source_surface_only_no_case: 9
- source_url_extracted: 6

Method:
- Reviewed each input row once against local source_path context and nearby local ledgers/source packs only.
- No broad web crawl, portal interaction, submission, publication, upload, email, registration, payment, or form use.
- Extracted concrete public URLs only where a local source file, local facts/source-document record, completion ledger, or seed object explicitly contained the URL.
- Used parent_source_wrapper where local material pointed to multiple possible parent sources requiring human selection.
- Used source_surface_only_no_case for internal methodology, maintenance, validation, planning, or release-state rows without a concrete public parent source surface.

Verification:
- Result TSV header matches required schema.
- Result TSV row count and queue_id set were checked against input.tsv.
- Boundary preserved: processing-state/source-surface review only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
