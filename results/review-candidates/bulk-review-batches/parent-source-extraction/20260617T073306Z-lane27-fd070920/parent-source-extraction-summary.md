# Parent source extraction summary — 20260617T073306Z-lane27-fd070920

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073306Z-lane27-fd070920/input.tsv`
Result TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073306Z-lane27-fd070920/parent-source-extraction-results.tsv`

Reviewed every input row exactly once using only local TSV/JSON/source context.

## Counts

- input_rows: 24
- output_rows: 24
- source_url_extracted: 2
- country_gap_no_parent_source: 22
- parent_source_wrapper: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Extracted URLs

- BPSE-03407 / LIMEN-SIGNAL-B99DF5019901AD22: Mongolia I03 sandbox metadata exposes `https://www.frc.mn/resource/frc/Document/2023/01/10/c0zszjpdskfvfyn3/Regulation%20on%20Sandbox%20Environment.pdf` at `pallas_atlas_countries.json:21994-22000`.
- BPSE-03414 / LIMEN-SIGNAL-BC1A34B658A7F6ED: Antarctica I03 metadata exposes `https://www.ats.aq/e/tools-and-resources.html` at `pallas_atlas_countries.json:33767-33773`, as negative-evidence context.

## Notes

Most rows are generated research-queue query bundles or atlas score/gap placeholders. Where local metadata did not contain an explicit concrete parent URL for the row's signal, the row was marked `country_gap_no_parent_source` rather than inventing a URL from country/source names.
