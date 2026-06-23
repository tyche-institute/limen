# Parent source extraction summary

Batch: 20260616T121757Z-lane6-8052a9c8
Input rows reviewed exactly once: 24

## Verdict counts
- country_gap_no_parent_source: 18
- parent_source_wrapper: 4
- source_surface_only_no_case: 1
- source_url_extracted: 1

## Method
- Used local TSV rows, cited source-path line context, local JSON metadata, and local source/bundle pointers only.
- Did not crawl the web or infer URLs from names.
- Extracted a URL only where a concrete URL was explicit in local metadata tied to the row context.
- Marked country/profile/score placeholders without a concrete parent URL as `country_gap_no_parent_source`.
- Marked manifest/case-bundle rows requiring a human choice among multiple candidate parents as `parent_source_wrapper`.

## Extracted URL
- BPSE-00680: Plataforma Nacional de Transparencia — https://www.plataformadetransparencia.org.mx/

## Verification
- Result TSV row count matches input row count.
- Result TSV queue_id set matches input queue_id set, with no omissions, extras, or duplicates.
