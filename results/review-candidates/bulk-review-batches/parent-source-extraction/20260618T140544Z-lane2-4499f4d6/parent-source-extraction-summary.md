# Parent source extraction summary — 20260618T140544Z-lane2-4499f4d6

Completed at: 2026-06-18T14:07:45Z

## Scope

- Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260618T140544Z-lane2-4499f4d6/input.tsv`
- Result TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260618T140544Z-lane2-4499f4d6/parent-source-extraction-results.tsv`
- Rows reviewed: 2
- Boundary: processing-state/source-surface review only; no reviewed-core promotion, ObscureAI addition, incident truth, legal/safety/compliance finding, prevalence, or ranking.

## Verdict counts

| verdict | count |
|---|---:|
| source_url_extracted | 2 |
| parent_source_wrapper | 0 |
| country_gap_no_parent_source | 0 |
| source_surface_only_no_case | 0 |
| duplicate_existing_core | 0 |
| reject_noise | 0 |

## Evidence inspected

- `sources.md:1397-1401` and local drain ledger `20260618T132251Z-direct-source-review-queue.tsv:12565` for `BPSE-03653` / `LIMEN-SIGNAL-E10DC9E7C6AD4CEB`.
- `sources.md:1268-1278` and local drain ledger `20260618T132251Z-direct-source-review-queue.tsv:13855` for `BPSE-03654` / `LIMEN-SIGNAL-A1170675592C32AE`.

## Verification

- Result header exactly matches configured header.
- Input rows: 2.
- Output rows: 2.
- Input queue_id set equals output queue_id set: yes.
- Duplicate output queue_id values: none.
- Extra output queue_id values: none.
- Omitted input queue_id values: none.
- Only allowed `bulk_source_verdict` values used: yes.
- No broad web crawl, portal interaction, publishing, upload, email, registration, payment, or form submission performed.
