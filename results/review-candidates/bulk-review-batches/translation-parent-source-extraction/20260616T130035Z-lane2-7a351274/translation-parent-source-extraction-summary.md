# Translation parent-source extraction summary

Batch: 20260616T130035Z-lane2-7a351274
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260616T130035Z-lane2-7a351274/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260616T130035Z-lane2-7a351274/translation-parent-source-extraction-results.tsv

## Scope

Reviewed all 16 input rows exactly once using local metadata and local source context only. No web crawl, portal form, upload, publication, email, registration, payment, reviewed-core promotion, ObscureAI addition, incident truth finding, legal finding, safety finding, compliance finding, prevalence claim, or ranking was performed.

## Verdict counts

- source_url_extracted: 15
- parent_source_wrapper: 1
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Verification

- Input rows: 16
- Output rows: 16
- Queue-id set check: passed during write; final verification command run after manifest update.
- Notes: BTPS-00020 is a protocol/wrapper row, not a concrete parent source. Pakistan MOITT/AI Week rows expose explicit URLs in local metadata but local body fetches failed, so claim ceilings remain source-surface only.
