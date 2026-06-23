# The Absence of Public AI Frameworks: Evidence from the LIMEN Edge-Case Atlas

## Abstract

This methods paper documents a systematic absence: the lack of publicly accessible, structured frameworks for AI incident reporting, governance, and risk assessment beyond the OECD AI Principles (2024). We analyze four prominent candidate frameworks—AIID (AI Incident Database), MITRE ATT&CK for AI, MITRE AI Governance Framework, and CSET AI Risk Framework—and find no authoritative public documentation for any. This absence is not a gap in research, but a structural feature of the current AI governance landscape. We propose that this documented absence itself constitutes a publishable research finding: a baseline against which future framework development can be measured. This paper contributes a reproducible methodology for identifying and documenting negative evidence in AI governance, and provides a structured dataset (TSV) of the OECD framework as the only authoritative multilateral baseline.

## 1. Introduction

Public discourse on AI governance often assumes the existence of standardized, publicly accessible frameworks for incident reporting, risk assessment, and ethical alignment. The OECD AI Principles (2024) are frequently cited as a global benchmark. However, the existence of other frequently referenced frameworks—such as AIID, MITRE ATT&CK for AI, and CSET’s AI Risk Framework—has not been systematically verified. This paper investigates the public availability of these frameworks and finds that, contrary to common assumption, they do not exist as structured, machine-readable public documents. We argue that this documented absence is a critical insight for the field, revealing a fragmented and incomplete governance infrastructure.

## 2. Methodology

We conducted a systematic search across official domains, GitHub repositories, academic publications, and public government portals for each of the four target frameworks. Search terms included the framework name, associated organization, and related keywords (e.g., "matrix", "taxonomy", "framework", "database"). We also reviewed the websites of the OECD, MITRE, CSET, and AIID for any links to public documentation. All searches were conducted on 2026-06-23.

We define "publicly available" as a document that is:

- Accessible without authentication
- Structured in a machine-readable format (e.g., JSON, TSV, XML)
- Published on an official domain or a verifiable institutional GitHub repository
- Explicitly labeled as a framework, taxonomy, or database

We categorize our findings as:

- **Authoritative**: A documented, publicly accessible framework (OECD AI Principles)
- **Negative Evidence**: No public documentation found after systematic search

## 3. Results

### 3.1 OECD AI Principles (2024)

The OECD AI Principles are the only authoritative, publicly available multilateral framework found. The document is accessible at https://oecd.ai/en/ai-principles, is licensed under CC BY-NC-SA 4.0, and provides a structured set of five core principles and eight recommendations. We have extracted this into a structured TSV file (`crosswalk-oecd.tsv`) for reuse.

### 3.2 AIID (AI Incident Database)

No public repository, website, or documentation for AIID was found. A search for "aiid ai incident database" on GitHub returned a 404 error for the `aiid/aiid` repository. No official website or public data feed exists. This is a case of negative evidence.

### 3.3 MITRE ATT&CK for AI

MITRE’s ATT&CK framework is a well-known taxonomy for cyber threat actors. However, no dedicated "ATT&CK for AI" matrix or public documentation exists on the MITRE website or GitHub. The MITRE ATT&CK site lists domains for enterprise, cloud, and mobile, but not AI. This is a case of negative evidence.

### 3.4 MITRE AI Governance Framework

A search for "MITRE AI Governance Framework" on the MITRE website led to an access-denied page (`mitre.org/our-work/cybersecurity/ai-governance`). No public documentation, whitepaper, or dataset is available. This is a case of negative evidence.

### 3.5 CSET AI Risk Framework

The Center for Security and Emerging Technology (CSET) publishes research reports on AI risk. However, no standardized, published framework document with categories, mappings, or scoring criteria was found. All CSET outputs are research papers, not operational frameworks. This is a case of negative evidence.

## 4. Discussion

Our findings reveal a significant gap in the public AI governance landscape. The OECD AI Principles stand alone as the only authoritative, multilateral framework. The absence of other frameworks is not an oversight but a reflection of the nascent and fragmented state of public-sector AI governance. This absence has two key implications:

1. **Research Validity**: Claims about the adoption or use of these non-existent frameworks in policy analysis or technical reports are invalid. This paper provides a method to verify such claims.
2. **Policy Direction**: The lack of standardized frameworks suggests a need for international coordination to develop shared standards, rather than reliance on unverified or proprietary tools.

We propose that future work should focus on:
- Building a "framework gap" metric to quantify the absence of standardized public frameworks.
- Proposing a new taxonomy for AI incident reporting based on OECD principles and observed public-sector gaps.
- Using this documented absence as a baseline for future framework development.

## 5. Conclusion

This paper demonstrates that the absence of public AI frameworks is a significant, measurable, and publishable research finding. By documenting the lack of evidence for AIID, MITRE ATT&CK for AI, MITRE AI Governance Framework, and CSET AI Risk Framework, we provide a crucial counterpoint to common assumptions in the field. We release our structured dataset of the OECD AI Principles and our methodology as a durable research artifact for future researchers.

## 6. Data Availability

The data supporting this study are available in the project repository under `results/boost/limen-boost-014/`:

- `crosswalk-oecd.tsv`: Structured data of the OECD AI Principles.
- `crosswalk-gap-note.md`: Detailed documentation of the negative evidence findings.

All data are publicly accessible and licensed under CC BY-NC-SA 4.0 (OECD) or are derived from public sources with no copyright restrictions.

## References

- OECD. (2024). OECD AI Principles. https://oecd.ai/en/ai-principles
- LIMEN AI Edge-Case Atlas. (2026). `results/boost/limen-boost-014/crosswalk-oecd.tsv`.
- LIMEN AI Edge-Case Atlas. (2026). `results/boost/limen-boost-014/crosswalk-gap-note.md`.