---
title: "LIMEN: A Public-Source Observatory for Artificial-Intelligence Edge Cases"
author: "LIMEN project"
date: "Preprint snapshot, June 7, 2026"
fontsize: 10pt
geometry: margin=0.72in
papersize: letter
colorlinks: true
linkcolor: black
urlcolor: blue
header-includes:
  - \usepackage{float}
  - \usepackage{booktabs}
  - \usepackage{tabularx}
  - \usepackage{array}
  - \usepackage{needspace}
  - \usepackage{graphicx}
  - \usepackage{caption}
  - \captionsetup{font=small,labelfont=bf}
  - \newcolumntype{Y}{>{\raggedright\arraybackslash}X}
  - \setlength{\parskip}{0.48em}
  - \setlength{\parindent}{0pt}
  - \setlength{\tabcolsep}{4.5pt}
  - \renewcommand{\arraystretch}{1.14}
  - \sloppy
  - \clubpenalty=10000
  - \widowpenalty=10000
  - \displaywidowpenalty=10000
  - \raggedbottom
---

\Needspace{10\baselineskip}
# 1. Introduction: The Evidence-Infrastructure Problem

LIMEN\footnote{This preprint uses the frozen June 7, 2026 snapshot. Historical local version labels remain provenance metadata; the article uses reader-facing names.} is a public-source observatory for artificial-intelligence edge cases: unusual, harmful, risky, absurd, agentic, security, procedural, institutional, synthetic-identity, artificial-intelligence-washing, and hard-to-classify uses that appear in open records. The observatory does not treat every public mention as the same kind of evidence. A regulator order, a court charging document, a vendor security advisory, a publisher retraction notice, a government project page, and a local-language news report support different sentences.

Motivation. Public records now contain a wide range of artificial-intelligence governance signals, but those signals arrive through uneven evidence channels. Some records are official and dated. Some are summary pages. Some are complaint-stage documents. Some are blocked on a host while still documented in a link audit. Some are language-dependent. Some are duplicate-adjacent but not duplicates. A research atlas that collapses these differences into a flat case list creates false confidence. LIMEN keeps the evidence channel visible.

The project has grown into a large working corpus: 57,603 recorded discovery signals, 156 public-link checks, 15 source-family rows, 15 watch categories, 13 dated public-record anchors, 7 candidate examples, 7 side or appendix anchors, and a 21-row reviewed core. The preprint does not hide that scale. It uses the scale as infrastructure. The main scientific object is the evidence system that turns a large public-source surface into auditable, bounded rows.

The security and agentic-control background draws on MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems, called ATLAS hereafter.\footnote{MITRE ATLAS public site: \url{https://atlas.mitre.org/}. MITRE ATLAS fact sheet: \url{https://atlas.mitre.org/pdf-files/MITRE_ATLAS_Fact_Sheet.pdf}.} ATLAS is useful because it treats artificial-intelligence security as a structured adversarial-threat problem: tactics, techniques, mitigations, case studies, realistic demonstrations, and red-team observations can be separated from ordinary incident narration. LIMEN uses that distinction as theory for source architecture. ATLAS supports mechanism and technique context; it does not turn a LIMEN row into a direct same-event case-study match unless that exact join is independently verified.

The core move is simple. LIMEN separates discovery, candidates, reviewed examples, side anchors, and holds. It assigns stable public identifiers. It records dates, jurisdictions, languages, source-family bins, evidence strength, confidence tags, duplicate status, public-link state, and claim limits. It treats public uncertainty as a data field.

The conclusion is operational. Future artificial-intelligence observatories should publish their source architecture, not only their examples. New rows should be valuable because they fill a geography, source-family, language, lifecycle, or category gap; resolve a duplicate ambiguity; or raise a claim limit with a stronger public record. Raw volume alone is not a research result.

\clearpage
\Needspace{10\baselineskip}
# 2. Data

\Needspace{8\baselineskip}
## World Matrix

The world matrix records where reviewed and anchor rows sit geographically and linguistically. The frozen preprint package contains English-language official records, global security records, and a smaller but important multilingual layer. Translation-dependent rows stay visible because they change how claims can be written.

\Needspace{16\baselineskip}
\begin{table}[H]
\caption{World matrix. Rows are reviewed-core or anchor rows in the frozen preprint package.}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.25\textwidth}>{\raggedright\arraybackslash}p{0.14\textwidth}>{\raggedright\arraybackslash}p{0.17\textwidth}Y@{}}
\toprule
Jurisdiction or geography & Rows & Languages & Source condition \\
\midrule
Global & 8 & English & Mainly security advisories and research records; mechanism examples rather than deployment counts. \\
United States & 8 & English & Enforcement, charging-stage, and official side-anchor material. \\
United Kingdom & 2 & English & Data-protection regulator records on biometric governance. \\
Finland & 2 & Finnish & Local-language procedural and synthetic-media leads with translation caution. \\
Slovenia & 2 & Slovenian & One official project page and one local public-sector lead. \\
Unknown or multijurisdictional & 2 & English & Publisher and research-integrity source-depth anchors. \\
Single-row jurisdictions & 4 & Italian, Lithuanian, Estonian, Danish & Italy, Lithuania, Estonia, and Denmark each add one row; three are translation-dependent. \\
\bottomrule
\end{tabularx}
\end{table}

