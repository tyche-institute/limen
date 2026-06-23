# LIMEN: A Public-Source Observatory for AI Edge Cases under Source, Language, and Governance Uncertainty

**Authors:** Anton Sokolov (Tyche Institute)

**Preprint version:** v0.6 | **Date:** 2026-06-19

**Keywords:** AI edge cases, evidence architecture, denominator discipline, source-family governance, duplicate governance, legal uncertainty, multilingual visibility, security crosswalk, provenance limits, observatory methods

---

## Abstract

Public-source research on AI edge cases typically reports aggregate counts
without exposing denominator classes, duplicate governance, source-authority
heterogeneity, or legal-interpretation boundaries. LIMEN addresses this gap
by treating evidence architecture as its primary contribution. The observatory
separates discovered records from duplicate-governed records, authoritative
rows from summary-grade rows, and publication-safe lineages from queue-only
leads. The current package supports 15 taxonomy categories under a core
denominator of 39 governed record references collapsed into 29 unique
lineages, a publication-safe funnel of 21 lineages, a 15-row source-family
saturation map, a 27-edge duplicate-review graph, a 12-row jurisdiction and
language surface, and a reviewed-core demonstration of 250 cases across
34 jurisdictions. LIMEN does not claim completeness, prevalence, or legal
violation. Its contribution is that public evidence, routed through explicit
denominator discipline and source-family governance, can support bounded
accountability arguments reusable across venues and companion observatories.

---

## 1. Introduction

Public-source research on AI edge cases — misuse incidents, security
vulnerabilities, normative anomalies, institutional absurdities, and agentic
failures — faces a recurring methodological problem. Existing corpora and
incident databases typically report aggregate counts without making their
denominator classes, duplicate governance, source-authority heterogeneity,
translation ceilings, and legal-interpretation boundaries visible to a
reviewer. A reader who encounters a headline number cannot easily determine
whether two rows describe the same event, whether a category label rests on
one mediated news article or on a regulator's order text, or whether a
multilingual lead has been verified by a human translator. These hidden
infrastructure choices produce denominator drift: the same corpus can yield
different "totals" depending on whether one counts discovered records,
duplicate-governed lineages, publication-safe lineages, or authority-anchored
rows.

LIMEN (the AI Edge-Case Atlas observatory) addresses this problem by
treating evidence architecture as the primary contribution rather than corpus
size. Instead of claiming completeness or prevalence, LIMEN makes its
processing stages, denominator classes, source-family blockers, and claim
ceilings explicit enough for a hostile reviewer to audit. The observatory
separates discovered records from duplicate-governed records, authoritative
rows from summary-grade rows, and publication-safe lineages from
queue-only leads. Every count-bearing sentence in this article names its
denominator class and figure or table reference.

The contribution is threefold. First, LIMEN provides a structured
public-source observatory for AI edge cases under source, language, and
governance uncertainty, with a controlled figure-and-table package that a
dashboard and a manuscript can share without denominator drift. Second, it
makes source-family saturation, duplicate governance, legal uncertainty,
multilingual visibility, security-threshold routing, and provenance limits
explicit as observability surfaces rather than hidden assumptions. Third, it
demonstrates that bounded accountability arguments — what public evidence can
and cannot support — are themselves publishable research contributions when
the evidence architecture is reproducible and reviewer-safe.

LIMEN is one layer in a coordinated three-observatory program. GAIA owns
public-evidence visibility across governance registries and policy surfaces.
PALLAS owns evidence-readiness and source-sidecar constraints for country and
institutional AI-readiness assessment. LIMEN owns taxonomy, duplicate
governance, proof ceilings, and dashboard/paper parity for edge-case
accountability. The three layers are complementary evidence surfaces, not one
fused corpus, and this article presents only the LIMEN layer with its own
local denominators. This observatory approach builds on documentation
standards such as Datasheets for Datasets [18] and Model Cards [19], extends
the algorithmic auditing framework [20] into public-source edge-case routing,
and situates its governance discussion within the broader AI ethics and
accountability literature [21, 22, 24].

## 2. Related Work and Positioning

LIMEN is a routing and control layer, not a replacement for official
documents, security registries, or existing incident databases. Its
positioning relative to six comparator surfaces is bounded by design.

**Incident databases and risk repositories.** The AI Incident Database (AIID)
provides community-reported incident records with taxonomy labels and
severity grading [1]. The MIT AI Risk Repository catalogs risk incidents with
structured harm-type and severity metadata [2]. CSET's AI Harm Index tracks
documented AI-related harms with sector and impact coding [3]. LIMEN differs
from all three in that it does not attempt a unified incident total; instead,
it routes public-source material through explicit duplicate governance and
denominator-class surfaces so that a reviewer can see which records are
discovered, which are duplicate-governed, and which are publication-safe.
Recent incident-reporting standardization work [26] and risk taxonomies [16, 17]
similarly emphasize that aggregation without denominator discipline obscures
evidence quality heterogeneity.
AIID, MIT AI Risk, and CSET remain bounded public comparators whose records
inform LIMEN's seed corpus but whose counts are not treated as external
validation of LIMEN totals.

