You are Hermes/Codex performing a bounded LIMEN source-review batch.

Input TSV:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/source-review-batches/20260614T091814Z-lane07-9e1d20a9/source-review-input.tsv

Required outputs:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/source-review-batches/20260614T091814Z-lane07-9e1d20a9/source-review-results.tsv
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/source-review-batches/20260614T091814Z-lane07-9e1d20a9/source-review-summary.md

Update this manifest status/details when complete:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/source-review-batches/20260614T091814Z-lane07-9e1d20a9/manifest.json

Task:
- Review every row in source-review-input.tsv exactly once.
- Use local metadata and local source files only. Do not broad web crawl. Do not email, upload, submit, publish, register, pay, deploy, or take public/portal actions.
- This is source-surface triage only. Do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.
- If a local source_path exists and the needed evidence is local, you may inspect only the relevant local lines/nearby context. If it is too large or unavailable, classify from the local row metadata and say so in the reason.

Write source-review-results.tsv with exactly this header:
signal_id	source_review_verdict	source_review_role	reason	claim_ceiling	next_action	source_path

Allowed source_review_verdict values:
- source_reviewed_candidate
- merge_existing_surface
- negative_evidence_candidate
- needs_named_source_extraction
- translation_review_needed
- reject_noise

Rubric:
- source_reviewed_candidate: row names a concrete official, regulator, institutional, vendor/advisory, court, register, procurement, notice, or other direct source surface sufficient for bounded source-surface existence review.
- translation_review_needed: row names a plausible direct source surface but the local evidence is materially non-English or translation-sensitive.
- needs_named_source_extraction: row is a source-pack, country profile, index row, wrapper, or adjacent artifact that points toward a source but does not expose a named reviewable source surface yet.
- negative_evidence_candidate: row records a search-negative, gap warning, weak-source warning, or absence/evidence-limit result.
- merge_existing_surface: row duplicates or points to an already-modeled local registry/dashboard/atlas surface and should be deduplicated rather than promoted again.
- reject_noise: row is internal manuscript/prose/script/config/log/package noise or another derived artifact that should not remain in the direct-source queue.

Keep reasons concise. Replace tabs and newlines inside fields with spaces.
Write one output row per input signal_id, no omissions, no extras, no duplicate signal_id values.

Write source-review-summary.md with:
- batch id
- rows reviewed
- verdict counts
- boundary statement
- next smallest queue-hardening move

Before stopping, verify that source-review-results.tsv has exactly the same signal_id set and row count as source-review-input.tsv.
