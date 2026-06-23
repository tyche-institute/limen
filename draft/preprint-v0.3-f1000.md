# LIMEN: a reviewer-safe public-source observatory for AI edge cases under source, language, and governance uncertainty

**Anton Sokolov** · Tyche Institute, Tallinn, Estonia · ORCID 0000-0003-2452-7096

*Method Article — prepared for F1000Research. v0.4.2.*
Live observatory: https://limen.eatf.eu · public case atlas: https://obscure-ai.eatf.eu

---

## Abstract

Catalogues of "AI failures" are easy to assemble and hard to trust. Existing incident lists tend to merge a regulator's final order, a charging-stage allegation, a documented software vulnerability and a viral news anecdote into one undifferentiated count — and then invite readers to treat that count as prevalence. This article describes LIMEN, a public-source observatory whose contribution is not the size of its corpus but an *evidence architecture*: a reproducible method for cataloguing AI edge cases that keeps source authority, evidence maturity, duplicate control, legal uncertainty and language coverage explicit, and that bounds every count by what the underlying record can support. The method has five steps — gather, adversarially verify, tier, bound, link — and one governing rule: never report a single fused corpus total, only separate denominator classes each carrying its own claim ceiling. We document the data model, the refute-by-default verification protocol, the tiering criteria, and the per-case claim-ceiling and caveat schema, and we demonstrate the method on a reviewed core of 250 evidence-grade AI edge cases (157 regulator/court records, 82 contested/interim matters, 11 security disclosures) drawn from 34 jurisdictions, plus a separately-marked layer of 46 media-documented incidents that is excluded from the evidence-grade denominator. Technical validation reports the results of an adversarial per-item verification pass (no fabricated cases found among the legal/regulatory batches; tier and fact corrections applied; two entries removed) and the source-link coverage of the released dataset. The reviewed core is presented not as a complete or representative map of AI harm but as a worked demonstration that an edge-case atlas can scale across jurisdictions and themes while remaining reviewer-safe. We make no claim of corpus completeness, incident prevalence, representativeness, legal violation by inference, or a single fused total.

**Keywords:** AI incidents, AI harms, AI edge cases, evidence tiering, AI governance, AI accountability, regulatory enforcement, observatory, claim ceilings, provenance, reproducibility.

## 1. Introduction

Public interest in where artificial intelligence goes wrong has produced a growing number of incident lists and "AI harm" trackers. They are valuable, but they share a structural weakness: the act of putting heterogeneous events in one table quietly equalises them. A binding regulator decision sits in the same column as an unproven complaint; a confirmed software vulnerability sits beside a media anecdote; a single jurisdiction's enforcement action sits beside a global news story. Readers — and especially downstream researchers and journalists — then reach for the row count as if it measured something: how common a harm is, how complete the catalogue is, how one country compares to another. None of those inferences is supported by the way such tables are built.

Our premise is that the honest contribution of an edge-case observatory is not the size of its corpus but the discipline of its evidence handling. Concretely, an edge-case atlas should make four things visible at all times:

1. **Source authority** — what kind of body produced the record (a court, a regulator, a prosecutor at charging stage, a security coordinator, a news outlet), because that determines what the record can prove.
2. **Evidence maturity** — whether a matter is final, interim, contested or merely alleged.
3. **Duplicate and denominator control** — which counts are distinct, which are views of the same event, and which "totals" are actually view-specific rather than a single corpus total.
4. **Coverage limits** — where language, jurisdiction or access barriers mean absence of evidence is not evidence of absence.

This article contributes (i) a reproducible method — an *evidence architecture* — that operationalises these four requirements; (ii) a per-case data model and a four-class denominator scheme that are never summed across the evidence-grade boundary; (iii) an adversarial, refute-by-default verification protocol; and (iv) a worked demonstration on a recently-expanded reviewed core, together with its technical validation and an openly available dataset. The method, not the corpus size, is the result.

## 2. Background and related work

