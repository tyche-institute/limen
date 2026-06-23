## Dashboard Hook: Security-Agentic Threshold Ladder and Authority-Balance Sidecar

### Purpose

To visualize the bounded evidence-layer asymmetry claim from the security claim-ceiling matrix (paper-fragment.md) as a threshold ladder and authority-balance sidecar.

### Data Source

- Primary: `results/security/security-agentic-watch-v0.1.tsv`
- Supporting: `results/boost/limen-boost-004/claim-support.tsv`, `results/boost/limen-boost-004/source-authority-balance.tsv`

### Visualization Components

1. **Threshold Ladder (4 rows)**
   - **Tier 1**: Core results (3 rows) — Auto-GPT, Claude Code, LangChain CVE-2026-44843 — with vendor-advisory-backed exact fix visibility.
   - **Tier 2**: Appendix-supporting results (4 rows) — CrewAI (2), LangChain, LlamaIndex — with partial remediation or independent-lab support.
   - **Tier 3**: Limitations queue (1 row) — Langflow — with exact AVID interoperability but no remediation authority.
   - **Tier 4**: Zero-state gap — peer-reviewed security case support — empty.

2. **Authority-Balance Sidecar (default 21 lineages, projected 23)**
   - **Vendor-advisory**: 3 platforms (Auto-GPT, Claude Code, LangChain)
   - **Independent-lab**: 2 platforms (LangChain, LlamaIndex)
   - **Coordination notice**: 1 platform (CrewAI)
   - **Exact AVID join**: 1 row (Langflow)
   - **Supply-chain/plugin extension**: 0 rows — explicit gap
   - **Peer-reviewed support**: 0 rows — explicit gap

### Interpretation

- The ladder shows evidence maturity diverges across dimensions, not across platforms.
- The sidecar shows authority is concentrated in vendor advisories and independent-lab sources, with no supply-chain or scholarly support.
- The zero-state gaps are visible as empty slots, not as missing data.

### Caption Rule

"Security-agentic threshold ladder (Figure 7) shows four tiers of evidence maturity; authority-balance sidecar (default visible 21 lineages, projected 23-lineage sidecar only) shows distribution across authority types. Zero-state gaps remain explicit. This is not a prevalence or safety claim."

### Next Step

Integrate this hook into the dashboard's security-agentic panel and align the figure caption with the manuscript's claim-ceiling matrix.