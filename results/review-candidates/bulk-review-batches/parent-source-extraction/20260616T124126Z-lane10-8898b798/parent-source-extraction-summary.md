# Parent source extraction summary

Batch: 20260616T124126Z-lane10-8898b798
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T124126Z-lane10-8898b798/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T124126Z-lane10-8898b798/parent-source-extraction-results.tsv

Reviewed input rows exactly once: 24
Output rows: 24

Verdict counts:
- source_url_extracted: 3
- parent_source_wrapper: 6
- country_gap_no_parent_source: 9
- source_surface_only_no_case: 5
- duplicate_existing_core: 0
- reject_noise: 1

Verification:
- Output TSV uses the required header.
- Queue_id order, set, and row count match input.tsv.
- Extracted URLs were taken only from explicit local JSON/HTML metadata.
- No web crawl or external submission action was performed.
