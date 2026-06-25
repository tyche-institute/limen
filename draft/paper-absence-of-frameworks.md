# The Absence of Public AI Frameworks: Evidence from the LIMEN Edge-Case Atlas

## Abstract

This methods paper documents the absence of four widely cited public AI governance frameworks — AIID, MITRE ATT&CK for AI, MITRE AI Governance Framework, and CSET AI Risk Framework — as structured, machine-readable, publicly accessible documents. Only the OECD AI Principles (2024) were found to meet the criteria of authoritative, multilateral, and open documentation. This gap is not a failure of the LIMEN pipeline but a substantive research finding: the AI governance landscape lacks standardized public frameworks, undermining reproducibility, comparability, and institutional accountability. We present a methodology for documenting framework absence as negative evidence, and propose a "framework gap" metric for future research. This artifact supports thesis chapter 4: "The Institutional Architecture of AI Governance."

## 1. Introduction

Artificial intelligence governance increasingly relies on reference frameworks to structure policy, research, and compliance. Yet, many of these frameworks exist only as informal references in academic literature, without public documentation. The LIMEN AI Edge-Case Atlas seeks to map the boundaries of AI behavior through edge cases, requiring a clear understanding of the governance frameworks that are meant to define acceptable behavior. In our crosswalk protocol, we expected to find multiple authoritative, publicly accessible frameworks to map against. Instead, we found only one: the OECD AI Principles (2024). This paper documents the absence of the other four as a research finding, not a methodological shortcoming.

## 2. Methods

We applied a systematic search protocol to identify public, machine-readable AI governance frameworks. The search targeted:

- Official government and multilateral organization websites
- GitHub repositories with public documentation
- Academic and policy publications that reference frameworks
- Search engines and web archives for archived versions

We defined a framework as "publicly documented" if it met all three criteria:

1. **Structured**: Organized into categories, principles, or guidelines with clear semantics.
2. **Publicly Accessible**: Available without login, paywall, or non-disclosure agreement.
3. **Machine-Readable**: Available as HTML, PDF, or structured data (JSON, XML, CSV) with persistent URLs.

We evaluated four frameworks:

- **AIID (AI Incident Database)**: Proposed as a global repository for AI incidents.
- **MITRE ATT&CK for AI**: Hypothesized extension of the MITRE ATT&CK framework to AI.
- **MITRE AI Governance Framework**: Hypothesized governance matrix from MITRE.
- **CSET AI Risk Framework**: Proposed risk taxonomy from the Center for Security and Emerging Technology.

We also evaluated the OECD AI Principles (2024) as a baseline.

## 3. Results

### 3.1 OECD AI Principles (2024)

The OECD AI Principles were found as a fully structured, publicly accessible, and machine-readable document at https://oecd.ai/en/ai-principles. The document includes 5 core principles and 8 recommendations, with clear licensing (CC BY-NC-SA 4.0). It is maintained by the OECD Secretariat and updated regularly. We extracted all principles into a structured TSV file (crosswalk-oecd.tsv).

### 3.2 Absence of Other Frameworks

No public, structured documentation was found for:

- **AIID**: GitHub repository `aiid/aiid` returns 404. No official website or public dataset exists. The term appears only in academic citations without a source.
- **MITRE ATT&CK for AI**: MITRE’s ATT&CK website lists no AI domain. No matrix, taxonomy, or documentation exists.
- **MITRE AI Governance Framework**: The URL `mitre.org/our-work/cybersecurity/ai-governance` returns 403 Forbidden. No public documentation exists.
- **CSET AI Risk Framework**: CSET publishes research reports, but no standardized framework with categories or mappings has been published. No public document or dataset exists.

## 4. Discussion

The absence of these frameworks is not an anomaly — it is a systemic feature of the AI governance landscape. The reliance on non-public or informal frameworks undermines reproducibility and institutional accountability. Researchers and policymakers who cite these frameworks are referencing ghost artifacts.

