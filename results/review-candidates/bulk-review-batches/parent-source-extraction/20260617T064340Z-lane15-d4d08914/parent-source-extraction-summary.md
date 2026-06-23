# Parent source extraction summary

- Batch: 20260617T064340Z-lane15-d4d08914
- Input rows reviewed: 24
- Output rows written: 24
- Processing boundary: local metadata/source context only; no web crawl or promotion decisions.

## Verdict counts
- source_url_extracted: 1
- parent_source_wrapper: 1
- country_gap_no_parent_source: 22

## Extracted/wrapper notes
- BPSE-02196: extracted Bank of Guyana National Payments System URL from local source-pack evidence tied to the warning line.
- BPSE-02188: marked parent_source_wrapper because Jordan I03 atlas context lists multiple Central Bank of Jordan I03 parent sources.
- BPSE-02207 and generated query-pack rows: no concrete parent source URL was exposed by the reviewed local row/context.

## Verification
- Result TSV header matches configured schema.
- Queue-id set and row count were validated against input.tsv.
