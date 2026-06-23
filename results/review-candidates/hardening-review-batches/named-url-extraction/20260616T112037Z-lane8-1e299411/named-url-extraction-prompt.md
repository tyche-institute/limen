You are Hermes/Codex performing a bounded LIMEN named-url-extraction batch.

Input TSV:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/hardening-review-batches/named-url-extraction/20260616T112037Z-lane8-1e299411/input.tsv

Required outputs:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/hardening-review-batches/named-url-extraction/20260616T112037Z-lane8-1e299411/named-url-extraction-results.tsv
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/hardening-review-batches/named-url-extraction/20260616T112037Z-lane8-1e299411/named-url-extraction-summary.md

Update this manifest status/details when complete:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/hardening-review-batches/named-url-extraction/20260616T112037Z-lane8-1e299411/manifest.json

Task:
- Review every row in input.tsv exactly once.
- Use local metadata and local source files only. Inspect only relevant local lines/nearby context.
- Recover a concrete original public URL only when it is explicitly present in local metadata, local source context, or a cache/snapshot locator. Do not invent URLs from hostnames.
- Do not broad web crawl. Do not email, upload, submit, publish, register, pay, deploy, or take public/portal actions.
- This is URL/source-surface hardening only. Do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.

Write named-url-extraction-results.tsv with exactly this header:
row_id	signal_id	url_extraction_verdict	extracted_source_url	source_name	evidence_location	reason	claim_ceiling	next_action

Allowed url_extraction_verdict values:
- url_extracted: an explicit http(s) source URL was recovered locally; extracted_source_url must contain it.
- source_path_is_snapshot_only: local cache/snapshot confirms a source surface but no original URL is locally recoverable.
- wrapper_needs_parent_source: row points to a wrapper/source pack/index that needs parent source extraction first.
- duplicate_or_existing_core: row is already resolved by reviewed-core/source-ledger lineage.
- reject_noise: internal, derivative, or irrelevant noise.

Keep reasons concise. Replace tabs and newlines inside fields with spaces.
Write one output row per input row_id, no omissions, no extras, no duplicate row_id values.

Write the summary markdown with:
- batch id
- rows reviewed
- verdict counts
- boundary statement
- next smallest hardening move

Before stopping, verify that the result TSV has exactly the same row_id set and row count as input.tsv.
