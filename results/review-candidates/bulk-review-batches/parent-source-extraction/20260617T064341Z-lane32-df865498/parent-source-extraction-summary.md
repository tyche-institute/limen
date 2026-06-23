# Parent source extraction batch summary

- Batch: 20260617T064341Z-lane32-df865498
- Completed at UTC: 2026-06-17T06:45:02Z
- Input rows reviewed exactly once: 24
- Output rows written: 24
- Queue-id verification: PASS (same set, no omissions, no extras, no duplicates)
- Boundary: processing-state review only; no source promotion or factual/legal/safety/compliance finding made.

## Verdict counts
- country_gap_no_parent_source: 24

## Local evidence inspected
- /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv: 12 referenced rows; inspected target lines and nearby local context.
- /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv: 12 referenced rows; inspected target lines and nearby local context.

## Rationale
All input rows are `country_query_pack` rows from local observability research queue CSV files. The referenced lines list country-level search queries and preferred source categories, not concrete public parent-source URLs. Nearby local context also consists of adjacent country query/profile rows. Therefore each row is marked `country_gap_no_parent_source` rather than inventing a URL from a country/source name.

## Reviewed rows
| queue_id | signal_id | country/source row | source line | verdict |
|---|---|---|---:|---|
| BPSE-02570 | LIMEN-SIGNAL-D00BF3B3A1211A9F | British Indian Ocean Territory | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:114 | country_gap_no_parent_source |
| BPSE-02571 | LIMEN-SIGNAL-D0122AA3F3225606 | Isle of Man | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:98 | country_gap_no_parent_source |
| BPSE-02572 | LIMEN-SIGNAL-D062BF0615DFAD50 | Uruguay | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:154 | country_gap_no_parent_source |
| BPSE-02573 | LIMEN-SIGNAL-D0638773568B83FB | Nicaragua | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:130 | country_gap_no_parent_source |
| BPSE-02574 | LIMEN-SIGNAL-D06B8ECD406993B2 | Estonia | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:145 | country_gap_no_parent_source |
| BPSE-02575 | LIMEN-SIGNAL-D0B5F61308F29E92 | Libya | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:99 | country_gap_no_parent_source |
| BPSE-02576 | LIMEN-SIGNAL-D0F3DDA4DC8A889C | South Georgia | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:103 | country_gap_no_parent_source |
| BPSE-02577 | LIMEN-SIGNAL-D131902F8D4D9FFD | Portugal | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:144 | country_gap_no_parent_source |
| BPSE-02578 | LIMEN-SIGNAL-D1578FC960118F2B | Belgium | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:164 | country_gap_no_parent_source |
| BPSE-02579 | LIMEN-SIGNAL-D1D90EFF4A58E4D8 | Dominican Republic | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:173 | country_gap_no_parent_source |
| BPSE-02580 | LIMEN-SIGNAL-D1EFA75526AA0ADF | Belgium | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:164 | country_gap_no_parent_source |
| BPSE-02581 | LIMEN-SIGNAL-D223A017BC123A4D | Eritrea | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:118 | country_gap_no_parent_source |
| BPSE-02582 | LIMEN-SIGNAL-D225F0C4725552C4 | Comoros | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:110 | country_gap_no_parent_source |
| BPSE-02583 | LIMEN-SIGNAL-D236894BB4B45795 | Palestine | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:112 | country_gap_no_parent_source |
| BPSE-02584 | LIMEN-SIGNAL-D2C68C81D3D8C8A7 | Turkmenistan | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:123 | country_gap_no_parent_source |
| BPSE-02585 | LIMEN-SIGNAL-D2F27F8FEFB27975 | Germany | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:140 | country_gap_no_parent_source |
| BPSE-02586 | LIMEN-SIGNAL-D38D481BD30C8E4B | Yemen | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:131 | country_gap_no_parent_source |
| BPSE-02587 | LIMEN-SIGNAL-D4C01BC97FB2E64E | Greece | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:141 | country_gap_no_parent_source |
| BPSE-02588 | LIMEN-SIGNAL-D511394EB7E26AFF | Cambodia | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:116 | country_gap_no_parent_source |
| BPSE-02589 | LIMEN-SIGNAL-D523EAE41F069D38 | Azerbaijan | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:180 | country_gap_no_parent_source |
| BPSE-02590 | LIMEN-SIGNAL-D54375E33C556A9B | Afghanistan | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:113 | country_gap_no_parent_source |
| BPSE-02591 | LIMEN-SIGNAL-D5DA4896A19E62E3 | Lithuania | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:160 | country_gap_no_parent_source |
| BPSE-02592 | LIMEN-SIGNAL-D6031A0C78853D13 | Italy | /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:149 | country_gap_no_parent_source |
| BPSE-02593 | LIMEN-SIGNAL-D647E757147AB89C | Estonia | /srv/tyche/pallas/pallas-ai-agent-observatory/program/08-observability-index/OBSERVABILITY_RESEARCH_QUEUE.csv:145 | country_gap_no_parent_source |

