# Parent source extraction summary

Batch: 20260617T073306Z-lane32-8824b7a9

Reviewed 24 input rows exactly once using local metadata/source files only. No web crawl or external submission was performed.

Verdict counts:

- country_gap_no_parent_source: 3
- parent_source_wrapper: 20
- source_url_extracted: 1

Notes:
- Jurisdiction research-queue rows were treated as parent_source_wrapper because the local CSV rows list multiple query/source-type targets without a concrete public URL.
- Atlas country/profile score placeholders were marked country_gap_no_parent_source when no indicator-specific parent URL was explicit in nearby top_sources.
- One explicit local parent URL was extracted for Pakistan I03 regulatory sandbox: https://www.secp.gov.pk/regulatory-sandbox/.

Verification:
- Input rows: 24
- Output rows: 24
- Queue ID set matches input: yes
- Duplicate output queue_id values: none
