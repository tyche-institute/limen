# Parent source extraction summary

Batch: `20260617T064339Z-lane10-cb4a3ada`
Completed at UTC: `2026-06-17T06:45:51Z`

## Scope

- Reviewed every input row exactly once using local metadata/source files only.
- No web crawling, publishing, uploading, submissions, or portal-form use.
- Boundary observed: processing-state review only; no reviewed-core promotion or substantive incident/legal/safety/compliance finding.

## Outputs

- Results TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064339Z-lane10-cb4a3ada/parent-source-extraction-results.tsv`
- Summary: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064339Z-lane10-cb4a3ada/parent-source-extraction-summary.md`

## Verdict counts

- source_url_extracted: 0
- parent_source_wrapper: 3
- country_gap_no_parent_source: 21
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

- Country/query-pack rows were marked `country_gap_no_parent_source` because inspected local rows contain desired search strings and source preferences, not concrete public parent URLs.
- Second-pass/source-refresh rows with multiple local candidate URLs were marked `parent_source_wrapper` rather than forcing a single parent URL.

## Verification

- Result TSV header matches the configured schema.
- One output row was written for each input `queue_id` with no extras, omissions, or duplicate `queue_id` values.
- Queue-id set and row count were verified after writing.
