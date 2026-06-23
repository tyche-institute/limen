# Parent source extraction summary — 20260618T140013Z-lane1-402ec66a

Completed at: 2026-06-18T14:06:32Z

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260618T140013Z-lane1-402ec66a/input.tsv`
Result TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260618T140013Z-lane1-402ec66a/parent-source-extraction-results.tsv`

## Verification

- Input data rows: 1
- Output data rows: 1
- Queue-id set: identical
- Duplicate output queue_id values: none
- Boundary: local metadata/local source context only; no web crawl, submission, upload, publication, email, registration, payment, or portal/form action.

## Verdict counts

- source_url_extracted: 1
- parent_source_wrapper: 0
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

- BPSE-03652 / LIMEN-SIGNAL-297D5294C717008C: extracted the explicitly listed C2PA 2.2 technical specification URL from local source context (`sources.md:1096`) and corroborating local review metadata (`source-review-input.tsv:16`).
