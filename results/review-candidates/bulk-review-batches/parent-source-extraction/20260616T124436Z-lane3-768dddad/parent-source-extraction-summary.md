# Parent source extraction summary

Batch: `20260616T124436Z-lane3-768dddad`

Input rows reviewed: 24
Output rows written: 24

Verdict counts:

- `source_url_extracted`: 3
- `parent_source_wrapper`: 8
- `country_gap_no_parent_source`: 9
- `source_surface_only_no_case`: 4

Verification:

- Reviewed every input queue_id exactly once.
- Used local source files, nearby context, local facts metadata, cache manifest, and local source-ledger pointers only.
- Did not infer URLs from source names.
- Did not web crawl or perform external side effects.
- Results TSV queue_id set and row count were checked against input.tsv.

Extracted URLs:

- BPSE-01729: https://www.kela.fi/tekoalyrekisteri
- BPSE-01734: https://www.edpb.europa.eu/our-work-tools/documents/our-documents_en
- BPSE-01740: https://algoritmes.overheid.nl/en/algoritme/so0760/84321578/chatbot-bo
