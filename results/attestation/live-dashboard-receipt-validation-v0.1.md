# LIMEN live dashboard receipt validation v0.1

Generated: 2026-06-07T04:26:45Z

## Inputs

- `dashboard/limen-dashboard-spec-v0.1.md`
- `results/dashboard-paper/status.md`
- `results/boost/limen-dashboard-paper-forge/duplicate-review-graph.tsv`
- `schema/limen-envelope.schema.json`

## Outputs

- `results/attestation/downstream-dashboard-artifact-audit-v0.1.tsv`
- `results/attestation/live-dashboard-envelope-receipt-v0.1.json`

## Validation results

- Downstream audit row count: 3
- Live dashboard receipt `LIMEN-ENV-LIVE-0002`: PASS
- Schema used: `schema/limen-envelope.schema.json`

## Interpretation boundary

The new live dashboard receipt proves only that the stated local dashboard-package files were read, hashed, summarized into a bounded downstream-artifact audit table, and wrapped in a schema-valid LIMEN envelope at the recorded time. It does not prove truth of underlying cases, duplicate correctness beyond the cited local export state, legal validity, compliance, certification, safety, transparency-log inclusion, VC issuance, or signature verification.
