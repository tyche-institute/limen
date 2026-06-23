# Case extraction summary — 20260616T225549Z-lane46-179cdf7f

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane46-179cdf7f/input.tsv`

Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane46-179cdf7f/case-extraction-results.tsv`

Reviewed source_cluster_key rows: 16

Verdict counts:
- closed_noncase_source_surface: 14
- blocked_no_public_source: 1
- reject_noise: 1

Extraction notes:
- No cluster was promoted to reviewed-core or ObscureAI.
- Most supplied URLs were programme pages, portals, document indexes, policy/legal text, standards pages, or other generic source surfaces.
- The EasyChair submitted-paper URL was blocked because the exact supplied URL redirects to login and exposes no public source text.
- The FCA social image asset was rejected as noise.
- All bounded claims are limited to source-surface accounting and avoid incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, and ranking claims.

Verification:
- Result TSV row count and source_cluster_key set were checked against input.tsv.
