You are Hermes/Codex performing a bounded LIMEN bulk-translation-review batch.

Input TSV:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260617T073304Z-lane1-15598271/input.tsv

Required outputs:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260617T073304Z-lane1-15598271/bulk-translation-review-results.tsv
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260617T073304Z-lane1-15598271/bulk-translation-review-summary.md

Update this manifest when complete:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260617T073304Z-lane1-15598271/manifest.json

Task:
- Review every row in input.tsv exactly once.
- Use local metadata and local source files only. You may use multilingual understanding, but do not turn machine translation into a factual/legal/policy claim.
- Distinguish concrete source-surface review from case-level promotion. Most rows should remain source-surface/context unless a concrete edge-case claim is explicit.
- Do not broad web crawl. Do not submit, publish, upload, email, register, pay, or use portal forms.

Write bulk-translation-review-results.tsv with exactly this header:
queue_id	signal_id	bulk_translation_verdict	language_reviewed	source_url_or_locator	source_name	reason	claim_ceiling	next_action

Allowed bulk_translation_verdict values:
- translation_source_reviewed
- needs_original_language_source
- cross_project_duplicate
- machine_translation_hold
- candidate_for_parent_source_extraction
- source_surface_only_no_case
- reject_noise

Keep reasons concise. Replace tabs and newlines inside fields with spaces.
Write one output row per input queue_id, no omissions, no extras, no duplicate queue_id values.
Before stopping, verify that the result TSV has exactly the same queue_id set and row count as input.tsv.
Boundary: this is processing-state review only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
