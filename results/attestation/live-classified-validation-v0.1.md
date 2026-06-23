# Live classified receipt validation

Updated: 2026-06-07T07:22:45Z
Lane: `limen-attestation-receipt-profile`

Validation result: pass.

Checked artifacts:
- `results/attestation/live-classified-security-envelope-v0.1.json`
- `results/attestation/live-classified-security-note-v0.1.md`
- `schema/limen-envelope.schema.json`

What this proves:
- LIMEN now has one live `classified` envelope over a real shared case record (`LIMEN-000008`) rather than only example-corpus coverage for case-level classification.
- The receipt stays within the profile's process-only claim scope and points to an already existing downstream reviewer-safe security package.

What this does not prove:
- truth of any underlying allegation or impact example;
- realized credential disclosure, SSRF, or incident occurrence;
- legality, compliance, certification, safety, detached-signature verification, VC issuance, or transparency-log inclusion.
