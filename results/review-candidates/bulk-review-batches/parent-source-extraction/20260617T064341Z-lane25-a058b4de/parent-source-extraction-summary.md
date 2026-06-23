# Parent source extraction summary: 20260617T064341Z-lane25-a058b4de

Completed: 2026-06-17T06:45:41Z
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064341Z-lane25-a058b4de/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064341Z-lane25-a058b4de/parent-source-extraction-results.tsv

## Scope

Reviewed every input row exactly once using local metadata and local source-file context only. No web crawling or external source discovery was performed. This batch is processing-state review only and makes no incident/legal/safety/compliance/prevalence/ranking claims.

## Verdict counts

- country_gap_no_parent_source: 24
- source_url_extracted: 0
- parent_source_wrapper: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

All 24 rows were country query-pack, atlas profile, score, or gap-summary placeholders. Local evidence did not expose a concrete original public parent-source URL for the queued signal. For rows that contained nearby atlas source lists, those sources were adjacent general profile evidence and did not explicitly identify an AI-specific parent source URL for the queued gap signal.

## Verification

The result TSV was written with the configured header and one row per input queue_id. Queue-id set and row-count parity were checked after writing.
