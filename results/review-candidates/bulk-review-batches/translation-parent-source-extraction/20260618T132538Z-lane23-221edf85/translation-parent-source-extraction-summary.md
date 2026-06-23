# Translation parent source extraction summary

Batch: 20260618T132538Z-lane23-221edf85
Task: translation-parent-source-extraction
Completed at UTC: 2026-06-18T13:26:11Z

## Counts

- Input rows reviewed exactly once: 1
- Output rows written: 1
- source_url_extracted: 1
- parent_source_wrapper: 0
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Evidence basis

- Used local metadata and local source files only.
- Inspected the configured source line and nearby context in `/srv/tyche/projects/public-ai-registry/results/submission-preprint-packages/public-ai-registry-preprint-package-20260618T033625Z/zenodo/public-ai-registry-observatory-initial-corpus-20260608/data/registry-deployed-record-accession-all-20260607.csv`.
- The original public URL was extracted only because it is explicitly present at `/srv/tyche/projects/public-ai-registry/results/submission-preprint-packages/public-ai-registry-preprint-package-20260618T033625Z/zenodo/public-ai-registry-observatory-initial-corpus-20260608/data/registry-deployed-record-accession-all-20260607.csv:62`.

## Boundary note

Processing-state review only: no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim.

## Verification

- Result TSV header matches the configured schema.
- Result TSV queue_id set equals input.tsv queue_id set.
- Result TSV row count equals input.tsv row count.
