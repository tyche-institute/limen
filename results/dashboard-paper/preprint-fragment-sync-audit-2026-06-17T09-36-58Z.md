# LIMEN preprint fragment synchronization audit

Timestamp (UTC): 2026-06-17T09:36:58Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`
Source file audited: `draft/preprint.md`
Sprint posture: hostile-reviewer manuscript-assembly pass; no new crawling; dashboard/paper parity only.

## Why this audit exists

The current dashboard spec and article architecture already expose the live figure/table contract, denominator classes, and blocked overreads. The remaining manuscript-facing risk is that `draft/preprint.md` still mixes that shared front door with older shard-local fragments and boost-local routing bundles. This audit records that mixture as a bounded synchronization blocker rather than silently treating the manuscript as fully normalized.

## Audit method

Reviewed `draft/preprint.md` after re-checking:
- `/etc/tyche-factory/current-publication-sprint.md`
- `publication-goal-card-current.md`
- `/srv/tyche/athena/memory-transfer/20260608-athena-codex-memory/ATHENA-CODEX-MEMORY-TRANSFER-2026-06-08.md`
- `/srv/tyche/shared/status/gaia-pallas-limen-stabilization.md`
- `dashboard/limen-dashboard-spec-v0.1.md`
- `papers/article-architecture-v0.1.md`
- `results/dashboard-paper/status.md`

Target question: does the manuscript front door now route through the live shared dashboard bundle, or do shard-local fragments still create slot-number or authority-balance drift risk?

## Main finding

`draft/preprint.md` is synchronized at the front door, but not yet fully normalized downstream.

What is already synchronized:
- the preprint points to `results/dashboard-paper/live-export-audit-2026-06-17T08-56-03Z.tsv`;
- it names the live Figure 2 core (`39 governed record refs / 29 unique lineages`), Figure 2 extended (`44 / 34`), Figure 5 (`21 publication-safe lineages`), and Figure 7 (`4 threshold rows`) contracts;
- it carries the shared no-fused-denominator rule.

What still remains mixed:
- 6 shard-fragment headings remain in the manuscript body (`Shard 003`, `004`, `007`, `008`, `009`, `010`);
- the file still cites 47 unique `results/boost/...` bundle paths;
- 14 `Table 1*` references remain alongside 3 `Table 6*` references;
- these older table-slot labels coexist with the live shared figure/table registry, which raises drift risk when captions or reviewer-response prose are reused.

## Fragment inventory

| Fragment / section | Main live role now | Residual drift signal | Immediate interpretation |
| --- | --- | --- | --- |
| `Shard 003 framing fragment` | authoritative source-depth / anchor routing support | references `Table 1A`, `Figure 8`, and `Table 6`-adjacent prose via boost-local routers | useful evidence-architecture note, but slot naming is not yet fully aligned to the live article bundle |
| `Shard 004 framing fragment` | bounded Route B security-governance asymmetry prose | no direct caption-control anchor in the fragment itself | semantically useful, but still reads like lane-local prose rather than shared manuscript object text |
| `Shard 007 framing fragment` | provenance-confusion and governance-asymmetry fragment | uses `Table 1F` and boost-local panel contracts | publishable as bounded sidecar logic, but still tied to shard-local travel kits |
| `Shard 008 framing fragment` | procedural-contamination / research-integrity source-depth panel | uses `Table 1E` and live `CCR-010`, but still keeps boost-local manuscript slot references | closest to shared-panel normalization, yet still not fully reduced to the shared panel grammar |
| `Shard 009 framing fragment` | AI-washing posture ladder | uses `Table 1C` prose without explicit shared front-door restatement | mostly stable content, but needs live-slot reconciliation |
| `Shard 010 framing fragment` | taxonomy-routing / residual-category argument | still references staged mechanical `35 / 27` provenance alongside live `39 / 29` and mentions `Table 6`-family reuse | useful caution surface, but most exposed to slot-number and denominator-overload drift |
| `Public-sector disclosure asymmetry fragment` | shared `sf09` methods/results note | uses `Table 1B`, `CCR-015`, and 12 boost-local support paths | content remains strong, but the routing stack is too boost-heavy for a clean preprint front door |
| `Multilingual readiness fragment` | shared Figure 6 / Table 1D multilingual note | uses `CCR-006`, `CCR-016`, and boost-local publication cells | strong bounded fragment, but still partly lane-local in packaging |

## Reviewer-safe blocker register

1. Slot-label drift
   - Live architecture uses the shared Figure 1-8 / Table A-C bundle.
   - `draft/preprint.md` still contains `Table 1A-1F` and `Table 6/6A` language.
   - Risk: captions, cross-references, or reviewer-response prose may cite incompatible slot systems.

2. Authority-stack drift
   - The front door is shared and current.
   - Downstream sections still lean on many boost-local travel kits and shard-local routers.
   - Risk: manuscript prose may appear current while quietly depending on older lane-specific packaging logic.

3. Denominator overload risk in taxonomy/security fragments
   - The manuscript correctly distinguishes Figure 2, Figure 5, and Figure 7 at the top.
   - Some downstream fragments still juxtapose legacy mechanical, live dashboard, and sidecar contracts in one paragraph.
   - Risk: hostile readers may treat the file as internally multi-denominator even when the top-level contract is correct.

4. Shared-route versus shard-route ambiguity
   - Some fragments already cite live caption-control IDs (`CCR-010`, `CCR-015`, `CCR-006`, `CCR-016`).
   - Others remain mostly shard-local prose blocks.
   - Risk: normalization progress is uneven and hard to verify quickly.

## Paper-readiness reading

This is a useful negative result, not a failure.

The preprint is not blocked on new evidence collection. It is blocked on manuscript packaging discipline:
- convert shard-fragment prose into shared article objects;
- reconcile older table-slot labels against the live figure/table registry;
- keep boost-local travel kits as provenance support, not as the manuscript front door.

That means the next publishability move should stay inside manuscript synchronization rather than reopening collection.

## Exact next smallest move

Patch `draft/preprint.md` in a bounded way so that:
1. old slot labels (`Table 1A-1F`, `Table 6/6A`) are either remapped or explicitly quarantined;
2. each surviving shard fragment points first to the shared dashboard/article object, then only secondarily to boost-local support bundles;
3. the top-level denominator contract remains the only count-bearing front door.

## Observatory hook

This audit feeds:
- manuscript-assembly QA for LIMEN dashboard/paper parity;
- reviewer-response preparation on denominator discipline;
- future dashboard/paper bridge tooling that checks whether preprint fragments still depend on boost-local routing bundles.