**Governance and policy observatories.** The OECD AI Policy Observatory (AIM)
tracks national AI policy instruments across jurisdictions [4]. AVID (the AI
Vulnerability Database) provides structured vulnerability records linked to
AI systems and model behaviors [5]. LIMEN complements both by focusing on
edge-case evidence that governance monitors may not capture: institutional
absurdities, provenance-confusion incidents, procedural contamination in
public process, and normative anomalies that fall between regulatory
categories. OECD AIM and AVID remain bounded comparators with constrained
reuse mechanics in LIMEN's source-family governance.

**Security and adversarial taxonomies.** MITRE ATLAS provides a structured
taxonomy of adversary techniques against AI systems [6]. NIST AI RMF provides a
risk-management framework with mapped subcategories [7]. EU AI Act and
ISO/IEC 42001 provide regulatory and management-system anchors [8, 9]. OWASP's
Top 10 for Large Language Model Applications adds an operational security
taxonomy for deployed LLM systems [15]. LIMEN's
security crosswalk (Table 5, Figure 7 threshold ladder; authority-balance sidecar default 21 / projected 23 lineages) maps local evidence rows to these
frameworks without claiming framework-level coverage. The crosswalk is an
interoperability surface, not a security-prevalence finding.

**Provenance and attestation standards.** C2PA/HASH provide content
provenance standards [10]. The EU AI Act Article 50 transparency obligations
provide a regulatory anchor for provenance-discussion [8, 27]. Crawford et al.'s
*Excavating AI* framework situates training-set and provenance transparency
as a political question, not merely a technical one [23]. LIMEN's Route C
(Figure 8) shows local-bundle provenance readiness against these standards
without claiming detached-signature verification, transparency-log inclusion,
or Verifiable Credential issuance. The attestation surface is a methods
companion, not a trust-assurance claim.

The safe comparative reading is asymmetric by design: AVID and MITRE ATLAS
are the only structured seed-import surfaces in the current package; OECD AIM
and AIID remain bounded public comparators with constrained reuse mechanics;
MIT AI Risk remains a concept-layer bridge; and CSET AI Harm remains a
comparator for harm-coding discipline. Comparator progress is described only
when a source changes exactness, case-linkage, or manuscript-safe replication,
not when packaging alone becomes cleaner.

## 3. Observatory Architecture and Methods

LIMEN's first paper-safe package is framed as an observatory architecture rather than as a corpus-completeness claim. The current dashboard/article layer supports a bounded figure-and-table set, but every count-bearing object must travel with its denominator class and blocked interpretation.

The main package is a controlled visibility stack: a source-family saturation map (Figure 1), a taxonomy heatmap (Figure 2, Table 2), a legal-uncertainty matrix (Figure 3), a duplicate-control graph (Figure 4), a publication-safe lineage funnel (Figure 5), a jurisdiction/language visibility map (Figure 6), and bounded Route B (Figure 7 threshold ladder, with authority-balance sidecar default 21 / projected 23 lineages) and Route C (Figure 8) companions for security-threshold routing and attestation trust-surface readiness. These objects are useful because they show how public evidence, authority depth, language route, duplicate control, and publication ceiling differ across the same edge-case atlas.

The package remains denominator-bound. The reviewed core consists of 250 evidence-grade cases (tier T1: security disclosures with CVE identifiers, T2: contested or interim regulatory proceedings, T3: regulator or court records with direct authority text) drawn from a total dataset of 296 cases; the remaining 46 cases are media-only reports excluded from evidence-grade denominators because they lack direct regulator, court, security-disclosure, or institutional authority. The duplicate-control graph is join-safety and subtype-overlay infrastructure, not recurrence evidence. The multilingual map is an uneven-observability surface, not a country comparison. The security-threshold and attestation companion panels describe bounded route-state and provenance ceilings, not legal truth, safety, compliance, certification, or atlas completeness.

### 3.1. Denominator registry for the article

This article treats dashboard and paper counts as view-specific
denominators, not as one LIMEN corpus total. The denominator registry is summarized in Table 1.

|| Surface | Authority file | Denominator class | Manuscript role |
|| --- | --- | --- | --- |
|| Figure 2 / Table 2 live taxonomy core | `results/dashboard/taxonomy-heatmap.tsv` | 39 governed record refs / 29 unique lineages | Default taxonomy-support denominator |
|| Figure 2 / Table 2 extended taxonomy surface | `results/dashboard/taxonomy-heatmap.tsv` | 44 governed record refs / 34 unique lineages | Explicitly labeled extended sidecar only |
|| Legacy mechanical Figure 2 source | Historical provenance (reproducibility package) | 35 visible rows / 27 lineages | Historical provenance only |
|| Figure 5 publication-safe funnel | `results/dashboard/evidence-funnel.tsv` | 21 publication-safe lineages | Evidence-maturity and publication-ceiling discussion |
|| Figure 7 security / agentic threshold ladder and authority-balance sidecar | `results/dashboard/security-threshold-ladder-panel.tsv` plus `results/dashboard-paper/figure7-sidecar-consumption-matrix-v0.1.tsv` | 4 threshold rows; sidecar default visible 21 lineages with projected 23-lineage sidecar only | Route B threshold-change logic and sidecar-visible authority-balance transport; not a live 23-lineage default |

