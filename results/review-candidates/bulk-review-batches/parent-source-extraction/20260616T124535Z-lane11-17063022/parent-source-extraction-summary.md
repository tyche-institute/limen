# Parent-source extraction summary

Batch: 20260616T124535Z-lane11-17063022
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T124535Z-lane11-17063022/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T124535Z-lane11-17063022/parent-source-extraction-results.tsv

## Scope

Reviewed every input row exactly once using local metadata, local source files, source-pack rows, and local ledger pointers only. No web crawl or external interaction was performed. Findings are processing-state source-surface routing only, not incident truth, legal/safety/compliance findings, prevalence, ranking, or reviewed-core promotion.

## Verdict counts

- source_url_extracted: 9
- parent_source_wrapper: 5
- country_gap_no_parent_source: 3
- source_surface_only_no_case: 7
- duplicate_existing_core: 0
- reject_noise: 0

Total output rows: 24

## Verification

- Output header matches the required schema.
- One output row was written for each input queue_id.
- Queue_id order follows input.tsv.
- URL extraction was limited to URLs explicitly present in local source context, local metadata, source packs, or ledgers.