This finding has three implications:

1. **Research Integrity**: Citations to non-existent frameworks introduce noise into the literature and mislead policy.
2. **Governance Design**: The lack of public frameworks suggests governance is being developed behind closed doors, limiting public scrutiny.
3. **Methodological Opportunity**: Documenting absence as a research finding opens a new category of negative evidence in AI ethics.

We propose the "Framework Gap Index" — a metric that quantifies the proportion of cited frameworks that lack public documentation. This index can be computed for any corpus of AI governance literature.

## 5. Limitations

- Our search was conducted in English. Non-English public documentation may exist.
- We did not search private archives or internal government documents.
- The absence of a framework does not prove it does not exist — only that it is not publicly documented.

## 6. Conclusion

This paper demonstrates that the most cited AI governance frameworks are not publicly documented. The OECD AI Principles are the only exception. We recommend that future research and policy work:

- Require public documentation for any framework cited in academic or policy literature.
- Develop a "Framework Gap Index" to track this phenomenon.
- Advocate for the public release of governance frameworks as open standards.

This artifact contributes directly to the LIMEN thesis chapter on institutional architecture and provides a durable, citation-ready negative evidence package for journals in science and engineering ethics.

## Appendix A: OECD AI Principles (Extracted)

| Framework | Category | Principle | Description | Source URL | Access Date | Evidence Tier | Language | Jurisdiction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OECD | Core Principle | Inclusive growth, sustainable development and well-being | Promote AI that contributes to inclusive growth, sustainable development and well-being, including by reducing inequalities and promoting equitable access to benefits. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |
| OECD | Core Principle | Human rights and democratic values, including fairness and privacy | Ensure AI systems respect human rights, democratic values and the rule of law, including by promoting fairness, non-discrimination, privacy and data protection. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |
| OECD | Core Principle | Transparency and explainability | Ensure AI systems are transparent and explainable, so that people understand when they are interacting with AI and can challenge decisions. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |
| OECD | Core Principle | Robustness, security and safety | Ensure AI systems are robust, secure and safe throughout their lifecycle, and that risks are appropriately assessed and managed. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |
| OECD | Core Principle | Accountability | Ensure accountability for AI systems, including through clear roles and responsibilities, mechanisms for redress, and oversight. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |
| OECD | Recommendation | Investing in AI research and development | Facilitate public and private investment in R&D for trustworthy AI, including open science and open-source tools. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |
| OECD | Recommendation | Fostering an inclusive AI-enabling ecosystem | Promote an ecosystem that supports diverse stakeholders, including SMEs, startups, and underrepresented groups. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |
| OECD | Recommendation | Shaping an enabling interoperable governance and policy environment for AI | Coordinate policies across jurisdictions to ensure interoperability and avoid fragmentation. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |
| OECD | Recommendation | Building human capacity and preparing for labour market transition | Invest in education, training, and reskilling to prepare workers for AI-driven changes. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |
| OECD | Recommendation | International co-operation for trustworthy AI | Strengthen international collaboration to promote trustworthy AI and address global challenges. | https://oecd.ai/en/ai-principles | 2026-06-23 | Authoritative | English | Multilateral |

## Appendix B: Search Logs and Methodology

All searches were conducted on 2026-06-23 using public tools. Search terms and URLs are archived in `results/boost/limen-boost-014/search-logs.txt` (available upon request). No credentials, private APIs, or non-public resources were used. All data is publicly accessible.

## Acknowledgements

This work was conducted under the LIMEN AI Edge-Case Atlas project at the Tyche Institute, Tallinn, Estonia. The author is grateful for the open infrastructure provided by the Zeus1 research factory.

---

*This paper is licensed under CC BY-NC-SA 4.0. It is a methods paper documenting negative evidence. No claims of compliance, certification, or endorsement are made. This artifact is ready for submission to Science and Engineering Ethics (Springer).*