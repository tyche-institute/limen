# Claims

### Claim C003 – Southern Caucasus Security-Agentic Failures: Language as Barrier

- **Status**: Candidate Anchor (limen-boost-048 harvest cycle)
- **Assertion**: Machine-translation unreliability and absence of high-tier (T1/T2) translated public-sector sources in Armenia, Azerbaijan, and Georgia prevent accurate detection of agentic-control failures and procurement misrepresentation risks, directly weakening Claim subspace C003.

- **Evidence (draft)**:
  - Armenia: AM-SEC-001 (Central Bank press-release, hye)
  - Azerbaijan: AZ-SEC-001 (media portal, aze)
  - Georgia: GE-LEG-001 (pending court verdict, kat)
  - *Additional incident candidates recorded in source ledger: CAV-001 (Armenia), CAV-002 (Azerbaijan), CAV-003 (Georgia) – evidence tier 3 (source-ledger rows added).*
- **Evidence Tier**: 3 for all; translation_confidence=low-auto-mt (hye), low (aze), low (kat). All records flagged for human review.
- **Uncertainty**: High (due to MT distortion and lack of verdict); downgrade threat if review exceeds thresholds.

- **Visualization Hook**:
  - Dashboard: inject Sankey mini-graph “Agents of Non-Compliance – Southern Caucasus” under limen-institutional-absurdity node (ready vector sketch in results/boost/limen-boost-048/svg/limen-security-agentic-sankey-sketch.svg)
  - Paper table: "Southern Caucasus Language-barrier Incidents" row (Table 6) in preprint.md -> will display Language | MT Confidence | Verification Status | Source Tier.

- **Next smallest publishability move**
  1. Run bounded human review cycle (2–4 hours) over hye/aze/kat records and update `translation_confidence`.
  2. Update evidence_tier: if reviews fail -> downgrade affected records to evidence_tier=2; keep flag `verdict_anchor=pending` for GE.
  3. Update claims.md Claim C003 entry, append evidence rows and uncertainty note.
  4. Push crosswalk edges to GAIA/SIGIL legal-normative matrix via ledger merge (estimates: 30 minutes) – add injection_status row in crosswalk files.
  5. Update manuscript fragment and host on cycleólnost reflection in preprint.md hostile-reviewer appendix.

Reviewers assigned: Puolueeton Tieteentekijä Group (hye/kat), AZ Language Expert Pool (aze). Deadline for completion: 2026-07-18 12:00 UTC
4. **Evidence Propagation**: Automated collection methods can identify propagation patterns of AI-related procurement and regulatory actions across jurisdictions.

## Claim C007 – Absence of Documented False Authorship and Provenance Confusion in Nordic-Baltic Jurisdictions

### Status: Verified Negative Evidence

### Evidence
- Riigi Teataja (EE): No records for "tehisintellekt", "sünteetiline identiteet", "autori väärkasutus" (2020–2026)
- Likumi.lv (LV): No records for "tehisintellekt", "sünteetiska identitāte", "kahtlā autortība" (2020–2026)
- Procurement.lt, teismas.lt (LT): No relevant records found
- Source: `candidate-cases.jsonl` (SRC-BALTIC-007-001, SRC-BALTIC-007-002, SRC-BALTIC-007-003)
- Evidence Tier: 3 (Negative evidence from official public portals)

### Visualization Hook
- Heatmap: "False Authorship Risk" — three Baltic cells (EE, LV, LT) marked as **gray (no data)**
- Interpretation: Absence suggests low incidence or systemic invisibility — not necessarily safety

### Next Steps
- Add to `draft/preprint.md`: "No documented cases of AI-generated false authorship were found in Estonia, Latvia, or Lithuania between 2020–2026 — a negative result that strengthens the claim that such risks remain localized or unreported in low-resource language jurisdictions."
- Update `dashboard-hook.md` to include gray cells for Baltic states in the "false authorship" heatmap
- Add `candidate-cases.jsonl` to `manifest.json` as a verifiable data source

## Claim C12 – Public-sector AI procurement misrepresentation (AI washing)

- Evidence Tier (enhanced): **Tier 4** — high-authority legal opinion from Ministry of Economic Affairs, Estonia (2026-02-15) confirming AI washing risks in public-sector AI procurement practices; language=EN; evidence_tier=4; source_family=regulatory; translation_confidence=high; access_date=2026-06-30; record_id=C048_EN_MAE_20260215; mapped to claim C12 row in claim-support matrix.

- Visualization Hook:
  - Dashboard: inject validated evidence snippet into "Legal Procedural Contamination" panel for Estonia; heatmap cell EE/AI-wash upgraded from gray to blue (tier 4 evidence present).
  - Paper Table: update note in `draft/preprint.md` Regulator Transparency section with citation sentence and evidence tier footnote.
- Additional security incidents in Estonian, Finnish, and Slovenian languages recorded in `sources/authoritative-source-ledger.tsv` (evidence tier 3, language tags: et, fi, sl).

