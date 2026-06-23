## Security Claim-Ceiling Matrix: Evidence-Layer Asymmetry

The current public security package supports a bounded claim about evidence-layer asymmetry: exact external interoperability, remediation visibility, vendor-authored notice depth, source independence, and mechanism coverage still do not move together across the eight seeded rows, so the package is presently strongest as a claim-ceiling, source-role, and publication-routing demonstration rather than as a prevalence or comparative-safety dataset.

### Denominator Class

This claim is bounded to the following denominator: eight authoritative or candidate rows across six platforms, as defined in the shared security package (`results/security/security-agentic-watch-v0.1.tsv`).

### Evidence-Layer Dimensions

Across the eight rows, the following dimensions diverge:

- **Interoperability**: Only one row (Langflow) has exact AVID interoperability; the rest remain negative or indirect.
- **Remediation Visibility**: Three rows (Auto-GPT, Claude Code, LangChain CVE-2026-44843) have vendor-advisory-backed exact fix visibility; two rows (CrewAI) have partial remediation via coordination and release notes; three rows (LangChain, LlamaIndex, Langflow) have no direct vendor bulletin.
- **Notice Depth**: Three rows have vendor-advisory notice; two have third-party coordination notice; one has a repo issue; two have independent-lab advisory.
- **Source Independence**: Two rows (LangChain, LlamaIndex) are backed by independent-lab advisories; the rest rely on vendor or coordination sources.
- **Mechanism Coverage**: The package now spans unsafe code execution (3 rows), exfiltration (3 rows), memory/state contamination (1 row), and identity-boundary abuse (1 row).

### Zero-State Gaps

Two explicit zero-state gaps remain:

- **Peer-reviewed security case support**: No row is backed by a peer-reviewed paper or conference-grade case analysis.
- **Supply-chain or plugin extension**: No row is a clean supply-chain or dependency-trust exemplar.

### Publication Use

This claim supports the manuscript's methods/results section on evidence-layer heterogeneity and the dashboard's security-agentic threshold ladder. It does not support claims about prevalence, completeness, ecosystem maturity, or comparative safety.

### Reviewer Caution

Do not convert this asymmetry into a general security failure claim, a platform ranking, or an implication of widespread vulnerability. The package is strongest as a demonstration of evidence architecture, not as a measure of real-world harm or adoption.