# Claim Evidence Mapping - LIMEN Project

## Purpose
This document maps modest sample claims to RATS-style evidence roles, and indicates how each claim can be represented using Verifiable Credentials, SCITT/transparency receipts, and C2PA content provenance where relevant.

## Sample Claim Mappings

| Claim ID | Claim Text | Evidence Role (RATS) | Evidence Tier | Mapping to Standards / Artifacts | Verifiable Credential Type | SCITT / Transparency Receipt | C2PA Provenance |
|----------|------------|----------------------|---------------|----------------------------------|---------------------------|------------------------------|-----------------|
| C1 | Misuse of AI-driven facial recognition in public spaces | **Claim** | Tier 2 (Trusted Third-Party Audit) | Crosswalk to EU AI Act Art. 5 | `Assertion` with `claim_code: AI-FR-MISUSE-001` | Receipt ID `SCITT-2026-06-24-C1` documenting classification step | Provenance hash `C2PA-2026-06-24-C1` for visual map of deployment |
| C2 | Algorithmic bias against minority language processing in automated translation | **Claim** | Tier 3 (Peer-Reviewed Literature) | Crosswalk to OECD AI Principles §1 | `Assertion` with `claim_code: BIAS-LANG-001` | Receipt ID `SCITT-2026-06-24-C2` for review step | Provenance hash for comparative language matrix |
| C3 | Unauthorized data sharing during model fine‑tuning on proprietary datasets | **Claim** | Tier 2 (Trusted Third‑Party Audit) | Crosswalk to ISO/IEC 42001 §8.2 | `Assertion` with `claim_code: DATA-UNAUTH-001` | Receipt ID `SCITT-2026-06-24-C3` for detection step | Provenance hash for dataset lineage diagram |
| C4 | Generation of AI‑generated misinformation targeting EU election narratives | **Claim** | Tier 1 (Authoritative Public Source) | Crosswalk to NIST AI RMF 2023‑04 | `Assertion` with `claim_code: MISINF-EU-001` | Receipt ID `SCITT-2026-06-24-C4` for clustering step | Provenance hash for distribution network map |

| C5 | Non-English jurisdictions and rare languages are systematically underrepresented in AI governance frameworks | **Aggregated Claim** | Tier 2 (Trusted Third-Party Audit) | Crosswalk to EU AI Act Art. 5; link to source evidence | Assertion (placeholder claim_code: UNDREPR-001) | To be minted | To be assigned |
| C6 | AI systems deployed in emerging markets face distinct agentic-control challenges compared to regulated markets | **Aggregated Claim** | Tier 2 (Trusted Third-Party Audit) | Crosswalk to OECD AI Principles §1; link to source evidence | Assertion (placeholder claim_code: EMERG-MARKET-001) | To be minted | To be assigned |
## Evidence Role Definitions (RATS)

- **Source** – Identifier and provenance of the original public record.
- **Claim** – The asserted fact or allegation being examined.
- **Evidence Tier** – Confidence level (Tier 1 = Authoritative Public Source, Tier 2 = Trusted Third‑Party Audit, Tier 3 = Peer‑Reviewed Literature).
- **Processing Step** – Classification, clustering, or review action performed.
- **Verification Flag** – Human‑validated or algorithm‑validated status.

## Integration Points

- **Verifiable Credentials** – Use W3C VC model; each claim maps to a VC of type `Assertion` with a unique `claim_code`.
- **SCITT / Transparency Receipts** – Record each processing step (classification, clustering, review) as a SCITT receipt, enabling audit trails.
- **C2PA** – Attach content‑provenance metadata to derived visualizations (e.g., maps, matrices) to track lineage from raw source to published figure.

> **Note:** These mappings are illustrative. Actual claim IDs, receipt numbers, and provenance hashes will be generated during pipeline execution.