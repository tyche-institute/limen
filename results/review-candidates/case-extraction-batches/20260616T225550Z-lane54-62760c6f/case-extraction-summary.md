# Case extraction summary: 20260616T225550Z-lane54-62760c6f

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225550Z-lane54-62760c6f/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225550Z-lane54-62760c6f/case-extraction-results.tsv

Reviewed 16 source_cluster_key values exactly once.

Verdict counts:
- case_candidate_for_hardening: 1
- closed_duplicate_existing_core: 0
- closed_noncase_source_surface: 14
- blocked_no_public_source: 0
- needs_original_source_text: 1
- reject_noise: 0

Notes:
- One candidate was retained for hardening only: Microsoft Source Asia's Jugalbandi public-service access article.
- One cluster needs original source text: the Dominican Republic DGM page was blocked by Cloudflare/bot verification, so metadata alone was not used for a final case verdict.
- All other clusters were closed as noncase source surfaces because they are portals, institutional homepages, policy/guidance/index pages, regulatory sandbox programme descriptions, or generic service pages without a concrete AI edge-case event/finding.
- No reviewed-core promotion, ObscureAI addition, publication, upload, portal action, or broad web crawling occurred.

Verification:
- Output TSV uses the required header.
- Output TSV has one data row per input source_cluster_key, no omissions, extras, or duplicates.
- Fields were sanitized to remove tabs/newlines inside values.
