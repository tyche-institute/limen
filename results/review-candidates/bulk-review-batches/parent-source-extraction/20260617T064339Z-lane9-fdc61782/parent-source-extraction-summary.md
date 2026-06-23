# Parent source extraction summary

Batch: `20260617T064339Z-lane9-fdc61782`

## Outcome

- Input rows reviewed: 24
- Output rows written: 24
- Verification: PASS — output TSV queue_id set and row count match input.tsv; no duplicate output queue_id values.
- Web/network use: none. Local metadata and local source/source-pack files only.

## Verdict counts

- country_gap_no_parent_source: 24

## Notes

- All country_query_pack rows were country/query placeholders, not named source surfaces; no explicit public parent URL was present in the inspected local rows or nearby context.
- BPSE-02008 was checked against the Monaco source-pack pointer (`mc-source-hardening.md`); the relevant I03 row is a gap_finding with URL `N/A`, so no parent URL was extracted.

## Reviewed evidence

- BPSE-01994: Estonia research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:145; no URL fields in local row.
- BPSE-01995: Paraguay research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:166; no URL fields in local row.
- BPSE-01996: French Polynesia research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:93; no URL fields in local row.
- BPSE-01997: Afghanistan research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:113; no URL fields in local row.
- BPSE-01998: Equatorial Guinea research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:126; no URL fields in local row.
- BPSE-01999: Western Sahara research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:124; no URL fields in local row.
- BPSE-02000: Timor-Leste research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:132; no URL fields in local row.
- BPSE-02001: Guadeloupe research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:167; no URL fields in local row.
- BPSE-02002: Antigua and Barbuda research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:125; no URL fields in local row.
- BPSE-02003: Latvia research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:174; no URL fields in local row.
- BPSE-02004: Greece research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:141; no URL fields in local row.
- BPSE-02005: South Korea research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:147; no URL fields in local row.
- BPSE-02006: Dominican Republic research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:173; no URL fields in local row.
- BPSE-02007: Belgium research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:164; no URL fields in local row.
- BPSE-02008: PALLAS Monaco I03 score/gap row at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_SECOND_PASS_CANDIDATE_MATRIX_DELTA.csv:2318; /srv/tyche/pallas/pallas-ai-agent-observatory/prompts/waves/pallas-hardening-sprint-16/mc-source-hardening.md:56; local metadata/source-pack has no parent URL.
- BPSE-02009: Tokelau research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:107; no URL fields in local row.
- BPSE-02010: Maldives research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:111; no URL fields in local row.
- BPSE-02011: Argentina research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:179; no URL fields in local row.
- BPSE-02012: Hong Kong research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:169; no URL fields in local row.
- BPSE-02013: Heard Island and McDonald Islands research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:96; no URL fields in local row.
- BPSE-02014: New Caledonia research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:100; no URL fields in local row.
- BPSE-02015: Grenada research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:119; no URL fields in local row.
- BPSE-02016: Cambodia research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:116; no URL fields in local row.
- BPSE-02017: Luxembourg research query pack at /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:157; no URL fields in local row.
