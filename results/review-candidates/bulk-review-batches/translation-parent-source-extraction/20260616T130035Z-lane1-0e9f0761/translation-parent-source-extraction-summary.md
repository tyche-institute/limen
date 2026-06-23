# Translation parent-source extraction summary

Batch: 20260616T130035Z-lane1-0e9f0761
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260616T130035Z-lane1-0e9f0761/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260616T130035Z-lane1-0e9f0761/translation-parent-source-extraction-results.tsv

## Verification

- Input rows reviewed: 16
- Output rows written: 16
- Queue ID set match: yes
- Duplicate output queue_id values: no
- Header matches configured schema: yes
- Local-only review: yes; used input metadata and local source-file context only.

## Verdict counts

- source_url_extracted: 14
- parent_source_wrapper: 2
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

- Wrapper rows were kept bounded to processing-state review and marked `parent_source_wrapper` where a local source/index listed multiple possible parent sources requiring human selection.
- No reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking was made.
