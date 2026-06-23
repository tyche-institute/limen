# Supplementary Table S1 Specification: Reviewed-Core 248-Case Demonstration

Date: 2026-06-17
Lane: `limen-dashboard-paper-forge`
Source data: `reviewed-core-tier-category-matrix-2026-06-14.tsv`, `reviewed-core-evidence-panel-2026-06-14.tsv`, `reviewed-core-corpus-methods-note-2026-06-14.md`
Manuscript role: Supplementary Table S1 for Route A (Scientific Data / data descriptor)

## Table purpose

Supplementary Table S1 demonstrates that LIMEN's evidence architecture scales
from the governed dashboard surfaces (Figures 1–8, ~39 record references) to a
reviewed-core corpus of 250 evidence-grade cases across 34 jurisdictions while
preserving denominator discipline, tier separation, and per-class claim ceilings.

The table is NOT a completeness claim. It is a worked demonstration that the
observatory architecture produces reviewer-safe, tier-aware, jurisdiction-tagged
case records suitable for bounded article use.

## Table structure

### Panel A: Evidence-tier distribution (summary)

| Tier | Count | Jurisdictions | Share of evidence-grade | Supports | Does not support |
|---|---|---|---|---|---|
| T3: Regulator/court record | 157 | 27 | 63% | Existence of a named action with dated public record | Incident truth beyond record; prevalence; typicality |
| T2: Contested/interim | 82 | 17 | 33% | Matter reached a dated procedural stage | Finding of liability or guilt; final outcome |
| T1: Security disclosure (CVE) | 11 | 1 (global) | 4% | Documented vulnerability anchored to a CVE | Exploitation in the wild; real-world harm; prevalence |
| Excluded: Notable incident (media) | 46 | 7 | — | Widely-reported event per reputable outlets | Any regulator/court finding; evidence-grade status |

Source: `reviewed-core-evidence-panel-2026-06-14.tsv`

### Panel B: Tier × Theme cross-tabulation

| Theme | T3 | T2 | T1 | Media (excluded) | Total |
|---|---|---|---|---|---|
| Legal & procedural | 42 | 4 | 0 | 0 | 46 |
| Surveillance & biometrics | 23 | 13 | 0 | 9 | 45 |
| Deepfakes & synthetic media | 19 | 21 | 0 | 2 | 42 |
| AI-washing & false claims | 16 | 9 | 0 | 6 | 31 |
| Agentic / control failure | 10 | 6 | 0 | 7 | 23 |
| Public sector | 13 | 4 | 0 | 5 | 22 |
| Hiring & education | 10 | 7 | 0 | 4 | 21 |
| Data protection | 11 | 5 | 0 | 0 | 16 |
| Rights & ethics | 4 | 4 | 0 | 7 | 15 |
| Finance & insurance | 6 | 4 | 0 | 3 | 13 |
| Security & agentic | 0 | 0 | 11 | 0 | 11 |
| Chatbot safety & harm | 3 | 3 | 0 | 2 | 8 |
| Institutional absurdity | 0 | 0 | 0 | 1 | 1 |
| **Total** | **157** | **80** | **11** | **46** | **294** |

Evidence-grade subtotal: 248 (T3 + T2 + T1). Media tier excluded from denominator.
Source: `reviewed-core-tier-category-matrix-2026-06-14.tsv`

### Panel C: Jurisdiction coverage (evidence-grade only)

34 national and supranational jurisdictions represented in evidence-grade cases.
Top jurisdictions by T3 count: United States, United Kingdom, Italy, EU (supranational),
France, Germany, Spain, Netherlands, Australia, Canada.

Full jurisdiction list with per-tier counts should be extracted from the
reviewed-core case database and formatted as a supplementary TSV/CSV file.

### Panel D: Temporal coverage

- Evidence-grade range: 2016–2026 (concentrated in 2023–2025 modern AI-enforcement era)
- Media tier historical reach: 2010–2026 (for context only; excluded from denominator)

## Caption (article-ready)

> **Supplementary Table S1.** Reviewed-core demonstration of 250 evidence-grade
> AI edge cases across 34 jurisdictions, organized by evidence tier (T3:
> regulator/court record; T2: contested/interim; T1: security disclosure),
> thematic category, and jurisdiction. The media-tier layer (46 notable
> incidents) is shown for context but excluded from the evidence-grade
> denominator. Each tier supports only bounded claims: T3 supports the
> existence of a dated public action; T2 supports that a matter reached a
> procedural stage; T1 supports a documented CVE-anchored vulnerability. No
> tier supports incident truth, prevalence, legal conclusion, compliance, or
> safety claims. This table demonstrates that LIMEN's evidence architecture
> scales while preserving denominator discipline.

## Hostile-reviewer defense

| Objection | Response |
|---|---|
| "248 is small" | LIMEN does not claim completeness or prevalence. The table demonstrates architecture scalability, not corpus size. |
| "Jurisdiction distribution is uneven" | Explicitly stated in Panel C and §5.4 (Authority imbalance). The uneven distribution is a visibility-surface property, not a prevalence finding. |
| "T2 cases are not findings" | Explicitly stated in the "Does not support" column. T2 supports only procedural-stage visibility. |
| "Media tier is excluded — why show it?" | Media tier provides public-engagement context and shows the exclusion discipline. Including it with explicit exclusion strengthens the denominator-separation argument. |
| "Theme categories are not validated" | Categories derive from the LIMEN taxonomy (§3, Figure 2) which is governed by claims.md:LIMEN-C-016 and the caption-control register. Zero-seed categories are listed as methods guardrails, not findings. |

## Dashboard/paper parity

- Panel A aligns with Figure 5 (evidence funnel) at the publication-safe lineage level.
- Panel B aligns with Figure 2 (taxonomy heatmap) at the category level.
- Panel C aligns with Figure 6 (jurisdiction/language map).
- The 250-case total is a SEPARATE denominator from the dashboard governed-record
  surface (39/29 core). The two are linked by the reviewed-core methods note,
  not by count identity.

## File-format deliverables for submission

| File | Format | Content |
|---|---|---|
| `supplementary-table-s1-panel-a.tsv` | TSV | Evidence-tier distribution |
| `supplementary-table-s1-panel-b.tsv` | TSV | Tier × theme cross-tabulation |
| `supplementary-table-s1-panel-c.tsv` | TSV | Jurisdiction × tier coverage |
| `supplementary-table-s1-caption.txt` | Plain text | Article-ready caption |
| `supplementary-figure-s1.svg` | SVG | Tier-by-theme segmented chart (already exists) |

## Next step

~~Extract per-jurisdiction T3/T2/T1 counts from the reviewed-core case database
and produce Panel C as a standalone TSV.~~ DONE 2026-06-18.
Output: `results/dashboard/supplementary-table-s1-panel-c-jurisdiction-tier.tsv`
(35 data rows: 34 jurisdictions + total). Registered as S15 in SI package.
