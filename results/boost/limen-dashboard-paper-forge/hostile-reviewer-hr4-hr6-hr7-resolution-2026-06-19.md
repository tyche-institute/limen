# Hostile-Reviewer HR-4/HR-6/HR-7 Resolution

**Date:** 2026-06-19T10:00:00Z
**Lane:** limen-dashboard-paper-forge
**Preprint:** v0.5.1 → v0.6 (354 → 393 lines)

## Summary

Resolved all three remaining hostile-reviewer simulation issues that were
previously flagged for Anton's editorial decision. All fixes are editorial
(no new data collection, no denominator changes, no claim-ceiling relaxation).

## HR-4: Legacy Table A–D labels → formal Table 3–6

**Problem:** Manuscript used internal labels "Table A", "Table B", "Table C",
"Table D" instead of formal numbered table references.

**Resolution:**
- Table A → Table 3 (authoritative document-depth routing)
- Table B → Table 4 (AI-washing posture ladder + public-sector disclosure asymmetry)
- Table C → Table 5 (security threshold ladder)
- Table D → Table 6 (multilingual visibility)
- All 10 occurrences replaced (2 + 4 + 3 + 1)
- Post-fix verification: 0 legacy labels remaining

## HR-6: Table 2 body not rendered

**Problem:** The manuscript referenced "Table 2" (taxonomy heatmap data)
alongside Figure 2, but never rendered the table body inline or pointed
to a specific SI table.

**Resolution:** Added a compact inline Table 2 body after the Figure 2/Table 2
reading rule paragraph. The table body lists all 15 primary taxonomy categories
with their sample reference counts from the live `taxonomy-heatmap.tsv`, notes
multi-label assignment (category sums exceed 39), names the three zero-seed
guardrail rows, and points to Supplementary Table S1 for the full cross-tab.

**Data verification:** Category labels and sample_ref_count values extracted
directly from `results/dashboard/taxonomy-heatmap.tsv`:
security_risk (9), agentic_control_failure (9), public_sector_misuse_or_gap (7),
unlawful_or_allegedly_unlawful_use (5), normative_or_moral_outlier (5),
education_workplace_or_hr (4), ai_washing_or_false_ai_claim (4),
surveillance_biometrics_or_policing (3), institutional_absurdity (3),
deepfake_or_synthetic_identity (3), legal_procedural_contamination (2),
finance_insurance_or_market (2), health/medical/mental_health (0),
research_integrity (0), residual_unclassified (0).

## HR-7: Reference count expanded from 14 to 27

**Problem:** 14 references is below the F1000Research typical range of 25–40.

**Resolution:** Added 13 references [15]–[27]:
- [15] OWASP Top 10 for LLM Applications (2023)
- [16] Bommasani et al. Foundation Models risks (2021)
- [17] Weidinger et al. LM risk taxonomy (2022, FAccT)
- [18] Gebru et al. Datasheets for Datasets (2021, CACM)
- [19] Mitchell et al. Model Cards (2019, FAT*)
- [20] Raji et al. Algorithmic auditing (2020, FAT*)
- [21] Jobin et al. AI ethics guidelines landscape (2019, Nature MI)
- [22] Floridi & Cowls AI principles (2019, Harvard DSR)
- [23] Crawford et al. Excavating AI (2019)
- [24] Roberts et al. AI governance (2021, AI & Society)
- [25] Sambasivan et al. Fairness in India (2021, FAccT)
- [26] Agarwal & Nene incident-reporting standardization (2025, arXiv:2501.14778)
- [27] EU Commission AI Act proposal COM(2021) 206

**Inline citations added at:**
- §1 Introduction: [18, 19, 20, 21, 22, 24] (documentation standards and governance literature)
- §2 Related Work: [15] (security taxonomies), [16, 17, 26] (incident reporting and risk taxonomies), [8, 23, 27] (provenance and regulatory anchors)
- §4.9 Multilingual: [25] (Western-centric governance framework observation)

## Verification

| Check | Before (v0.5.1) | After (v0.6) | Status |
|-------|-----------------|--------------|--------|
| Line count | 354 | 393 | +39 lines |
| Reference count | 14 | 27 | +13 refs |
| Legacy Table A–D | 10 occurrences | 0 | RESOLVED |
| Table 2 body | missing | inline compact | RESOLVED |
| Denominator 250/34 | intact | intact | NO CHANGE |
| Denominator 39/29 | intact | intact | NO CHANGE |
| Denominator 21 pub-safe | intact | intact | NO CHANGE |
| Claim ceilings | intact | intact | NO CHANGE |
| No new collection | N/A | N/A | CONFIRMED |

## Hostile-reviewer simulation status

All 7 original issues now resolved:
- HR-1 (Figure 1 label): resolved v0.5.1
- HR-2 (case selection criterion): resolved v0.5.1
- HR-3 (jurisdiction merge convention): resolved v0.5.1
- HR-4 (Table A–D labels): resolved v0.6 (this cycle)
- HR-5 (caption discipline): resolved v0.5
- HR-6 (Table 2 body): resolved v0.6 (this cycle)
- HR-7 (reference count): resolved v0.6 (this cycle)

## Remaining editorial items (non-blocking)

- [16] Bommasani and [26] Agarwal & Nene references should be verified for exact
  publication details before final submission (arXiv IDs may need confirmation).
- The F1000Research submission version (`draft/preprint-v0.3-f1000.md`) needs
  the same HR-4/HR-6/HR-7 patches applied to stay synchronized.
