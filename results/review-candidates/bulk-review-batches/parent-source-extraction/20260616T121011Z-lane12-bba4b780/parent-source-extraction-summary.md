# Parent source extraction summary

- Batch: 20260616T121011Z-lane12-bba4b780
- Input rows reviewed exactly once: 24
- Output rows written: 24
- Verification: result TSV queue_id set and row count match input.tsv
- Boundary: processing-state parent-source triage only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

## Verdict counts
- source_url_extracted: 6
- parent_source_wrapper: 2
- country_gap_no_parent_source: 16

## Notes
- Country research queues, country profiles, and country score/profile summaries were marked country_gap_no_parent_source when inspected local context exposed only search themes, score/gap summaries, or source-name snippets.
- Extracted URLs came only from local Gaia ledgers/source-document exports or Pallas source-refresh packs tied to the inspected source rows.
- The lane manifest and Mozambique I03 matrix row were marked parent_source_wrapper because local context did not expose a single selected parent source.
