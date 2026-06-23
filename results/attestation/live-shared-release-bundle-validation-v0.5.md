# Live shared release bundle validation v0.5

Generated: 2026-06-07T23:33:32Z
Lane: `limen-attestation-receipt-profile`
Project: `limen-ai-edge-case-atlas`

## Summary

- Created `results/attestation/shared-release-bundle-manifest-v0.5.tsv` as a refreshed bounded project-level local bundle manifest spanning attestation, dashboard, article-architecture, and preprint surfaces after post-v0.4 shared-surface drift.
- Created `results/attestation/live-shared-release-bundle-envelope-v0.5.json` as a schema-targeted `published` receipt over that refreshed manifest.
- Created `results/attestation/shared-release-bundle-refresh-audit-v0.5.tsv` to show which previously manifested v0.4 bundle members changed before the refresh and which remained stable.
- JSON Schema validation: PASS (`schema/limen-envelope.schema.json`).

## Bundle contents

- Bundle member count: 8
- Shared consumer surfaces covered: article_architecture, attestation_methods_note, dashboard, preprint.
- Members with changed hash versus v0.4: 4
- Members unchanged versus v0.4: 4
- Current trust posture: local shared bundle only; no detached signature, verified transparency receipt, VC issuance, or trust-anchor binding claimed.

## Why this matters

- This refresh converts the post-v0.4 drift finding into a current truthful local publication object rather than leaving Route C anchored to a stale bundle snapshot for active shared surfaces.
- The refreshed manifest remains reviewer-checkable because every listed file has a concrete path and SHA-256 hash.
- The bundle still attests observation and processing provenance only.

## Validator output

```text
VALID
```
