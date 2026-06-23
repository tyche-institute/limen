# Parent source extraction summary

Batch: 20260617T073304Z-lane5-478ad03e
Task: bounded LIMEN parent-source-extraction batch
Input rows reviewed exactly once: 24

## Verdict counts
- source_url_extracted: 5
- parent_source_wrapper: 5
- country_gap_no_parent_source: 14

## Method
- Used local input TSV, cited local JSON/CSV rows, and local atlas top_sources only.
- Extracted URLs only when a single relevant parent URL was explicitly present in local metadata for the requested signal topic.
- Marked profile/score/gap rows without a single local parent URL as country_gap_no_parent_source.
- Marked research queue prompts or multiple relevant local parent URLs as parent_source_wrapper.

## Extracted URL queue_ids
- BPSE-02868: https://gppa.gm/ (GPPA official procurement portal; /srv/tyche/pallas/pallas-ai-agent-observatory/program/01-pallas-atlas/app/data/pallas_atlas_countries.json:30693)
- BPSE-02869: https://adilet.zan.kz/rus/docs/Z1500000434 (Law on Public Procurement; /srv/tyche/pallas/pallas-ai-agent-observatory/program/01-pallas-atlas/app/data/pallas_atlas_countries.json:21268)
- BPSE-02872: https://www.arap.cv/ (ARAP official public procurement regulator portal; /srv/tyche/pallas/pallas-ai-agent-observatory/program/01-pallas-atlas/app/data/pallas_atlas_countries.json:29965)
- BPSE-02884: https://www.armp.sn/ (ARMP official procurement regulator portal; /srv/tyche/pallas/pallas-ai-agent-observatory/program/01-pallas-atlas/app/data/pallas_atlas_countries.json:32987)
- BPSE-02885: https://www.marchespublics.ne/ (Public procurement portal of Niger; /srv/tyche/pallas/pallas-ai-agent-observatory/program/01-pallas-atlas/app/data/pallas_atlas_countries.json:32217)

## Verification
- Result TSV header matches required schema.
- Result TSV row count and queue_id set verified against input.tsv after writing.
