# Parent source extraction summary

Batch: 20260616T121422Z-lane10-30c4b1f8
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T121422Z-lane10-30c4b1f8/input.tsv
Output: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T121422Z-lane10-30c4b1f8/parent-source-extraction-results.tsv

## Results

- Input rows reviewed: 24
- Output rows written: 24
- source_url_extracted: 1
- parent_source_wrapper: 5
- country_gap_no_parent_source: 18
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Extracted URLs

- BPSE-00470 / Regulatory Sandbox | FCA: https://www.fca.org.uk/firms/innovation/regulatory-sandbox
  - Evidence: cached HTML at /srv/tyche/atlas/tyche-thesis-atlas-factory/source-cache/v0.2/objects/dc/dc55afd30b050ca679015bf6.html:1094 and source-cache manifest line 30.

## Notes

Most rows are country research-queue prompts, country index/matrix/profile wrappers, or generic manifest/target-evidence placeholders. They do not expose an explicit original public URL in the local context. Wrapper rows with multiple candidate parent sources were not collapsed into invented URLs.

## Verification

Verified one output row per input queue_id, with no omissions, extras, or duplicate queue_id values.
