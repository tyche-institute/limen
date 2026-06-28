# LIMEN Attestation Envelope Profile v0.1

## 1. Overview
This document defines the evidence-envelope profile for observing, extracting, classifying, reviewing, clustering, and publishing LIMEN cases. It outlines the minimal viable schema for attestation metadata, linking observed data to RATS-style evidence roles and provenance standards (Verifiable Credentials, SCITT, C2PA).

## 2. Non-Claims Disclaimer
The attestation process records *what was observed and processed*; it does **not** determine the truth, legality, safety, compliance, or certification of any source material. Claims about factual veracity or legal validity are out-of-scope.

## 3. Evidence Roles (RATS)
- **Record** – Raw source data (e.g., document, transaction, sensor reading).
- **Assert** – Statement or claim made by the source.
- **Test** – Empirical verification results or benchmark scores.
- **Support** – Mapping of claims to evidence sources, including provenance links.

Each LIMEN case is annotated with one or more RATS roles to facilitate downstream analysis and publication.

## 4. Provenance Standards
### 4.1 Verifiable Credentials (VC)
Metadata about the source (e.g., authoritativeness, jurisdiction) is stored as a VC object, signed by the source or an authorized authority.

### 4.2 SCITT / Transparency Receipts
For public procurement or sandbox interactions, SCITT receipts capture the receipt of a request and the response metadata, enabling audit trails.

### 4.3 C2PA / Content Provenance
Where applicable, C2PA manifests are attached to recorded media (e.g., PDFs, images) to capture creation and modification history.

## 5. Classification Pipeline
1. **Observation Harvest** – Ingest source records from public APIs, databases, or crawls.
2. **Extraction** – Parse structured/unstructured fields; tag language, jurisdiction, script.
3. **Classification** – Assign RATS roles; map to legal/regulatory taxonomies.
4. **Review** – Human or algorithmic validation of classification.
5. **Clustering** – Group similar cases by evidence role, jurisdiction, or standards mapping.
6. **Publication** – Export annotated cases, provenance bundles, and clustering maps.

Each stage outputs immutable artifacts stored under `attestation/` and `results/attestation/`.

## 6. Artifact Manifest
- `attestation/limen-envelope-profile-v0.1.md` – This profile.
- `schema/limen-envelope.schema.json` – Optional JSON schema for validation.
- `results/attestation/status.md` – Operational status and key metrics.
- `journal.md` – Entry summarizing cycle contributions.

## 7. Validation & Governance
- All artifacts are versioned with SHA-256 checksums.
- Changes require review by the project lead (Anton Sokolov) before publication.
- Outputs align with the current publication sprint and manuscript goals.

---  

*Prepared on 2026-06-28 by the LIMEN Attestation Receipt Profile lane.*