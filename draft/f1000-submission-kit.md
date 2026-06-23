# F1000Research submission kit — LIMEN Method Article

Everything below is paste-ready. The only steps I cannot do are the ones that require your F1000 login and accepting the APC (see "What only you can do").

## Files to upload
| Slot in the portal | File |
|---|---|
| **Main article** (must be Word or LaTeX, **not** PDF) | `preprint-v0.3-f1000.docx` |
| **Cover letter** | `cover-letter-f1000.docx` (or paste the text) |
| Figure (if asked separately) | `figure-reviewed-core-tier-by-theme.png` (already embedded in the .docx; F1000 may also want it as a separate file) |
| Underlying data | already deposited — give the DOI **10.5281/zenodo.20701594** (do **not** re-upload; F1000 links it) |

## Form fields (paste-ready)

- **Article type:** Method Article
- **Title:** LIMEN: a reviewer-safe public-source observatory for AI edge cases under source, language, and governance uncertainty
- **Author:** Anton Sokolov — sole author
- **Affiliation:** Tyche Institute, Tallinn, Estonia
- **ORCID:** 0000-0003-2452-7096
- **Corresponding email:** anton.sokolov@tyche.institute
- **Keywords:** AI incidents; AI harms; AI edge cases; evidence tiering; AI governance; AI accountability; regulatory enforcement; observatory; claim ceilings; provenance; reproducibility

### Abstract (paste verbatim — synchronized with F1000 v0.4 manuscript, 2026-06-18)
Catalogues of "AI failures" are easy to assemble and hard to trust. Existing incident lists tend to merge a regulator's final order, a charging-stage allegation, a documented software vulnerability and a viral news anecdote into one undifferentiated count — and then invite readers to treat that count as prevalence. This article describes LIMEN, a public-source observatory whose contribution is not the size of its corpus but an *evidence architecture*: a reproducible method for cataloguing AI edge cases that keeps source authority, evidence maturity, duplicate control, legal uncertainty and language coverage explicit, and that bounds every count by what the underlying record can support. The method has five steps — gather, adversarially verify, tier, bound, link — and one governing rule: never report a single fused corpus total, only separate denominator classes each carrying its own claim ceiling. We document the data model, the refute-by-default verification protocol, the tiering criteria, and the per-case claim-ceiling and caveat schema, and we demonstrate the method on a reviewed core of 250 evidence-grade AI edge cases (157 regulator/court records, 82 contested/interim matters, 11 security disclosures) drawn from 34 jurisdictions, plus a separately-marked layer of 46 media-documented incidents that is excluded from the evidence-grade denominator. Technical validation reports the results of an adversarial per-item verification pass (no fabricated cases found among the legal/regulatory batches; tier and fact corrections applied; two entries removed) and the source-link coverage of the released dataset. The reviewed core is presented not as a complete or representative map of AI harm but as a worked demonstration that an edge-case atlas can scale across jurisdictions and themes while remaining reviewer-safe. We make no claim of corpus completeness, incident prevalence, representativeness, legal violation by inference, or a single fused total.

### Data availability (paste verbatim — synchronized with F1000 v0.4 manuscript, 2026-06-18)
A citable, archived snapshot of the underlying dataset is deposited at Zenodo (DOI: 10.5281/zenodo.20701594, CC-BY-4.0): the catalogue (cases.json, 296 cases), a field dictionary (README.md), the per-class evidence panel, the theme-by-tier matrix, and Figure 1. The dataset is openly browsable at https://obscure-ai.eatf.eu (JSON at https://obscure-ai.eatf.eu/data/cases.json); the live observatory is at https://limen.eatf.eu.

### Underlying data DOI
10.5281/zenodo.20701594

### Competing interests
No competing interests are declared.

### Grant information
The author declares that no grants were involved in supporting this work.

### Prior posting / preprint disclosure (F1000 asks)
An earlier draft is publicly archived at Zenodo (DOI: 10.5281/zenodo.20700813). This is permitted under F1000Research's preprint policy; the submitted version is the expanded Method Article.

## Suggested reviewers (candidates — verify independence + look up a current email before entering; do NOT enter anyone you have collaborated with)
F1000Research invites reviewers; you may suggest experts. Candidates by area:
1. **AI-incident documentation** — a lead of the AI Incident Database (Responsible AI Collaborative) or the OECD.AI incidents expert group. Strong topical fit; note they run a peer system, which an editor may read as a competing interest — judge accordingly.
2. **AI incidents & controversies** — Charlie Pownall (AIAAIC founder), independent. Good fit for the cataloguing/evidence angle.
3. **AI risk taxonomy** — a contributor to the MIT AI Risk Repository (MIT FutureTech), for the risk-vs-incident framing.
4. **Computational legal / AI governance** — an academic working on AI accountability and evidence (law-and-technology faculty). Fits the proof-ceiling / legal-uncertainty angle.
5. **Research-data curation / open data** — a data-curation or research-data-management scholar, for the dataset/reproducibility angle.

For each: find the current institutional email yourself; I have deliberately not filled emails to avoid inventing contact details.

## What only you can do
- Log in to F1000Research (or create the submission under your account).
- Accept the APC (F1000 invoices the article-processing charge; publish-then-review means the article goes live before peer review).
- Click **Submit**.

If you'd rather I drive the portal form with you: log in to F1000Research in Chrome with the Claude-in-Chrome extension connected, and I can fill the fields step by step from this kit — but you confirm and click the final Submit.
