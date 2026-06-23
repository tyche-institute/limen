# Reviewer-facing source-family blocker note: sf08, sf09, sf11

Date: 2026-06-17T12:49:19Z
Lane: limen-dashboard-paper-forge
Manuscript slot: Appendix / Limitations companion
Caption-control anchors: CCR-008 (Figure 1), CCR-001 (Figure 2), CCR-015 (Table B), CCR-017 (Table C)
Evidence authority: `results/dashboard/source-family-coverage.tsv`

## Purpose

This note explains to a hostile reviewer why three seeded source families —
sf08 (court and tribunal records), sf09 (public-sector registers and
procurement), and sf11 (security research and advisories) — remain the
principal stronger-source blockers in LIMEN's current package, what each
blocker concretely means for manuscript claims, and what would change if the
blocker were resolved.

## Blocker priority order

The manuscript should present the blocker order as sf08 -> sf09 -> sf11,
reflecting authority depth rather than frequency: court records would most
improve legal-process narration, public-sector registers would most improve
procurement/governance visibility, and peer-reviewed security scholarship
would most improve the technical-scholarly frontier.

## sf08: Court and tribunal records

Current state:
- Seeded and grounded, but court-facing text capture remains the primary gap.
- LIMEN-000002 (EEOC / iTutorGroup) has two official EEOC press summaries but
  no captured court-docket complaint, consent decree, or judicial order text.
- LIMEN-000005 caption metadata normalization remains fragile because the
  live canonical host returns restricted access.
- Reachable PACER/iQuery shells and blocked CourtListener access are not
  treated as court-text substitutes.

What this means for claims:
- The manuscript can narrate agency-to-court procedural posture from EEOC
  summaries but cannot quote complaint language, decree terms, or judicial
  findings.
- Table A (authoritative document-depth facet) correctly shows LIMEN-000002
  at summary-grade depth rather than document-grade.
- No legal-process closure or disposition-language claim is safe for this row.

What would change:
- One genuinely different public court-facing or clearly labeled open-mirror
  complaint/decree/docket/order text for LIMEN-000002, or one materially
  different OCR/public-caption source stabilizing LIMEN-000005 exact caption
  metadata, would promote the affected rows from summary-grade to
  document-grade depth and strengthen the Table A depth-diversity claim.

## sf09: Public-sector registers and procurement

Current state:
- Seeded and grounded, with Amsterdam as the richest exact-row register
  exemplar and Helsinki as the strongest buyer-side continuity row.
- Amsterdam exposes supplier, governance-companion fields, and downloadable
  current/history register exports, but the tested public procurement route
  still shows an exact-name non-hit for ChatAmsterdam and no
  row-specific tender/award/contract/DPIA companion.
- Helsinki has an official same-buyer procurement package with IBM-consistent
  award metadata, but the linkage remains family-level rather than exact
  row-to-contract proof for the parking-chatbot page.
- UK ICO rows (Serco, Chelmer) serve as regulator-document comparators, not
  procurement evidence.
- ORION serves as a low-trace official-project-page floor.

What this means for claims:
- Table B correctly frames the five-row package as disclosure-surface
  heterogeneity rather than procurement completeness or transparency ranking.
- The manuscript cannot claim procurement-chain reconstruction, deployment
  proof, or cross-jurisdiction transparency comparison from this panel.

What would change:
- One static official buyer-side tender/award/contract/DPIA/impact-assessment
  companion tied directly to an Amsterdam register row, or one page-specific
  Helsinki companion explicitly tied to the parking-chatbot row, would
  materially strengthen the procurement-traceability claim and could support
  a stronger Table B reading.

## sf11: Security research and advisories

Current state:
- Seeded and grounded, with AVID and MITRE ATLAS as structured seed-import
  surfaces and multiple vendor/CERT advisories populating the security shard.
- The explicit gap row GAP-peer_reviewed_security_case_support remains open:
  no live seeded row currently carries an incident-specific peer-reviewed,
  workshop-grade, or conference-grade technical case attachment.
- AVID/CERT/vendor/remediation signals, generic agent-security literature,
  and more Langflow/CrewAI notice-depth polishing do not substitute for
  row-specific scholarly closure or broader family balance.

What this means for claims:
- Figure 7 and Table C correctly present the security shard as bounded
  Route B companion material with an explicit scholarly-frontier gap.
- The manuscript cannot claim scholarly consensus, peer-reviewed validation,
  or ecosystem-wide security prevalence from the current package.

What would change:
- One incident-specific peer-reviewed, workshop, or conference-grade technical
  case attachment mapped cleanly to a live seeded row would close the explicit
  GAP row and support a stronger Route B reading. A second bounded
  trust-boundary exemplar or stronger independent attachment would further
  diversify the security evidence base.

## Summary for hostile reviewer

The three blockers are not hidden deficiencies. They are explicitly named in
the manuscript's denominator registry, source-family saturation map (Figure 1),
limitations section, and appendix fragments. Each blocker has:
1. A named exact upgrade trigger;
2. A documented negative-evidence class;
3. A clear statement of what current claims are and are not safe;
4. A caption-control register entry governing figure/table reuse.

The package is publishable with these blockers visible because LIMEN's
contribution is evidence architecture and reviewer-safe observability, not
corpus completeness. A reader who understands the sf08/sf09/sf11 blocker
order can correctly interpret every figure and table in the article without
overreading.
