# Live shared release bundle validation v0.9

Updated: 2026-06-08T17:18:00Z
Lane: `limen-attestation-receipt-profile`
Project: `limen-ai-edge-case-atlas`
Validation scope: local published bundle envelope plus manifest/member hash currentness

## What was checked

- Parsed `results/attestation/live-shared-release-bundle-envelope-v0.9.json` successfully as JSON.
- Parsed `schema/limen-envelope.schema.json` successfully as JSON.
- Recomputed the bundle-member hashes recorded in `results/attestation/shared-release-bundle-manifest-v0.9.tsv` across all 8 listed artifacts.
- Compared the new bundle manifest against `results/attestation/shared-release-bundle-manifest-v0.8.tsv` and recorded the per-file drift in `results/attestation/shared-release-bundle-refresh-audit-v0.9.tsv`.

## Result

- The v0.9 shared local publication object is internally consistent as a local currentness receipt: the manifest, refresh audit, and published envelope agree on the same bundle target and non-claim floor.
- Trust posture remains `project_shared_local_bundle_only`.
- No detached signature, transparency receipt, VC issuance, trust-anchor binding, truth, legality, compliance, certification, or safety witness was validated or implied.

## Drift summary versus v0.8

- Changed bundle members: attestation/limen-envelope-profile-v0.1.md, results/attestation/status.md, results/attestation/external-trust-readiness-matrix-v0.1.tsv, dashboard/limen-dashboard-spec-v0.1.md, papers/article-architecture-v0.1.md.
- Unchanged bundle members: schema/limen-envelope.schema.json, results/attestation/limen-attestation-role-crosswalk-v0.1.tsv, draft/preprint.md.

## Paper/thesis use

- Reviewer-facing methods and appendix note for one truthful current local publication object.
- Dashboard/provenance legend source for current local-bundle status without overstating stronger trust surfaces.
