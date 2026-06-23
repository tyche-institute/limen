# Parent source extraction summary

Batch: 20260617T073306Z-lane30-776100f1
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073306Z-lane30-776100f1/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073306Z-lane30-776100f1/parent-source-extraction-results.tsv

## Verification

- Input rows reviewed: 24
- Output rows written: 24
- Queue ID set: exact match
- Duplicate output queue_id values: 0
- Header: exact configured header
- Scope: local metadata/source context only; no web crawl or external portal actions.

## Verdict counts

- country_gap_no_parent_source: 16
- parent_source_wrapper: 8

## Notes

Most rows were generated country/query bundles or atlas indicator/profile score rows with no explicit matching parent URL in the local source context. Jurisdiction source-pack rows were marked as wrappers because the local row lists multiple target source categories and requires a human to choose a concrete parent source before source-surface review.
