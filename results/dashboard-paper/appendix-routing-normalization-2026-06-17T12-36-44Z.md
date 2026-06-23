# LIMEN appendix routing normalization

Cycle timestamp (UTC): 2026-06-17T12:36:44Z
Lane id: `limen-dashboard-paper-forge`
Project root: `/srv/tyche/projects/limen-ai-edge-case-atlas`
Sprint posture: hostile-reviewer manuscript-assembly pass; bounded appendix-grade routing normalization; no denominator expansion or corpus growth.

## Purpose

The LIMEN preprint appendix fragments carry 19 unique `results/boost/` path references alongside 9 `results/dashboard/` shared references. This normalization audit maps every boost-local reference to the shared dashboard/dashboard-paper control that already governs it, and adds a shared-control front-door rule to each appendix fragment so that manuscript reuse always checks the caption-control register first.

## Governing inputs

- `draft/preprint.md` (94 lines, 8 appendix/fragment sections)
- `results/dashboard-paper/caption-control-register-v0.1.tsv` (21 CCR rows)
- `results/dashboard-paper/dashboard-paper-figure-route-registry-2026-06-16T23-33-03Z.tsv`
- `results/dashboard-paper/live-export-audit-2026-06-17T10-50-02Z.tsv`
- `results/dashboard-paper/appendix-routing-normalization-2026-06-17T12-36-44Z.tsv` (new)

## Audit result

| Fragment | Boost-local refs | Shared control | CCR rule | Action |
| --- | --- | --- | --- | --- |
| shard 003 authority-depth | 3 | `authoritative-document-depth-facet-v0.1.tsv` + `caption-control-register:CCR-009` | CCR-009 | add shared front door |
| shard 004 security-evidence | 5 | `security-agentic-claim-ceiling-matrix-v0.1.tsv` + `caption-control-register:CCR-017` | CCR-017 | add shared front door |
| shard 007 provenance-confusion | 7 | `caption-control-register:CCR-013` | CCR-013 | add shared front door |
| shard 008 procedural-contamination | 5 | `procedural-contamination-source-depth-panel-v0.1.tsv` + `caption-control-register:CCR-010` | CCR-010 | add shared front door |
| shard 009 AI-washing posture | 1 | `ai-washing-posture-table-v0.1.tsv` + `ai-washing-authority-diversification-panel-v0.1.tsv` + `caption-control-register:CCR-003` | CCR-003 | add shared front door |
| shard 010 taxonomy-routing | 1 | `caption-control-register:CCR-001` | CCR-001 | add shared front door |
| public-sector disclosure | 3 | `public-sector-proof-ceilings-v0.1.tsv` + `caption-control-register:CCR-015` | CCR-015 | add shared front door |
| multilingual readiness | 0 | `caption-control-register:CCR-006, CCR-016` | CCR-006, CCR-016 | already shared-first |

Total boost-local references normalized: 25 (19 unique paths, some referenced in multiple fragments).
Total fragments now carrying shared-control front-door rule: 7 of 8.

## Shared-control front-door rule

For each appendix fragment, manuscript reuse should now follow this order:

1. Check `results/dashboard-paper/caption-control-register-v0.1.tsv` for the governing CCR row.
2. Check the shared `results/dashboard/` export named in that CCR row.
3. Only then descend into the boost-local helper files listed in the CCR `lane_guardrail_source` column.

This rule does not delete or invalidate any boost-local reference. It adds a deterministic shared-control-first check so that:
- caption wording stays synchronized across fragments;
- denominator discipline is inherited from the shared CCR rather than reconstructed from boost prose;
- a hostile reviewer can verify any manuscript sentence against one register rather than 25+ scattered boost files.

## What this cycle did NOT do

- No new corpus material was collected.
- No denominator was changed.
- No figure count or route split was altered.
- No crawling, boost fan-out, or download was launched.
- The normalization is manuscript-governance only.

## Paper-readiness delta

- Every appendix fragment now has an explicit shared-control entry point.
- The 25-row normalization TSV makes the mapping machine-readable.
- The front-door rule is stated once and referenced per fragment.
- Remaining residue: the deeper preprint body still contains inline boost-local prose within each fragment paragraph (not yet rewritten), but the front-door rule now governs reuse order.

## Remaining blockers

1. Full inline rewrite of appendix fragment prose to replace boost-local citations with shared-control-first language (not done this cycle — bounded normalization only).
2. `sf08` court-depth, `sf09` buyer-side, `sf11` peer-reviewed gaps remain unchanged.
3. Route C remains local-bundle provenance only.

## Next smallest publishability move

Apply the front-door rule as inline prose patches to the three heaviest appendix fragments (shard 007, shard 008, shard 004), replacing the boost-local-first sentence structure with shared-control-first language while preserving the bounded claim content.
