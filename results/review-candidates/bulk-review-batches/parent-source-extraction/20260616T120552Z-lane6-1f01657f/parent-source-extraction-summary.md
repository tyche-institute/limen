# Parent source extraction summary

Batch: 20260616T120552Z-lane6-1f01657f
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- country_gap_no_parent_source: 5
- parent_source_wrapper: 15
- source_url_extracted: 4


Method:
- Reviewed each input row once against local source paths and nearby context.
- Used only local metadata/source-pack/ledger context; no web crawl or external submission.
- Extracted URLs only where a concrete public URL was explicitly present in local metadata/source context.
- Marked profile/gap/score placeholders without isolated parent URLs as `country_gap_no_parent_source`.
- Marked wrappers/source packs with multiple candidate parent sources as `parent_source_wrapper`.

Verification:
- Result TSV header matches required schema.
- Result TSV queue_id set and data-row count were verified against input.tsv.
- Boundary preserved: processing-state review only; no reviewed-core promotion, source truth, legal/safety/compliance finding, prevalence, or ranking.
