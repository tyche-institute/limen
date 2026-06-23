# Live superseded receipt validation v0.1

Updated: 2026-06-07T06:48:37Z
Lane: `limen-attestation-receipt-profile`
Project: `limen-ai-edge-case-atlas`
Schema: `schema/limen-envelope.schema.json`

## Validation scope

Validated one live `superseded` receipt over a real local artifact:

1. `results/attestation/live-superseded-status-envelope-v0.1.json`

## Result

- Superseded live receipt: PASS
- Subject: `results/attestation/status.md`

## Interpretation

The current profile now demonstrates a live `superseded` action on a real local LIMEN artifact rather than only describing correction paths in prose. This receipt still attests observation-and-processing steps only. It does not assert allegation truth, legal validity, compliance, certification, safety, signature verification, VC issuance, transparency-log inclusion, or global finality of the replacement artifact.

## Paper/thesis use

This validation note can support a hostile-reviewer appendix claim that LIMEN records bounded provenance corrections to its own package instead of silently overwriting status language.

## Next blocker

The remaining gap is still a shared project-level export workflow or real trust-assurance layer, not basic supersession coverage.
