# Parent source extraction summary

Batch: 20260617T064600Z-lane30-07e38271
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 1
- parent_source_wrapper: 1
- country_gap_no_parent_source: 22

Notes:
- Used local metadata/source files only; no web crawling or portal interaction.
- Most rows were research queue placeholders with country/query targets but no explicit parent URL in the inspected local row context.
- BPSE-02621 is a derived matrix aggregate with multiple named source examples and no URL in the matrix row, so it remains a parent-source wrapper.
- BPSE-02624 had an explicit Montserrat procurement URL in atlas top_sources and was extracted with a source-posture-only ceiling.
