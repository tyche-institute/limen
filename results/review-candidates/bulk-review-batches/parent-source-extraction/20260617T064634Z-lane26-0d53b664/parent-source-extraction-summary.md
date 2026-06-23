# Parent source extraction summary

- Batch: 20260617T064634Z-lane26-0d53b664
- Input rows reviewed: 24
- Output rows written: 24
- Verification: result queue_id set and row count match input.tsv

## Verdict counts
- source_url_extracted: 1
- parent_source_wrapper: 1
- country_gap_no_parent_source: 22

## Notes
- Used local metadata and local source lines only; no broad web crawl or external submission actions.
- BPSE-02730 has one explicit local I03 URL, recorded with a ceiling that it is adjacent statutory context only, not confirmed AI sandbox evidence.
- BPSE-02726 has three explicit local I08 procurement URLs, so it remains a wrapper requiring human selection or candidate split.
- All remaining rows are country profile/research queue placeholders or gap rows with no extractable parent source URL in inspected local context.
