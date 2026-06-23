# Parent source extraction summary

Batch: 20260617T064622Z-lane22-8c787221
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064622Z-lane22-8c787221/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064622Z-lane22-8c787221/parent-source-extraction-results.tsv

## Scope

Reviewed every input row exactly once using local metadata and local source files only. No web crawling, portal interaction, submission, promotion, or source invention was performed.

## Results

- Input rows: 24
- Output rows: 24
- source_url_extracted: 0
- parent_source_wrapper: 0
- country_gap_no_parent_source: 24
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

All rows were country/profile/research-queue placeholders. The local evidence rows list country-level search targets or atlas gap summaries, not a concrete original public parent-source URL for the queued target. Extracted URL fields were therefore left blank and rows were marked `country_gap_no_parent_source`.

## Verification

Automated verification passed.

- Required header matches: True
- Input row count: 24
- Output row count: 24
- Physical output lines including header: 25
- Queue-id set matches input: True
- Duplicate output queue_ids: 0
- Allowed verdicts only: True