*Table 1. Denominator registry for the article. Authority files listed are the canonical source-of-truth exports used to generate each figure or table surface.*

Caption rule: every count-bearing LIMEN sentence must name the denominator class. Figure 2 live 39/29 and extended 44/34 counts, Figure 5 21-lineage counts, and Figure 7 threshold/sidecar counts (4 threshold rows; 21 default / 23 projected sidecar lineages) are not interchangeable, and none of them supports incident prevalence, corpus completeness, legal violation, compliance, certification, safety, or truth claims.

Source-ledger export rule: every count-bearing dashboard, API, static-preview, figure-export, or caption-export reuse must pass the v1.4 source-ledger renderer gate recorded in the reproducibility package before packaging. The gate requires a `(dashboard_view, row_key)` match in `results/dashboard/source-ledger-join-v0.1.tsv` and may expose family-level reuse notes or candidate review links, but row-level `access_date`, `rights_terms_note`, license, or terms badges remain blocked until file-qualified source joins are manually verified.

The figure order follows the live shared-package numbering. Figure 1 carries the source-family saturation map with explicit thin-family overlays for sf08, sf09, and sf11. Figure 2 carries the taxonomy support heatmap under the live 39/29 core and 44/34 extended contract. Figure 3 carries the legal-uncertainty matrix as a claim-ceiling surface. Figure 4 carries the duplicate-review quality-control graph (see Caption Control Register, Supplementary Methods) with the current 27-edge graph treated as join-safety infrastructure rather than recurrence evidence. Figure 5 carries the publication-safe evidence-tier funnel with the separate 21 publication-safe lineages denominator. Figure 6 remains a bounded jurisdiction/language visibility surface with six-of-six translation-review-required metadata visible. Figure 7 remains the bounded 4-row security/agentic threshold companion rather than part of the Route A denominator, and any Figure 7 export must separately expose the authority-balance sidecar as default visible 21 lineages with a projected 23-lineage sidecar only. Figure 8 remains the bounded attestation trust-surface readiness companion showing local-bundle provenance ceilings.

Figure 2 and Table 2 require one explicit hostile-reviewer reading rule: the manuscript treats the live taxonomy heatmap as the consumer surface (see Claims Register, Supplementary Methods) and distinguishes the live 39/29 core from the explicit 44/34 extended sidecar and from the older 35/27 mechanical state. Zero-seed, overlay, and authority-fragility semantics are preserved, and residual taxonomy pressure is not converted into prevalence, novelty, or new-top-level-category claims.

**Table 2. Taxonomy support summary (39/29 core).** Under the live 39/29 denominator, the 15 primary taxonomy categories distribute as follows (sample reference counts per category; multi-label assignment means category sums exceed the 39 unique governed-record-ref total): `security_risk` (9 refs; includes LIMEN-000016 mapped to MITRE ATLAS L06:Deployment/S0100:Software Vulnerability via AVID-2026-R1707 and vendor advisory GHSA-xj5p-w2v5-fjm6) `agentic_control_failure` (9), `public_sector_misuse_or_gap` (7), `unlawful_or_allegedly_unlawful_use` (5), `normative_or_moral_outlier` (5), `education_workplace_or_hr` (4), `ai_washing_or_false_ai_claim` (4), `surveillance_biometrics_or_policing` (3), `institutional_absurdity` (3), `deepfake_or_synthetic_identity` (3), `legal_procedural_contamination` (2), `finance_insurance_or_market` (2), and three zero-seed guardrail rows (`health_medical_or_mental_health`, `research_integrity`, `residual_unclassified`). The full taxonomy × evidence-tier cross-tabulation, extended sidecar counts, overlay-ready annotations, and zero-seed/fragility flags are provided in Supplementary Table S1 and the reproducibility package.

Table 4 carries the public-sector disclosure asymmetry comparison (see Caption Control Register, Supplementary Methods), with manuscript-facing controls for proof ceilings and disclosure comparison. Amsterdam is bounded as an exact-row-rich register exemplar whose tested public routes still do not yield exact-name procurement proof; Helsinki is bounded at family-level procurement continuity rather than exact row-to-contract linkage; UK ICO rows are framed as regulator-document comparators rather than procurement evidence; and ORION is framed as a low-trace official-project-page floor.

For Figure 1 reuse, the canonical manuscript bundle stays on the shared source-family coverage and evidence-policy matrix exports (see Supplementary Methods). Seeded-family counts are useful only when they travel with typed claim ceilings, exact blocker forms, and threshold-changing conditions for sf08, sf09, and sf11.

