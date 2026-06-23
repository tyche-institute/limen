# LIMEN supersession-chain validation v0.1

Generated: 2026-06-08T10:25:17Z
Schema: `schema/limen-envelope.schema.json`

## Scope

This audit re-validates the example and live receipt corpus after adding an explicit `supersession` object for `superseded` envelopes.

## Result summary

- Rows checked: 25
- Expected outcomes matched: 25/25
- Positive example/live receipts revalidated: 21
- Negative controls for malformed supersession lineage: 4/4 failed as expected

## Interpretation

The updated schema now closes one reviewer-visible gap in correction provenance:

1. `superseded` envelopes must expose which earlier receipt they replace;
2. the superseded object must carry a concrete locator plus a hash-bound prior artifact state;
3. the correction reason must stay inside a bounded controlled vocabulary;
4. replacement scope remains process-bounded rather than a general truth or legality upgrade.

This strengthens correction legibility only. Passing validation still does not prove source truth, legal validity, compliance, certification, safety, or any external trust witness.
