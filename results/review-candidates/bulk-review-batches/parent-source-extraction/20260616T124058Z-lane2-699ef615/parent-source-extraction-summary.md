# Parent source extraction summary

Batch: 20260616T124058Z-lane2-699ef615

Input rows reviewed exactly once: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 6
- parent_source_wrapper: 5
- country_gap_no_parent_source: 9
- source_surface_only_no_case: 4
- duplicate_existing_core: 0
- reject_noise: 0

Method notes:
- Used local metadata, local source files, nearby context, and local source-pack/ledger pointers only.
- No web crawl, portal interaction, upload, publication, email, registration, payment, reviewed-core promotion, ObscureAI addition, or substantive incident/legal/safety/compliance finding was performed.
- Extracted URLs only where explicit in local source objects or local ledger/source-pack citations: Bank of Tanzania sandbox, Pakistan MOITT AI policy material, Barbados FSC sandbox, Retraction Watch Crossref GitLab CSV, Israel AI Policy 2023 PDF, and Paris algorithm-register dataset.
- Country score/profile/research-queue/mission placeholders without concrete parent URLs were kept at `country_gap_no_parent_source`.
- Multi-source aggregate/wrapper rows were kept as `parent_source_wrapper` rather than forcing a singular parent URL.

Verification:
- Queue-id set and row count checked by script after writing results.
