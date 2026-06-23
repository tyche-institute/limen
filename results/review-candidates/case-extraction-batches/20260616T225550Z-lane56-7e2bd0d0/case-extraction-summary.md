# Case extraction summary: 20260616T225550Z-lane56-7e2bd0d0

Input rows reviewed: 16
Output rows written: 16

Verdict counts:
- case_candidate_for_hardening: 1
- closed_noncase_source_surface: 15

Extraction notes:
- Reviewed every input source_cluster_key exactly once.
- Most clusters are final noncase source surfaces: standards pages, parent institutional pages, laws/guidance, vendor documentation/product pages, procurement/tender indexes, or incident intake forms without a concrete AI edge-case event/finding.
- One cluster remains a hardening candidate only: the LinkedIn post alleging an SSRN citation-scam pattern. It is not promoted; the claim is bounded to a public allegation/source lead and requires original SSRN/preprint/index records before reviewed-core consideration.
- No reviewed-core promotion, ObscureAI addition, incident-truth claim, legal/safety/compliance finding, deployment proof, prevalence claim, or ranking claim was made.

Verification:
- Result TSV header matches the required schema.
- Result TSV source_cluster_key set and row count were checked against input.tsv.
