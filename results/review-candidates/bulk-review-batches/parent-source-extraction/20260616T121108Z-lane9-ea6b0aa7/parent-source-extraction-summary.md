# Parent-source extraction summary

Batch: 20260616T121108Z-lane9-ea6b0aa7

Input rows reviewed exactly once: 24
Output rows written: 24

Verdict counts:
- source_url_extracted: 1
- parent_source_wrapper: 4
- country_gap_no_parent_source: 18
- source_surface_only_no_case: 1
- duplicate_existing_core: 0
- reject_noise: 0

Notes:
- Used local metadata and local source/context files only.
- Extracted a concrete public URL only where the local source-pack ledger explicitly exposed `source_url`/`final_url`.
- Research queue, manifest, matrix, and profile gap placeholders without explicit URLs were not converted into invented URLs.
- Wrapper/delta rows with multiple named surfaces but no concrete URL were left for human parent-source selection.

Verification:
- Result TSV header matches required schema.
- Result queue_id set and row count were verified against input.tsv.
