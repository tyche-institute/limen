# Parent source extraction summary

Batch: 20260616T122228Z-lane8-8b6000ad
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122228Z-lane8-8b6000ad/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122228Z-lane8-8b6000ad/parent-source-extraction-results.tsv

## Verification

- Input rows reviewed: 24
- Output rows written: 24
- Queue-id set match: yes
- Duplicate output queue_id values: none
- Header matches required schema: yes
- Local-only review: yes; used cited local rows and local source-pack/rollup pointers only.

## Verdict counts

- source_url_extracted: 5
- parent_source_wrapper: 5
- country_gap_no_parent_source: 14
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

Rows marked `source_url_extracted` had concrete URLs explicitly present in local source-pack/rollup records. Rows marked `parent_source_wrapper` exposed multiple possible parent sources or only summarized source examples, requiring human/source-pack selection of one review surface. Rows marked `country_gap_no_parent_source` were country profile, matrix, score, or research-queue placeholders with no single extractable parent URL in the cited local context.

Boundary preserved: processing-state review only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
