# Parent source extraction summary — 20260617T073429Z-lane15-9246d9c7

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073429Z-lane15-9246d9c7/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073429Z-lane15-9246d9c7/parent-source-extraction-results.tsv`
Rows reviewed: 24
Rows written: 24

## Verdict counts
- source_url_extracted: 2
- parent_source_wrapper: 1
- country_gap_no_parent_source: 21
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Method
- Reviewed each input queue row once against local source_path/source_line context.
- Used only local CSV rows and local `pallas_atlas_countries.json` metadata/top_sources.
- Did not perform broad web crawling or make incident/legal/safety/compliance claims.

## Notes
- Research queue rows were generic country/query placeholders with no concrete URL in local row context.
- Most country-profile rows were indicator/gap placeholders with no query-specific extractable parent URL.
- Extracted URLs only where local `top_sources` explicitly contained a concrete source URL; Vanuatu was marked wrapper because local metadata exposed two plausible sandbox parent surfaces.
