## Dashboard Hook: Identity Verification Flow with Synthetic Identity Risk

** Diagram Key**: 
1. User Authentication Layer
2. Biometric Verification
3. Document Validation
4. AI Content Detection
5. Provenance Chain

**Risk Annotations**:
- **Node 4**: Estonian e-Residency case shows 61% French translation coverage creating authorship ambiguity
- **Node 5**: 3/15 verification sources blocked in Baltic context (blocked-source-ledger.tsv)
- **Edge 2-3**: Synthetic identity risk increases when document validation relies on machine-translated provenance

**Visualization Requirements**:
- Color-code risk levels (green/yellow/red) based on source accessibility
- Include translation coverage percentages in node tooltips
- Link to case `synthetic-identity-EST-001` from node 4