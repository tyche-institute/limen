# Parent source extraction summary: 20260616T123325Z-lane9-b1b8fb72

Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 1
- parent_source_wrapper: 2
- country_gap_no_parent_source: 15
- source_surface_only_no_case: 6

Concrete URLs extracted:
- BPSE-01313: https://www.kela.fi/tekoalyrekisteri

Method notes:
- Used local metadata and local source files only.
- Rows that were country score/profile/research-queue placeholders without an explicit URL were marked `country_gap_no_parent_source`.
- Rows that aggregated multiple possible source families/targets without a selected parent were marked `parent_source_wrapper`.
- Methodology/style/aggregate rows with no standalone case URL were marked `source_surface_only_no_case`.
- No reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim is made.

Verification:
- Result TSV header matches required schema.
- Result TSV queue_id set and row count were verified against input.tsv.
