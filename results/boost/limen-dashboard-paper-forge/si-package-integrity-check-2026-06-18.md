# LIMEN SI package integrity check — dashboard/paper forge

Generated: 2026-06-18T04:26:22Z
Lane: `limen-dashboard-paper-forge`
Project root: `/srv/tyche/projects/limen-ai-edge-case-atlas`

## Scope

This bounded check verifies local SI package traceability for the current LIMEN dashboard/paper package. It does not reopen crawling, change denominators, upload/deposit anything, or strengthen legal/compliance/prevalence claims.

Inputs:

- `results/boost/limen-dashboard-paper-forge/si-package/si-package-manifest.json`
- Manifest-declared dashboard source files (`S1`–`S15`, `Figure-S1`, `Note-1`)
- SI-package Figure 2–8 SVG/PNG files under `results/boost/limen-dashboard-paper-forge/si-package`

## Remediation performed

The first check found two local package-copy blockers: `Figure-S1` and `Note-1` had valid source paths but no same-name copy inside the SI package directory. This cycle copied the two public/local artifacts into the SI package:

- `results/dashboard-paper/figure-reviewed-core-tier-by-theme.svg` -> `results/boost/limen-dashboard-paper-forge/si-package/figure-reviewed-core-tier-by-theme.svg`
- `results/dashboard-paper/caption-control-register-v0.1.tsv` -> `results/boost/limen-dashboard-paper-forge/si-package/caption-control-register-v0.1.tsv`

## Result after remediation

| Check | Result |
|---|---:|
| Manifest objects declared | 17 |
| Missing manifest source paths | 0 |
| Missing packaged copies / expected SI names | 0 |
| Packaged TSV/SVG copy hash mismatches where both sides exist | 0 |
| Required Figure 2–8 image files checked | 14 |
| Missing Figure 2–8 image files | 0 |

## Interpretation

- Evidence/interpretation boundary: this is an artifact-integrity check only. It supports reproducibility and dashboard/paper parity; it does not validate the truth of source allegations or any legal conclusion.
- Paper use: methods/SI reproducibility paragraph; reviewer response for file traceability and checksum availability.
- Dashboard hook: manifest-derived file status card with `object`, `source_path`, `packaged_copy`, `row_count`, `sha256`, and `copy_matches_source` fields.

## Findings needing attention

- No manifest-declared source paths were missing.
- No expected packaged copies were missing under the local naming rule used by this check.
- No source/package hash mismatches were observed where both files exist.
- All checked Figure 2–8 SVG/PNG files exist in the SI package.

## Machine-readable outputs

- `results/boost/limen-dashboard-paper-forge/si-package-integrity-check-2026-06-18.tsv`
- `results/boost/limen-dashboard-paper-forge/si-package-figure-integrity-2026-06-18.tsv`

## Claim ceiling

This strengthens the claim that the current LIMEN article package has a traceable local SI/dashboard file graph. It does not support claims that LIMEN is complete, representative, legally determinative, or externally deposited.

## Next smallest publishability move

Use these two TSVs to build a compact "SI file audit" appendix table and keep any future nonzero missing/mismatch rows as pre-submit blockers.
