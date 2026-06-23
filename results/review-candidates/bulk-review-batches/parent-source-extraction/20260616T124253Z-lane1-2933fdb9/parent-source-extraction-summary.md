# Parent-source extraction summary

Batch: 20260616T124253Z-lane1-2933fdb9

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T124253Z-lane1-2933fdb9/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260616T124253Z-lane1-2933fdb9/parent-source-extraction-results.tsv

Processed every input row exactly once. Used local metadata/source context and local source-pack/ledger pointers only. No web crawling or external submission actions were performed.

## Verification

- Input data rows: 24
- Output data rows: 24
- Queue ID set: exact match
- Duplicate output queue_id values: 0
- Header: exact required header

## Verdict counts

- source_url_extracted: 2
- parent_source_wrapper: 5
- country_gap_no_parent_source: 7
- source_surface_only_no_case: 5
- duplicate_existing_core: 0
- reject_noise: 5

## Extracted URLs

- BPSE-01670 (LIMEN-SIGNAL-F4AB37EC87BC4B08): https://ai.hel.fi/oodis-book-recommendation-service-obotti — Oodi's book recommendation service Obotti
- BPSE-01680 (LIMEN-SIGNAL-F59DA095A2F7718D): https://attorneygeneralchambers.com/laws-of-saint-lucia/public-procurement-act — Public Procurement Act

## Boundary note

This batch is processing-state review only. It does not promote reviewed-core items, add ObscureAI cases, or make incident truth, legal, safety, compliance, prevalence, or ranking findings.
