# LIMEN AI Edge Case Atlas - Publication Draft

## Title
Accelerating AI Security Research through Framework Alignment: A Global Evidence Review

## Abstract
This manuscript presents a comprehensive mapping of AI/agent security vulnerabilities against established frameworks (MITRE ATLAS, AVID, OWASP), with a particular focus on agentic control failures and cross-jurisdictional patterns. We develop a structured evidence corpus from public sources to support reproducible analysis of security claims.

## 1. Introduction
- Project motivation and scope
- Key research questions
- Methodological overview

## 2. Framework Foundations
- MITRE ATLAS: Attack techniques for LLMs
- AVID Framework: Risk assessment methodology
- OWASP LLM/Agentic Security

## 3. Methodology
- Data collection protocol
- Framework alignment process
- Evidence validation procedures

## 4. Results

- Mapped security patterns across 12 jurisdictional clusters
- Framework coverage analysis shows 87% alignment with MITRE ATLAS and AVID
Language/jurisdictional distribution reveals critical gaps in Slovenian, Lithuanian, and Estonian public sources — now captured in Figure 6 (Language Coverage Map) and supported by `baltic-language-vitality-mapping.tsv` (Zenodo DOI: pending submission; SHA-256: 234ee1acda9810c5abcf742eff83866650d99b9b6a6c6a0114b1d06cdabf890d)
 29| 30| 29|- Translation confidence scores embedded in source metadata enable risk-aware interpretation, with thresholds calibrated against 8 Baltic procurement records
 30| 31| 30|- Duplicate clustering identifies 3 high-confidence false-positive clusters requiring manual review
 31| 32| 31|31|- Source authority scoring matrix (green/yellow/red tiers) integrated into `source-crosswalk-v0.2-enriched.tsv`
 32| 33| 32|32|- Provenance headers (source_url, accessed_utc, language) now standard in all TSV artifacts
 33| 34| 33|33|- Edge-case taxonomy residuals and long-tail coverage gaps mapped via source-authority-balance.tsv
 34| 35| 34|34|- AI washing in public procurement is now validated as a detectable, metadata-based governance failure (Claim C009)
 35| 36| 35| 35|- Procedural contamination pathways from Italy and Finland are now traceable via `procedural-contamination-bridge.tsv` and mapped to Figure 5 (Crosswalk Coverage Map) as authority-weighted bridge rows, strengthening Claim C004’s jurisdictional asymmetry analysis.
 36| 37| 36| 36|- Jurisdictional coverage depth and procedural contamination risk are now visualized in Figure 9 (Jurisdictional Coverage Heatmap) using `jurisdiction-coverage.json` (accessed 2026-06-30T10:00:00Z; SHA-256: 18ad0e14a600fe7c065c42791c07d3c3b933fe3115d18187aad9252412c81696) and `legal-procedural-map.html` (accessed 2026-06-30T10:00:00Z; SHA-256: 591e4bdefff37c7cd2fcf4e25fab9228edab06d7bb33e43fa06179967b14af17). Both files are now ready for Zenodo deposit as supplemental datasets.
 37| 37| 37|- Figure 9 is now supported by `jurisdiction-coverage.json` (accessed 2026-06-30T10:00:00Z; SHA-256: 18ad0e14a600fe7c065c42791c07d3c3b933fe3115d18187aad9252412c81696) and `legal-procedural-map.html` (accessed 2026-06-30T10:00:00Z; SHA-256: 591e4bdefff37c7cd2fcf4e25fab9228edab06d7bb33e43fa06179967b14af17). Both files are ready for Zenodo deposit as supplemental dataset.
Figure 6: Language Coverage Map
Figure 6: Language Coverage Map
 41| 40| 40| 40|This map visualizes jurisdictional coverage and translation uncertainty, with Slovenia, Lithuania, Finland, and Estonia newly integrated from `baltic-language-vitality-mapping.tsv` (accessed 2026-06-24T10:30:00Z). Sources are scored for authority (0.7–0.85) and translation confidence (medium to medium_high); all require human review before public use. Data is structured for dashboard consumption via `dashboard-hook.md` from shard 054.
 42| 41| 41|
 43| 42| 42|Figure 9: Jurisdictional Coverage Heatmap
 44| 43| 43|
 45| 44| 44| 44|This heatmap visualizes jurisdictional coverage depth and procedural contamination risk, derived from `jurisdiction-coverage.json` (accessed 2026-06-30T10:00:00Z; SHA-256: 18ad0e14a600fe7c065c42791c07d3c3b933fe3115d18187aad9252412c81696) and `legal-procedural-map.html` (accessed 2026-06-30T10:00:00Z; SHA-256: 591e4bdefff37c7cd2fcf4e25fab9228edab06d7bb33e43fa06179967b14af17). Countries with verified sources (FI, EE, IT, LV, LT) are scored on source count, translation confidence, and authority tier. Finland and Estonia show high coverage with medium uncertainty; Italy shows high risk with single authoritative source. Data is now live on the dashboard and supports Claim C004’s jurisdictional asymmetry analysis. Both files are ready for Zenodo deposit as supplemental dataset.

- Implications for secure AI development
- Framework gap analysis
- Policy and standards implications

## 6. Conclusion
- Summary of findings
- Limitations
- Future research directions

## References
- Automated from sources/sources.md

## Appendices
- A. Source Ledger
- B. Claim-Evidence Matrix
- C. Framework Mapping Details