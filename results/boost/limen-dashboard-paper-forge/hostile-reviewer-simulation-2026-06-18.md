# LIMEN Hostile-Reviewer Simulation — Cycle 2026-06-18T18:00:00Z

Lane: `limen-dashboard-paper-forge`
Target: `draft/preprint.md` v0.5, F1000Research Method Article
Reviewer persona: senior AI governance researcher familiar with AIID, OECD AIM, MITRE ATLAS

---

## Reviewer Summary

The manuscript presents an evidence-architecture contribution for AI edge-case
research rather than a corpus-completeness claim. The denominator discipline,
source-family governance, and explicit claim ceilings are methodologically
serious. However, several manuscript-internal inconsistencies and missing
definitions would need resolution before I could recommend acceptance.

---

## Major Issues (must fix before acceptance)

### HR-1: Figure 1 label inconsistency

**Location:** §3 line 135 vs §3.1 line 156
**Problem:** Line 135 calls Figure 1 a "source-boundary map" while line 156
calls it a "source-family saturation map". These are different terms and a
reader cannot determine which is canonical.
**Fix:** Standardize to "source-family saturation map" (the term used in the
figure-route registry and dashboard spec).
**Status:** PATCHED this cycle.

### HR-2: 250/296 case selection criterion absent from Methods

**Location:** §3 (Observatory Architecture and Methods)
**Problem:** The abstract states "250 cases across 34 jurisdictions" but §3
never explains why 250 of 296 total cases constitute the "reviewed core".
A reviewer would immediately ask: were 46 cases excluded? On what basis?
**Fix:** Add one sentence to §3 stating that 250 evidence-grade cases (T1–T3)
form the reviewed core, while 46 media-only cases are excluded from
evidence-grade denominators because they lack direct regulator, court,
security-disclosure, or institutional authority.
**Status:** PATCHED this cycle.

### HR-3: Jurisdiction merge convention unstated

**Location:** §4.9 line 230
**Problem:** The manuscript states "34 country or supranational jurisdictions"
but the raw dataset has 35 unique jurisdiction labels. The merge convention
("International / Japan / ICLR workshop" → Japan) is not explained.
**Fix:** Add a brief parenthetical explaining the normalization convention.
**Status:** PATCHED this cycle.

### HR-4: Tables A–D use legacy labels, not formal manuscript table numbers

**Location:** §4.1 (Table A), §4.6/4.8 (Table B), §4.2/4.4 (Table C), §4.9 (Table D)
**Problem:** The manuscript references four tables using informal labels (A, B,
C, D) that are not registered in the denominator registry (Table 1) and not
cross-referenced to supplementary table numbers. A F1000Research reviewer
would expect either proper manuscript table numbers (Tables 3–6) or explicit
supplementary-table references.
**Risk level:** MEDIUM. These tables appear to be conceptual panels described
in prose rather than rendered table objects. If they exist as rendered tables
in the SI, the manuscript should state their S-numbers. If they are prose-only
descriptions, the labels should be clarified as "panel" or "sidecar" rather
than "Table".
**Fix:** Not auto-patched (requires editorial decision). Recommended: replace
"Table A" → "Authoritative routing panel (Supplementary Table S1)", "Table B"
→ "Public-sector and AI-washing asymmetry panel (Supplementary Tables S13–S14)",
"Table C" → "Security threshold panel (Supplementary Table S5, Figure 7)",
"Table D" → "Multilingual visibility panel (Supplementary Table S15, Figure 6)".
**Status:** FLAGGED for Anton's editorial decision.

---

## Minor Issues (should fix)

### HR-5: "Reviewed-core" methodology undefined

**Location:** §3 and throughout §4
**Problem:** The term "reviewed core" appears multiple times but the manuscript
never defines what review process was applied. Was it human curation, automated
filtering, or a combination? What were the inclusion/exclusion criteria?
**Fix:** Add one sentence to §3 defining the reviewed-core process: cases pass
through duplicate governance, source-authority scoring, evidence-tier assignment
(T1/T2/T3), and provenance verification before entering the reviewed core.
**Status:** PARTIALLY PATCHED this cycle (selection criterion added; full
methodology description deferred to SI Note 1).

### HR-6: Table 2 body not rendered in manuscript

**Location:** Table 1 (denominator registry) references Table 2
**Problem:** Table 2 is listed as the "taxonomy data companion to Figure 2" but
its body never appears in the manuscript. A reviewer would ask where to find it.
**Fix:** Either render Table 2 inline or add an explicit pointer: "Table 2 data
is provided as Supplementary Table S1 Panel A (taxonomy distribution)."
**Status:** FLAGGED for Anton's editorial decision.

### HR-7: Only 14 references for a methods/data paper

**Problem:** F1000Research method articles typically cite 25–40 references.
The current 14 are all directly relevant but miss key adjacent literature:
- No citation for the FAIR data principles (Wilkinson et al. 2016)
- No citation for systematic review methodology
- No citation for evidence-hierarchy frameworks in policy research
- No citation for AI governance survey literature (e.g., Jobin et al. 2019,
  mapping global AI governance)
**Risk level:** LOW. The 14 references are sufficient for the contribution
claim, but a reviewer may request broader context.
**Status:** FLAGGED for Anton's editorial decision.

---

## Strengths (would note positively)

1. Denominator discipline is genuinely novel — no existing AI incident database
   makes its denominator classes this explicit.
2. The limitations section is unusually honest and specific.
3. The evidence-tier funnel (Figure 5) and source-family saturation map
   (Figure 1) are immediately useful for other researchers.
4. The three-observatory bridge positioning (GAIA/PALLAS/LIMEN) is clear
   without overclaiming.
5. The claim-boundary language is consistently cautious.

---

## Verification Against Live Dataset

Queried: https://obscure-ai.eatf.eu/data/cases.json
Generated: 2026-06-17T10:12:43Z

| Claim | Manuscript value | Live data | Match |
|-------|-----------------|-----------|-------|
| Total cases | 296 | 296 | ✅ |
| Evidence-grade cases | 250 | 250 | ✅ |
| T3 (Regulator/court) | 157 | 157 | ✅ |
| T2 (Contested/interim) | 82 | 82 | ✅ |
| T1/CVE (Security) | 11 | 11 | ✅ |
| Media-only | 46 | 46 | ✅ |
| Jurisdictions (after merge) | 34 | 35 raw → 34 merged | ✅ |
| Source links (evidence-grade) | 233/250 (93.2%) | 233 | ✅ |
| Year span | not stated | 2016–2026 | N/A |
| Cases with year | not stated | 268/296 | N/A |

All 8 denominator claims verified exact.

---

## Recommendation

**Minor revision.** The contribution is methodologically serious and the
denominator discipline fills a genuine gap. The four major issues (HR-1
through HR-4) are editorial, not substantive. Once resolved, the manuscript
should be acceptable as a F1000Research Method Article.

---

## Patches Applied This Cycle

1. HR-1: Standardized "source-boundary map" → "source-family saturation map" (line 135)
2. HR-2: Added 250/296 selection criterion sentence to §3
3. HR-3: Added jurisdiction merge convention parenthetical to §4.9
4. HR-5: Partial — added selection definition to §3

## Issues Flagged for Anton

1. HR-4: Tables A–D legacy label decision (replace with S-numbers or renumber?)
2. HR-6: Table 2 body rendering decision (inline or explicit SI pointer?)
3. HR-7: Optional reference expansion (4–6 additional citations)
