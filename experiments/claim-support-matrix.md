# Claim-Support Matrix for LIMEN Edge-Case Atlas

## Overview
This matrix maps key publication claims to supporting evidence sources, indicating authority scores, evidence types, and uncertainty flags. The artifact is intended for inclusion in the methods paper and dashboard hook for evidence visualization.

| Claim ID | Claim Statement | Supporting Source | Authority Score | Evidence Type | Linked Artifact | Uncertainty |
|----------|----------------|-------------------|-----------------|---------------|-----------------|-------------|
| C1 | EU AI Act enforcement mechanisms provide provenance tracking for high‑risk AI systems. | EU AI Act Enforcement Mechanisms (source 6) | 5 | Regulation | `sources/EU_AI_Act_Enforcement.pdf` (placeholder) | Low – explicit in regulation text |
| C2 | LIMEN crosswalk enriches mapping between AI governance frameworks and edge‑case taxonomy with provenance metadata. | LIMEN Crosswalk: AI Governance Frameworks (source-crosswalk-v0.2-enriched.tsv) | 5 | Crosswalk Artifact | `results/crosswalk-enriched.tsv` | Medium – relies on enrichment process |
| C3 | NIST AI RMF compliance guide supports risk management in public AI procurement. | NIST AI RMF Compliance Guide (source 23) | 5 | Government Standard | `sources/NIST_AI_RMF_Guide.pdf` (placeholder) | Low – official guide |
| C4 | Baltic Public AI Registry includes coverage of Latvia, Estonia, Lithuania, and Finno‑Ugric governance frameworks. | Baltic Public AI Registry entries for LV, EE, LT (source 4) | 5 | Registry | `results/baltic-registry-2026-06.csv` | High – coverage varies, some entries missing |
| C5 | Security edge‑case taxonomy includes non‑malicious misuse incidents (Type 007). | Evidence Schema Updates – Type 007 (methods.md) | 4 | Taxonomy | `results/security-edge-cases.tsv` | Medium – classification depends on incident reporting |
| C6 | Multi‑jurisdictional governance frameworks can be reliably compared using authority scores. | LIMEN Crosswalk methodology | 5 | Methodology | `methods-methodology.md` | Medium – subjectivity in scoring |
| C7 | Language coverage in public AI documents is uneven; Baltic languages have lower source authority. | Source authority scores per language | 4 | Language Distribution | `results/language-authority.csv` | High – limited English translations |

## Usage
- **Manuscript**: Insert rows as needed to substantiate claims in the article.
- **Dashboard**: Feed into evidence visualization pipeline (e.g., `dashboard/claims-heatmap.ipynb`).
- **Review**: Validate each claim against the latest source versions; update authority scores as required.

## Provenance
- **Generated**: 2026‑06‑28
- **Author**: Athena (Tyche Operations Agent)
- **Checksum**: placeholder‑checksum‑for‑claim‑support‑matrix
- **Version**: 0.1
- **Relevant Files**: `sources/*.md`, `results/crosswalk-enriched.tsv`, `methods.md`

*All data provenance, access dates, and rights notes are recorded in the source ledger (`sources/sources.md`).*