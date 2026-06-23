# Parent source extraction summary

Batch: 20260616T123321Z-lane6-7e15c20e
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- country_gap_no_parent_source: 13
- parent_source_wrapper: 5
- source_surface_only_no_case: 4
- source_url_extracted: 2

Notes:
- Used only local cited rows, nearby context, and local source-pack/ledger pointers.
- Did not crawl the web or make incident/legal/safety/compliance findings.
- Extracted concrete parent URLs only where a local source-refresh/ledger row explicitly exposed a single usable URL for the cited source surface.
- Rows that were country profile/score/gap placeholders without extractable URLs were marked country_gap_no_parent_source.
- Rows requiring human choice among multiple local parent sources were marked parent_source_wrapper.
