# Source-Family Saturation Status - LIMEN Boost Shard 001

## Overview
This report summarizes the current saturation status of source families as recorded in `source-family-coverage.tsv`. Last updated: 2026-06-25.

## Source Family Status Matrix
| family_id | source_family | priority | saturation_state | dashboard_readiness | next_verification_move |
|------------|---------------|----------|------------------|----------------------|------------------------|
| sf01      | AI Incident Database (AIID) | P0 | seeded | grounded_now | Verify one snapshot-manifest or single-record machine-readable extraction that ties public page labels to field names without broad harvesting |
| sf02      | OECD AI Incidents Monitor (OECD AIM) | P0 | seeded | grounded_now | Trace one public detail page back to a stable list/discovery route and document the minimal safe metadata subset |
| sf03      | AI Vulnerability Database (AVID) | P0 | seeded | grounded_now | Treat the current AVID appendix as the reviewer-safe control surface |
| sf04      | MITRE ATLAS | P0 | seeded | grounded_now | Treat the current ATLAS appendix as the reviewer-safe control surface |
| sf05      | MIT AI Risk Repository | P0 | seeded | grounded_now | Extract one compact manual risk-category bridge for the most used LIMEN harm labels |
| sf06      | CSET AI Harm taxonomy | P1 | seeded | grounded_now | Keep the family explicitly outside machine-ingest claims and add a second low-drift reviewer pass |
| sf07      | Regulator and enforcement sources | P0 | seeded | grounded_now | Add one non-U.S./non-UK follow-through row tied to a public record |
| sf08      | Court and tribunal records | P0 | seeded | grounded_now | Reopen only if one genuinely different public court-facing route appears |
| sf09      | Public-sector registers and procurement | P1 | seeded | grounded_now | Prefer Amsterdam only where a genuinely different static official route is plausible |
| sf10      | Company and platform notices | P1 | seeded | grounded_now | Verify missing direct vendor remediation details for Langflow and CrewAI |
| sf11      | Security research and advisories | P1 | seeded | grounded_now | Exploit an existing seeded row first for peer-reviewed closure |
| sf12      | Reputable multilingual media | P1 | seeded | grounded_now | Resolve one additional direct source from Baltic region |
| sf13      | Academic and research-integrity sources | P1 | seeded | grounded_now | Prefer a live/direct SAGE notice-text recovery |
| sf14      | Social and web lead sources | P2 | planned | planned_not_seeded | Use governed LinkedIn lead as control surface |
| sf15      | Creative/absurd and normative outliers | P2 | planned | planned_not_seeded | Use governed residual row as control surface |

## Next Steps
1. Prioritize verification moves for P0/P1 families (sf01-sf13)
2. Continue expanding Baltic region coverage (sf12)
3. Monitor frontier families (sf14-sf15) for governance-grade upgrade candidates
4. Update dashboard with current saturation metrics

## Publication Hooks
- Figure 1: Source-family saturation map
- Table 2: Evidence-tier assignments and authority profiles
- Appendix: Source-family route impact matrix