The comparator layer is narrated with the same control logic. The six-family comparator note — AIID, OECD AIM, AVID, MIT AI Risk, CSET AI Harm, and MITRE ATLAS — is treated as a bounded appendix/comparison surface rather than as external validation.

## 4. Results: Evidence Architecture Surfaces

### 4.1. Authoritative document-depth routing

LIMEN's authoritative-document routing separates at least five materially different support states across its core rows (Supplementary Table S1): one case with regulator-hosted order text (LIMEN-000001), one agency-to-court progression with a public civil-action number but no captured court-facing document (LIMEN-000002), two UK regulator matters that include regulator summary, enforcement record, and direct notice text (LIMEN-000003, LIMEN-000004), one FCC enforcement-lifecycle package spanning allegation-stage and consent-decree documents (LIMEN-000008), and security-facing rows where vendor advisories or coordination-center bulletins supply notice-layer evidence without adjudicative force. Six rows are selective-anchor-ready (LIMEN-000001, LIMEN-000003, LIMEN-000004, LIMEN-000006, LIMEN-000007, LIMEN-000008), LIMEN-000002 remains blocked by absent court-facing text, and LIMEN-000005 remains usable only for accusation-stage wording until caption normalization improves.

This strengthens a methods/results argument that LIMEN should model document-chain coverage explicitly. Public visibility alone does not tell a reviewer whether a row supports quoted order language, bounded procedural posture, direct notice-text anchors, remediation notice metadata, allegation-to-disposition lifecycle wording, or only a limitation-grade lead. The anchor-routing rule keeps official-authority rows, reviewed-core security rows, and appendix-only security anchors separate while still discussing them inside one article package (Table 3).

### 4.2. Security-evidence routing and threshold logic

Across LIMEN's current eleven-row public security seed, evidence-layer asymmetry is the principal result (Table 5, Figure 7 threshold ladder; sidecar default 21 / projected 23 lineages): three rows (LIMEN-000001, LIMEN-000003, LIMEN-000008) sit in the core results bucket because they combine primary CVE text with vendor-authored advisory visibility and exact fix language; eight rows (LIMEN-000002, LIMEN-000004, LIMEN-000005, LIMEN-000006, LIMEN-000007, LIMEN-000009, LIMEN-000012, LIMEN-000016) belong in appendix-supporting results because they depend on reviewed-advisory or source-qualified wording, coordination-plus-CVE-linked fix visibility below formal vendor-bulletin certainty, independent-lab remediation language, a bounded identity-boundary exemplar, or a three-row trust-boundary slice spanning PraisonAI, Playwright MCP, and ToolHive; and one explicit gap row keeps the need for peer-reviewed security case support visible until a live row gains incident-specific support.

The reviewer-safe interpretation is therefore structural: current public agentic-security evidence is heterogeneous across interoperability, remediation visibility, vendor-authored notice depth, source independence, mechanism family, and anchor layer, and that heterogeneity is now explicit enough to drive a manuscript panel split rather than a single flattened security table. The Route B threshold contract (Supplementary Table S2) travels with this finding whenever the paper shifts from generic asymmetry prose to venue-fit claims, and the threshold-change matrix (Supplementary Table S3) travels with it whenever the prose shifts from safe current-state interpretation to exact row-level upgrade conditions.

### 4.3. Provenance-confusion and synthetic-identity routing

Deepfake, synthetic-identity, false-authorship, and provenance-confusion incidents are treated here as an evidence-class problem before they are treated as a counting problem. One document-visible pathway reaches disposition-stage closure: FCC public texts support a bounded lifecycle from the February 2024 declaratory ruling through the May notice of apparent liability to the August 2024 consent decree in the Lingo Telecom matter [14], including a USD 1,000,000 civil penalty and explicit STIR/SHAKEN and KYC/KYUP terms. The New Hampshire origin-side branch sits in an intermediate archive-recovered state: public Wayback copies preserve official charging-page text, but the live canonical host still returns 403 and no later-stage authority follow-through is yet in the local package. Finnish and Lithuanian rows remain limitations-only multilingual leads. The correct interpretation is structural rather than event-count-based: public governance attention to provenance confusion and AI impersonation is document-visible in LIMEN, but only one current cluster reaches direct disposition-stage closure while comparable multilingual authority-grade records remain thin.

The authority-promotion funnel sharpens that asymmetry into an operational publication rule. The Finnish row is now stronger than discovery friction alone because a browser-reachable direct article shell exposes the exact title, date, and bounded preview paragraphs with suspicion-stage police-investigation framing, but the row still remains a preview-text-visible candidate below full-body readability and below public-authority corroboration. The Lithuanian row is presently a mixed rights/access barrier case that is more useful as a methods-and-limitations example unless a clearly compliant alternative official surface appears. This route split matters because it tells reviewers why the atlas can already visualize governance visibility around synthetic identity while still withholding stronger event-level language for specific multilingual rows.

