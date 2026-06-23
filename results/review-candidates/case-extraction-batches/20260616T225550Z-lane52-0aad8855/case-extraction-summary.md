# Case extraction summary: 20260616T225550Z-lane52-0aad8855

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225550Z-lane52-0aad8855/input.tsv
Output TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225550Z-lane52-0aad8855/case-extraction-results.tsv

Reviewed source_cluster_key count: 16
Result row count: 16
Verification: PASS - output source_cluster_key set exactly matches input source_cluster_key set; no duplicates, no omissions, no extras.

Verdict counts:
- case_candidate_for_hardening: 3
- closed_duplicate_existing_core: 0
- closed_noncase_source_surface: 12
- blocked_no_public_source: 1
- needs_original_source_text: 0
- reject_noise: 0

Case candidates for later hardening:
- https://innovationisrael.org.il/en/press_release/personalized-education-tech - official Israel AI education sandbox announcement; harden only as announced program intent, not verified classroom deployment/outcomes.
- https://intic.gov.mz/itu-aprova-apoio-ao-estabelecimento-do-sandbox-regulatorio-de-inteligencia-artificial-em-mocambique - official Mozambique INTIC report of ITU support approval for establishing an AI regulatory sandbox; harden only as support/establishment action.
- https://irs.gov/about-irs/using-voice-and-chat-bots-to-improve-the-collection-taxpayer-experience - official IRS article on voice/chat bots for collection taxpayer experience; harden with explicit AI-characterization check.

Boundary notes:
- No reviewed-core promotion was performed.
- No ObscureAI addition was performed.
- No incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, or ranking claim was made.
- Exact URL inspection was limited to source_url_or_locator values from input.tsv; no broad crawling or general web search was used.