Several public efforts already catalogue AI incidents, harms and controversies, and they have established that such cataloguing is valuable and feasible. The AI Incident Database (AIID), maintained by the Responsible AI Collaborative, is the most prominent: an open, indexed record that collates media reports into deduplicated "incidents" of real-world AI harm [1]. The OECD AI Incidents and Hazards Monitor (AIM) tracks incidents and hazards in near-real time from reputable news to build an evidence base for policy [2]. The AIAAIC Repository documents incidents and broader controversies, from misleading marketing to labour and environmental impacts [3]. The AI Vulnerability Database (AVID) catalogues failure modes of general-purpose and agentic AI, separating an evidenced "report" from an abstracted "vulnerability" [4]. Complementing these incident registers, the MIT AI Risk Repository consolidates 777 risks from 43 frameworks into a taxonomy of *risks* rather than realized events [5], and the Database of AI Litigation tracks AI-related court cases [6]. This activity is itself a response to a governance environment — the EU AI Act [7] and the NIST AI Risk Management Framework [8] — in which the ability to point to *what actually went wrong, and how strongly it is evidenced*, is increasingly consequential.

These efforts share a reporting convention from which LIMEN departs. With few exceptions they are organised as one-row-per-entry catalogues whose entries are counted together, and — by their own published methodologies — they do not assign a per-record *evidence tier* or keep *denominator classes* separate: the OECD monitor states that it does not independently verify the third-party information it aggregates [2], and AIID's own related-work survey of peer trackers describes none that attach source-grade, confidence or base-rate metadata to entries [1]. AVID's report-versus-vulnerability split is the closest structural analogue, but it is security-framed rather than a graded evidence schema for heterogeneous public records [4]. The consequence is a recognised limitation of the field: media-sourced incident counts grow with reporting attention and over-represent acute, Anglophone and dramatic harms, so a row count conflates observation propensity with underlying rate. The broader programme of supporting *verifiable claims* about AI [9] points in the same direction — toward evidence a third party can check — but has not been applied to the construction of incident catalogues.

LIMEN's contribution is to make that missing layer systematic and reviewer-facing: a per-record evidence tier, four denominator classes that are never summed across the evidence-grade boundary, and a claim ceiling attached to every case stating what it can and cannot be used to claim. This evidence-architecture framing also draws on broader documentation, auditing, risk-taxonomy and governance literatures: foundation-model risk analyses [15,16], language-model risk taxonomies [17], dataset and model documentation standards [18,19], end-to-end algorithmic-auditing proposals [20], cross-jurisdictional AI ethics syntheses [21,22], provenance critiques [23], AI-governance work [24], evidence about non-Western fairness contexts [25], and recent calls to standardise AI incident reporting [26]. These literatures support the methodological point without converting LIMEN's counts into prevalence, legal, compliance or safety claims.

## 3. Methods

LIMEN's pipeline is deliberately conservative. Each candidate edge case passes through five steps — gather, adversarially verify, tier, bound, link — under one governing rule described first.

### 3.1 Design principle: separate denominator classes

The core design choice is that the observatory never reports one corpus total. It reports separate denominator classes, each with its own meaning and its own ceiling. The reviewed core uses four (Table 1).

The media class is reported but **excluded from the evidence-grade denominator**. It exists because some of the most instructive AI failures — a chatbot taught to be offensive within a day [10], an experimental recruiting tool that downgraded résumés mentioning women [11], a home-valuation/iBuying model whose collapse cost a company hundreds of millions [12] — never produced a legal record, yet are real, well-documented and important to a general audience. Including them while fencing them off from the evidence-grade count is itself a demonstration of the architecture: the catalogue can serve the public without letting media anecdote inflate its evidentiary claims.

### 3.2 Data model

