# LIMEN live receipt validation v0.1

Generated: 2026-06-07T03:53:02Z

## Inputs

- `results/attestation/limen-envelope-examples-v0.1.json`
- `results/attestation/receipt-example-coverage-v0.1.tsv`
- `results/attestation/receipt-field-population-policy-v0.1.tsv`
- `schema/limen-envelope.schema.json`

## Outputs

- `results/attestation/live-receipt-field-state-audit-v0.1.tsv`
- `results/attestation/live-envelope-receipt-v0.1.json`

## Validation results

- Live audit row count: 6
- Example receipts re-validated against schema: 6 PASS / 0 FAIL
- Live receipt `LIMEN-ENV-LIVE-0001`: PASS

## Interpretation boundary

The new live receipt is an automatically generated local export artifact. It proves only that the stated local files were read, hashed, summarized into the field-state audit, and wrapped in a schema-valid LIMEN envelope at the recorded time. It does not prove truth of the underlying cases, legal validity, compliance, certification, safety, transparency-log inclusion, VC issuance, or signature verification.
