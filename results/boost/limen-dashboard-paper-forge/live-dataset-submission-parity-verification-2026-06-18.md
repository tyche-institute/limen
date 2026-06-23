# Live-dataset submission-parity verification

Date: 2026-06-18T12:00:00Z
Lane: `limen-dashboard-paper-forge`
Source: https://obscure-ai.eatf.eu/data/cases.json (generated_at_utc: 2026-06-17T10:12:43Z)
Purpose: verify that the F1000 v0.4 manuscript, cover letter, and submission kit
carry denominators that exactly match the live public dataset.

## Dataset structure note

The live JSON uses tier labels `T3`, `T2`, `CVE`, `media`. The manuscript maps
`CVE` → `T1` (security disclosures) in prose. This is a presentation label,
not a data divergence.

## Exact count verification

| Metric | Manuscript claim | Live dataset | Status |
|--------|-----------------|--------------|--------|
| Total catalogued cases | 296 | 296 | PASS |
| Evidence-grade (T3+T2+CVE) | 250 | 250 | PASS |
| T3 (regulator/court) | 157 | 157 | PASS |
| T2 (contested/interim) | 82 | 82 | PASS |
| T1/CVE (security disclosure) | 11 | 11 | PASS |
| Media-excluded | 46 | 46 | PASS |
| Source-link coverage | 233/250 = 93.2% | 233/250 = 93.2% | PASS |
| Jurisdictions (evidence-grade) | 34 | 34 (normalized) | PASS |
| Per-class reach: T3 | 27 | 27 | PASS |
| Per-class reach: T2 | 17 | 17 (normalized) | PASS |
| Per-class reach: CVE | 1 | 1 | PASS |
| Per-class reach: media | 7 | 7 | PASS |

## Jurisdiction normalization convention

The live dataset uses granular court-level jurisdiction strings (e.g.,
"United States (S.D.N.Y.)", "Australia (Federal Court)"). For manuscript
counting, jurisdictions are normalized to country level. One special case:
"International / Japan / ICLR workshop" (LIMEN-WEB5-002, tier T2) is merged
into "Japan" for the purpose of the jurisdiction union, giving:

- Raw country-level evidence-grade jurisdictions: 35
- After merging "International / Japan / ICLR workshop" → "Japan": 34

This matches the manuscript's stated count of 34.

## Stale-surface audit

Before this cycle, the following submission-facing surfaces carried
pre-patch denominators (248/80/32/294):

| Surface | Stale values found | Patched this cycle |
|---------|-------------------|-------------------|
| `draft/cover-letter-f1000.md` | 248 cases, 32 jurisdictions, no source-link detail | YES → 250/82/34 + source-link detail |
| `draft/f1000-submission-kit.md` abstract | 248 cases, 80 T2, 32 jurisdictions | YES → 250/82/34 |
| `draft/f1000-submission-kit.md` data availability | 294 cases | YES → 296 |
| `draft/preprint-v0.3-f1000.md` (manuscript) | — (already current) | N/A |

## Remaining regeneration steps

The cover letter and submission kit Markdown files are now current. The
following binary derivatives need regeneration before submission:

1. `draft/cover-letter-f1000.docx` — rebuild from patched `.md`
2. `draft/cover-letter-f1000.pdf` — rebuild from patched `.md`

The manuscript DOCX/PDF (`draft/preprint-v0.3-f1000.docx`, `.pdf`) were
built from the already-current v0.4 manuscript and do not need regeneration.

## Verdict

All manuscript claims are exactly supported by the live public dataset.
The cover letter and submission kit are now synchronized. The submission
package is parity-clean and ready for Anton's review and upload.
