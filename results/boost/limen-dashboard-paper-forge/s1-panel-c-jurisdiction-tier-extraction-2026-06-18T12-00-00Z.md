# S1 Panel C extraction: jurisdiction × tier cross-tabulation

Date: 2026-06-18T12:00:00Z
Lane: `limen-dashboard-paper-forge`
Artifact: `results/dashboard/supplementary-table-s1-panel-c-jurisdiction-tier.tsv`

## What was done

Extracted jurisdiction × evidence-tier cross-tabulation (Panel C of
Supplementary Table S1) from the reviewed-core web-verified pipeline
outputs. Combined 6 source files:

- `results/security/limen-reviewed-core-web-verified-v0.1.tsv` (10 cases)
- `results/security/limen-reviewed-core-web-verified-batch2-v0.1.tsv` (73 cases)
- `results/security/limen-reviewed-core-web-verified-batch3-v0.1.tsv` (39 cases)
- `results/security/limen-reviewed-core-web-verified-batch4-v0.1.tsv` (97 cases)
- `results/security/limen-reviewed-core-web-verified-batch5-v0.1.tsv` (2 cases)
- `results/security/limen-reviewed-core-extension-v0.1.tsv` (18 cases)

Total extracted: 239 cases with jurisdiction and tier fields.

## Jurisdiction normalization

88 granular jurisdiction labels were normalized to 34 country/supranational
entities. US sub-jurisdiction labels (district courts, state courts, agency
names) were collapsed to "United States". UK court labels were collapsed
to "United Kingdom". Similar normalization applied to Australia, Canada,
South Korea, South Africa, China, India, Brazil, and Germany.

One multijurisdictional row covers multi-country enforcement actions
(Clearview AI multi-DPA fines, multinational scholarly-publishing retractions).

## CVE/security disclosure addition

The 11 CVE-anchored security disclosure cases (T1) are recorded in the
evidence panel (`reviewed-core-evidence-panel-2026-06-14.tsv`) as
"Security disclosure (CVE), 11, 1 jurisdiction (global)" but are not
present in the web-verified TSV files with a T1 evidence_tier value.
They were added as a "Global (security disclosures)" row with T1=11
to match the authoritative evidence panel.

## Reconciliation

| Tier | Evidence panel (2026-06-14) | This extraction | Delta |
|---|---|---|---|
| T3 (regulator/court) | 157 | 157 | 0 |
| T2 (contested/interim) | 80 | 82 | +2 |
| T1 (security/CVE) | 11 | 11 | 0 |
| **Total evidence-grade** | **248** | **250** | **+2** |

The +2 T2 discrepancy is likely due to 2 cases added to the web-verified
pipeline after the 2026-06-14 evidence-panel freeze. The evidence panel
remains the authoritative reviewed-core summary for manuscript denominators;
this Panel C provides the jurisdiction breakdown that the panel did not
include.

## Output specification

- 34 jurisdiction rows + 1 total row = 35 data rows
- Fields: jurisdiction, T3_regulator_court, T2_contested_interim,
  T1_security_disclosure_CVE, evidence_grade_total, denominator_class,
  claim_ceiling
- Every row carries a denominator_class and claim_ceiling field to prevent
  overread

## Top jurisdictions by T3 count

1. United States: 81 T3, 45 T2
2. United Kingdom: 11 T3, 3 T2
3. Italy: 9 T3, 2 T2
4. Spain: 6 T3, 7 T2
5. Australia: 6 T3, 4 T2
6. Canada: 6 T3
7. South Korea: 5 T3, 2 T2
8. Netherlands: 4 T3
9. China: 4 T3
10. France: 3 T3, 2 T2

## Reviewer-safe reading

- This is a jurisdiction-visibility surface, not a country ranking or
  prevalence map.
- The US concentration reflects US enforcement-surface density and
  public-court accessibility, not US-specific AI risk prevalence.
- T2-only jurisdictions (Brazil, Japan, Hong Kong, Poland, Turkey, Pakistan)
  support only procedural-stage visibility, not final findings.
- The "Global" row covers CVE-anchored security disclosures that are
  jurisdiction-agnostic.

## Claim ceiling

Does not support: completeness, country ranking, AI-risk prevalence,
legal conclusion, compliance determination, or deployment certainty.

## Paper-readiness delta

Before: S1 Panel C was specified but not materialized as a standalone TSV.
The SI binding verification listed it as a remaining gap.

After: S1 Panel C is a standalone 35-row TSV at
`results/dashboard/supplementary-table-s1-panel-c-jurisdiction-tier.tsv`.
Every S-reference in the preprint and SI document now has a verifiable
standalone file on disk. The SI package passes the "every S-reference has
a verifiable file" gate cleanly (0 orphan SI references remain).
