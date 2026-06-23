# Parent-source extraction summary

Batch: `20260617T064340Z-lane24-0d525e82`
Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane24-0d525e82/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane24-0d525e82/parent-source-extraction-results.tsv`

## Outcome

- Input rows reviewed exactly once: 24
- Output rows written: 24
- Queue-id set verified equal to input: yes
- Duplicate output queue IDs: none

## Verdict counts

- `country_gap_no_parent_source`: 23
- `source_url_extracted`: 1

## Notes

- Rows BPSE-02378 through BPSE-02400 were local research-queue or aggregate country/index gap placeholders. Their local rows contain seed queries, search-target classes, or aggregate source examples but no single concrete original parent-source URL to extract.
- BPSE-02401 had a local second-pass source-pack pointer (`se-source-hardening`). The exact SE/I05 source-refresh row explicitly provides the Government Offices SOU 2025:101 URL for the narrow high-risk AI registration proposal. The output is limited to URL extraction/provenance and does not promote a reviewed-core claim.

## Boundary compliance

No web crawl, portal use, publication, upload, email, registration, payment, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking was performed.
