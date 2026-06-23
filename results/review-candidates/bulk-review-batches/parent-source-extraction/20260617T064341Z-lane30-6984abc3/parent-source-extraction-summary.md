# Parent source extraction summary

- Batch: 20260617T064341Z-lane30-6984abc3
- Completed at UTC: 2026-06-17T06:44:38Z
- Input rows reviewed: 24
- Output rows written: 24
- Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064341Z-lane30-6984abc3/parent-source-extraction-results.tsv

## Verdict counts
- source_url_extracted: 0
- parent_source_wrapper: 0
- country_gap_no_parent_source: 24
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Local evidence inspected
Reviewed each input row once against its referenced local CSV line and nearby research-queue context. The referenced rows contain country names, focus query strings, and preferred source-type hints, not concrete public parent URLs.
- /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv: lines 98, 98, 111, 117, 142, 158, 161, 164, 168, 171, 177
- /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv: lines 93, 106, 109, 110, 114, 119, 133, 142, 143, 160, 163, 174, 177

## Boundary note
This batch is processing-state parent-source extraction only. No reviewed-core promotion, incident finding, legal/safety/compliance finding, prevalence claim, or ranking was made.
