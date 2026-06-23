# Parent source extraction summary

Batch: 20260617T073315Z-lane4-7d3dbc5d
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073315Z-lane4-7d3dbc5d/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073315Z-lane4-7d3dbc5d/parent-source-extraction-results.tsv

Rows reviewed: 24
Output rows: 24

Verdict counts:
- country_gap_no_parent_source: 8
- parent_source_wrapper: 15
- source_url_extracted: 1

Method:
- Reviewed each input row once against local source_path/source_line context.
- Used local research-queue rows and atlas top_sources only; no web crawl or external portal action.
- Extracted a URL only when a nearby atlas top_sources entry explicitly carried the matching indicator_id for the requested parent-source topic.
- Marked jurisdiction/query packs as parent_source_wrapper because they list multiple target source classes rather than a concrete parent source.
- Marked atlas indicator/profile rows without a matching explicit top_sources URL as country_gap_no_parent_source.

Verification:
- Result TSV header matches the configured schema.
- Result TSV row count and queue_id set are verified by the companion script/check below and manifest status.