The provenance-confusion routing is governed by a question-role matrix and publication-cell geometry (Supplementary Table S4; see Caption Control Register, Supplementary Methods). In the current package, there are two left-anchor cells (Article 50 and C2PA), one governance-context cell (the broader U.S. institutional-response ladder), one default main-results cell (the FCC lifecycle-closure cluster), and two limitations-only multilingual cells (Finland and Lithuania), while New Hampshire remains a non-default methods badge carrying archive-recovered official origin-side text, and the Pennsylvania severe-misuse row remains metadata-only. Finland stays the best next non-telecom hidden-to-visible candidate, Lithuania stays barrier-hidden, New Hampshire stays off the default table body unless one later-stage public-authority layer lands, and Pennsylvania stays appendix/metadata-only even if reused.

### 4.4. Security claim-ceiling panel

The current security evidence group is now strong enough for a reviewer-safe claim-ceiling table and a manuscript panel split, not for a broad security prevalence argument (Supplementary Table S5). Three rows sit in core results with exact fix visibility and vendor-authored notice depth, eight more belong in appendix/supporting use because they depend on formal reviewed-advisory or source-qualified package-history wording (LIMEN-000002), coordination-plus-CVE-linked exact-fix visibility below formal vendor-advisory depth (LIMEN-000004, LIMEN-000005), independent-lab source-qualified remediation language (LIMEN-000006, LIMEN-000007), one vendor-advisory-centric non-MCP authorization-boundary row (LIMEN-000009), or a now three-row trust-boundary slice spanning PraisonAI (LIMEN-000009), Playwright MCP (LIMEN-000012), and ToolHive (LIMEN-000016); and one explicit gap row keeps the peer-reviewed security zero state visible.

The publication-cell matrix, trust-boundary breadth board, supply-chain frontier, and peer-review frontier (Supplementary Tables S6–S9) keep the panel split reviewer-legible. The Route B threshold ladder (Figure 7, Table 5) remains bounded at 4 rows and is not part of the Route A denominator; the Figure 7 authority-balance sidecar must stay captioned as default visible 21 lineages with a projected 23-lineage sidecar only. A new non-advisory primary-source security row or a first peer-reviewed incident-specific study would materially change the threshold contract, but absent those upgrades the panel split remains the correct publication posture.

### 4.5. Procedural-contamination and research-integrity routing

LIMEN's procedural-contamination and research-integrity slice supports a source-depth claim: the package combines two distinct procedural-contamination families and several research-integrity evidence states without flattening them into one support bucket (Supplementary Table S10). On the procedural side, LIMEN pairs the Italian DPA order-text row with a direct-source-resolved Finnish Yle article that names Internal Finland Police and the Eastern Finland Administrative Court, describes AI-assisted administrative appeals, and records fabricated-case-reference plus workload-burden signals. The Finland row is reviewer-legible as an authority-escalation ladder: direct broadcaster evidence, official actor-role verification, official governance context, bounded police/ministry no-hit searches, and bounded judicial search-surface friction are kept analytically separate instead of being overread as one official confirmation state.

On the research-integrity side, the same evidence group now visibly spans mediated editor statement, a blocked retraction DOI pair with public PubMed corroboration for both the retraction notice and the retracted original record, and two direct Springer-originating notice-text exemplars spanning a journal-article surface and a book surface; the gain is venue-type breadth, not cross-publisher closure. The mixed package is table-ready as one hostile-reviewer panel (Supplementary Table S11) rather than a set of scattered notes.

The package is routed through one shared manuscript-ready control surface (Supplementary Table S12; see Caption Control Register, Supplementary Methods): a seven-row procedural-contamination source-depth sidecar panel that keeps the Italian document-grade anchor, the Finnish broadcaster-plus-official-probe comparator, the mediated and DOI-pair intermediate research-integrity states, the two direct notice-text exemplars, and a mixed residual bucket visibly separate.

The reviewer-safe interpretation remains methodological. LIMEN can show why legal/procedural contamination and research-integrity rows need source-depth-aware narration, but the package still does not justify incident counts, misconduct tallies, sanction inventories, prevalence claims, or system-wide legal-process conclusions. The top source-depth classes remain thin, but the direct-notice slice is no longer singleton: the current package contains two direct Springer-originating notice-text exemplars spanning one journal-article surface and one book surface, while procedural document-grade depth still rests on only one process-integrity family. The residual floor is also no longer uniformly weak: one fake-article-network row now has an archived SSRN platform-action exemplar, while two residual rows remain below direct action-record state. The source-depth sidecar should therefore stay framed as a bounded evidence-depth panel and claim-ceiling device rather than as a substantive count surface.

### 4.6. AI-washing posture ladder

The AI-washing posture sidecar is best read as a four-row ladder (Table 4): two settled or regulator-final AI-washing exemplars grounded in SEC enforcement materials, both in regulated finance [11]; one separate authoritative charging-stage hidden-human-behind-AI record outside regulated finance [12]; and one explicit queue row for the still-missing regulator-final or adjudicated hidden-human-as-AI upgrade.

