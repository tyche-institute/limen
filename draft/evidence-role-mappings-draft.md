# Evidence-Role Mapping Draft (Human Review)

## 1. Purpose
This draft documents the mapping between source evidence items and evidence roles used in the LIMEN Attestation Receipt Profile (ARP). It supports the EU AI Act Article 19 alignment claim and informs the clustering methodology for evidence organization.

## 2. Mapping Methodology
The mapping follows a three-step process:
1. Source selection based on inclusion criteria (public/open, relevant to AI governance, digital identity, trust architectures).
2. Role assignment using role taxonomy (e.g., `profile-definition`, `evidence-role`, `clustering-input`).
3. Provenance annotation with metadata (language, jurisdiction, access date, rights).

Each mapping includes:
- Source identifier (file path or URL)
- Assigned evidence role
- Brief description of relevance
- Language and jurisdiction metadata
- Confidence flag (high/medium/low)
- Access and rights notes

## 3. Evidence-Role Mappings
| Source | Role | Description | Language | Jurisdiction | Access Date | Rights/Terms | Confidence |
|--------|------|-------------|----------|--------------|--------------|--------------|------------|
| /srv/tyche/projects/limen-ai-edge-case-atlas/attestation/limen-envelope-profile-v0.1.md | Profile Definition | Defines the attestation receipt profile structure | English | EU | 2026-06-25 | CC0 | High |
| /srv/tyche/projects/limen-ai-edge-case-atlas/sources/baltic-language-vitality-mapping.tsv | Language Evidence | Maps Baltic language vitality to UNESCO levels | Baltic languages | Estonia, Latvia, Lithuania, Slovenia | 2026-06-24 | CC0 | High |
| /srv/tyche/projects/limen-ai-edge-case-atlas/sources/G-001.jsonl | Procurement Example | Finland public tender with AI washing risk | Finnish | Finland | 2026-06-23 | Public Domain | Medium |
| /srv/tyche/projects/limen-ai-edge-case-atlas/sources/detecting-ai-washing-in-procurement-tenders.md | Detection Method | Metadata-only detection of AI washing in tenders | English | International | 2026-06-23 | CC-BY-4.0 | High |
| (additional entries will be populated as evidence ledger expands) |  |  |  |  |  |  |  |

*Additional sources will be populated as the evidence ledger expands.*

## 4. Clustering Methodology
The clustering approach groups sources by semantic similarity and jurisdictional relevance:
- **Vectorization**: Sources are vectorized using multilingual sentence embeddings.
- **Similarity Scoring**: Cosine similarity is computed between vectors.
- **Linkage**: Hierarchical agglomerative clustering with a distance threshold of 0.35.
- **Cluster Labels**: Assigned based on dominant jurisdiction and topic.
- **Uncertainty Handling**: Clusters with mixed language content are flagged for review.

Clusters are linked to evidence roles to enable role-based dashboard hooks.

## 5. Outstanding Items for Human Review
- Validate role assignments for sources with medium confidence.
- Review clustering boundaries for cross-language clusters.
- Confirm confidence flag assignments for non-English sources.
- Verify rights and terms metadata completeness.

## 6. Appendices
- **Appendix A**: Source Access Details (full provenance list).
- **Appendix B**: Role Taxonomy Definitions.
- **Appendix C**: Glossary of Terms.

*Prepared for Anton Sokolov's legal review scheduled for 2026-09-30.*