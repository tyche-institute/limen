# LIMEN attestation action/state validation v0.1

Generated: 2026-06-07T05:39:00Z
Schema: `schema/limen-envelope.schema.json`
Corpus: `results/attestation/limen-envelope-examples-v0.1.json`

## Summary

- Positive examples passing: 6
- Positive examples failing unexpectedly: 0
- Negative controls failing as expected: 9
- Negative controls passing unexpectedly: 0

## Positive example coverage

- `LIMEN-ENV-EXAMPLE-0001`: `classified` / `case_record`
- `LIMEN-ENV-EXAMPLE-0002`: `reviewed` / `case_record`
- `LIMEN-ENV-EXAMPLE-0003`: `clustered` / `duplicate_cluster`
- `LIMEN-ENV-EXAMPLE-0004`: `classified` / `crosswalk_row`
- `LIMEN-ENV-EXAMPLE-0005`: `published` / `artifact`
- `LIMEN-ENV-EXAMPLE-0006`: `published` / `artifact`

## Negative controls exercised

- `NEG-PUBLISHED-WRONG-SUBJECT`: FAIL — Based on LIMEN-ENV-EXAMPLE-0005; subject_ref.kind: 'artifact' was expected
- `NEG-PUBLISHED-NO-OUTPUTS`: FAIL — Based on LIMEN-ENV-EXAMPLE-0005; <root>: 'outputs' is a required property
- `NEG-REVIEWED-MISSING-REVIEW-STATUS`: FAIL — Based on LIMEN-ENV-EXAMPLE-0002; <root>: 'review_status' is a required property
- `NEG-REVIEWED-MISSING-REVIEW-NOTES`: FAIL — Based on LIMEN-ENV-EXAMPLE-0002; <root>: 'review_notes' is a required property
- `NEG-CLUSTERED-ARTIFACT-SUBJECT`: FAIL — Based on LIMEN-ENV-EXAMPLE-0003; subject_ref.kind: 'artifact' is not one of ['duplicate_cluster', 'case_record']
- `NEG-TRANSPARENCY-PROOF-PENDING-NO-RECEIPT-HASH`: FAIL — Based on LIMEN-ENV-EXAMPLE-0006; transparency: 'receipt_hash' is a required property
- `NEG-VC-ISSUED-NO-ISSUER`: FAIL — Based on LIMEN-ENV-EXAMPLE-0006; vc: 'issuer' is a required property
- `NEG-SIGNATURE-PLACEHOLDER-NO-SIGNATURE-REF`: FAIL — Based on LIMEN-ENV-EXAMPLE-0006; signature_placeholders: 'signature_ref' is a required property
- `NEG-SUPERSEDED-WRONG-SUBJECT`: FAIL — Based on LIMEN-ENV-LIVE-0005; subject_ref.kind: 'crosswalk_row' is not one of ['artifact', 'case_record']

## Interpretation boundary

Passing validation means the envelope shape matches the LIMEN profile and its action-sensitive guards. It does not prove allegation truth, legal validity, compliance, certification, safety, signature verification, VC issuance, or transparency-log inclusion unless a concrete receipt instance independently carries and supports those claims.
