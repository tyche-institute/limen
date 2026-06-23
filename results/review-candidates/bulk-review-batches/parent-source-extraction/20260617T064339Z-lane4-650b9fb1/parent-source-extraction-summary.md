# Parent source extraction summary

Batch: 20260617T064339Z-lane4-650b9fb1
Completed at UTC: 2026-06-17T06:46:23Z

## Scope

Reviewed every input row exactly once using local metadata and local source files only. No web crawl or external submission actions were performed. This is processing-state review only: no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

## Results

- Input rows: 24
- Output rows: 24
- source_url_extracted: 1
- parent_source_wrapper: 2
- country_gap_no_parent_source: 21
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

- BPSE-01909 had a single explicit local I08 parent URL in `top_sources` and was extracted.
- BPSE-01898 and BPSE-01917 had multiple explicit local I08 procurement surfaces, so they were marked `parent_source_wrapper` for human parent-source choice.
- Research-queue rows contained country/topic search prompts and category names but no concrete public URL.
- Remaining country profile/score/summary placeholders did not expose an extractable indicator-specific parent URL in the inspected local profile context.

## Verification

The result TSV was checked for exact header, allowed verdict values, no duplicate queue IDs, one output row per input row, and identical queue_id set to `input.tsv`.
