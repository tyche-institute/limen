# Parent source extraction summary — 20260616T124016Z-lane11-1bdcb9e4

Input rows reviewed exactly once: 24
Output rows written: 24

## Verdict counts
- country_gap_no_parent_source: 11
- parent_source_wrapper: 4
- source_surface_only_no_case: 7
- source_url_extracted: 2

## Method
- Used local metadata and local source files only.
- Inspected the referenced local source lines and nearby context for each row.
- Extracted a concrete original public URL only when explicitly present in a local source-cache manifest or local source context.
- Country profile, matrix, score, and research-queue placeholders without direct parent URLs were marked `country_gap_no_parent_source`.
- Internal aggregates or digests requiring a human choice among multiple possible parent sources were marked `parent_source_wrapper`.
- Internal outlines, methodology/config/manifest/title surfaces with no case-level source were marked `source_surface_only_no_case`.

## Extracted URLs
- BPSE-01538: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- BPSE-01546: https://osf.io/preprints/metaarxiv/26zag_v1

Boundary honored: processing-state review only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