Each case is a record with a stable identifier and the following reader-facing fields: a short **title** and **summary**; the **authority/body** of record and a human-readable **record anchor** (the dated instrument — decision, docket, complaint, advisory — or, where a direct link is unavailable, the authority, date and instrument needed to retrieve it); **jurisdiction** and **country**; **year**; the **evidence class** and its tier; one or more **themes**; the **AI system or system type** involved; a **CVE** identifier for security disclosures; a **source** link to the primary record; and a **claim-ceiling caveat** stating, in plain language, what the record does *not* prove. The released dataset serialises these fields as JSON (one object per case) and as per-batch tab-separated tables.

### 3.3 Gather

Candidates are drawn from primary public surfaces — regulator decisions and press releases, court dockets and rulings, prosecutor announcements, securities-enforcement filings, data-protection authority decisions, and security advisories and CVE records — and, separately and explicitly labelled, from reputable journalism for incidents that never reached a legal forum. Discovery is multi-channel (by authority, by theme, by system, and across languages) precisely because no single channel surfaces everything; the unevenness of discovery is treated as a limitation to report, not a coverage claim to make.

### 3.4 Adversarial verification (refute by default)

Each candidate is checked against its primary source by an independent, skeptical pass instructed to *refute by default*: to drop a case it cannot confirm exists, and to demote a case whose framing overstates the record. Concrete demotion triggers include a settlement described as a finding; an investigation described as a penalty; a charging-stage matter described as a verdict; a wrong date, amount or party; and an appeal or reversal omitted. The pass operates on the record, not on the plausibility of the story: a striking but unconfirmable incident is dropped, while a mundane but documented one is kept. Results of this pass are reported in Section 5.

### 3.5 Tiering

Each surviving case is assigned to exactly one evidence class (Table 1) rather than to one flat list. The assignment rule is conservative and posture-aware: a matter is placed in **Regulator / court record** only when a named body has issued a dated decision, ruling, settlement or official report; in **Contested / interim** when the matter has demonstrably reached a dated stage (opened, charged, filed, under appeal) but has no final finding; and in **Security disclosure (CVE)** when a vulnerability in a named AI/agent system is anchored to a public CVE. Anything resting only on reporting is placed in the **media** class and excluded from the evidence-grade denominator. When a case could be read up a tier, it is placed in the lower one.

### 3.6 Bounding: claim ceilings and caveats

Each case carries a *claim ceiling* — the strongest statement the record actually supports — and an explicit *caveat* naming what is not proven (appeal status, charging-stage posture, settlement-without-admission, recency risk). The caveat is a first-class field, not an afterthought: it travels with the case into every view, including the public interface, so a reader is never shown a claim without simultaneously being shown its boundary.

### 3.7 Linking and source locators

Every case is bound to its primary record. In the released reviewed core, the large majority of cases carry a direct hyperlink to the primary source — 233 of 250 evidence-grade cases (93.2%), including all 11 security disclosures and all 46 media incidents. The remaining 17 cases carry the issuing authority name and case title, sufficient to retrieve the source from the issuing body's register, rather than a clickable link; these are predominantly regulator/court records whose authoritative documents are not served at a stable public URL. Source-link coverage is reported as a dataset property (Section 5), not assumed.

### 3.8 Duplicate and denominator discipline

Distinct records, merged records and subtype overlays are kept separate, so that a single event reported by several bodies is not counted several times and a denser cross-reference graph is never read as recurrence. No count in the work is produced by adding numbers across classes; "totals" within the article are always view-specific and labelled as such.

### 3.9 The observatory panels

Around the case core, the observatory maintains a set of analytic panels that apply the same discipline to the wider public-evidence problem. Each panel is denominator-bound and travels with its own claim ceiling; none is interchangeable with another.

