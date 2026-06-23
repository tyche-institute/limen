# Parent source extraction summary

Batch: 20260617T064339Z-lane12-682963e0
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064339Z-lane12-682963e0/input.tsv
Output: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064339Z-lane12-682963e0/parent-source-extraction-results.tsv

Reviewed rows: 24
Verification: output queue_id set and row count match input.tsv; no duplicate queue_id values.

Verdict counts:
- country_gap_no_parent_source: 6
- parent_source_wrapper: 13
- source_surface_only_no_case: 2
- source_url_extracted: 3

Notes:
- Used local input rows, local source context, and local PALLAS ledger/source-pack files only.
- Extracted concrete URLs only where an explicit local URL was present and a single parent/source surface was selected.
- Wrapper verdicts indicate multiple local candidates or broad source-pack context requiring human selection.
- Gap verdicts indicate country/profile/query placeholders without a concrete matching parent source URL for the requested surface.
