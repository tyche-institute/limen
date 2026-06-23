# Parent source extraction summary

- Batch: 20260617T073304Z-lane1-eee85ab6
- Input rows reviewed: 24
- Output rows written: 24
- Queue-id verification: passed (same set, same count, no duplicates)
- Boundary: processing-state extraction only; no reviewed-core promotion or substantive incident/legal/safety/compliance/prevalence/ranking claim.

## Verdict counts
- country_gap_no_parent_source: 15
- parent_source_wrapper: 4
- source_url_extracted: 5

## Notes
- Used only local input TSV, local PALLAS atlas JSON, and local observability queue CSV context.
- Extracted URLs only where a single matching local top_sources URL was explicit for the requested indicator.
- Marked rows with multiple matching local top_sources as parent_source_wrapper.
- Marked country/profile/score/gap rows without a matching explicit local URL as country_gap_no_parent_source.

