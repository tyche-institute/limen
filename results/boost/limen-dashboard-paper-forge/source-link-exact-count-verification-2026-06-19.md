# Source-link exact count verification

Generated: 2026-06-19T06:00:00Z
Lane: limen-dashboard-paper-forge
Sprint: hostile-reviewer pass
Method: live query against public dataset at https://obscure-ai.eatf.eu/data/cases.json

## Result

| Metric | Count |
|--------|-------|
| Total cases in dataset | 296 |
| Evidence-grade cases | 250 |
| Media cases (excluded from evidence-grade) | 46 |
| Evidence-grade with direct URL | 233 |
| Evidence-grade without direct URL | 17 |
| Evidence-grade source-link coverage | 233/250 = 93.2% |
| Media with direct URL | 46/46 = 100% |
| All security/CVE with direct URL | 11/11 = 100% |

## Manuscript patch

F1000 v0.4 `draft/preprint-v0.3-f1000.md` patched:
- §3.7: "at least 232 of 250 (about 93%)" → "233 of 250 (93.2%)"
- §5: "at least 232 (≈93%)" → "233 (93.2%)"
- Record-locator description corrected: "authority, date and instrument" → "issuing authority name and case title"

## 17 cases without direct URL

All 17 are authoritative regulator/court or research-integrity records whose
primary documents are not served at a stable public URL:

| ID | Authority | Tier |
|----|-----------|------|
| LIMEN-AUTH-000001 | Garante (Italy) | T3 |
| LIMEN-AUTH-000002 | U.S. EEOC | T3 |
| LIMEN-AUTH-000003 | UK ICO | T3 |
| LIMEN-AUTH-000004 | UK ICO | T3 |
| LIMEN-AUTH-000005 | U.S. DOJ | T2 |
| LIMEN-AUTH-000006 | U.S. SEC | T3 |
| LIMEN-AUTH-000007 | U.S. SEC | T3 |
| LIMEN-AUTH-000010 | U.S. FTC | T3 |
| LIMEN-AUTH-000011 | U.S. FTC | T3 |
| LIMEN-AUTH-000012 | Datatilsynet (Denmark) | T3 |
| LIMEN-AUTH-000013 | U.S. FTC | T3 |
| LIMEN-AUTH-000014 | U.S. FTC | T3 |
| LIMEN-AUTH-000015 | CNIL (France) | T3 |
| LIMEN-PROC-003 | SAGE Publishing | T2 |
| LIMEN-PROC-004 | NEJM | T3 |
| LIMEN-PROC-005 | Springer | T3 |
| LIMEN-PROC-006 | Springer | T3 |

Distribution: 15 × T3 (regulator/court record), 2 × T2 (contested/interim).
All carry the issuing authority name and descriptive case title in the public
dataset, which together function as a retrieval locator.

## Data-quality note

The 17 cases have empty `source` and `anchor` fields in the public JSON.
Their `authority` and `title` fields are populated and function as implicit
locators. A future dataset version could populate `anchor` with a formal
record locator string (authority + date + instrument type) for each.

## Hostile-reviewer defense

- The count 233 is exact, computed from the live public dataset on 2026-06-19T06:00:00Z.
- It is reproducible: `curl -sL https://obscure-ai.eatf.eu/data/cases.json | python3 -c "..."`.
- No new collection was performed; this is a measurement of the released dataset.
- The manuscript prose now states the exact number rather than a conservative floor.
- The 17 locator-only cases are named by ID and authority, so a reviewer can
  independently verify that each is retrievable.

## D-12 blocker resolution

Status: RESOLVED. The exact source-link count is 233/250 (93.2%).
The conservative "≥232" floor in prior manuscript versions is replaced
with the exact count.
