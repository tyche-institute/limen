# Parent source extraction summary — 20260618T132345Z-lane2-5fa222d2

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260618T132345Z-lane2-5fa222d2/input.tsv`

Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260618T132345Z-lane2-5fa222d2/parent-source-extraction-results.tsv`

Rows reviewed exactly once: 6

Verdict counts:
- `parent_source_wrapper`: 4
- `source_url_extracted`: 2

Boundary respected: local metadata/source files only; no web crawl or external actions. Extracted URLs are limited to URLs explicitly present in local source-pack/crosswalk pointers. Rows that remained dashboard/methods wrappers were marked `parent_source_wrapper` rather than inventing a URL.

Per-row notes:
- BPSE-03646: dashboard overlap wrapper; no concrete public parent URL in reviewed context.
- BPSE-03647: extracted AVID primary URL from local crosswalk pointer.
- BPSE-03648: dashboard sample list of multiple source families; wrapper.
- BPSE-03649: static dashboard source-family coverage wrapper; wrapper.
- BPSE-03650: methods manual example categories; wrapper.
- BPSE-03651: extracted AVID primary URL from local crosswalk pointer.