\Needspace{8\baselineskip}
## Source Pack

The source pack groups public records by evidence channel. A row can belong to more than one bin when, for example, a public-sector register also involves a regulator or a company notice also links to a security advisory.

ATLAS sits in the source pack as a structured security comparator rather than as another case list. It supports the security and agentic-control theory of the paper, especially the difference between mechanism evidence, mitigation context, and event proof.

\Needspace{15\baselineskip}
\begin{table}[H]
\caption{Source pack. Counts and roles are separated across reviewed rows, anchors, and comparator context.}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.33\textwidth}>{\raggedright\arraybackslash}p{0.11\textwidth}Y@{}}
\toprule
Reader-facing source family & Count or role & Typical role in the paper \\
\midrule
Regulators and enforcement agencies & 11 & Official public records, orders, complaints, settlements, or decision pages. \\
Security advisories and research & 8 & Mechanism evidence for agentic and tool-boundary failures. \\
Structured security frameworks & context layer & ATLAS technique and mitigation context for adversarial artificial-intelligence security. \\
Local-language news and investigations & 5 & Candidate and limited-core material with cautious translation handling. \\
Public-sector registers and procurement & 2 & Governance visibility for public-sector artificial-intelligence use. \\
Publisher and research-integrity records & 2 & Source-depth anchors for retraction and reference-validity examples. \\
Court and tribunal records & 1 & Charging-stage legal-process material with no merits conclusion. \\
Company and platform notices & 1 & Platform-side security or product-posture evidence. \\
\bottomrule
\end{tabularx}
\end{table}

\clearpage
\Needspace{8\baselineskip}
## Four-Bin Ledger

The four-bin ledger is the paper denominator control. It keeps strong examples, limited examples, side anchors, and holds in separate lanes.

\Needspace{14\baselineskip}
\begin{table}[H]
\caption{Four-bin ledger.}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.31\textwidth}>{\raggedright\arraybackslash}p{0.10\textwidth}Y@{}}
\toprule
Bin & Rows & Use in the preprint \\
\midrule
Bounded reviewed examples & 15 & Main examples. These rows have strong enough public support for narrow factual description. \\
Limited reviewed core & 6 & Coverage and methods rows. These rows remain in the reviewed core but carry lower confidence. \\
Side anchors & 5 & Source-depth and governance supports outside the main denominator. \\
Document or chronology holds & 2 & Candidate material held until document reading or chronology review is complete. \\
\bottomrule
\end{tabularx}
\end{table}

\Needspace{8\baselineskip}
## Workflow Bands

Workflow bands describe movement through the observatory. Signals become candidates only after minimal public-source capture. Candidates become reviewed examples only after duplicate control, evidence-strength coding, confidence tagging, and a written claim limit.

\Needspace{15\baselineskip}
\begin{table}[H]
\caption{Workflow bands.}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.26\textwidth}>{\raggedright\arraybackslash}p{0.12\textwidth}Y@{}}
\toprule
Band & Count & Paper treatment \\
\midrule
Discovery signals & 57,603 & Public-source mining output; triage material only. \\
Public-link checks & 156 & Retrieval, blockage, public-link, and source-check evidence. \\
Source anchors & 13 & Dated public records usable as source supports. \\
Candidate examples & 7 & Queue material; excluded from reviewed-case claims until promoted. \\
Reviewed core & 21 & Main frozen denominator for the preprint. \\
Side anchors & 7 & Context, source-depth, and governance material outside the core. \\
\bottomrule
\end{tabularx}
\end{table}

