# Parent source extraction summary

Batch: 20260616T121650Z-lane5-684a7ed3
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T121650Z-lane5-684a7ed3/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T121650Z-lane5-684a7ed3/parent-source-extraction-results.tsv

Reviewed rows: 24
Output rows: 24

Verdict counts:

- source_url_extracted: 3
- parent_source_wrapper: 4
- country_gap_no_parent_source: 17
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Method: inspected each input row once against the cited local path/line and nearby context, then used only local source-refresh/source-pack/ledger metadata when an explicit parent-source pointer was present. No web crawl, portal interaction, publication, upload, email, registration, payment, reviewed-core promotion, ObscureAI addition, incident truth finding, legal finding, safety finding, compliance finding, prevalence claim, or ranking was performed.

Verification: result TSV queue_id set and row count were checked against input.tsv before manifest update.
