# Parent-source extraction summary

Batch: 20260616T123444Z-lane10-1961a3bd
Input rows reviewed: 24
Output rows written: 24

## Verdict counts
- source_url_extracted: 1
- parent_source_wrapper: 9
- country_gap_no_parent_source: 6
- source_surface_only_no_case: 8
- duplicate_existing_core: 0
- reject_noise: 0

## Verification
- Reviewed every input queue_id once in input order.
- Used only local files, local context, and local source-refresh/source-basis ledgers.
- Did not infer URLs from names or DOI strings.
- Rows with aggregate country gaps/profile placeholders and no extractable URL were marked `country_gap_no_parent_source`.
- Rows bundling multiple source-refresh or source-basis URLs were marked `parent_source_wrapper` instead of choosing a parent automatically.
- Boundary preserved: processing-state parent-source review only; no reviewed-core promotion, incident/legal/safety/compliance finding, prevalence claim, or ranking.
