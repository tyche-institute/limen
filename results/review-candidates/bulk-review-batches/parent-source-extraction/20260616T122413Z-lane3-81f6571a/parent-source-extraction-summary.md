# Parent source extraction summary

Batch: 20260616T122413Z-lane3-81f6571a
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 1
- source_surface_only_no_case: 1
- parent_source_wrapper: 20
- country_gap_no_parent_source: 2

Method:
- Reviewed each input queue_id once against the cited local row and nearby context.
- Used only local metadata/source files and local source-refresh/source-hardening pointers found in the project tree.
- Did not invent URLs from source names and did not web crawl.

Notes:
- Extracted one direct URL for ASIC ERS where the local source-refresh row exposed a concrete parent URL.
- Marked Puerto Rico PRITS as source_surface_only_no_case because it is a negative-check/search-limited surface, not sandbox evidence.
- Marked source-pack/wrapper rows with multiple plausible parent sources as parent_source_wrapper for human selection.
- Marked country profile/gap placeholders without relevant explicit URLs as country_gap_no_parent_source.
