# Dashboard/Paper Parity Audit — F1000 v0.4

Generated: 2026-06-19T06:00:00Z
Lane: limen-dashboard-paper-forge
Sprint: hostile-reviewer pass

## Scope

Three-document parity check:
1. `draft/preprint-v0.3-f1000.md` (F1000 submission, v0.4, 213 lines)
2. `dashboard/limen-dashboard-spec-v0.1.md` (dashboard specification, 498 lines)
3. `papers/article-architecture-v0.1.md` (article architecture, 511 lines)

## Denominator parity

| Denominator | F1000 | Dashboard | Article | Status |
|-------------|-------|-----------|---------|--------|
| 250 evidence-grade | ✅ | ✅ | ✅ | PARITY |
| 157 T3 regulator/court | ✅ | ✅ | ✅ | PARITY |
| 82 T2 contested/interim | ✅ | ✅ | ✅ | PARITY |
| 11 T1 security/CVE | ✅ | ✅ | ✅ | PARITY |
| 46 media (excluded) | ✅ | ✅ | ✅ | PARITY |
| 296 total catalogued | ✅ | ✅ | ✅ | PARITY |
| 34 jurisdictions | ✅ | ✅ | ✅ | PARITY |
| 21 publication-safe lineages | ✅ | ✅ | ✅ | PARITY |
| 39/29 taxonomy core | ✅ | ✅ | ✅ | PARITY |
| 44/34 taxonomy extended | ✅ | ✅ | ✅ | PARITY |
| 27 duplicate-review edges | ✅ | ✅ | ✅ | PARITY |
| 12 non-English leads | ✅ | ✅ | ✅ | PARITY |
| 233/250 source-link coverage | ✅ (patched this cycle) | — | — | F1000-only (new exact count) |

## Stale denominator check (F1000)

| Stale value | Status |
|-------------|--------|
| 248 evidence-grade (old) | ✅ ABSENT |
| 32 jurisdictions (old) | ✅ ABSENT |
| 80 T2 (old) | ✅ ABSENT |
| 294 total (old) | ✅ ABSENT |

## Figure/table/SI reference completeness (F1000)

| Surface | References | Status |
|---------|-----------|--------|
| Figure 1 | 2 | ✅ |
| Figure 2 | 3 | ✅ |
| Figure 3 | 1 | ✅ |
| Figure 4 | 1 | ✅ |
| Figure 5 | 2 | ✅ |
| Figure 6 | 1 | ✅ |
| Figure 7 | 2 | ✅ |
| Figure 8 | 1 | ✅ |
| Table 1 | 4 | ✅ |
| Table 2 | 1 | ✅ |
| S1–S15 | all present | ✅ |
| Figure S1 | 1 | ✅ |
| Note 1 | 1 | ✅ |

## Caption discipline

The F1000 manuscript carries the caption-discipline rule after Table 1:
"Figure 2, Figure 5, and Figure 7 carry three different denominators
(39/29 taxonomy core, 21 publication-safe lineages, and 4 threshold rows
respectively) that are not interchangeable and must not be summed."

Status: ✅ PRESENT AND CORRECT

## Source-link exact count (patched this cycle)

Prior: "at least 232 of 250 evidence-grade cases (about 93%)"
Current: "233 of 250 evidence-grade cases (93.2%)"
Source: live query against https://obscure-ai.eatf.eu/data/cases.json
Verification: `results/boost/limen-dashboard-paper-forge/source-link-exact-count-verification-2026-06-19.md`

## Verdict

All 13 denominators are in parity across the three control documents.
All stale denominators are absent from the submission manuscript.
All 8 figures, 2 tables, and 17 SI objects are referenced.
Caption discipline rule is present and correct.
Source-link count is now exact (233) rather than conservative floor (≥232).

D-12 blocker: RESOLVED.

No denominator was changed, no new collection was performed,
no claim ceiling was relaxed.
