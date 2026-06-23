# Parent source extraction summary

Batch: 20260617T064623Z-lane32-58ef32d7
Completed at UTC: 2026-06-17T06:48:04Z
Input rows reviewed: 24
Output rows written: 24

## Verdict counts
- source_url_extracted: 0
- parent_source_wrapper: 0
- country_gap_no_parent_source: 24
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Method
- Used only local input metadata and local source CSV files.
- For each row, inspected the configured source line and nearby local context (±2 lines).
- No broad web crawl or external source lookup was used.
- All 24 rows were country/profile research-queue placeholders listing search targets, not concrete public parent-source URLs.

## Reviewed rows
- BPSE-02690: LC Saint Lucia; query=public sector AI; evidence=OBSERVABILITY_RESEARCH_QUEUE.csv:115; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02691: NC New Caledonia; query=AI procurement; evidence=OBSERVABILITY_RESEARCH_QUEUE.csv:100; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02692: KM Comoros; query=regulatory sandbox; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:110; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02693: TK Tokelau; query=algorithm register; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:107; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02694: NF Norfolk Island; query=algorithm register; evidence=OBSERVABILITY_RESEARCH_QUEUE.csv:101; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02695: TL Timor-Leste; query=regulatory sandbox; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:132; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02696: CA Canada; query=algorithm register; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:156; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02697: UY Uruguay; query=regulatory sandbox; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:154; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02698: KN Saint Kitts and Nevis; query=regulatory sandbox; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:122; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02699: KP North Korea; query=public sector AI; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:133; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02700: PS Palestine; query=AI procurement; evidence=OBSERVABILITY_RESEARCH_QUEUE.csv:112; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02701: NI Nicaragua; query=AI procurement; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:130; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02702: TC Turks and Caicos Islands; query=algorithm register; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:127; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02703: BR Brazil; query=regulatory sandbox; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:158; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02704: CZ Czechia; query=public sector AI; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:148; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02705: BE Belgium; query=AI procurement; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:164; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02706: LB Lebanon; query=public sector AI; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:120; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02707: RU Russia; query=public sector AI; evidence=OBSERVABILITY_RESEARCH_QUEUE.csv:177; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02708: SS South Sudan; query=AI procurement; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:104; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02709: PE Peru; query=regulatory sandbox; evidence=OBSERVABILITY_RESEARCH_QUEUE.csv:172; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02710: MV Maldives; query=regulatory sandbox; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:111; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02711: CC Cocos (Keeling) Islands; query=regulatory sandbox; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:92; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02712: PK Pakistan; query=algorithm register; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:171; verdict=country_gap_no_parent_source; url_like_context=false
- BPSE-02713: GY Guyana; query=AI procurement; evidence=PALLAS_OBSERVABILITY_RESEARCH_QUEUE.csv:168; verdict=country_gap_no_parent_source; url_like_context=false

## Verification
- Result TSV header matches required schema.
- Result TSV row count matches input row count.
- Result TSV queue_id set matches input queue_id set with no duplicates.
