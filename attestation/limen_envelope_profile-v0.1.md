# LIMEN Attestation Envelope Profile v0.1

## Purpose
Define the evidence‑envelope profile for LIMEN case observation, extraction, classification, review, clustering, and publication. Records what was observed and processed, linking each artifact to provenance metadata. Does not make truth, legal, safety, compliance, or certification claims.

## Scope
- **Observational focus**: Capture observations in the LIMEN workflow (source IDs, extraction timestamps, classification outcomes, etc.).
- **Non‑claims**: No adjudication of veracity, legality, safety, compliance, or certification status.
- **Provenance**: Link all observations to source provenance (URL, access date, language, jurisdiction, rights/terms notes).

## Evidence Roles (RATS‑style)
- **Raw Observation** – Unprocessed data (e.g., PDF text, API response).
- **Processed Record** – Structured record after extraction (e.g., JSON instance).
- **Evidence Link** – Mapping to supporting artifacts (verifiable credentials, SCITT receipts, C2PA provenance).
- **Attestation Statement** – Signed assertion of the extraction process, decoupled from substantive truth claims.

## Mapping to Standards
- **Verifiable Credentials (VCs)**: Wrap Processed Records in VCs, preserving source metadata and providing cryptographic proof of extraction.
- **SCITT / Transparency Receipts**: Attach a transparency receipt to each artifact for public auditability of the extraction pipeline.
- **C2PA Content Provenance**: Record chain‑of‑custody metadata for digital artifacts (PDF, image, dataset) using C2PA standards.
- **Signature & Proof**: Include a placeholder for cryptographic signature (e.g., Ed25519) to bind the attestation statement to the processor.

## Non‑Claims
- No assertion is made regarding correctness, legal standing, or regulatory compliance of observed content.
- Language, jurisdiction, or source‑authority metadata are descriptive only (e.g., “language: Estonian (et)”) and carry no evaluative weight.
- Uncertainty is explicitly recorded (confidence scores, source‑authority levels, notes).

## Artifact Checklist
- `attestation/limen-envelope-profile-v0.1.md` – This profile.
- `schema/limen-envelope.schema.json` – JSON schema for envelope structure.
- `results/attestation/status.md` – Status log for this profiling effort.
- Short entry in `journal.md` indicating completion.

## Usage Example
```json
{
  "observation_id": "obs-2026-06-24-001",
  "source": {
    "url": "https://example.gov/regulation/xyz",
    "accessed_utc": "2026-06-24T12:34:56Z",
    "language": "et",
    "jurisdiction": "EE"
  },
  "evidence_role": "Processed Record",
  "vc_mapping": {
    "credential_status": "Revoked",
    "issuer": "Eesti Idrahaldus"
  },
  "receipt_type": "SCITT",
  "c2pa_provenance": "c2pa-v1.0:...",
  "uncertainty": {
    "confidence": 0.87,
    "notes": "Machine‑translated from Estonian; translation confidence medium."
  }
}
```

*This example shows a minimal envelope that can be serialized to JSON, signed, and attached to a Verifiable Credential.*