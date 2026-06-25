# LIMEN Evidence Envelope Profile v0.1

## Objective
This profile defines the structure and process for collecting, verifying, and classifying AI edge cases and negative observations while maintaining provenance and avoiding claims of truth, legality, or compliance.

## Evidence Handling
1. **Attestation Scope**: Records what was observed in public sources without asserting validity.
2. **Provenance**: Capture source URL, access timestamp (UTC), language, jurisdiction, and source family (e.g., 'regulatory', 'incident-report', 'research').
3. **Classification**: Use non-judgmental tags like `unintended-consequence`, `boundary-case`, `security-risk`, `ambiguous-compliance`, or `norm-violation`.

## Schema (Optional)
[JSON Schema](schema/limen-envelope.schema.json) defines:
- `source` (object with url, accessed_utc, language, jurisdiction)
- `classification` (array of tags)
- `observation` (text excerpt with context)
- `review_status` (pending/verified/dropped)
- `related_claims` (array of claim IDs)

## Publication Readiness
- **Weak Claims Policy**: Any assertion in manuscripts must link to at least two verified evidence envelopes.
- **Figure 2/5 Parity**: All dashboard figures must have corresponding paper descriptions and vice versa.
- **Limitation Statement**: Include a limitation note in every manuscript section using LIMEN data.

## Boundaries
1. No truth claims about source allegations
2. No legal compliance assessments
3. No safety/test certification statements
4. No machine-translated legal conclusions
5. No fused denominator assertions (GAIA/PALLAS/LIMEN remain separate)

## Review Process
1. Initial triage: automated schema validation
2. Source verification: check URL accessibility and language metadata
3. Classification review: ensure tags are descriptive, not evaluative
4. Claim linking: verify evidence-envelope-to-claim connections
