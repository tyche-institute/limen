# LIMEN-000013: Microsoft Playwright MCP Server Origin-header Validation Failure
- **rec_id**: LIMEN-000013
- **theme**: 004 security and agentic-control failures without exploit details
- **category**: supply_chain_or_plugin_extension / mcp_server_trust_boundary
- **paper_use**: supply-chain exemplar for MCP/browser-agent trust-boundary failure with visible fixed-version release note; supports graph/sankey table 1A alternative paths and observatory hooks in table-1A-currentness-regime; provides a bounded security exemplar to lift the package’s supply-chain/plugin-extension zero-state.«

- **authority_note**: Public vulnerability record plus vendor release-note.
  - NVD CVE-2025-9611 text: server before 0.0.40 did not validate Origin header, allowing unauthorized requests to a locally running MCP server via DNS rebinding; public text confirms scope and affected versions.
  - Microsoft Playwright MCP Server v0.0.40 release note states server now adds allowed hosts to mitigate DNS rebinding attack; serves as exact vendor fix narrative below advisories standard.
  - OSV re-iterates the above sources.
  - No CERT/CC or AVID serial IDs yet confirmed; package-state evidence only.

- **sources_needed**: neutral patched-version narrative; interpreter must not claim realized exploitation or generalized MCP prevalence.
  - Tier: T3_authoritative_source (vendor release note) + T1_single_public_source (NVD text) mix as clear mitigation-text bounded exemplar.

- **visualization/dashboard hook**:
  - Table 1A: new candidate `supply_chain_or_plugin_extension / mcp_server_trust_boundary` row linked to LIMEN-000013.
  - Sankey: path from `CVE_tracked_vulnerability` via `vendor_fix_communication_isolation` to `dashboard_verified_patch_version_available`.
  - Static hook doc: `/dashboard/supply-chain-mpc-trust-boundary.md` 1-paragraph summary referencing LIMEN-000013, links, and patch horizon.

- **next**: Locate an incident-specific peer-reviewed security analysis of this MCP case, or add one candidate CVE-specific ATLAS/OWASP join once vendor bulletin formalizes this as a security advisory.
