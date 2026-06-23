# Security agentic publication routing note

Created: 2026-06-07T07:22:41Z
Updated: 2026-06-08T18:15:36Z
Lane: `limen-security-agentic-watch`

## Why this artifact exists

The security package already had claim-ceiling, mitigation-visibility, evidence-role, and balance-gap layers, but it still needed one reviewer-facing routing surface that says which rows belong in core results, which belong in appendix/supporting tables, and which state remains an explicit gap rather than a row-level incident claim.

## Main routing result

- `1_core_results`: `LIMEN-000001`, `LIMEN-000003`, and `LIMEN-000008`.
  These remain the cleanest vendor-backed rows with exact fixed-version visibility and can anchor the main security-governance results paragraph and one compact comparison table.
- `2_appendix_supporting_results`: `LIMEN-000002`, `LIMEN-000004`, `LIMEN-000005`, `LIMEN-000006`, `LIMEN-000007`, `LIMEN-000009`, `LIMEN-000012`, and `LIMEN-000016`.
  These rows now cover exact-AVID plus formal-advisory interoperability asymmetry, coordination-plus-CVE-linked exact-fix visibility, independent-lab source-qualified execution cases, identity-boundary abuse, and two MCP/deployment-trust exemplars without pretending those support forms are equivalent.
- `0_gap_only`: `GAP-peer_reviewed_security_case_support`.
  The package still lacks incident-specific peer-reviewed, workshop, or conference-grade technical case support for a live seeded row, so the remaining zero state should stay explicit instead of being buried inside row prose.

## Paper-readiness delta

This converts the current eleven-row security seed plus one explicit gap control into a manuscript-safe routing layer that can feed:

- a core results table on notice depth and exact fix visibility;
- an appendix table on authority-shape asymmetry and mechanism diversity;
- a dashboard facet that separates core rows, appendix/supporting rows, and the still-open scholarly gap without reviving retired limitations-only wording.

## Suggested dashboard fields

`publication_bucket`, `authority_family`, `interoperability_state`, `fix_visibility_state`, `claim_ceiling_now`, `minimum_citation_surface`, `next_smallest_publishability_move`.

## Remaining blocker

The package still has no incident-specific peer-reviewed security case support, still lacks a direct ATLAS same-case join, and still keeps its trust-boundary breadth thin and MCP-specific. This routing layer makes those ceilings easier to show, but it does not solve them.
