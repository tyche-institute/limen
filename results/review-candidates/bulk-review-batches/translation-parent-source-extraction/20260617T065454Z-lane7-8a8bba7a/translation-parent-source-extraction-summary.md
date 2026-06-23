# Translation parent source extraction summary

Batch: 20260617T065454Z-lane7-8a8bba7a
Task: translation-parent-source-extraction
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260617T065454Z-lane7-8a8bba7a/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260617T065454Z-lane7-8a8bba7a/translation-parent-source-extraction-results.tsv

## Outcome

- Input rows reviewed exactly once: 2
- Output rows written: 2
- source_url_extracted: 2
- parent_source_wrapper: 0
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Row notes

- BTPS-00123 / LIMEN-SIGNAL-926A52050896F7C8: extracted the concrete Ísland.is public URL from local translation/source-refresh metadata. Claim ceiling remains source-surface/sandbox-pilot only with current-status caveat.
- BTPS-00124 / LIMEN-SIGNAL-CCACC40DBF8AE9A9: extracted the concrete CNIL public URL from local source-pack row 2145 and local translation ledger. Adjacent line 2144 is a related bilan source, but the reviewed row points to the sandbox notice URL.

## Verification

- Used local metadata/source files only; no web crawl or external portal action.
- Result TSV uses the configured header and allowed verdicts.
- Queue-id set and row count verification completed by script after writing.
