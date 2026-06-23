You are Hermes/Codex performing a bounded LIMEN parent-source-extraction batch.

Input TSV:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane22-ff175a98/input.tsv

Required outputs:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane22-ff175a98/parent-source-extraction-results.tsv
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane22-ff175a98/parent-source-extraction-summary.md

Update this manifest when complete:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane22-ff175a98/manifest.json

Task:
- Review every row in input.tsv exactly once.
- Use local metadata and local source files only. Inspect relevant local lines and nearby context.
- Recover a concrete original public URL only when explicitly present in local metadata, local source context, or a local source-pack/ledger pointer. Do not invent URLs from source names.
- If a row is just a country gap/profile/score placeholder with no extractable parent source URL, mark `country_gap_no_parent_source`.
- If a row points to a wrapper/source-pack that needs a human to choose among multiple parent sources, mark `parent_source_wrapper`.
- Do not broad web crawl. Do not submit, publish, upload, email, register, pay, or use portal forms.

Write the configured result TSV with exactly this header:
queue_id	signal_id	bulk_source_verdict	extracted_source_url	source_name	evidence_location	reason	claim_ceiling	next_action

Allowed bulk_source_verdict values:
- source_url_extracted
- parent_source_wrapper
- country_gap_no_parent_source
- source_surface_only_no_case
- duplicate_existing_core
- reject_noise

Keep reasons concise. Replace tabs and newlines inside fields with spaces.
Write one output row per input queue_id, no omissions, no extras, no duplicate queue_id values.
Before stopping, verify that the result TSV has exactly the same queue_id set and row count as input.tsv.
Boundary: this is processing-state review only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
