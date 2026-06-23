# LIMEN envelope schema validation v0.1

Generated: 2026-06-07T03:17:36Z

## Corpus

- `results/attestation/limen-envelope-examples-v0.1.json`
- `results/attestation/receipt-example-coverage-v0.1.tsv`
- `results/attestation/receipt-field-population-policy-v0.1.tsv`
- `schema/limen-envelope.schema.json`

## Validation results

Positive corpus check:

- LIMEN-ENV-EXAMPLE-0001: PASS
- LIMEN-ENV-EXAMPLE-0002: PASS
- LIMEN-ENV-EXAMPLE-0003: PASS
- LIMEN-ENV-EXAMPLE-0004: PASS
- LIMEN-ENV-EXAMPLE-0005: PASS
- LIMEN-ENV-EXAMPLE-0006: PASS

Negative control checks for the new state-sensitive rules:

- `proof_pending_without_receipt_hash`: FAIL as expected (`receipt_hash` is required)
- `placeholder_signature_without_signature_ref`: FAIL as expected (`signature_ref` is required)
- `issued_vc_without_issuer`: FAIL as expected (`issuer` is required)

## Coverage

- Example 1: authoritative regulator-backed case classification receipt.
- Example 2: multilingual candidate review receipt with translation caution.
- Example 3: reviewed-not-duplicate clustering receipt.
- Example 4: legal/normative crosswalk-row receipt showing bounded Article 50 mapping logic.
- Example 5: dashboard/publication export receipt for the evidence funnel artifact.
- Example 6: publication-bundle receipt with SCITT/VC/signature placeholder fields and explicit non-implementation caution.

## Interpretation boundary

Passing schema validation means the envelope shape is machine-consistent with the profile. The new conditional checks also confirm that stronger publication-state labels cannot omit their minimum identifying fields. None of this implies truth of source allegations, legal validity, compliance, certification, substantive correctness of the underlying case interpretation, or existence of a verified signature, issued credential, or transparency-log inclusion proof unless a concrete receipt instance actually carries and supports those fields.
