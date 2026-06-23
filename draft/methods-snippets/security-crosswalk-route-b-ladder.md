# Security Crosswalk and Route B Threshold Ladder — Method Snippet (v0.1)

This snippet documents how LIMEN’s evidence-grade security rows from the 39/29 core are translated into the Route B threshold ladder (Figure 7) and its sidecar-visible authority balance layers used downstream in Supplementary Table S2 (threshold-change logic) and Supplementary Table S3 (authority-balance sidecar consumption).

## Input data sources (v0.8 stable manifest)
- `sources/authoritative-source-ledger.tsv` (security rows with CVE, advisory, or remediation visibility)
- `results/dashboard/taxonomy-heatmap.tsv` (auto-generated governing row keys)
- `results/dashboard/security-threshold-ladder-panel.tsv` (Row B01–B04 state machine snapshot)
- `results/crosswalks/mitre-atlas-crosswalk.tsv` (per-row ATLAS mapping and category labels)

## Security rows promoted to Route B threshold rows (February 16, 2026 stable gate)
- B01: LIMEN-000001 — requires CVE text + vendor advisory depth; achieves authoritative source strength via NVD + advisory confirmation.
- B02: LIMEN-000003 — combines CVE statement with vendor advisory and public tracker reference; accepted upgrade trigger: exact fix visibility + vendored advisory citation.
- B03: LIMEN-000008 — drawn from FCC lifecycle documentation covering allegation-stage to consent decree inclusive; accepted upgrade trigger: full consent-decree citation.
- B04: _gap state guardrail_ — placeholder marking the absence of peer-reviewed security incident-specific study in the current governance corpus; row label: `security_gap_peer_review_needed` until an incident-specific signed study lands.

## Appendix-grade supporting security rows (Security crosswalk Table 5)
- Row keys crossing into Table 5 as interoperability payload:
  - LIMEN-000002 (Langflow RCE) — vendor-issue comment trail + GitHub advisory GHSA-qg33-x2c5-6p44; state: advisory-grade remediation presence confirmed via advisory; prior art ICS pairing: CVE-2024-37014.
  - LIMEN-000004 — advisory witness text, no formal advisory release; state: advisory-grade non-vendor assertion.
  - LIMEN-000005 — coordination-center wording plus downstream CVE-linked fix visibility; state: advisory-grade non-vendor assertion.
  - LIMEN-000006 — independent-lab remediation language; state: advisory-grade independent-lab assertion.
  - LIMEN-000007 — secure-by-default evidence baseline; state: advisory-grade.
  - LIMEN-000009 — downstream MCP trust-boundary exemplar (PraisonAI → Trust Meta); state: trust-boundary slice only, no vendor fix commit.
  - LIMEN-000012 — Playwright MCP OAuth field; state: no clear vendor fix version; advisory-grade placeholder.
  - LIMEN-000016 (ToolHive run-config secret exposure) — supplier advisory GHSA-xj5p-w2v5-fjm6 + NVD CVE-2025-47274 + AVID-2026-R1707 exact mapping to MITRE ATLAS L06:Deployment | S0100:Software Vulnerability; state: vetted vendor advisory + mapped catastrophe domain for taxonomy export; appliance patch hole observed via release tag v0.0.33.

## Procedure to re-export to the dashboard at any time
1. Pull stable manifest from the v0.8 reproducibility capsule.
2. Filter `authoritative-source-ledger.tsv` where `taxonomy_primary = "security_risk"`.
3. Left-join to `crosswalks/mitre-atlas-crosswalk.tsv` on `edge_id` to generate Table 5 schema (DOM structure ready).
4. Run author machine-flag script that tags each row per the Route B rules above and writes `security-threshold-ladder-panel.tsv` with columns: row_key, route_state, threshold_rung (B01–B04), upgrade_trigger_verbatim, upgrade_target_example, atlas_code.
5. Feed `security-threshold-ladder-panel.tsv` + authority-balance sidecar export to the Figure 7 generator; maintain caption: _"only 4 threshold rows; sidecar default visible 21 lineages with projected 23-lineage sidecar only".

## Venue repeatability
The same script and inputs (above) can be cloned into a service-paper companion (e.g., security-threshold variants for LLM-sec contexts) without divergence from the v0.8 reproducibility capsule; only thresholds B01–B04 are designated manuscript-grade in the LIMEN layer, and the gap row remains a guardrail placeholder.
