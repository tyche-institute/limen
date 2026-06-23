# Case extraction summary: 20260616T225502Z-lane05-e19b26a0

- Input rows reviewed: 16
- Output rows written: 16
- Verdict counts: {'closed_noncase_source_surface': 15, 'needs_original_source_text': 1}
- Case candidates for hardening: 0
- Reviewed-core promotions: 0
- ObscureAI additions: 0

## Extraction notes

Every input source_cluster_key was handled exactly once. The batch is dominated by policy, regulator guidance, legal text, sandbox/programme, standards, API/developer, and source-family/index pages. These surfaces can support provenance or contextual accounting, but do not by themselves provide a concrete event/action/vulnerability/finding/official case record with a bounded claim.

The EUDI wallet URL resolved to a page-not-found surface during exact-URL checking, so it was marked `needs_original_source_text` rather than promoted or treated as a substantive source. Digdir guidance URLs that returned HTTP 403 were still closed as noncase source surfaces based on input metadata and source type; no case claim was extracted from them.

Boundary respected: no reviewed-core promotion, no ObscureAI addition, no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence claim, or ranking claim.
