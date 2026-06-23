# Parent source extraction summary

Batch: 20260617T064340Z-lane22-ff175a98
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane22-ff175a98/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane22-ff175a98/parent-source-extraction-results.tsv

## Scope

Processed 24 input rows exactly once using local metadata and local source/ledger context only. No web crawl, portal submission, upload, publication, email, registration, payment, reviewed-core promotion, ObscureAI addition, or substantive incident/legal/safety/compliance finding was performed.

## Verdict counts

- source_url_extracted: 1
- parent_source_wrapper: 0
- country_gap_no_parent_source: 23
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Extracted parent source URLs

- BPSE-02323 / LIMEN-SIGNAL-764251A3D05C8E8A: Anpassningar till AI-förordningen SOU 2025:101 — https://www.regeringen.se/rattsliga-dokument/statens-offentliga-utredningar/2025/10/sou-2025101/
  - Evidence: /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_SECOND_PASS_CONFIDENCE_CHANGES.csv:856; /srv/tyche/pallas/pallas-ai-agent-observatory/reports/PALLAS_SECOND_PASS_SOURCE_REFRESH_ROLLUP.csv:3681

## No-parent-source rows

All remaining rows were country research-queue or profile/manifest placeholders. Their local lines contain jurisdiction/search-target or score/label metadata but no explicit parent public URL.

## Verification

- Input data rows: 24
- Output data rows: 24
- Queue-id set: verified after writing by script.
