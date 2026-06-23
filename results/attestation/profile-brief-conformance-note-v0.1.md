# LIMEN attestation brief conformance note v0.1

Generated: 2026-06-08T20:30:20Z
Lane: `limen-attestation-receipt-profile`
Project: `limen-ai-edge-case-atlas`
Canonical lane output path: `results/attestation/`

## Scope checked

This note checks the current LIMEN attestation package against the lane brief for:

- `attestation/limen-envelope-profile-v0.1.md`
- optional `schema/limen-envelope.schema.json`
- `results/attestation/status.md`
- short `journal.md` entry
- bounded mapping to RATS-style roles, Verifiable Credentials, SCITT/transparency receipts, and C2PA/content provenance
- explicit non-claims: no truth, legality, safety, compliance, or certification claim

## Conformance summary

| brief item | current artifact | status | reviewer-safe reading |
|---|---|---|---|
| Evidence-envelope profile | `attestation/limen-envelope-profile-v0.1.md` | complete | Canonical profile defines purpose, lifecycle actions, subject model, field semantics, validation rules, and publication/dashboard hooks. |
| Machine-checkable schema | `schema/limen-envelope.schema.json` | complete_optional | JSON parses and enforces action/state-sensitive receipt structure plus the baseline non-claims floor. |
| Status surface | `results/attestation/status.md` | complete | Route-C package state, claim ceiling, current blocker, and next route are recorded in one reviewer-facing status note. |
| RATS-style mapping | `results/attestation/limen-attestation-role-crosswalk-v0.1.tsv` | complete | Uses bounded role analogies only; does not imply hardware-rooted or secure-enclave attestation. |
| VC mapping | `results/attestation/external-trust-readiness-matrix-v0.1.tsv` | bounded_complete | VC is modelled as an optional future portability layer, not a live issued credential. |
| SCITT / transparency mapping | `results/attestation/route-c-readiness-audit-v0.1.tsv` and `results/attestation/external-trust-readiness-matrix-v0.1.tsv` | bounded_complete | Transparency receipt fields are defined, but no live inclusion proof or third-party log witness is claimed. |
| C2PA relevance | `attestation/limen-envelope-profile-v0.1.md` and `results/attestation/envelope-field-role-claim-matrix-v0.1.tsv` | complete | C2PA is treated as optional source-side provenance context for relevant synthetic-media cases only. |
| Explicit non-claims | `attestation/limen-envelope-profile-v0.1.md`, `schema/limen-envelope.schema.json`, `claims.md:LIMEN-C-014` | complete | Package remains limited to observation-and-processing provenance; it does not decide truth, legality, safety, compliance, or certification. |

## Current strongest defensible claim

LIMEN can show machine-checkable observation-and-processing provenance across observed, extracted, classified, reviewed, clustered, published, and superseded actions, plus one active local shared publication bundle at `results/attestation/shared-release-bundle-manifest-v0.10.tsv`, one compact support-artifact index at `results/attestation/profile-support-artifact-index-v0.1.tsv`, and preserved historical snapshots. That supports a narrow methods/provenance companion note, dashboard provenance legend, and thesis appendix routing layer without conflating chronology with the active publication object.

## Current blocked overread

The package still cannot honestly claim:

- detached-signature verification;
- transparency-log inclusion or verified inclusion proof;
- issued VC portability;
- external trust-anchor binding;
- allegation truth;
- legal validity or non-compliance findings;
- safety, certification, or audit assurance.

## Smallest publishability move next

If the attestation route is reopened, prefer one real witness upgrade bound to `results/attestation/shared-release-bundle-manifest-v0.10.tsv` (detached signature or transparency receipt) over more placeholder expansion. Treat `v0.1` through `v0.9` as historical chronology only, keep `v0.10` as the current local publication object unless a later real refresh lands, and refresh `results/attestation/profile-required-output-snapshot-v0.12.tsv` only when one of the required front-door outputs actually changes. If no safe witness material exists, preserve the blocker note rather than widening claims.
