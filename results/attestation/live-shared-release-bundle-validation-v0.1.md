# Live shared release bundle validation v0.1

Generated: 2026-06-07T10:42:51Z
Lane: `limen-attestation-receipt-profile`
Project: `limen-ai-edge-case-atlas`

## Summary

- Created `results/attestation/shared-release-bundle-manifest-v0.1.tsv` as a bounded project-level local bundle manifest spanning attestation, dashboard, article-architecture, and preprint surfaces.
- Created `results/attestation/live-shared-release-bundle-envelope-v0.1.json` as a schema-targeted `published` receipt over that manifest.
- JSON Schema validation: PASS (`schema/limen-envelope.schema.json`).

## Bundle contents

- Bundle member count: 8
- Shared consumer surfaces covered: attestation methods note, dashboard, article architecture, preprint.
- Current trust posture: local shared bundle only; no detached signature, verified transparency receipt, VC issuance, or trust-anchor binding claimed.

## Why this matters

- This is the first explicit project-level local release target that later signature/transparency/VC wiring could attach to without inventing a release surface after the fact.
- The manifest is reviewer-checkable because every listed file has a concrete path and SHA-256 hash.
- The bundle still attests observation and processing provenance only.

## Validator output

```text
VALID
```
