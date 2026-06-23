# Translation parent source extraction summary

Batch: 20260616T130035Z-lane3-75cc2149
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260616T130035Z-lane3-75cc2149/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260616T130035Z-lane3-75cc2149/translation-parent-source-extraction-results.tsv
Rows reviewed: 16
Completed at UTC: 2026-06-16T13:02:19Z

## Verdict counts

- source_url_extracted: 16

## Method

Reviewed each input row once against the configured local source_path/source_line and nearby local context. Extracted only concrete public URLs explicitly present in local metadata, local CSV/JSONL source rows, or local source-pack rows. No broad web crawl or external submission/publishing action was performed.

## Boundary

Processing-state review only. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking is asserted.

## Verification

The result TSV was checked for exact input queue_id set equality, matching row count, no omitted rows, no extra rows, and no duplicate queue_id values.
