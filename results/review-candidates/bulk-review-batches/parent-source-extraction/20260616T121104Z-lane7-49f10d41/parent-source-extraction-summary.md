# Parent source extraction summary

Batch: 20260616T121104Z-lane7-49f10d41
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T121104Z-lane7-49f10d41/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T121104Z-lane7-49f10d41/parent-source-extraction-results.tsv

Reviewed rows: 24
Output rows: 24

Verdict counts:
- source_url_extracted: 16
- parent_source_wrapper: 4
- country_gap_no_parent_source: 4
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Verification:
- One output row was written for every input queue_id.
- No duplicate output queue_id values.
- Queue_id set matches input.tsv exactly.
- URLs were extracted only from local source rows, local source-pack/rollup rows, or local seed JSON.
- No web crawl or external submission was performed.
