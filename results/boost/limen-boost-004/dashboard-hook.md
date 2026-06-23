# Dashboard Hook: Security-Agentic Threshold Ladder

**Hook ID:** security-agentic-threshold-ladder-v0.1

**Purpose:** Visualize the bounded evidence-layer asymmetry claim from shard 004.

**Input Source:** `results/boost/limen-boost-004/claim-ceiling-matrix.tsv`

**Visualization Type:** Vertical threshold ladder with authority-balance sidecar.

**Ladder Rows (Core):**
- 1. Core Results (3 rows): Auto-GPT, Claude Code, LangChain CVE-2026-44843
- 2. Appendix Supporting (8 rows): Langflow, CrewAI x2, LangChain, LlamaIndex, PraisonAI, Playwright MCP, ToolHive
- 3. Gap (1 row): Peer-reviewed security case support

**Authority-Balance Sidecar (Default Visible):**
- 21 lineages: vendor-advisory + exact fix (6), coordination + release-note (2), independent-lab + source-qualified (2), MCP/deployment-trust (2), identity-boundary (1), exact AVID join (2)

**Projected Sidecar (for future expansion):**
- 23 lineages: add one peer-reviewed security case, one supply-chain/plugin trust exemplar

**Caption Rule:**
The security-agentic threshold ladder (Figure 7) shows the current public evidence package as a bounded claim-ceiling surface: 3 core rows, 8 appendix rows, and 1 explicit gap. The authority-balance sidecar (default visible 21 lineages, projected 23-lineage sidecar only) reflects source-role diversity, not ecosystem prevalence. No row supports prevalence, compliance, safety, or certification claims.

**Dashboard Field:** `security_threshold_ladder_panel.tsv`

**Linked Artifact:** `results/boost/limen-boost-004/paper-fragment.md`

**Version:** v0.1

**Last Updated:** 2026-06-23T18:45:00Z

**Maintained By:** limen-boost-004

**Note:** This hook must be consumed only by the security section of the manuscript and the dashboard's Route B panel. Do not use for public-facing summary, policy brief, or claim expansion.