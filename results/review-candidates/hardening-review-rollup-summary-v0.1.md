# LIMEN hardening review rollup

- Generated: 2026-06-23T17:24:37Z
- All queues complete: `True`
- Current output clean: `True`
- Has stale extra result rows: `True`

## named-url-extraction

- Queue rows: `214`
- Result rows: `214`
- Complete: `True`
- Verdict counts: `{"duplicate_or_existing_core": 1, "source_path_is_snapshot_only": 18, "url_extracted": 114, "wrapper_needs_parent_source": 81}`
- Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/named-url-extraction-results-v0.1.tsv`

## translation-source-review

- Queue rows: `554`
- Result rows: `554`
- Complete: `True`
- Verdict counts: `{"candidate_for_url_extraction": 72, "cross_project_duplicate": 349, "machine_translation_hold": 17, "needs_original_language_source": 16, "reject_noise": 38, "translation_source_reviewed": 62}`
- Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/translation-source-review-results-v0.1.tsv`

## Boundary

Hardening review outputs are bounded source-review aids only. Promotion to reviewed core remains a separate human case-hardening step.
