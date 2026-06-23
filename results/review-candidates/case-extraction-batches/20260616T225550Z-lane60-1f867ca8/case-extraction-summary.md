# Case extraction summary: 20260616T225550Z-lane60-1f867ca8

Input rows reviewed: 16
Output rows written: 16

Verdict counts:
- case_candidate_for_hardening: 1
- needs_original_source_text: 1
- closed_noncase_source_surface: 14
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- reject_noise: 0

Extraction notes:
- One official agency page was treated as a bounded case candidate: Sri Lanka vocational education ministry launch of a fully AI-based government service-delivery chatbot integrated with Hotline 1966.
- The Pakistan FBR chatbot news URL remains a plausible concrete lead, but inspection returned a Cloudflare/403 interstitial, so it is marked needs_original_source_text rather than promoted as a case candidate.
- Standards/specification pages (SLSA, SPDX, C2PA), policy/guidance/law/project pages (SPDP, TEM, Traficom, TTJA), journal/index surfaces, and the Panama fintech hub page were closed as noncase source surfaces.
- TED notice 3515-2024 was closed as noncase because local audit material marks it as excluded keyword-noise/negative control and the public page returned no reviewable text in this run.

Verification:
- The result TSV was generated in input order with one row per input source_cluster_key.
- No reviewed-core promotion, ObscureAI addition, public action, broad crawl, or incident/legal/safety/compliance finding was made.
