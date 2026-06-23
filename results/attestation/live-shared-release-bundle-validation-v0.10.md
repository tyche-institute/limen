# Live shared release bundle validation v0.10

Updated: 2026-06-08T20:42:02Z
Lane: `limen-attestation-receipt-profile`
Project: `limen-ai-edge-case-atlas`
Validation scope: local published bundle envelope plus manifest/member hash currentness

## What was checked

- Parsed `results/attestation/live-shared-release-bundle-envelope-v0.10.json` successfully as JSON.
- Parsed `results/attestation/live-shared-release-bundle-envelope-v0.9.json` successfully as JSON and repaired the stale path-string `supporting_input_refs[]` / `supporting_output_refs[]` encoding so the older live receipt again matches the schema's index-based reference contract.
- Parsed `schema/limen-envelope.schema.json` successfully as JSON.
- Validated both shared-bundle live receipts (`v0.9` and `v0.10`) against `schema/limen-envelope.schema.json` after converting assertion support references back to integer indices, which is the contract already shown in the canonical profile example.
- Recomputed the bundle-member hashes recorded in `results/attestation/shared-release-bundle-manifest-v0.10.tsv` across all 8 listed artifacts.
- Compared the new bundle manifest against `results/attestation/shared-release-bundle-manifest-v0.9.tsv` and recorded the per-file drift in `results/attestation/shared-release-bundle-refresh-audit-v0.10.tsv`.

## Result

- The v0.10 shared local publication object is internally consistent as a local currentness receipt: the manifest, refresh audit, and published envelope agree on the same bundle target and non-claim floor.
- The previously discovered schema/envelope mismatch was a reference-encoding defect in the live shared-bundle receipts, not evidence for any stronger trust layer.
- Trust posture remains `project_shared_local_bundle_only`.
- No detached signature, transparency receipt, VC issuance, trust-anchor binding, truth, legality, compliance, certification, or safety witness was validated or implied.

## Drift summary versus v0.9

- Changed bundle members: `attestation/limen-envelope-profile-v0.1.md`, `results/attestation/status.md`, `results/attestation/external-trust-readiness-matrix-v0.1.tsv`, `dashboard/limen-dashboard-spec-v0.1.md`, `papers/article-architecture-v0.1.md`, `draft/preprint.md`.
- Unchanged bundle members: `schema/limen-envelope.schema.json`, `results/attestation/limen-attestation-role-crosswalk-v0.1.tsv`.

## Paper/thesis use

- Reviewer-facing methods and appendix note for one truthful current local publication object after schema-contract repair.
- Validation appendix and dashboard/provenance legend source for current local-bundle status without overstating stronger trust surfaces.
