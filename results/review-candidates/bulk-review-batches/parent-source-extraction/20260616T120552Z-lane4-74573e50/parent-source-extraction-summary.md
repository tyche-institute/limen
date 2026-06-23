# Parent source extraction summary

Batch: 20260616T120552Z-lane4-74573e50
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- country_gap_no_parent_source: 7
- parent_source_wrapper: 12
- source_surface_only_no_case: 1
- source_url_extracted: 4

Boundary notes:
- Used local metadata, local source context, and local source-pack/ledger pointers only.
- No web crawl, portal interaction, upload, publication, registration, payment, or legal/safety/compliance finding was performed.
- Extracted URLs are processing-state parent-source recoveries only; all substantive claims remain at the row claim ceilings.

Verification:
- Result TSV header matches the required schema.
- One result row was written for every input queue_id, in input order.
- Queue_id set and row count were verified equal before manifest update.
