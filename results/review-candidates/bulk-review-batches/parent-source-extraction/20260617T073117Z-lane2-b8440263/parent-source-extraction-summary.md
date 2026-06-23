# Parent source extraction summary

Batch: 20260617T073117Z-lane2-b8440263

## Scope
- Reviewed every input row exactly once using local metadata and local source files only.
- Inspected the cited source line and nearby local context for each row.
- No web crawling or external source recovery was performed.

## Results
- Input rows: 24
- Output rows: 24
- Verdict counts:
  - country_gap_no_parent_source: 24

## Evidence basis
- /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv: 14 cited rows; local queue rows contain country/search-theme/profile placeholders rather than concrete parent source URLs.
- /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv: 10 cited rows; local queue rows contain country/search-theme/profile placeholders rather than concrete parent source URLs.

## Verification
- Exact header: True
- Same queue_id set: True
- Same row count: 24 input / 24 output
- Duplicate output queue_id values: 0
- Verification passed: True
