# LIMEN Boost Shard 044 Status

## Paper/Thesis Use
This shard contributes to the "Security and Agentic-Control Failures" section of the LIMEN paper, specifically supporting Figure 7 (Security/Agentic Threshold Ladder) and Table 5 (Security Evidence Routing). The output feeds directly into the Route B threshold contract and authority-balance sidecar.

## Evidence Used
- LIMEN-000001: FCC consent decree with exact fix language (Tier T1)
- LIMEN-000003: UK regulator matter with direct notice text (Tier T1)
- LIMEN-000008: FCC enforcement lifecycle package (Tier T1)
- LIMEN-000002: Agency-to-court progression with missing court document (Tier T2)
- LIMEN-000004: UK regulator summary + enforcement record (Tier T2)
- LIMEN-000005: Coordination-plus-CVE-linked fix visibility (Tier T2)
- LIMEN-000006: Independent-lab remediation language (Tier T2)
- LIMEN-000007: Bounded identity-boundary exemplar (Tier T2)
- LIMEN-000009: Vendor-advisory-centric non-MCP authorization-boundary row (Tier T2)
- LIMEN-000012: Playwright MCP trust-boundary slice (Tier T2)
- LIMEN-000016: ToolHive trust-boundary slice (Tier T2)
- LIMEN-000017: Gap row for peer-reviewed security case support (Tier T3)

## Uncertainty and Evidence Tier
- Tier T1 (3 rows): Direct, authoritative, fixable evidence with vendor-authored notice depth.
- Tier T2 (8 rows): Reviewed-advisory or source-qualified wording; requires caution.
- Tier T3 (1 row): Explicit gap — no current evidence, only a placeholder for future peer-reviewed case.

## Visualization/Dashboard Hook
- Figure 7: Security/Agentic Threshold Ladder — shows 4 threshold rows (T1) with authority-balance sidecar (21 default / 23 projected).
- Table 5: Security Evidence Routing — maps 12 rows to the threshold ladder and sidecar.
- Dashboard: "Security Threshold" view with toggle for sidecar visibility.

## Next Smallest Publishability Move
Update `results/dashboard/security-threshold-ladder-panel.tsv` and `results/dashboard-paper/figure7-sidecar-consumption-matrix-v0.1.tsv` with the 12-row routing table from this shard, ensuring the sidecar is explicitly captioned as "default visible 21 lineages with projected 23-lineage sidecar only". Then verify that `draft/preprint.md` Section 4.2 and Table 5 reflect this update. Finally, append this shard's journal entry to `journal.md`.