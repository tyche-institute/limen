# Case extraction summary — 20260616T225502Z-lane14-ae57c955

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane14-ae57c955/input.tsv`

Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225502Z-lane14-ae57c955/case-extraction-results.tsv`

Verdict counts:

- closed_noncase_source_surface: 16
- case_candidate_for_hardening: 0
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Review notes:

- Reviewed all 16 input `source_cluster_key` values exactly once.
- The batch consists of register/catalogue/guidance/policy/open-data/source-family surfaces. None of the rows isolate a concrete AI edge-case event, vulnerability, finding, enforcement action, or official case-level record suitable for reviewed-core/ObscureAI hardening.
- Exact public URL checks were limited to URLs supplied in `source_url_or_locator`; no broad web crawling or invented URLs were used. Some exact URL fetches were blocked/timed out, but the supplied local metadata was still sufficient to close them as noncase source surfaces rather than cases.
- No reviewed-core promotion, ObscureAI addition, submission, publication, upload, registration, payment, login, email, or other public action occurred.

Verification:

- Input row count: 16
- Result row count: 16
- Unique input keys: 16
- Unique result keys: 16
- Key-set equality: PASS
- Duplicate output keys: none
