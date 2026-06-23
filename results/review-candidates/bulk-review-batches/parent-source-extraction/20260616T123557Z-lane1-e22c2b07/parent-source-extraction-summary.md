# Parent source extraction summary

Batch: 20260616T123557Z-lane1-e22c2b07

Input rows reviewed exactly once: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 5
- parent_source_wrapper: 2
- country_gap_no_parent_source: 14
- source_surface_only_no_case: 3
- duplicate_existing_core: 0
- reject_noise: 0

Method notes:
- Used local metadata, local source files, and adjacent local source-pack/ledger pointers only.
- No web crawl, portal interaction, upload, publication, email, registration, payment, reviewed-core promotion, or substantive incident/legal/safety/compliance finding was performed.
- Extracted URLs only where explicit in local ledgers/source-pack citations: Retraction Watch Crossref GitLab CSV and AESIA guide PDF.
- Country score/profile/research-queue placeholders without a concrete parent URL were kept at `country_gap_no_parent_source`.
- Multi-source wrapper rows were left as `parent_source_wrapper` rather than forcing a singular parent URL.

Verification:
- Queue-id set and row count checked by script after writing results.