The SEC's March 2024 press release states that Delphia and Global Predictions settled charges for making false and misleading statements about their purported use of artificial intelligence, with $400,000 in total civil penalties. The Delphia order states that the firm represented that it used AI and machine learning with retail client spending and social-media data when no such data was being used in its investment process, and ordered a $225,000 civil money penalty. The Global Predictions order states that the firm made false and misleading claims about its AI use, its claimed status as the first regulated AI financial advisor, and the services it offered, and ordered a $175,000 civil money penalty.

Separately, the DOJ SDNY press release states that Albert Saniger was charged with making false and misleading statements about nate's AI capabilities and that nate relied heavily on human workers to perform transactions users believed were automated, while also stating that the charges are accusations and that the defendant is presumed innocent unless and until proven guilty [12]. Separately from that four-row core, the FTC DoNotPay complaint/final-order package [13] now gives the evidence group one bounded official non-finance sidecar: the complaint said DoNotPay described the service as the world's first robot lawyer and an AI lawyer capable of drafting legal materials, while the final order bars representations that a covered product or service operates like a human lawyer.

The reviewer-safe interpretation is that LIMEN can show an AI-washing posture ladder across two settled SEC exemplars, one charging-stage DOJ exemplar, and one bounded FTC non-finance sidecar, but the ladder does not support AI-washing prevalence, sector ranking, or enforcement-completeness claims.

### 4.7. Taxonomy-routing guardrails and residual pressure

Under LIMEN's live 39/29 duplicate-governed taxonomy contract, the strongest repeated patterns fit the existing multi-label taxonomy and are more useful as bounded overlays, boxed comparators, or appendix-grade nested subtypes than as new top-level labels. The route-state split is now explicit: `runtime_execution_abuse` and `false_capability_or_faux_automation` are ready for bounded overlay or sidecar reuse; `public_authority_biometric_and_border_governance` is usable as a boxed comparator; `trust_boundary_and_authorization_failure` is appendix-ready but still nested inside the broader security pair; `procedural_hallucination_in_public_process`, `detector_governance_and_false_detection_claims`, and `deepfake_intimate_image_local_abuse` remain queue or singleton-watch material; `institutional_absurdity` remains visibly seeded but authority-thin; and `residual_unclassified` remains a methods guardrail rather than a latent count-bearing category.

This is the main publication-safe gain: LIMEN can now show that residual taxonomy pressure improves reviewer-legible routing and claim ceilings even when no new top-level category is justified. The security overlay remains useful because repeated mechanism families can support a Figure 2 or a Route B security inset without implying ecosystem prevalence. The AI-capability-misstatement slice remains useful because settled SEC rows, charging-stage hidden-human allegations, and bounded FTC non-finance rows can be compared only if the taxonomy keeps them in the same overlay space. The methods guardrail is that none of these overlays converts into a new top-level category, a prevalence finding, or a corpus-completeness argument.

### 4.8. Public-sector disclosure asymmetry

LIMEN's public-sector slice is best read as an institutional-asymmetry panel (Table 4): the five-row package spans one official project-page floor (ORION), two direct regulator-document comparators (Serco and Chelmer), one register-rich but buyer-side-unresolved municipal row (Amsterdam), and one register-plus-family-level same-buyer procurement bridge (Helsinki). The bounded contribution is structural: different public-sector disclosure surfaces expose different parts of the reconstruction problem, and those parts do not move together.

The institutional-asymmetry matrix and traceability ladder (Supplementary Tables S13–S14) show that exact-row machine readability, buyer-side traceability, direct legal-basis visibility, public-assessment inspectability, and supplier visibility are presently distributed across different rows rather than collapsing into one ideal case. The strongest current contrast remains Amsterdam versus Helsinki. Amsterdam is the richest exact-row register exemplar because the public municipal register exposes supplier, governance-companion fields, and downloadable current/history exports; the tested public procurement route still shows an exact-name ChatAmsterdam non-hit, while a same-buyer Azure/Public Cloud procurement-family chain is publicly visible on TenderNed without yet yielding a reviewer-checkable row-specific tender, award, contract, or downloadable companion assessment for the same register row. Helsinki sits one rung higher on buyer-side continuity because an official same-buyer procurement package with IBM-consistent award metadata is public, but that linkage remains family-level rather than exact row-to-contract proof for the parking-chatbot page.

Table 4 should be read through the claims register (see Claims Register, Supplementary Methods) and caption-control rules (see Caption Control Register, Supplementary Methods). Keep Amsterdam explicitly bounded as an exact-row-rich register exemplar with no exact-name procurement hit yet, Helsinki bounded at family-level procurement continuity rather than exact contract linkage, the UK ICO rows framed as regulator-document comparators rather than procurement evidence, and ORION bounded as a low-trace official-project-page floor. The five-row package stays a bounded observability surface rather than drifting into prevalence or procurement-completeness rhetoric.

### 4.9. Multilingual readiness