- **Source-family map** — which families of public source are currently usable, which remain thin, and the exact blocker preventing stronger use; an observability-boundary surface, not a completeness claim.
- **Taxonomy support heatmap** — category support over a duplicate-governed denominator, with authority-backed, candidate-only and zero-seed categories kept visibly distinct; zero-seed categories are a humility channel, not empty cells awaiting a number.
- **Legal-uncertainty matrix** — per category, how far public evidence can and cannot be pushed toward legal conclusions.
- **Duplicate-control graph** — join-safety and subtype-overlay infrastructure; explicitly not recurrence evidence.
- **Publication-safe evidence funnel** — the collapse from discovered records to publication-safe lineages, used to discuss evidence maturity, not to count incidents.
- **Authority-balance and authority-geography panels** — the composition and geographic concentration of the strongest-anchored records, presented limitations-forward rather than as a cross-country comparison.
- **Multilingual visibility map** — where non-English discovery surfaces local cases that English-centric feeds miss, with translation-review caution on every row.
- **Security panel** — the agentic-security evidence split into core, appendix-supporting and explicit-gap states.

These panels, the reviewed case core, and the wider candidate funnel from which the core is drawn (a larger pool of unverified leads that are explicitly *not* counted as cases) are maintained as a live observatory at https://limen.eatf.eu. The public case atlas at https://obscure-ai.eatf.eu is its reader-facing companion: the same reviewed cases, plus the separately-marked media layer, presented for a general audience.

## 4. Operation and use cases

The reviewed core currently holds **296** catalogued cases. Of these, **250 are evidence-grade**, distributed across the three evidence-grade classes and kept separate rather than summed (Table 1). A further **46** cases are media-documented incidents, reported but excluded from the evidence-grade denominator.

Table 1. Reviewed-core denominator classes — definition, counts, jurisdiction reach, share of the evidence-grade total, and what each class supports and does not support. The classes are reported separately and never summed across the evidence-grade boundary; the media class is shown for completeness but excluded from the evidence-grade denominator.

| Class | What it is | Cases | Jur. | Share | Supports | Does *not* support |
|---|---|--:|--:|--|---|---|
| **Regulator / court record** | A named regulator decision, court ruling, settlement or official report with a date | 157 | 27 | 63% | The existence of a dated public action | Incident truth beyond the record; prevalence; typicality |
| **Contested / interim** | A matter opened, charged, filed or under appeal at a dated stage | 82 | 17 | 33% | That the matter reached that stage | Any finding of liability or guilt; the final outcome |
| **Security disclosure (CVE)** | A documented vulnerability in a named AI/agent system, anchored to a CVE | 11 | 1 | 4% | That the vulnerability was disclosed | Exploitation in the wild; real-world harm; prevalence |
| **Notable incident (media)** | A widely-reported incident documented by reputable outlets | 46 | 7 | *excl.* | That a widely-reported event occurred | Any regulator/court finding; legal conclusion; evidence-grade status |

*Caption rule: Figure 2, Figure 5, and Figure 7 carry three different denominators (39/29 taxonomy core, 21 publication-safe lineages, and 4 threshold rows respectively) that are not interchangeable and must not be summed. None of these denominators supports incident prevalence, corpus completeness, legal violation, compliance, certification, safety, or truth claims.*


Coverage spans **34 jurisdictions** (including national, supranational, and global codings), with a further set of evidence-grade cases coded as global (the security disclosures) or cross-jurisdictional (multinational scholarly-publishing retractions) rather than tied to one country. Evidence-grade cases concentrate in **2016–2026**, the modern era of AI-specific enforcement; the media layer reaches back to **2010** to give historical context. The cases span thirteen themes — legal and procedural contamination, surveillance and biometrics, deepfakes and synthetic media, AI-washing and false capability claims, agentic and control failures, public-sector algorithmic decisions, hiring and education, data-protection enforcement, rights and ethics, finance and insurance, security and agentic vulnerabilities, chatbot safety and harm, and institutional absurdity.

**Figure 1** presents the reviewed core as a theme-by-tier composition in which the evidence classes are drawn as separate segments, never as a single bar. The figure is therefore not a ranking of how common each harm is; it is a visibility surface showing how differently the *evidence* is distributed across themes. Security vulnerabilities are entirely CVE-anchored; surveillance and deepfake themes carry a substantial contested/interim share (reflecting charging-stage prosecutions and matters under appeal); legal-and-procedural and data-protection themes are dominated by final regulator/court records.

