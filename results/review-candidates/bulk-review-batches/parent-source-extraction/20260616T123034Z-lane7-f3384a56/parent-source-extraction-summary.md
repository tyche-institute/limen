# Parent source extraction summary — 20260616T123034Z-lane7-f3384a56

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T123034Z-lane7-f3384a56/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T123034Z-lane7-f3384a56/parent-source-extraction-results.tsv`

## Verification

- Input data rows: 24
- Output data rows: 24
- Queue ID set match: yes
- Duplicate output queue IDs: no
- Header matches required schema: yes
- Embedded tabs/newlines inside fields: none detected
- Scope: local metadata/source files/source-pack or ledger pointers only; no web crawl or portal actions.

## Verdict counts

- country_gap_no_parent_source: 4
- parent_source_wrapper: 9
- reject_noise: 2
- source_surface_only_no_case: 5
- source_url_extracted: 4

## Extracted URLs

- BPSE-01154: https://legislation.mt/eli/ln/2025/226/eng — Artificial Intelligence Regulations, 2025 - AI regulatory sandbox
- BPSE-01162: https://www.sainthelena.gov.sh/ — Official site keyword checks for sandbox/artificial intelligence/algorithm
- BPSE-01166: https://www.digdir.no/kunstig-intelligens/digdir-lanserer-tverrsektoriell-oversikt-over-offentlig-ki-bruk/4331 — Digdir lanserer tverrsektoriell oversikt over offentlig KI-bruk
- BPSE-01173: https://bsl.gov.sl/BSL_Sandbox_Program.html — Bank of Sierra Leone official sandbox page

## Notes

Rows marked `parent_source_wrapper` expose multiple local parent candidates or source-family parents and need a human/source-review step to choose a single surface. Rows marked `country_gap_no_parent_source` are country profile/score placeholders without a concrete extractable parent source URL on the reviewed row. No reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking was made.
