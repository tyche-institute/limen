# Parent source extraction summary: 20260617T064340Z-lane20-c5291d6e

Status: complete
Input rows: 24
Output rows: 24

Verdict counts:
- country_gap_no_parent_source: 23
- parent_source_wrapper: 1

Verification:
- same_queue_id_set_as_input: true
- duplicate_output_queue_ids: 0
- no_omitted_rows: true
- no_extra_rows: true

Notes:
- Used local metadata/source context only; no web crawl or external actions.
- No concrete original public URL was extracted for country/profile/research-query placeholders.
- BPSE-02273 was retained as a parent_source_wrapper because the local Spain I05 source pack exposes multiple possible parent rows rather than one canonical URL for the derived review row.