![Reviewed core by theme and evidence tier. Each theme's bar is composed of separate evidence-class segments (regulator/court, contested/interim, CVE, media); the segments are never summed into a single magnitude. The chart shows how the *evidence* is distributed across themes, not how common any harm is.](/srv/tyche/projects/limen-ai-edge-case-atlas/results/dashboard-paper/figure-reviewed-core-tier-by-theme.png){ width=95% }

**Figure 2** presents the taxonomy support heatmap under the live 39 governed record references collapsed into 29 unique lineages (with a 44/34 extended sidecar explicitly labeled). Categories are shown with authority-backed, candidate-only, and zero-seed states kept visibly distinct; zero-seed categories are a humility channel, not empty cells awaiting a number. The figure does not rank categories by prevalence; it shows how the *evidence* is distributed across the taxonomy.

**Figure 3** presents the legal-uncertainty matrix as a claim-ceiling surface. Each category is shown with the strongest legal or regulatory statement the current evidence can support, and with explicit language about what cannot be concluded. The matrix is a routing device for manuscript prose, not a legal finding.

**Figure 4** presents the duplicate-control graph with 27 duplicate-review edges. The graph is join-safety and subtype-overlay infrastructure — it ensures that a single event reported by several bodies is not counted several times. It is explicitly not recurrence evidence.

**Figure 5** presents the publication-safe evidence-tier funnel showing the collapse from discovered records to 21 publication-safe lineages. The funnel is used to discuss evidence maturity and publication ceilings, not to count incidents.

**Figure 6** presents the jurisdiction and language visibility map across 12 non-English leads with six-of-six translation-review-required metadata visible. The map is an uneven-observability surface showing where non-English discovery surfaces local cases that English-centric feeds miss. It is not a country comparison or readiness ranking.

**Figure 7** presents the security and agentic threshold ladder as a bounded 4-row companion panel. It shows which security rows sit in core results, which belong in appendix-supporting use, and where the explicit gap for peer-reviewed security case support remains. It is not part of the main Route A denominator and does not support security prevalence claims.

**Figure 8** presents the attestation trust-surface readiness companion showing local-bundle provenance ceilings across the seven lifecycle actions. Route C currently shows local-bundle provenance only; no detached signature, transparency-log inclusion, or Verifiable Credential is present. The figure is a methods companion, not a trust-assurance claim.

**Table 2** accompanies Figure 2 as the taxonomy data companion, listing each category with its governed-record count, unique-lineage count, seeded or overlay status, and the exact claim ceiling attached to it. Under the live 39/29 denominator, the 15 primary taxonomy categories distribute as follows (sample reference counts per category; multi-label assignment means category sums exceed the 39 unique governed-record-ref total): `security_risk` (9 refs), `agentic_control_failure` (9), `public_sector_misuse_or_gap` (7), `unlawful_or_allegedly_unlawful_use` (5), `normative_or_moral_outlier` (5), `education_workplace_or_hr` (4), `ai_washing_or_false_ai_claim` (4), `surveillance_biometrics_or_policing` (3), `institutional_absurdity` (3), `deepfake_or_synthetic_identity` (3), `legal_procedural_contamination` (2), `finance_insurance_or_market` (2), and three zero-seed guardrail rows (`health_medical_or_mental_health`, `research_integrity`, `residual_unclassified`). The full taxonomy × evidence-tier cross-tabulation, extended sidecar counts, overlay-ready annotations, and zero-seed/fragility flags are provided in Supplementary Table S1 and the reproducibility package.


**Use cases.** For a journalist, each case provides a named authority, a date and either a link or a record locator, so a story can cite the instrument rather than the rumour, and filters by jurisdiction or theme surface local angles. For a researcher, the dataset is a structured, evidence-tiered starting point whose proof ceilings are explicit, so that a citation can be matched to the strength of the underlying record rather than to a headline. For a governance audience, the panels make the *limits* of public evidence legible — which is often the operative question. In all three uses, the same discipline holds: the reader can always see what a case proves, what it does not, and where to check.

The reviewed core grew by more than an order of magnitude over a single assembly cycle, from a small curated seed to 250 evidence-grade cases, **without** relaxing any ceiling. Growth added breadth (more jurisdictions, more themes, more recent enforcement) but did not convert any class into a prevalence estimate, a completeness claim, or a fused denominator.

## 5. Technical validation

**Adversarial per-item pass.** Every evidence-grade case and the media layer were subjected to the refute-by-default pass of Section 3.4. Across the verified legal/regulatory batches the pass found no fabricated cases. It removed entries that did not survive scrutiny — for example, an item recorded as a national police enforcement action that, on checking, was a research-and-development project, and an incident that could not be independently confirmed — and it corrected tier and fact errors throughout (for instance, demoting charging-stage matters that had been framed as findings, and correcting dates and amounts). Two entries were removed in the final sweep.

**Count discipline.** The class counts reported here (157 / 82 / 11 evidence-grade; 46 media; 296 total) were recomputed directly from the released dataset and reconciled against the per-class evidence panel; the theme totals sum to 296 across thirteen themes, and the per-class jurisdiction reach (27 / 17 / 1 / 7) and the 34-jurisdiction union were recomputed rather than asserted. An earlier draft's "36 jurisdictions" did not survive this recomputation and was corrected to 34.

**Source-link coverage.** Of the 250 evidence-grade cases, 233 (93.2%) carry a direct link to the primary source and the remaining 17 carry the issuing authority and case title (Section 3.7); all 11 CVE cases and all 46 media cases carry a direct link. Source-link coverage is therefore a measured property of the release, not an assumption.

**Reproducibility.** The figure and the per-class evidence panel and tier-by-theme matrix that underlie the counts are regenerated from the dataset by a build pipeline, so the published numbers, the figure and the dataset cannot silently diverge.

**Supplementary information.** The submission is accompanied by 15 supplementary tables, one supplementary figure, and one supplementary note. Supplementary Table S1 presents the reviewed-core 248-case demonstration as a 4-panel jurisdiction × tier breakdown (now superseded by the 250-case S15 panel as the current denominator source of truth). Supplementary Table S2 defines the Route B threshold contract for the security panel. Supplementary Table S3 presents the threshold-change matrix for row-level upgrade conditions. Supplementary Table S4 presents the provenance-confusion publication-cell geometry. Supplementary Table S5 presents the security claim-ceiling panel. Supplementary Tables S6, S7, S8, and S9 present the publication-cell matrix, trust-boundary breadth, supply-chain frontier, and peer-review frontier for the security panel. Supplementary Table S10 presents the procedural-contamination source-depth panel. Supplementary Table S11 presents the research-integrity hostile-reviewer panel. Supplementary Table S12 presents the procedural-contamination manuscript-routing sidecar. Supplementary Tables S13 and S14 present the public-sector institutional-asymmetry matrix and traceability ladder. Supplementary Table S15 presents the current jurisdiction × tier breakdown (250 evidence-grade cases, 34 jurisdictions) as the live denominator source of truth. Supplementary Figure S1 is a frozen tier-by-theme snapshot. Supplementary Note 1 documents the caption-control register and figure-route registry.


## 6. Limitations

The observatory's limitations are not incidental; they are the boundary that makes the rest defensible.

- **Not complete or representative.** The reviewed core is a catalogue of locatable, source-anchored cases, not a sample of all AI harm. Selection follows evidence availability, which is itself uneven by language, jurisdiction and sector.
- **No prevalence or trend.** No count estimates how often a harm occurs; the year distribution reflects enforcement and reporting activity, not an underlying rate.
- **No legality by inference.** Contested and charging-stage matters are not findings of liability; security disclosures are not evidence of exploitation; media incidents are not legal conclusions.
- **No fused denominator.** Counts across classes and panels are deliberately not added together.
- **Recency risk.** The most recent (2025–2026) and media-tier items carry higher uncertainty; each is bound to its source for direct checking.
- **Aggregate geography and recurrence are deferred** until normalised cross-case identifiers exist; the current panels support visibility, not comparison.

## 7. Conclusions

The observatory's claim is modest and, we argue, more useful for being modest: a reviewer-safe, evidence-tiered, source-linked catalogue of AI edge cases whose denominator classes stay separate and whose claims stay bounded. The reviewed core of 250 evidence-grade cases demonstrates that such an atlas can scale across jurisdictions and themes while holding its proof ceilings, and a public companion shows the same discipline surviving in front of a general audience. What the method offers is not the biggest list of AI failures, but a defensible architecture for cataloguing them — one in which a reader can always see what each case proves, what it does not, and where to check.

## Data availability

A citable, archived snapshot of the underlying dataset is deposited at Zenodo (DOI: 10.5281/zenodo.20701594, CC-BY-4.0). It contains the catalogue (`cases.json`, 296 cases), a field dictionary and reading guidance (`README.md`), the per-class evidence panel and the theme-by-tier matrix, and Figure 1. The same dataset is openly browsable, with per-case tier, claim ceiling, caveat and source, at https://obscure-ai.eatf.eu (JSON at https://obscure-ai.eatf.eu/data/cases.json), and the live observatory — reviewed core, candidate funnel and analytic panels — is at https://limen.eatf.eu. A versioned snapshot of this manuscript is archived at Zenodo (DOI: 10.5281/zenodo.20700813).

## Software availability

The catalogue is data, not a software product; the figure, evidence panel and tier-by-theme matrix are regenerated from the dataset by build scripts available from the author on request, and the regenerated figure and tables are included in the dataset deposit (DOI: 10.5281/zenodo.20701594).

## Author contributions

Anton Sokolov: conceptualisation, methodology, data curation, validation, software, writing — original draft and revision.

## Competing interests

No competing interests are declared.

## Grant information

The author declares that no grants were involved in supporting this work.

## Acknowledgements

The author thanks the maintainers of the public registers, dockets, advisories and CVE records on which a source-anchored catalogue of this kind depends.

## References

1. McGregor S. Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database. *Proceedings of the AAAI Conference on Artificial Intelligence*. 2021; **35**(17): 15458–15463. https://doi.org/10.1609/aaai.v35i17.17817

2. OECD. AI Incidents and Hazards Monitor (AIM). OECD.AI Policy Observatory. https://oecd.ai/en/incidents (methodology: https://oecd.ai/en/incidents-methodology; accessed 15 June 2026).

3. AIAAIC. AI, Algorithmic, and Automation Incidents and Controversies Repository. https://www.aiaaic.org/ (accessed 15 June 2026).

4. AI Risk and Vulnerability Alliance. AI Vulnerability Database (AVID). https://avidml.org/ (accessed 15 June 2026).

5. Slattery P, Saeri AK, Grundy EAC, et al. The AI Risk Repository: A Comprehensive Meta-Review, Database, and Taxonomy of Risks from Artificial Intelligence. *arXiv*. 2024; arXiv:2408.12622. https://doi.org/10.48550/arXiv.2408.12622

6. Brauneis R. Database of AI Litigation (DAIL). Ethical Tech Initiative, George Washington University Law School. https://blogs.gwu.edu/law-eti/ai-litigation-database/ (accessed 15 June 2026).

7. Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). *Official Journal of the European Union*. OJ L, 2024/1689, 12.7.2024. http://data.europa.eu/eli/reg/2024/1689/oj

