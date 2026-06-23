# Parent-source extraction summary

Batch: `20260616T122527Z-lane11-beb70a06`
Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122527Z-lane11-beb70a06/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T122527Z-lane11-beb70a06/parent-source-extraction-results.tsv`

Reviewed rows: 24
Output rows: 24

Verdict counts:
- `country_gap_no_parent_source`: 19
- `parent_source_wrapper`: 1
- `source_url_extracted`: 4

Verification:
- One output row was written for every input `queue_id`.
- No extra or duplicate `queue_id` values were introduced.
- Processing stayed within local metadata/source files and adjacent local source-pack pointers.
- No web crawl, submission, upload, portal interaction, legal/safety/compliance finding, prevalence claim, or reviewed-core promotion was performed.

Notable extracted URLs:
- Retraction Watch CSV via local Nekropolis source-pack reference: `https://gitlab.com/crossref/retraction-watch-data/-/raw/main/retraction_watch.csv`
- AVID source-family public surface via local crosswalk: `https://avidml.org/`
- Estonia I05 local hardening source surface: `https://ria.ee/riigi-infosusteem/tehisaru/aruait`
