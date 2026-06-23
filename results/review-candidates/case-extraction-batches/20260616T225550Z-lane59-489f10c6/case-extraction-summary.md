# Case extraction summary — 20260616T225550Z-lane59-489f10c6

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225550Z-lane59-489f10c6/input.tsv
Output TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225550Z-lane59-489f10c6/case-extraction-results.tsv

Reviewed source clusters: 16
Output rows: 16
Verification: PASS — output source_cluster_key set and row count match input.tsv; no duplicate output keys.

Verdict counts:
- case_candidate_for_hardening: 1
- closed_noncase_source_surface: 15
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Candidate retained for hardening:
- https://api.github.com/repos/langchain-ai/langchain/security-advisories/GHSA-pjwx-r37v-7724 — public GitHub Security Advisory for LangChain unsafe deserialization through overly broad `load()` allowlists. Claim is capped to advisory text, affected version ranges, patched versions, and exposure conditions stated by the advisory.

Noncase source surfaces:
- Remaining 15 clusters are policy/guidance/law, legislative, scholarly/DOI, portal, vendor documentation/product, or generic source-family surfaces without a concrete extracted AI edge-case event, vulnerability/finding, or official record suitable for reviewed-core hardening.

Boundary observed: no reviewed-core promotion, no ObscureAI addition, no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, or ranking claim.