8. National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. U.S. Department of Commerce; 2023. https://doi.org/10.6028/NIST.AI.100-1

9. Brundage M, Avin S, Wang J, et al. Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims. *arXiv*. 2020; arXiv:2004.07213. https://doi.org/10.48550/arXiv.2004.07213

10. Schwartz O. In 2016, Microsoft's Racist Chatbot Revealed the Dangers of Online Conversation. *IEEE Spectrum*. 2019. https://spectrum.ieee.org/in-2016-microsofts-racist-chatbot-revealed-the-dangers-of-online-conversation

11. Dastin J. Amazon scraps secret AI recruiting tool that showed bias against women. *Reuters*. 10 October 2018.

12. Zillow Group, Inc. Zillow Group Reports Third-Quarter 2021 Financial Results & Shares Plan to Wind Down Zillow Offers Operations [press release / Form 8-K]. U.S. Securities and Exchange Commission; 2 November 2021. https://www.sec.gov/Archives/edgar/data/0001617640/000161764021000085/q32021991.htm

13. MITRE. ATLAS — Adversarial Threat Landscape for AI Systems. https://atlas.mitre.org (accessed 15 June 2026).

14. C2PA. Content Provenance and Authenticity: Technical Specification v2.0. Coalition for Content Provenance and Authenticity; 2024. https://c2pa.org (accessed 15 June 2026).

