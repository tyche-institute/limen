# Parent source extraction summary

- Batch: `20260617T073304Z-lane9-a692bd32`
- Input rows reviewed exactly once: 24
- Output rows written: 24
- Method: local-only inspection of input rows, nearby source lines, and local `pallas_atlas_countries.json` country `top_sources`; no web crawl or external submission.
- Boundary: processing-state review only; no incident truth, legal, safety, compliance, prevalence, or ranking claims.

## Verdict counts
- source_url_extracted: 4
- parent_source_wrapper: 0
- country_gap_no_parent_source: 20
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Extracted URLs
- BPSE-02964 / LIMEN-SIGNAL-C94783B241C7A292: https://eprocurement.gov.tj/ru/searchanno (Public procurement portal and electronic digital signature documentation — State public procurement portal; evidence /srv/tyche/pallas/pallas-ai-agent-observatory/program/01-pallas-atlas/app/data/pallas_atlas_countries.json:23857)
- BPSE-02967 / LIMEN-SIGNAL-D7C183F468C56B33: https://www.ufsa.gov.mz/ (UFSA procurement portal — Unidade Funcional de Supervisao das Aquisicoes (UFSA); evidence /srv/tyche/pallas/pallas-ai-agent-observatory/program/01-pallas-atlas/app/data/pallas_atlas_countries.json:27516)
- BPSE-02969 / LIMEN-SIGNAL-DFB98A24BDF2C1CD: https://e-mongolia.mn/home (E-Mongolia digital services portal — E-Mongolia; evidence /srv/tyche/pallas/pallas-ai-agent-observatory/program/01-pallas-atlas/app/data/pallas_atlas_countries.json:22024)
- BPSE-02981 / LIMEN-SIGNAL-F3202ED8577E9D5E: https://www.palaugov.pw/rfp-bids/ (ROP Procurement — Palau National Government; evidence /srv/tyche/pallas/pallas-ai-agent-observatory/program/01-pallas-atlas/app/data/pallas_atlas_countries.json:36940)

## Verification
- Result TSV header matches required schema.
- Queue-id set and row count verification performed after write; see manifest fields.
