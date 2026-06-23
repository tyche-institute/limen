# Case extraction summary: 20260616T225503Z-lane22-2d15bc6c

Completed at UTC: 2026-06-16T22:56:08Z

Input rows reviewed: 16
Output rows written: 16

Verdict counts:

- closed_noncase_source_surface: 16
- case_candidate_for_hardening: 0
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Method:

- Reviewed each source_cluster_key from input.tsv exactly once.
- Used the input metadata and exact source_url_or_locator values only.
- Performed exact-URL checks for public URLs where reachable; did not broad crawl or invent URLs.
- Applied extraction boundary: source/register/vendor/product/policy surfaces without a concrete event/action/vulnerability/finding/official record were closed as noncase source surfaces.

Outcome:

All 16 clusters were closed_noncase_source_surface. None contained enough bounded, concrete case-level evidence for later reviewed-core/ObscureAI hardening in this extraction pass.

Verification:

- Result TSV header matches the required schema.
- Result TSV has one row per input source_cluster_key.
- No duplicate output source_cluster_key values.
- Output source_cluster_key set matches input.tsv exactly.