\Needspace{8\baselineskip}
## Bridge Snapshot

The bridge snapshot shows how the dataset travels from internal work files to a reader-facing observatory. The bridge preserves uncertainty rather than smoothing it away.

\Needspace{15\baselineskip}
\begin{table}[H]
\caption{Bridge snapshot.}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.24\textwidth}>{\raggedright\arraybackslash}p{0.29\textwidth}Y@{}}
\toprule
Bridge & What it carries & Reader-facing effect \\
\midrule
Identifier bridge & Stable public identifiers with old local identifiers kept as aliases. & Reviewers can tell when two rows are the same event, related events, or only identifier collisions. \\
Source bridge & Source-family bins and public-link audit state. & A reader sees whether a row comes from an official record, advisory, register, publisher notice, or media lead. \\
Confidence bridge & High, medium, and low confidence tags. & Strong examples and limited rows are not written in the same tone. \\
Language bridge & Translation-dependent flags and language fields. & Non-English records are paraphrased conservatively and do not silently become English-source certainty. \\
Claim bridge & A written claim limit for each row. & The table says what a public record supports and stops there. \\
\bottomrule
\end{tabularx}
\end{table}

\clearpage
\Needspace{10\baselineskip}
# 3. Methods

\Needspace{8\baselineskip}
## Ten Indicators

Each row is coded through ten indicators. The indicators are deliberately practical: a dashboard builder, reviewer, or future curator can inspect them without reconstructing the entire collection history.

\Needspace{20\baselineskip}
\begin{table}[H]
\caption{Ten indicators used for row coding.}
\footnotesize
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.22\textwidth}>{\raggedright\arraybackslash}p{0.31\textwidth}Y@{}}
\toprule
Indicator & Coding question & Reader-facing output \\
\midrule
Public identifier & Which stable public row name should appear? & Non-colliding identifier and legacy alias record. \\
Date & What dated event, document, or publication is visible? & Date field, date-normalization note, or explicit gap. \\
Jurisdiction & Which jurisdiction or geography is supported? & Country, global, or multijurisdictional label. \\
Language & What language is the source record in? & Translation caution where needed. \\
Source authority & Who published the record? & Official, regulator, court, advisory, publisher, register, company, or media channel. \\
Document depth & How deep is the public record? & Order, complaint, charging document, advisory, notice, register page, summary, or article. \\
Public-link state & Is the source open, captured, blocked, or summary-only? & Link-audit note and access-limit flag. \\
Duplicate status & Is this same event, related pattern, same regulator batch, or identifier collision? & Merge, non-merge, cluster, or collision decision. \\
Confidence tag & How strong is the row for paper prose? & High, medium, or low tag. \\
Claim limit & What sentence can the source support? & Narrow statement, methods-only use, side-anchor use, or hold. \\
\bottomrule
\end{tabularx}
\end{table}

\Needspace{8\baselineskip}
## Confidence Tags

Confidence tags are not truth scores. They control how strongly the paper can write from public material.

\Needspace{12\baselineskip}
\begin{table}[H]
\caption{Confidence tags.}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.14\textwidth}>{\raggedright\arraybackslash}p{0.31\textwidth}Y@{}}
\toprule
Tag & Typical support & Allowed paper use \\
\midrule
High & Official, authoritative, or document-grade public source with stable date and row identity. & Bounded example, source-depth anchor, or governance anchor. \\
Medium & Official source present but chronology, document reading, or exact role still needs work. & Queue, side note, or held row until review closes. \\
Low & Single public source, translation dependence, or thin public proof. & Methods, coverage, and gap analysis; no strong event conclusion. \\
\bottomrule
\end{tabularx}
\end{table}

\clearpage
\Needspace{8\baselineskip}
## Source-Family Bins

Source-family bins translate the public record into a scientific coding surface. The bins prevent a local news title, a public register, and a final agency order from being treated as equal evidence.

ATLAS adds a theory-driven security bin: a structured graph can support threat-mechanism and mitigation language even when it cannot support a same-event claim for a reviewed row. This gives LIMEN a disciplined way to use security taxonomies without laundering taxonomy context into event proof.

