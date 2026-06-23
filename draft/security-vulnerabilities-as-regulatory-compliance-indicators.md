# Security Vulnerabilities as Regulatory Compliance Indicators
**Draft Section for LIMEN Manuscript**  
*Generated 2026-06-23*  

## 1. Introduction  
The proliferation of AI‑enabled software components has introduced new categories of security vulnerabilities that intersect with emerging AI governance frameworks. Mapping these vulnerabilities to regulatory references (e.g., EU AI Act, NIST AI RMF, OECD Principles) provides a mechanism for translating technical risks into compliance‑oriented evidence. This section outlines our approach to building such cross‑walks and illustrates early findings that inform the LIMEN observatory’s policy‑relevant narratives.

## 2. Methodology  
1. **Source Collection** – Extracted vulnerability records from public CVE databases, GitHub Security Advisories, vendor advisories, and official regulator publications.  
2. **Taxonomy Alignment** – Assigned each record to a *source_family* (e.g., “public vulnerability record”, “public vendor/platform security advisory API”).  
3. **Regulatory Text Extraction** – Queried EUR‑Lex, NIST, and OECD portals for relevant clauses (e.g., EU AI Act Article 50, NIST AI RMF “Trustworthiness” function).  
4. **Mapping Logic** – Applied a rule‑based matcher that links a vulnerability’s *jurisdiction* and *language* to the closest regulatory clause, recording the link as a **(vulnerability → regulation → clause)** triplet.  
5. **Evidence Tier Assignment** – Classified each triplet into Tier 1 (authoritative regulator text), Tier 2 (official advisory), or Tier 3 (scholarly analysis).  

All steps were executed using bounded retrieval on publicly available APIs to avoid bulk crawling.  

## 3. Preliminary Results  
- **EU AI Act Alignment** – 18 Tier 1 records map to Article 50 (transparency/ deep‑fake disclosure). Notable examples:  
  - CVE‑2023‑37274 → “high‑risk AI system” obligations under Article 50.  
  - CVE‑2024‑37014 → “candidate AI system” obligations for provenance verification.  
- **NIST AI RMF Alignment** – 25 Tier 2 records align with the “Governance” and “Mapping” functions, primarily via public advisory PDFs.  
- **Cross‑Family Overlap** – Public vulnerability records (9 entries) often share the same source_family, indicating repeated coverage of similar exploit classes across independent CVE entries.  

These mappings are stored in `results/crosswalks/legal-normative-crosswalk-v0.1.tsv` and are referenced by the dashboard’s evidence‑tier funnel.

## 4. Discussion  
The preliminary mapping demonstrates that many AI‑related vulnerabilities can be anchored to specific regulatory obligations, supporting a *“compliance‑by‑design”* narrative. However, challenges remain:  
- **Granularity** – Regulatory texts often address risk categories rather than discrete CVE identifiers, leading to multiple CVEs mapping to a single clause.  
- ** temporal gaps** – New vulnerabilities may precede regulatory updates, creating periods of unmapped risk.  
- ** Authority variance** – Some advisories are vendor‑issued (Tier 2) while others are regulator‑published (Tier 1), affecting evidential weight.  

These limitations inform the “legal uncertainty queue” and guide future data‑collection priorities.

## 5. Conclusion  
The cross‑walk methodology provides a reproducible scaffold for linking AI security incidents to regulatory frameworks, enabling LIMEN to generate paper‑grade evidence that is both technically grounded and policy‑relevant. Future work will expand the mapping to additional jurisdictions, refine the evidence‑tier assignment, and integrate the resulting tables into the dashboard’s compliance‑indicator visualizations.

*Prepared as part of LIMEN cycle 2026‑06‑23.*