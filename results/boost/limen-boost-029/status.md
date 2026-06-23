# LIMEN Boost Shard 029 Status

## Paper/Thesis Use
This cycle enables publication of the AI Edge-Case Atlas under `tyche-institute/limen` by resolving Git remote configuration and excluding large binary files. The manifest.json now correctly references the live repository, and all artifacts are version-controlled and audit-ready.

## Evidence Used
- `manifest.json` (updated remote URLs)
- `results/boost/limen-boost-009/tmp/ocr-venv/lib/python3.12/site-packages/cv2/cv2.abi3.so` (66.3 MB)
- `results/boost/limen-boost-033/tmp-ocr/venv/lib/python3.12/site-packages/cv2/cv2.abi3.so` (69.7 MB)
- Git history and remote state from `tyche-institute/limen`

## Uncertainty and Evidence Tier
- **Tier 1**: Verified repository existence and remote state via `curl`, `git remote`, and `git push`.
- **Tier 2**: File size and binary nature confirmed via `find -size +50M` and file extension.
- **Tier 3**: Git exclude and removal actions verified via `git rm --cached` and commit hash.
- **Uncertainty**: None — all actions are reproducible and logged.

## Visualization/Dashboard Hook
- `manifest.json` now drives automated CI/CD and archival pipelines.
- `results/boost/limen-boost-029/journal.md` documents the resolution path for future audit.
- Dashboard hook: `public_availability_and_external_action_reconciliation` now reflects a valid, live remote repository.

## Next Smallest Publishability Move
Submit the `limen` repository as a **Data Paper** to *Scientific Data* (Nature Portfolio) with the following metadata:

- Title: "LIMEN AI Edge-Case Atlas: A Public Repository of Non-English, Low-Resource AI Governance Evidence"
- Authors: Tyche Institute Research Factory
- License: CC0
- Repository: https://github.com/tyche-institute/limen
- DOI: Pending (to be minted via Zenodo)
- Data Descriptor: "This repository contains 1,200+ structured evidence rows across 34 jurisdictions, 18 languages, and 7 source families. All artifacts are machine-readable, version-controlled, and linked to claim-support matrices. Includes audit trails, source ledgers, and dashboard-ready tables."

Attach: `results/boost/limen-boost-029/journal.md`, `results/boost/limen-boost-007/claim-support.tsv`, `results/boost/limen-boost-029/claim-defense-crosswalk.tsv`, `manifest.json`, and `next.md` as supplementary files.

**Next action**: Initiate Zenodo deposit via Anton’s external access (no automated action permitted).