\Needspace{15\baselineskip}
\begin{table}[H]
\caption{Source-family bins.}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.34\textwidth}Y@{}}
\toprule
Bin & Reader-facing definition \\
\midrule
Regulators and enforcement agencies & Public agencies, enforcement bodies, data-protection regulators, and official decision pages. \\
Court and tribunal records & Charging documents, pleadings, orders, judgments, or tribunal materials available in public form. \\
Security advisories and research & Vendor notices, vulnerability records, advisories, and independent public technical research. \\
Structured security frameworks & ATLAS-style adversarial-threat taxonomies, technique graphs, mitigation records, and case-study context used for mechanism support rather than direct event proof. \\
Public-sector registers and procurement & Government project pages, registers, procurement files, and public-administration disclosures. \\
Publisher and research-integrity records & Retraction notices, correction notices, publisher pages, and research-integrity records. \\
Company and platform notices & Public platform, vendor, or company statements about products, incidents, or fixes. \\
Local-language news and investigations & Journalism or local reporting used as leads or limited evidence unless stronger records exist. \\
\bottomrule
\end{tabularx}
\end{table}

\Needspace{8\baselineskip}
## Workflow Promotion Gates

Promotion gates make movement explicit. A row can become more useful when the public source improves. It can also stay in place when the record remains thin.

\Needspace{14\baselineskip}
\begin{table}[H]
\caption{Workflow promotion gates.}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.22\textwidth}>{\raggedright\arraybackslash}p{0.33\textwidth}Y@{}}
\toprule
Gate & Required check & Result \\
\midrule
Source visibility & At least one public source is recorded with a URL, document path, or access note. & Signal can become a candidate. \\
Date and jurisdiction & Date, geography, and language are preserved or explicitly marked missing. & Candidate becomes comparable. \\
Duplicate control & Same-event and identifier-collision checks are complete. & Candidate can enter a stable denominator. \\
Evidence strength & Source family, document depth, and confidence tag are coded. & Row can be placed in the four-bin ledger. \\
Claim limit & A narrow sentence is written and over-claims are excluded. & Row can be used as reviewed example, side anchor, limited row, or hold. \\
\bottomrule
\end{tabularx}
\end{table}

\clearpage
\Needspace{10\baselineskip}
# 4. Results

\Needspace{8\baselineskip}
## Evidence-Gradient

The evidence-gradient is steep. LIMEN records 57,603 discovery signals, but only 21 duplicate-controlled rows sit in the reviewed core for this preprint. Fifteen of those rows carry high-confidence bounded use. Six remain limited-core rows for methods, coverage, and gap analysis.

\Needspace{22\baselineskip}
\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{../figures/preprint-figure1-evidence-gradient.png}
\caption{Evidence-gradient. Discovery scale, public-link checking, reviewed rows, reviewed core, high-confidence examples, and limited-core rows are separate layers.}
\end{figure}

The gradient gives the corpus its shape. Discovery is large enough to sustain aggressive future collection. The reviewed core is small enough to inspect. Public-link checks and source anchors sit between them, making the transition from lead material to paper material auditable.

\clearpage
\Needspace{8\baselineskip}
## Register Scarcity

Register scarcity is visible at the category level. Security risk and agentic control failure are heavily seeded with authoritative public records. The zero-seed rows require typed interpretation rather than one flat reading: health remains a true local zero, research integrity remains zero-seed in headline counts but locally non-empty through the source-depth package, and residual remains a methods guardrail rather than an empirical absence row. Institutional absurdity is seeded by public sources but lacks authoritative support in the current snapshot.

\Needspace{24\baselineskip}
\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{../figures/preprint-figure2-register-scarcity.png}
\caption{Register scarcity. Category seeds and authoritative seeds are shown together so visible gaps remain part of the result.}
\end{figure}

This scarcity map directs collection. The next useful row is a record that changes an empty or thin category, strengthens a source family, or resolves a translation-dependent lead. A larger pile of already-covered English security examples would add less scientific value than one strong public record in a zero-seed category.

\clearpage
\Needspace{8\baselineskip}
## Lifecycle-Infrastructure Contrast

