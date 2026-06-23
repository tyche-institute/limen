# Parent-source extraction summary

Batch: `20260616T121256Z-lane6-35af36d3`

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T121256Z-lane6-35af36d3/input.tsv`

Outputs:
- `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T121256Z-lane6-35af36d3/parent-source-extraction-results.tsv`
- `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T121256Z-lane6-35af36d3/parent-source-extraction-summary.md`

## Verification

- Input rows reviewed: 24
- Output rows written: 24
- Queue-id set match: yes
- Duplicate output queue_id values: none
- Header matches required schema: yes
- Boundary: processing-state parent-source URL triage only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

## Verdict counts

- source_url_extracted: 7
- parent_source_wrapper: 2
- country_gap_no_parent_source: 15
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

Rows marked `source_url_extracted` use only explicit URLs found in local source context, local source-refresh/source-pack CSVs, or local Gaia ledger exports. Generic country research-queue/profile/score placeholders with no concrete URL were marked `country_gap_no_parent_source`. Wrapper rows with multiple plausible parent sources were marked `parent_source_wrapper`.
