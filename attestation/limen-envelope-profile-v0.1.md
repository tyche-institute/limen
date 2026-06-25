# Evidence Envelope Profile for LIMEN Cases (v0.1)

**Purpose**  
This profile describes the observational and attestation workflow for LIMEN edge‑case evidence within the Atlas pipeline. It defines how raw sources are harvested, extracted, classified, clustered, reviewed, and packaged with cryptographic provenance. The profile does **not** assert the truth, legality, safety, compliance, or certification of any source; it only records what was observed and how it was processed.

---

## 1. Scope
- **LIMEN cases**: Publicly available legal or regulatory records that exhibit rare‑language, atypical jurisdiction, or unusual AI‑trust patterns (e.g., Baltic court decisions, Estonian AI‑related rulings).
- **Evidence envelope**: The full chain of custody from raw source to published artifact, annotated with provenance metadata.

---

## 2. Key Concepts
| Term | Meaning |
|------|----------|
| **RATS role** | Verifiable Credential categories (assertion, proof, metadata) used to tag each evidence piece. |
| **SCITT / Transparency receipt** | Cryptographic receipt that links a processed artifact to its source hash and processing timestamp. |
| **C2PA** | Content‑Provenance standard; used to embed provenance hashes into the envelope metadata. |
| **Non‑claim** | Any statement that does not make a verifiable factual claim about the source’s legal or factual status. |

---

## 3. Observation Pipeline
1. **Source Harvesting** – Pull records from public ledgers, court APIs, and multilingual repositories. Language detection tags each record (`lang:ET`, `lang:LV`, etc.).
2. **Extraction** – Parse PDFs/HTML, extract structured fields (case number, jurisdiction, AI‑related clause, outcome). Store as JSON objects under `/data/extracted/`.
3. **Classification** – Apply taxonomy tags (e.g., “AI‑bias”, “procurement‑risk”, “surveillance‑use”) using rule‑based classifiers. Each tag maps to a RATS role (assertion or metadata).

---

## 4. Clustering & Analysis
- **Feature Vector** – Combine language identifier, jurisdiction, taxonomy tags, and extracted keywords into a vector.
- **Clustering Algorithm** – Hierarchical clustering (distance‑based) groups similar cases. Output stored in `/results/clusters/`.
- **Cluster Metadata** – Include cluster ID, representative case, size, and confidence score.

---

## 5. Review & Attestation
1. **Internal Review** – Automated sanity checks; flag records with low confidence or ambiguous taxonomy.
2. **Human Legal Review** – Required for clusters flagged as “high‑impact” or “translation‑dependent”. Review outcome recorded in `review_log.md`.
3. **Cryptographic Envelope** – For each approved record:
   - Compute SHA‑256 hash of the original source.
   - Generate a SCITT receipt linking the hash to the processing timestamp.
   - Embed a C2PA manifest that references the hash and the RATS role.
   - Sign the envelope with the project’s attestation key (stored in `keys/attestation.pem`).

---

## 6. Content Provenance
- Each envelope stores:
  - `source_hash`
  - `extraction_timestamp`
  - `classification_tags`
  - `cluster_id`
  - `review_status`
  - `c2pa_manifest`
  - `scitt_receipt`
- These fields enable downstream tools (e.g., dashboard, citation graph) to trace every artifact back to its origin.

---

## 7. Non‑Claims Statement
All descriptions above record **observable actions** (harvesting, extracting, tagging). They do **not** claim that any case is legally binding, compliant, safe, or certified. No statement should be interpreted as a legal or regulatory endorsement.

---

## 8. Linked Artifacts
- `claims.md` – Claim‑support matrix tied to envelope entries.
- `results/attestation/status.md` – Current status of envelope creation.
- `schema/limen-envelope.schema.json` – Optional JSON schema for validating envelope JSON structure.

---

## 9. Future Work
- Expand provenance to include translation‑confidence scores.
- Integrate automatically with the Atlas dashboard for real‑time envelope visualization.
- Automate multi‑jurisdictional cross‑walks using the envelope metadata.

*Generated on 2026‑06‑26 by the LIMEN Attestation Receipt Profile lane.*