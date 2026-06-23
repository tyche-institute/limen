# translation-parent-source-extraction summary

Batch: 20260617T064827Z-lane1-13f313a7
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260617T064827Z-lane1-13f313a7/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260617T064827Z-lane1-13f313a7/translation-parent-source-extraction-results.tsv

Processed rows: 7
Output rows: 7
Verdicts:
- source_url_extracted: 7
- parent_source_wrapper: 0
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Method:
- Reviewed each input row exactly once against local metadata/source context.
- Used only local source-pack rows, local ledgers, and local extracted line context.
- Extracted a concrete public URL only where explicitly present in local metadata or source-pack/ledger pointers.
- No web crawling, publishing, uploading, forms, promotion, or substantive incident/legal/safety findings.

Verification:
- Queue-id set and row count were checked against input.tsv after writing.
- All output rows preserve the configured header and one row per input queue_id.
