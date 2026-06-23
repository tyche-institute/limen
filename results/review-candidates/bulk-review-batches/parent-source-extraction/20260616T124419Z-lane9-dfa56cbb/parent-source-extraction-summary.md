# Parent source extraction summary

Batch: 20260616T124419Z-lane9-dfa56cbb
Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T124419Z-lane9-dfa56cbb/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T124419Z-lane9-dfa56cbb/parent-source-extraction-results.tsv`

Reviewed every input row exactly once using local metadata/source files and local ledgers/source-pack pointers only. No web crawl or portal interaction was used.

## Counts by verdict

- country_gap_no_parent_source: 8
- parent_source_wrapper: 2
- source_surface_only_no_case: 2
- source_url_extracted: 12

## Verification

- Input data rows: 24
- Output data rows: 24
- Queue ID set: verified equal
- Duplicate output queue IDs: none
- Header: exact required parent-source-extraction-results.tsv header
- Boundary: processing-state/source-surface review only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