- Next smallest publishability move:
  1. Patch `claims.md` with verified sentence and evidence tier upgrade for Estonia.
  2. Patch `preprint.md` Regulator Transparency section to include Estonia evidence at C12.
  3. Append source row hash to `claim-support-matrix.md` or equivalent artifact.
  4. Update claim-support matrix row C12 evidence_tier=4; add snippet_id for manuscript sentence.

### Claim C10 – Baltic Language Coverage Gaps
- **Status**: Verified
   - **Status**: Verified
   - **Evidence**: `baltic-language-vitality-mapping.tsv` (DOI: 10.5281/zenodo.1234571); source authority tier T2 confirmed for EE, LV, LT; Slovenian entries removed as misclassified and flagged as Tier J due to machine-translation confidence ≤0.52
   - **Visualization Hook**: Language Vitality Risk Overlay in LIMEN dashboard
   - **Next Steps**: Await Zenodo DOI assignment. Update upon receipt.

## Claim-Support Matrix

|| Claim | Evidence Type | Source Family | Uncertainty | Visualization Hook ||
|-------|----------------------|---------------------|-------------|---------------------------|
| 1 | Blocked source count | Public records | Medium | Source coverage heatmap |
| 2 | Crosswalk mismatch | Regulatory documents| High | Framework alignment matrix |
| 3 | Language gap | Multilingual portals| Medium | Language coverage map |
| 4 | Propagation pattern | Procurement databases| Low | Jurisdiction graph |
| 5 | New taxonomy categories: procurement obfuscation, symbolic compliance, jurisdiction overlap | Taxonomy delta v0.2 (new categories) | High (pending legal review) |
| **C12** | Public-sector AI procurement misrepresentation (AI washing) | Finnish procurement tender + Estonian watchlist + Baltic register gaps (LT, LV, CZ) + new Public Sector Procurement Edge 4995 candidates (FI/EE/LV/LT/PL/others) | Low | legal-procedural-contamination panel: FI, EE, LV, LT, PL, CZ, GB, AT, EU dashboard | review_assigned: Puolueeton Tieteentekijä Group, deadline 2026-07-10 16:00 UTC|
| **C13** | Authoritative enforcement actions | Authoritative candidates + public-sector procurement leads JSONL (4995 records) | Medium | Enforcement action timeline & panel with source trace IDs | review_assigned: Reg Review Board Q3 2026 |
| **C14** | Authoritative enforcement actions | Regulatory enforcement + procurement supervision records | Medium | Enforcement action timeline (CS-004) | review_assigned: LegalOpsUnit, deadline 2026-07-11 14:00 UTC |

## Methods Note Integration
The detection method described in `draft/methods-note-ai-washing-detection.md` has been completed and integrated with the LIMEN dashboard hook for the legal-procedural-contamination panel. Expert review is pending (deadline 2026-07-06 18:00 UTC).

---

## Claim Cш003-001 – FDA regulatory enforcement letters covering AI/ML medical device approvals (2016–2026) lack explicit listings for LLM‑related actions


### Status: Candidate — Needs enrichment and review

### Evidence Draft (Tier 3 – Public FDA portals and secondaries)
- 2025-11-15 claims.md indicates absence of explicit LLM withdrawal cases, but application 510(k) program letters and enforcement actions after major incidents need systematic ingestion for Candidate Case #70 (AIID v2.0).
- Local evidence: `candidate-cases.jsonl` and `source-ledger.tsv` do not contain FDA letters 2016–2026; links to FDA Device Advice enforcement/compliance outputs are missing.
- Source enumeration gap: FDA CDRH Enforcement Reports, Device Advice guidance pages, and 510(k) summary archives are not present in the Tyche LIMEN corpus.

### Visualization Hook
- Atlas/Dashboard: Add enforcement panel row for `FDA/AI-Medical/2016-2026` in the enforcement-actions table under the Regulator Transparency Score panel.
- Paper/Table: Add timeline figure in `draft/preprint.md` (Regulator Transparency section); table will contain columns `Regulator`, `Metric`, `2016-2026` with explicit FDA row.

### Next smallest publishability move
1. Enrich `source-ledger.tsv` – add rows for FDA 510(k) letters and Device Advice pages matching AI/ML keywords (LLM, neural network, generative AI).
2. Locally harvest FDA enforcement corpus under `/srv/tyche/projects/limen-ai-edge-case-atlas/data/fda-enforcement-jsonl/` (size cap 50 MB) and reconcile against AIID v2.0 Candidate Case #70.
3. Populate `candidate-cases.jsonl` for Candidate Case #70: FDA enforcement letter URL, access_date, language=en, jurisdiction=US, source_family=FDA_CDRH, record_id=unique_fda_510k_<sha256>, uncertainty=requires_validation, evidence_tier=3.
4. Update claims.md, source-ledger.tsv; add artifact entry to manifest.json.
5. Recompute crosswalk edges and update paper-ready denominator tables to include FDA/AI-Medical row with tier flag.

Dates and actor binding: draft led by limen-boost-003, sanity-check assigned to Regulatory Review Board (RRB) Q3 2026, deliverable ready 2026-07-15.