# Translation parent-source extraction summary

Batch: 20260616T130035Z-lane6-a13ea36b
Input rows reviewed: 16
Result rows written: 16

## Verdict counts
- source_url_extracted: 14
- parent_source_wrapper: 2
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes
- Used local metadata and local source/source-refresh files only; no web crawl or external portal action.
- BTPS-00083 is a BOSCO dossier/timeline wrapper without a locally resolved concrete parent URL in the inspected bundle.
- BTPS-00092 is an Iceland score-delta placeholder whose linked source-refresh evidence contains multiple official sandbox parent URLs; it should be split or selected by a follow-up source pass.
- All extracted URLs are explicitly present in local metadata, source-pack, source-refresh, ledger, or JSON records.