LIMEN's current multilingual queue is useful as a visibility surface, not as a simple incident count (Figure 6, Table 6; see Claims Register, Supplementary Methods). The reviewed-core jurisdiction × tier breakdown (Supplementary Table S15) shows that 250 evidence-grade cases span 34 country or supranational jurisdictions (35 raw jurisdiction labels normalized by merging the compound label "International / Japan / ICLR workshop" into Japan), with the United States accounting for 126 of 250 rows and the remaining 33 jurisdictions contributing between 1 and 14 rows each. Three of six non-English leads have moved into direct-source-resolved status, but only one sits in the bounded substantive direct-official bucket while two belong in appendix/methods use and three remain queue-only in the verification/limitations layer. The key result is visibility asymmetry, not country ranking or incident counting: the resolved trio is heterogeneous, the medium-undercovered band is still live, the high-undercovered rows remain queue-only under rights/access or challenge-gating constraints, and the unresolved remainder matters because it shows where English-heavy discovery still hides governance evidence. This asymmetry is consistent with broader observations that algorithmic fairness and governance frameworks are often designed from English-language and Western-institutional perspectives [25].

## 5. Limitations

LIMEN's limitations are structural and explicit, not hidden. This section
names the principal ceilings a hostile reviewer should test.

### 5.1. Denominator separation

Figure 2, Figure 5, and Figure 7 carry three different denominators that are
not interchangeable: Figure 2 / Table 2 uses the 39/29 core (with 44/34 as an
explicitly labeled extended sidecar); Figure 5 uses the separate 21
publication-safe lineages denominator; and Figure 7 uses the bounded 4 threshold
rows, with the separate authority-balance sidecar shown as default visible
21 lineages and projected 23-lineage sidecar only. None of these denominators supports incident prevalence,
corpus completeness, legal violation, compliance, certification, safety, or
truth claims. A reviewer who treats them as one LIMEN corpus total will
misread the package. (See Claims Register and Caption Control Register, Supplementary Methods.)

### 5.2. Source-family blocker order

The three principal stronger-source blockers are sf08 (court and tribunal
records), sf09 (public-sector registers and procurement), and sf11 (security
research and advisories), in authority-depth priority order. Each blocker is
named in Figure 1, has a documented exact upgrade trigger, a negative-evidence
class, and a caption-control entry. The package is publishable with these
blockers visible because LIMEN's contribution is evidence architecture, not
corpus completeness. A fuller treatment appears in the Supplementary Methods appendix.

### 5.3. Translation dependence

Three of six non-English leads have moved to direct-source-resolved status,
but only one sits in the bounded substantive direct-official bucket. The
remaining multilingual rows still require translation review before sharper
legal or operational interpretation is safe. The manuscript does not rank
country readiness or make legal/policy conclusions from machine translation
alone.

### 5.4. Authority imbalance

The current authoritative evidence group is geographically and institutionally
concentrated: Italian, UK, and US regulator/enforcement surfaces dominate
the document-grade depth slice. This concentration is a visibility-surface
property, not a prevalence finding. A reviewer should read Table 3 as an
asymmetry panel, not as evidence that AI governance incidents are
disproportionately Anglo-American or European.

### 5.5. Zero-seed taxonomy categories

Several taxonomy categories in Figure 2 remain queue-only or singleton-watch
material: `procedural_hallucination_in_public_process`,
`detector_governance_and_false_detection_claims`,
`deepfake_intimate_image_local_abuse`, and `residual_unclassified`. These
are methods guardrails and residual-pressure indicators, not latent
count-bearing categories. The manuscript does not claim new top-level
category discovery.

### 5.6. Stronger-witness absence

Route C (attestation trust-surface readiness, Figure 8) currently shows
local-bundle provenance only. No detached signature, transparency-log
inclusion proof, or Verifiable Credential is present. Route B (security
threshold, Figure 7 threshold ladder; sidecar default 21 / projected 23 lineages) retains the explicit gap for peer-reviewed security
case support. Neither route supports external witness, trust assurance,
scholarly consensus, or ecosystem-wide security prevalence claims.

### 5.7. No fused denominator

LIMEN, GAIA, and PALLAS are complementary evidence layers, not one fused
empirical corpus. This article does not present a single denominator spanning
all three observatories. The shared bridge appendix explains why the layers
are complementary and how denominator discipline is preserved across them.

## 6. Conclusion

LIMEN is a structured public-source observatory for AI edge cases under
source, language, and governance uncertainty. Its contribution is evidence
architecture: a controlled visibility stack that keeps denominator classes,
duplicate governance, source-family blockers, legal and translation ceilings,
and proof boundaries visible to a hostile reviewer. The dashboard and paper
share controlled figure and table surfaces governed by a caption-control
register, so every count-bearing sentence names its denominator class.

The observatory does not claim corpus completeness, incident prevalence,
legal violation, compliance, certification, safety, or truth. It claims that
public evidence, when routed through explicit denominator discipline and
source-family governance, can support bounded accountability and
observability arguments that are reusable across venues, thesis chapters,
and companion observatories. The principal remaining work is not more
material but stronger depth within the three named blockers (sf08, sf09,
sf11) and continued manuscript-package discipline as the article moves
toward venue-specific variants.

