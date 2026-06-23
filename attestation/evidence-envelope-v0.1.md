# LIMEN Evidence Envelope v0.1

The LIMEN attestation profile is deliberately modest. It can attest that a
named process observed, hashed, extracted, classified, reviewed, or published a
record. It cannot attest that a case is true, unlawful, compliant,
non-compliant, safe, unsafe, or morally resolved.

## Attestable Claims

- Source URL or local source path was observed at a stated time.
- Source bytes or normalized text produced a stated hash.
- Extractor version, prompt hash, model/tool manifest, and schema version were
  used.
- A case record with a stated hash was emitted.
- A reviewer or lane assigned evidence tier, labels, and crosswalk fields.
- A duplicate-cluster operation used stated inputs and emitted stated outputs.
- A dashboard/publication artifact was generated from stated source records.

## Non-Claims

The envelope must not claim:

- legal compliance or non-compliance;
- official regulatory status;
- certification or audit assurance;
- truth of all source allegations;
- identity of a perpetrator unless already established by authoritative public
  source;
- safety or correctness of an AI system;
- completeness beyond declared source-family coverage.

## Suggested Envelope Fields

```json
{
  "envelope_type": "urn:tyche:limen:evidence-envelope:0.1",
  "run_id": "string",
  "case_id": "LIMEN-000001",
  "action": "observed|extracted|classified|crosswalked|reviewed|clustered|published",
  "timestamp_utc": "2026-06-07T00:00:00Z",
  "actor": "lane-or-reviewer-id",
  "source_ids": ["string"],
  "input_hashes": ["sha256:..."],
  "output_hashes": ["sha256:..."],
  "schema_versions": ["urn:tyche:limen:case:0.1"],
  "tool_manifest_hash": "sha256:...",
  "claim_scope": "observation_and_processing_only",
  "non_claims": [
    "truth",
    "legality",
    "compliance",
    "certification"
  ]
}
```

## Cross-Standard Vocabulary

- RATS-style language can describe attester, evidence, verifier, and
  attestation result.
- Verifiable credentials can carry bounded claims about a record or review.
- SCITT-style transparency can publish supply-chain/integrity receipts for
  record mutation detection.
- C2PA-style content credentials may be relevant for generated media provenance
  cases, but cannot by themselves resolve authenticity or harm.

