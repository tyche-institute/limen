# Parent source extraction summary

Batch: 20260616T123226Z-lane3-f1d7bdd2
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T123226Z-lane3-f1d7bdd2/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T123226Z-lane3-f1d7bdd2/parent-source-extraction-results.tsv

## Verification

- Input rows reviewed: 24
- Output rows written: 24
- Queue ID set match: yes
- Duplicate output queue IDs: 0
- Boundary: processing-state review only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

## Verdict counts

- country_gap_no_parent_source: 13
- parent_source_wrapper: 5
- source_surface_only_no_case: 5
- source_url_extracted: 1

## Notes

- One concrete URL was extracted from local source-cache metadata: BPSE-01238 -> https://www.edpb.europa.eu/our-work-tools/our-documents_en.
- Rows that were country/profile/score gap placeholders without an extractable URL were marked `country_gap_no_parent_source`.
- Rows pointing at multi-source wrappers, source lists, ledgers, or missing local extracted-text pointers were marked `parent_source_wrapper`.
- Rows that were aggregate notes, manuscript text, audit summaries, or reconnaissance seeds without standalone parent URLs were marked `source_surface_only_no_case`.
