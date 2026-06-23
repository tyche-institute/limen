# Parent source extraction summary

Batch: 20260617T064341Z-lane28-3343a4d8
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064341Z-lane28-3343a4d8/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064341Z-lane28-3343a4d8/parent-source-extraction-results.tsv

## Scope

Reviewed every input row exactly once using local metadata/source context only. No web crawl or external source recovery was performed.

## Verdict counts

- country_gap_no_parent_source: 24
- source_url_extracted: 0
- parent_source_wrapper: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Finding

All 24 rows point to `PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv` / `OBSERVABILITY_RESEARCH_QUEUE.csv` country/profile research-query rows. The inspected local rows contain ISO/country/profile fields and semicolon-separated query targets such as AI procurement, algorithm register, regulatory sandbox, and public sector AI. They do not contain a concrete original public URL or a named reviewable source surface. Therefore each row is marked `country_gap_no_parent_source`.

## Evidence examples

- BPSE-02474: British Virgin Islands / AI procurement at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:128
- BPSE-02475: Saint Kitts and Nevis / public sector AI at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:122
- BPSE-02476: Caribbean Netherlands / AI procurement at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:117
- BPSE-02477: Norfolk Island / AI procurement at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:101
- BPSE-02478: New Zealand / algorithm register at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:150
- BPSE-02479: United States / regulatory sandbox at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:142
- BPSE-02480: South Korea / public sector AI at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:147
- BPSE-02481: Estonia / public sector AI at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:145

## Verification

- Input data rows: 24
- Output data rows: 24
- Queue ID set match: yes
- Duplicate output queue_id values: none
- Result header matches required schema: yes
