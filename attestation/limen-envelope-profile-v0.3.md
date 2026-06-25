# LIMEN Attestation Envelope Profile v0.3

## Purpose
Define the evidence-envelope profile for LIMEN case observation, extraction, classification, review, clustering, and publication. The envelope records factual processing steps and source metadata without asserting truth, legality, safety, compliance, or certification.

## Scope
- Maps modest claims to RATS-style evidence roles (Record, Assertion, Tag, Summary).
- Links to Verifiable Credentials, SCITT/transparency receipts, and C2PA content provenance where applicable.
- Explicitly separates evidence from interpretation; non-claims are clearly marked.

## Evidence Roles (RATS)
- **Record** – Raw data capture (e.g., source ledger entry).
- **Assertion** – Statement about the record from a primary authority.
- **Tag** – Categorical label for classification.
- **Summary** – Aggregated view linking multiple records to a claim.

Each role includes a unique identifier and provenance metadata.

## Provenance Integration
- **C2PA** – Content‑provenance metadata attached to digital artifacts.
- **Verifiable Credentials** – Issuer‑signed claims about the evidence.
- **SCITT** – Transparency receipts for auditability of the processing pipeline.
- **JSON‑LD** – Structured context for linking evidence roles to external ontologies.

## Crosswalk Frameworks
| Source Family       | AIID | OECD AIPR | MITRE ATLAS | CSET AI Harm | NIST AI RMF |
|---------------------|------|----------|-------------|--------------|-------------|
| Public Registries    | ✅   | ✅       | ❌          | ❌          | ✅         |
| Court Records        | ✅   | ❌       | ✅          | ✅          | ❌         |
| Academic Studies     | ❌   | ✅       | ❌          | ❌          | ❌         |
| Industry Standards   | ❌   | ✅       | ❌          | ❌          | ✅         |
| Media Investigations  | ❌   | ❌       | ❌          | ✅          | ❌         |

## Dashboard Specifications
1. **Evidence Tier Funnel** – Shows progression from raw reports to authoritative tiers; metrics: source count, confidence score distribution.
2. **Geographic Coverage Map** – Country/language breakdown of evidence sources; highlights underserved regions/languages.
3. **Taxonomy Heatmap** – Frequency of edge case categories; time‑series trends.
4. **Duplicate Cluster Graph** – Visualizes redundant reports and sources.
5. **Legal Uncertainty Matrix** – Cross‑tab of jurisdictions vs. AI risk categories; shows gaps in regulatory coverage.

## Claim Mapping and Evidence Roles
- Map modest claims to RATS evidence roles with unique identifiers.
- For each claim, indicate mapping to Verifiable Credential (VC) type Assertion, SCITT receipt ID, and C2PA content hash.
- Clearly mark non‑claim elements as not asserting truth, legality, compliance, or certification.
- Reference the companion `attestation/claim-evidence-mapping.md` for sample mappings and standardization notes.

## Artifacts
- `attestation/limen-envelope-profile-v0.3.md` (this file).
- Optional schema: `schema/limen_envelope.schema.json`.
- Status updates stored in `results/attestation/status.md`.
- Publication‑ready summary in `journal.md`.

*Prepared for the LIMEN attestation receipt profile lane.*