## 7. References

[1] McGregor, S. (2021). The AI Incident Database. *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(17), 15872–15873. https://incidentdatabase.ai

[2] Schuett, J., et al. (2024). The AI Risk Repository: A Comprehensive Meta-Review, Database, and Taxonomy of Reasons Why AI Is Risky. *arXiv preprint arXiv:2408.12764*. https://airisk.mit.edu

[3] Center for Security and Emerging Technology (CSET). (2025). AI Harm Index. Georgetown University. https://cset.georgetown.edu

[4] OECD. (2024). AI Policy Observatory (OECD.AI). https://oecd.ai

[5] MITRE. (2024). AVID — AI Vulnerability Database. https://avidml.gitbook.io

[6] MITRE. (2024). ATLAS — Adversarial Threat Landscape for AI Systems. https://atlas.mitre.org

[7] NIST. (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. https://www.nist.gov/artificial-intelligence

[8] European Parliament and Council. (2024). Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (EU AI Act). *Official Journal of the European Union*, L 2024/1689.

[9] ISO/IEC 42001:2023. Information technology — Artificial intelligence — Management system. International Organization for Standardization.

[10] C2PA. (2024). Content Provenance and Authenticity: Technical Specification v2.0. Coalition for Content Provenance and Authenticity. https://c2pa.org

[11] U.S. Securities and Exchange Commission. (2024). SEC Charges Two Investment Advisers and Their CEOs With "AI Washing." Press Release 2024-43, March 18, 2024. (Delphia and Global Predictions.)

[12] U.S. Department of Justice, SDNY. (2024). Manhattan U.S. Attorney Announces Charges Against Founder of "nate" AI App for Securities Fraud. Press Release, December 2024. (Albert Saniger / nate.)

[13] Federal Trade Commission. (2024). FTC Takes Action Against DoNotPay for Falsely Touting Its AI Lawyer. Press Release, January 2024; Final Order, March 2024.

[14] Federal Communications Commission. (2024). Lingo Telecom, LLC — Notice of Apparent Liability and Consent Decree. FCC File No. EB-TCD-23-00035328. August 2024.

[15] OWASP. (2023). OWASP Top 10 for Large Language Model Applications. Open Worldwide Application Security Project. https://owasp.org/www-project-top-10-for-large-language-model-applications/

[16] Bommasani, R., et al. (2021). On the Opportunities and Risks of Foundation Models. *arXiv preprint arXiv:2108.07258*.

[17] Weidinger, L., et al. (2022). Taxonomy of Risks Posed by Language Models. *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22)*, 214–229.

[18] Gebru, T., et al. (2021). Datasheets for Datasets. *Communications of the ACM*, 64(12), 86–92.

[19] Mitchell, M., et al. (2019). Model Cards for Model Reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* '19)*, 220–229.

[20] Raji, I. D., et al. (2020). Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing. *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (FAT* '20)*, 33–44.

[21] Jobin, A., Ienca, M., & Vayena, E. (2019). The Global Landscape of AI Ethics Guidelines. *Nature Machine Intelligence*, 1, 389–399.

[22] Floridi, L., & Cowls, J. (2019). A Unified Framework of Five Principles for AI in Society. *Harvard Data Science Review*, 1(1).

[23] Crawford, K., Dobbe, R., & Paglen, T. (2019). Excavating AI: The Politics of Training Sets for Machine Learning. https://excavating.ai

[24] Roberts, M. H., et al. (2021). Artificial Intelligence Governance: Ethical Considerations and Implications for Social Responsibility. *AI & Society*, 36(1), 615–635.

[25] Sambasivan, N., et al. (2021). Re-imagining Algorithmic Fairness in India: Perspectives and Learnings from Interactions with Data Practitioners. *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)*, 268–280.

[26] Agarwal, A., & Nene, M. J. (2025). Advancing Trustworthy AI for Sustainable Development: Recommendations for Standardising AI Incident Reporting. *arXiv preprint arXiv:2501.14778*. https://doi.org/10.48550/arXiv.2501.14778

[27] European Commission. (2021). Proposal for a Regulation laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). COM(2021) 206 final. (Pre-adoption impact assessment and explanatory memorandum.)

## 8. Data Availability

The reproducibility package — including dashboard exports (taxonomy heatmaps, evidence funnels, source-family coverage maps, security threshold ladders, jurisdiction/language surfaces), the caption-control register, the figure-route registry, and the source-family evidence-policy matrix — is available in the project repository under `results/dashboard/` and `results/dashboard-paper/`. All case identifiers (LIMEN-000001 through LIMEN-000016 and beyond) are resolved against public-source documents cited in the provenance metadata of each export. The denominator registry (Table 1) provides the mapping from figure/table surfaces to authority files. Supplementary materials (claim-ceiling matrices, threshold-change contracts, and source-depth panels) are available as referenced in Supplementary Tables S1–S15 and the Supplementary Methods appendix.