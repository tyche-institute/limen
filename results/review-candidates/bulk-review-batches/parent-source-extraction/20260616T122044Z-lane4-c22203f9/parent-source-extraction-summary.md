# Parent Source Extraction Summary

Batch: 20260616T122044Z-lane4-c22203f9
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122044Z-lane4-c22203f9/input.tsv
Output: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122044Z-lane4-c22203f9/parent-source-extraction-results.tsv

Reviewed every input row exactly once using local metadata/source context only. No broad web crawl or external submission actions were performed.

## Counts

- input_rows: 24
- output_rows: 24
- country_gap_no_parent_source: 21
- parent_source_wrapper: 1
- source_url_extracted: 2

## Verification

- Queue ID set match: verified.
- Row count match: verified.
- Duplicate output queue_id values: none.
- Header matches required schema.

## Notes

- Extracted URLs only where explicit local `url`/`source_url` fields were present.
- Country gap/profile/score placeholders without explicit URLs were marked `country_gap_no_parent_source`.
- Source-pack target-evidence wrapper without a chosen parent URL was marked `parent_source_wrapper`.
