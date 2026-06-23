# Parent source extraction summary

- Batch: 20260617T064610Z-lane8-54acaa67
- Input rows reviewed: 24
- Output rows written: 24
- Method: local-only inspection of input metadata plus exact referenced local source lines and nearby queue/matrix context; no web crawling or external lookup.
- Boundary: processing-state review only; no reviewed-core promotion, incident truth, legal, safety, compliance, prevalence, or ranking claim.

## Verdict counts
- country_gap_no_parent_source: 24

## Source-role counts
- derived_matrix_wrapper: 3
- research_queue_wrapper: 21

## Local evidence files inspected
- /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv: 12 rows
- /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_COUNTRY_INDEX.csv: 1 rows
- /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv: 9 rows
- /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_READINESS_WORLD_COUNTRY_MATRIX.csv: 2 rows

## Notes
- All reviewed rows were country research-queue or aggregate matrix/profile placeholders.
- No row contained an explicit original public URL in the inspected local metadata or source context.
- Rows are therefore marked country_gap_no_parent_source rather than source_url_extracted or parent_source_wrapper.
