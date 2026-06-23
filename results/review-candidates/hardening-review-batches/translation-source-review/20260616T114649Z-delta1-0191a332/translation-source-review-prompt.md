You are Hermes/Codex performing a bounded LIMEN translation-source-review batch.

Input TSV:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/hardening-review-batches/translation-source-review/20260616T114649Z-delta1-0191a332/input.tsv

Required outputs:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/hardening-review-batches/translation-source-review/20260616T114649Z-delta1-0191a332/translation-source-review-results.tsv
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/hardening-review-batches/translation-source-review/20260616T114649Z-delta1-0191a332/translation-source-review-summary.md

Update this manifest status/details when complete:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/hardening-review-batches/translation-source-review/20260616T114649Z-delta1-0191a332/manifest.json

Task:
- Review every row in input.tsv exactly once.
- Use local metadata and local source files only. You may use multilingual understanding, but do not turn machine translation into a factual/legal claim.
- Do not broad web crawl. Do not email, upload, submit, publish, register, pay, deploy, or take public/portal actions.
- This is translation-aware source review only. Do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.

Write translation-source-review-results.tsv with exactly this header:
row_id	signal_id	translation_review_verdict	language_reviewed	source_url_or_locator	source_name	reason	claim_ceiling	next_action

Allowed translation_review_verdict values:
- translation_source_reviewed: the row has enough original-language or translated local context plus a named source/locator for bounded source-surface review.
- needs_original_language_source: plausible lead, but original-language source/URL is missing or insufficient.
- cross_project_duplicate: derived GAIA/Pallas/Atlas/public-registry artifact that should be routed upstream or deduplicated, not promoted here.
- machine_translation_hold: only machine-translated summary/gloss is present; keep held.
- candidate_for_url_extraction: source clues exist, but the next move is named URL extraction.
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
