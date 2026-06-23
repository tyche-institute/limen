# Parent source extraction summary

Batch: 20260616T123928Z-lane6-99a1cb8c
Input rows reviewed: 24
Output rows written: 24

## Verdict counts

- source_url_extracted: 5
- parent_source_wrapper: 10
- country_gap_no_parent_source: 7
- source_surface_only_no_case: 2

## Extracted URL rows

- BPSE-01520: https://ab.gov.ag/digitaltransformation/pdf/ud_dra_stakholder_workshop_survey/antigua_and_barbuda_digital_readiness_analysis.pdf
- BPSE-01522: https://shabait.com/?s=artificial+intelligence
- BPSE-01525: https://www.cnbs.gob.hn/hub-de-innovacion-financiera-de-honduras/
- BPSE-01528: https://ted.europa.eu/en/notice/-/detail/3515-2024
- BPSE-01535: https://www.ict.gov.pg/?s=algorithm+register

## Boundary notes

- Used local metadata and local source files only.
- Did not infer URLs from source names or perform broad web crawl.
- Wrapper verdicts indicate rows where local rollups exposed multiple parent-source candidates or only local diagnostic/source-family pointers.
- Country-gap verdicts indicate profile, score, weak-warning, or queue rows without an extractable parent URL.

## Verification

Queue-id set and row count were checked programmatically against input.tsv.
