# LIMEN Envelope Profile v0.1

## Purpose
Define the evidence envelope for LIMEN case observation, extraction, classification, review, clustering, and publication. This profile outlines the structure, metadata, and provenance components that make observed cases traceable, auditable, and citable.

## Envelope Components
1. **Header**
   - Case Identifier (unique ID)
   - Observation Timestamp (UTC)
   - Source Reference (URL, document ID, or physical source citation)
   - Language / Jurisdiction
   - Source Authority Score (confidence rating)

2. **Metadata Layer**
   - Extraction Methodology (e.g., crawler, API, manual entry)
   - Classification Tags (taxonomy codes, evidence tiers)
   - Citation Format (APA, IEEE, custom)
   - Rights / Terms of Use (license, public domain, etc.)

3. **Payload**
   - Raw Observation Text (original snippet)
   - Translated Text (if applicable)
   - Annotated Claims (modest claims with traceability links)
   - Supporting Evidence (source excerpts, figures, tables)

4. **Provenance & Receipt**
   - Verifiable Credential (VC) hash linking to source repository
   - SCITT / Transparency Receipt identifier (if available)
   - C2PA Content Provenance manifest (hash chain, signing info)
   - Checksums (SHA-256 of raw and processed files)

5. **Verification Signatures**
   - Digital signature (e.g., PGP, Ed25519) covering header and payload
   - Reviewer endorsement (optional, stored as signed statement)

## Mapping to Evidence Roles (RATS)
- **Observation** → Raw payload entry
- **Verification** → SCITT receipt + signature
- **Attestation** → VC hash + provenance manifest
- **Traceability** → C2PA manifest entries

## Non‑Claims
- The envelope does **not** assert the truth, legality, safety, compliance, or certification of any observed content. It merely records what was observed, how it was processed, and the provenance details.

## Integration Points
- Links to dashboard visualizations (evidence‑tier funnel, jurisdiction map)
- Feeds into taxonomy codebook updates and claim‑support matrices
- Provides structured input for standards‑gap scoring and PKI/trust topology edges

---  
*Generated on `2026-06-23` by the LIMEN Attestation Receipt Profile Lane.*