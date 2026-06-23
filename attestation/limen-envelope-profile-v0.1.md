LIMEN Attestation Receipt Profile v0.1
-------------------------------------

Purpose:
Define the evidence envelope for LIMEN case observation, extraction, classification,
review, clustering, and publication. This profile outlines what is recorded,
how it is structured, and how it maps to evidence roles without making truth,
legal, safety, compliance, or certification claims.

Scope:
- Observation: raw data captured from source.
- Extraction: transformation into structured records.
- Classification: assignment of RATS-style evidence roles.
- Review: human or automated validation.
- Clustering: grouping of related evidence.
- Publication: inclusion in evidence matrices, graphs, or dashboards.

Evidence Roles (RATS-inspired):
- Raw Observation (RO)
- Processed Record (PR)
- Verified Claim (VC)
- Supporting Evidence (SE)
- Refuted Claim (RC)

Provenance:
Each record must link to source path/URL, retrieval date, language, jurisdiction,
rights/terms, and a unique hash/checksum.

Structure:
{
  "profile_version": "0.1",
  "observation_schema": "...",
  "extraction_pipeline": "...",
  "classification_rules": "...",
  "review_workflow": "...",
  "clustering_approach": "...",
  "publication_targets": ["evidence_graphs", "standards_matrices", "policy_briefs"]
}

Publication Readiness:
- Link to journal.md and claims.md
- Generate evidence graphs for dashboard consumption
- Provide clear mapping to claim-support links
- Include uncertainty flags where applicable