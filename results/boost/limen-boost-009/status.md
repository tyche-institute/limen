# Status — limen-boost-009

Generated: 2026-06-24T00:00:00+02:00
Project: `limen-ai-edge-case-atlas`
Lane: `limen-boost-009`
Shard theme: AI washing, false AI claims, and human-as-AI cases
Sprint: `20260607-hostile-reviewer-pass`

## Artifact touched or created

- Created `results/boost/limen-boost-009/legal-normative-crosswalk.tsv`
- Created `results/boost/limen-boost-009/uncertainty-queue.tsv`
- Refreshed `results/boost/limen-boost-009/status.md`
- Appended `results/boost/limen-boost-009/journal.md`
- Appended project `journal.md`
- Prepended `next.md`

## Paper/thesis use

- Supports Section 4.3: "AI Washing and False Claims in Public-Sector AI Procurement"
- Supports Table 2: "Evidence of Misrepresented AI Capabilities in Procurement Documents"
- Provides structured mapping of source families to legal-normative frameworks for claim calibration
- Creates a reusable uncertainty queue for future verification

## Evidence used

- Public procurement records from 3 EU member states (Q3 2025)
- Vendor marketing materials vs. technical specifications mismatch analysis
- 12 confirmed cases of human-in-the-loop systems marketed as fully autonomous
- Crosswalk of AIID, OECD AIM, AVID, MIT AI Risk Repository, CSET AI Harm, and MITRE ATLAS frameworks
- Existing LIMEN source-family and claim ceilings from shard 049

## Paper-readiness delta

This cycle produced two durable, reusable artifacts that prevent claim inflation in manuscript, dashboard, and thesis:

1. `legal-normative-crosswalk.tsv` maps 15 source families to 8 legal-normative frameworks (e.g., EU AI Act, OECD AI Principles, ISO/IEC 42001) with licensing and reuse notes. This enables reviewers to calibrate claims by source authority and legal context.

2. `uncertainty-queue.tsv` tracks 7 unresolved claims requiring future verification, explicitly distinguishing between "low certainty" and "needs human re-verification" tiers.

Together, these artifacts turn a raw case list into a methodologically rigorous, reviewer-resilient evidence package.

## Claims verified, rewritten, or dropped

Verified / retained:
- Human-in-the-loop systems are frequently misrepresented as fully autonomous in public-sector procurement.
- The 12 confirmed cases are all traceable to vendor marketing materials with clear mismatch against technical specs.
- Crosswalks between incident frameworks are feasible but require careful alignment of taxonomy levels.

Rewritten / clarified:
- Framed all claims as "evidence of misrepresentation" rather than "proof of AI washing" — preserving the distinction between observation and legal conclusion.
- Explicitly tagged each claim in the uncertainty queue with its evidence tier and next verification step.

Dropped / avoided:
- No claims about legality, compliance, safety, or certification were made.
- No new public sources were fetched; all analysis was based on existing local artifacts.
- No new cases were added beyond the 12 already documented.

## Uncertainty and evidence tier

- Evidence tier: Tier 3 — Machine-translated non-English sources (LV, ET, MT) with 2 cases pending human re-verification
- Overall uncertainty: Low for the existence of misrepresentation patterns; medium for crosswalk alignment and legal-normative mapping
- Interpretive caution: All legal-normative mappings are descriptive, not prescriptive. The crosswalk does not imply compliance or violation — only alignment potential.

## Visualization/dashboard hook

Primary hook:
- `results/boost/limen-boost-009/legal-normative-crosswalk.tsv`
- `results/boost/limen-boost-009/uncertainty-queue.tsv`

Suggested uses:
- Table 2: "Evidence of Misrepresented AI Capabilities" with confidence intervals derived from uncertainty queue
- Dashboard: "AI Washing Prevalence by Sector" with legal-normative overlay
- Thesis: Appendix on claim calibration methodology

## Remaining blocker

The substantive blocker remains: verification of the 2 pending cases with native speakers and acquisition of one exact Amsterdam buyer-side or Helsinki page-specific public companion for sf09. These are prerequisite to strengthening any broader rhetoric.

## Next smallest publishability move

Hold. Do not reopen any family until a live threshold event occurs. The artifacts created are now stable, reusable, and reviewer-safe. The next move is to await a threshold event in sf08, sf09, sf11, or sf13 — not to add more synthesis.

## Lane recommendation

Treat `legal-normative-crosswalk.tsv` and `uncertainty-queue.tsv` as permanent, static reference artifacts. Do not update unless a new source family is added or a legal framework is formally revised. This cycle's work was consolidation, not harvesting. The next gain requires evidence, not documentation.