15. OWASP. OWASP Top 10 for Large Language Model Applications. Open Worldwide Application Security Project; 2023. https://owasp.org/www-project-top-10-for-large-language-model-applications/

16. Bommasani R, Hudson DA, Adeli E, et al. On the Opportunities and Risks of Foundation Models. *arXiv*. 2021; arXiv:2108.07258. https://doi.org/10.48550/arXiv.2108.07258

17. Weidinger L, Mellor J, Rauh M, et al. Taxonomy of Risks Posed by Language Models. *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency*. 2022: 214–229. https://doi.org/10.1145/3531146.3533088

18. Gebru T, Morgenstern J, Vecchione B, et al. Datasheets for Datasets. *Communications of the ACM*. 2021; 64(12): 86–92. https://doi.org/10.1145/3458723

19. Mitchell M, Wu S, Zaldivar A, et al. Model Cards for Model Reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency*. 2019: 220–229. https://doi.org/10.1145/3287560.3287596

20. Raji ID, Smart A, White RN, et al. Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing. *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency*. 2020: 33–44. https://doi.org/10.1145/3351095.3372873

21. Jobin A, Ienca M, Vayena E. The Global Landscape of AI Ethics Guidelines. *Nature Machine Intelligence*. 2019; 1: 389–399. https://doi.org/10.1038/s42256-019-0088-2

22. Floridi L, Cowls J. A Unified Framework of Five Principles for AI in Society. *Harvard Data Science Review*. 2019; 1(1). https://doi.org/10.1162/99608f92.8cd550d1

23. Crawford K, Dobbe R, Dryer T, et al. Excavating AI: The Politics of Images in Machine Learning Training Sets. 2019. https://excavating.ai

24. Roberts H, Cowls J, Morley J, Taddeo M, Wang V, Floridi L. The Chinese Approach to Artificial Intelligence: An Analysis of Policy, Ethics, and Regulation. *AI & Society*. 2021; 36: 59–77. https://doi.org/10.1007/s00146-020-00992-2

25. Sambasivan N, Arnesen E, Hutchinson B, Doshi T, Prabhakaran V. Re-imagining Algorithmic Fairness in India and Beyond. *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*. 2021: 315–328. https://doi.org/10.1145/3442188.3445896

26. Agarwal A, Nene MJ. Advancing Trustworthy AI for Sustainable Development: Recommendations for Standardising AI Incident Reporting. *arXiv*. 2025; arXiv:2501.14778. https://doi.org/10.48550/arXiv.2501.14778

27. European Commission. Proposal for a Regulation laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). COM(2021) 206 final. 2021. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206
