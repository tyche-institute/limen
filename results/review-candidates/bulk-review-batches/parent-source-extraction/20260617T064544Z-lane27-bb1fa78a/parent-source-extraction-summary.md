# Parent source extraction summary

- Batch: `20260617T064544Z-lane27-bb1fa78a`
- Input rows reviewed exactly once: 24
- Output rows written: 24
- Result TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064544Z-lane27-bb1fa78a/parent-source-extraction-results.tsv`

## Verdict counts
- `country_gap_no_parent_source`: 23
- `source_surface_only_no_case`: 1

## Review boundary
Used local metadata and local cited source context only. No web crawl or external submission/action was performed. No URLs were invented from source names.

## Findings
- The research-queue rows are country/profile/search-target placeholders listing queries and desired source classes, not concrete public parent-source URLs.
- The Belize weak-source warning heading contains no explicit parent URL at the cited line or nearby context inspected for this batch.
- Therefore no `source_url_extracted` rows were produced in this bounded batch.

## Verification
- Result TSV header matches the configured schema.
- Queue-id set and row count were verified against input.tsv.
- One output row per input queue_id; no omissions, extras, or duplicate queue_id values.