The workflow lifecycle is more complete than the public evidence for many events. LIMEN has live receipts for observation, extraction, classification, review, clustering, publication, and bounded replacement. Event records still vary by source depth, access state, language state, and duplicate state.

\Needspace{22\baselineskip}
\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{../figures/preprint-figure3-lifecycle-infrastructure-contrast.png}
\caption{Lifecycle-infrastructure contrast. Workflow audit coverage is separated from event-evidence strength.}
\end{figure}

The contrast prevents workflow maturity from becoming evidentiary overreach. A row can be carefully observed, extracted, classified, reviewed, clustered, and published while still relying on a summary-only page or a translation-dependent article. The workflow record improves auditability. It does not upgrade the source.

\clearpage
\Needspace{8\baselineskip}
## Comparator Cohort

The comparator cohort spans structured vulnerability records, ATLAS, incident monitors, risk vocabularies, enforcement records, and public registers. These systems play different roles. Some provide machine-readable identifiers. ATLAS provides an adversarial-technique and mitigation graph. Some provide public incident pages. Some provide concept vocabularies. Some provide official documents. LIMEN uses them as comparison surfaces, not as interchangeable truth sources.\footnote{MITRE describes ATLAS as a living knowledge base of adversary tactics and techniques grounded in real-world attack observations and realistic demonstrations from artificial-intelligence red teams and security groups. See MITRE news release, November 6, 2023: \url{https://www.mitre.org/news-insights/news-release/mitre-and-microsoft-collaborate-address-generative-ai-security-risks}.}

\Needspace{22\baselineskip}
\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{../figures/preprint-figure4-comparator-cohort.png}
\caption{Comparator cohort. Source-family counts and external comparison roles are shown in one view.}
\end{figure}

The cohort anchors the article in a broader research ecology. LIMEN is strongest where it records what public evidence can support across unlike systems. A vulnerability record can help with a security mechanism. ATLAS can support technique context and threat-model background. A risk vocabulary can help with category alignment. An enforcement record can support a bounded official-description sentence. These roles should remain distinct.

\clearpage
\Needspace{8\baselineskip}
## Workflow Bands

Workflow bands keep the monster corpus usable. Discovery signals, candidate examples, reviewed rows, high-confidence examples, limited rows, side anchors, and holds are not one list with different labels. They are operational lanes.

\Needspace{22\baselineskip}
\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{../figures/preprint-figure5-workflow-bands.png}
\caption{Workflow bands. Rows pass through source visibility, date and jurisdiction preservation, duplicate control, evidence-strength coding, and claim-limit writing before promotion.}
\end{figure}

The bands support fast collection without contaminating the paper denominator. New leads can keep arriving. The reviewed core does not move until a row passes the gates. Side anchors can enrich source-depth analysis without inflating the reviewed-case count. Holds remain visible rather than quietly disappearing.

\clearpage
\Needspace{8\baselineskip}
## Bridge Stress-Test

The bridge stress-test records the conditions most likely to break a publishable observatory: translation caution, low-confidence rows, access limits, anchor-export gaps, document holds, and identifier collisions. In the frozen package, seven rows require translation caution, six carry low confidence, four record access limits, nine need anchor-export synchronization, two remain on hold, and nine identifier-collision edges are already documented.

\Needspace{22\baselineskip}
\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{../figures/preprint-figure6-bridge-stress-test.png}
\caption{Bridge stress-test. The observatory exposes evidence constraints that would otherwise be hidden in prose or lost in appendices.}
\end{figure}

The stress-test turns review objections into work items. Synchronize the nine anchor-export gaps. Read the two held United States Federal Trade Commission rows before using them as examples. Preserve translation caution on the seven language-dependent rows. Keep the six low-confidence rows out of strong examples until stronger public records are added. Retain file-qualified aliases wherever older local identifiers collide.

Full-scale operation now follows six rules:

1. Keep the reviewed core stable for this paper while the discovery layer continues to grow.
2. Triage the 57,603 recorded discovery signals by source family, language, jurisdiction, and category gap.
3. Promote only rows that improve public evidence quality or coverage balance.
4. Refresh the public dashboard with separate layers for reviewed cases, side anchors, candidate leads, public-link checks, and discovery signals.
5. Complete an independent second-coder pass on evidence strength, source family, category, and claim scope.
6. Archive the paper package so the manuscript, figures, source tables, and dashboard exports can be inspected together.
