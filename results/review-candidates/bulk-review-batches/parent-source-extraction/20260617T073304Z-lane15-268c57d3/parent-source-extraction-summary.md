# Parent source extraction summary — 20260617T073304Z-lane15-268c57d3

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073304Z-lane15-268c57d3/input.tsv`
Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073304Z-lane15-268c57d3/parent-source-extraction-results.tsv`

## Scope and method

Reviewed every input row once using only the referenced local metadata/source files and nearby local context. No web crawl or external portal interaction was used. The inspected local rows were country query-pack/profile rows or atlas score/dimension placeholders; none contained an explicit public parent source URL or source-pack/ledger pointer to a concrete parent URL.

## Results

- Input rows reviewed: 24
- Output rows written: 24
- Unique queue_ids: 24

### Verdict counts

- country_gap_no_parent_source: 24

### Input role counts

- atlas_dimension_without_named_source: 3
- country_query_pack: 21

## Claim boundary

Processing-state review only. These rows should not be used for reviewed-core promotion, incident truth, legal/safety/compliance findings, prevalence, or ranking. The only supported claim is that the local candidate rows do not expose an extractable parent source URL and require source resolution before direct review.
