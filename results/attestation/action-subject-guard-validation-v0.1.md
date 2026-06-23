# LIMEN action-subject guard validation v0.1

Generated: 2026-06-08T10:03:10Z
Schema: `schema/limen-envelope.schema.json`

## Scope

This audit re-validates the canonical example corpus and the live receipt corpus after adding stricter action-to-subject guards for `observed`, `extracted`, `classified`, and `reviewed` envelopes.

## Result summary

- Rows checked: 19
- Expected outcomes matched: 19/19
- Positive examples/live receipts revalidated: 15
- Negative controls for malformed subject kinds: 4/4 failed as expected

## Interpretation

The updated schema now machine-rejects four previously prose-only overread paths:

1. `observed` receipts pretending to be case-level records;
2. `extracted` receipts pretending to be artifact-level publication objects;
3. `classified` receipts pointing back to raw source objects instead of case/crosswalk outputs;
4. `reviewed` receipts pointing to generic artifacts rather than reviewable case/crosswalk subjects.

This strengthens process legibility only. Passing validation still does not prove source truth, legal validity, compliance, certification, safety, or any external trust witness.
