# Double-blind anonymization notes — preprint v0.2

Blind manuscript: `preprint-v0.2-anon.md` → `preprint-v0.2-anon.pdf` (build: `build-preprint-v0.2-anon-pdf.sh`).
Non-blind title page (upload separately): `title-page.md` → `title-page.pdf`.
Source of truth for the public/non-blind version: `preprint-v0.2.md` (DOI 10.5281/zenodo.20700813).

## What was removed / neutralised for the blind copy

| De-anon vector | Public version | Blind version |
|---|---|---|
| Author + affiliation | "Anton Sokolov · Tyche Institute" | removed → "author and affiliation withheld for review" |
| ORCID | 0000-0003-2452-7096 | removed (lives only on the title page) |
| System name | "LIMEN" throughout title, prose, figure title | dropped from title; prose → "the observatory" / "we"; figure title → "Reviewed core: …" |
| Public companion URL | obscure-ai.eatf.eu (+ /data/cases.json) | "a public companion site (URL withheld for blind review)" |
| Figure asset | `figure-reviewed-core-tier-by-theme.png` (title says "LIMEN reviewed-core: …") | `…-anon.png` (title says "Reviewed core: …") |
| Internal provenance section | "Notes for assembly" listing repo paths, v0.1 scaffold, boost-lane | replaced with neutral "Data and code availability" |
| PDF metadata | Author=Anton Sokolov | Author=Anonymous, Title neutral |

## Verification done
- `grep -niE "LIMEN|Sokolov|Tyche|obscure-ai|eatf|ORCID|0000-0003|anton"` on the blind md → clean (only the local build *path* matches, not rendered text).
- `pdftotext preprint-v0.2-anon.pdf | grep …` → no identifying tokens in the rendered PDF.
- `pdfinfo` → Author=Anonymous, Title="Reviewer-safe AI edge-case observatory (blind)".
- Figure 1 re-rendered: no "LIMEN" in the SVG/PNG.

## Residual risk to weigh per venue
- The **public version of record is already public** (Zenodo DOI + obscure-ai.eatf.eu + tyche.institute) under the real name. A determined reviewer who searches a distinctive phrase from the abstract could find it. Double-blind ≠ anonymous-to-search; this only removes *in-document* identifiers. If the target venue forbids any prior public posting, that is a separate editorial question.
- Distinctive phrasings (e.g., "reviewer-safe", "evidence architecture", "denominator classes", "proof ceilings") are reused verbatim from the public version and are searchable. Reword if the venue's blinding policy is strict.
- Cover letter is venue-specific and not yet written (needs journal/editor) — draft once a venue is chosen.
