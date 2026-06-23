# Parent source extraction summary

- Batch: 20260617T064341Z-lane31-6a9c4080
- Input rows reviewed: 24
- Output rows written: 24
- Method: local TSV metadata, cited source lines, nearby context, and local source-pack/source-refresh pointers only; no web crawl or external interaction.

## Verdict counts
- source_url_extracted: 2
- parent_source_wrapper: 0
- country_gap_no_parent_source: 22
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Extracted local parent/source pointers
- BPSE-02559 (LIMEN-SIGNAL-CD69E4BE8011ABC2): First-pass public web search -> https://search.yahoo.com/search?p=Turkmenistan+AI+regulatory+sandbox (/srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_READINESS_WORLD_WEAK_SOURCE_WARNINGS.md:4226; /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_READINESS_SPRINT_4_SOURCE_PACK.csv:713)
- BPSE-02560 (LIMEN-SIGNAL-CDADFDA1E83F9BE1): M-25-21 annual AI use-case inventory requirement -> https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf (/srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_SECOND_PASS_CANDIDATE_MATRIX_DELTA.csv:1250; /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_SECOND_PASS_SPRINT_9_SOURCE_REFRESH.csv:305)

## Notes
- Country query-pack rows were classified as `country_gap_no_parent_source` because the inspected rows only contain country-level generated search targets and preferred source classes, not named parent-source URLs.
- BPSE-02559 extraction is a weak search-log URL from a local source-pack pointer, not an official sandbox source and not evidence of absence.
- BPSE-02560 extraction is federal OMB M-25-21 hardening only; it does not establish a UM-specific public algorithm register.
