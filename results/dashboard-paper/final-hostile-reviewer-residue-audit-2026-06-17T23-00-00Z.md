# Final hostile-reviewer residue audit

Audit time (UTC): 2026-06-17T23:00:00Z
Lane: `limen-dashboard-paper-forge`
Preprint: `draft/preprint.md` (354 lines, v0.5+)
Control files: `dashboard/limen-dashboard-spec-v0.1.md`, `papers/article-architecture-v0.1.md`

## Audit scope

This audit verifies that the preprint manuscript is free of internal pipeline
artifacts, that all table/figure slots are formally registered, and that the
manuscript can survive a hostile reviewer pass without exposing boost-local
paths, shard labels, or unregistered slot names.

## Residue counts

| Residue class | Count | Status |
| --- | --- | --- |
| `results/boost/` paths in prose | 0 | PASS |
| `shard` labels in prose | 0 | PASS |
| `lane` labels in prose | 0 | PASS |
| `pipeline` jargon in prose | 0 | PASS |
| Unregistered `Table 1*` legacy labels | 0 | PASS |
| Unregistered `Table 6*` legacy labels | 0 | PASS |

## Registered manuscript table/figure slots

| Slot | Type | Location | Registration |
| --- | --- | --- | --- |
| Table 1 | Methods infrastructure | §3.1 denominator registry | Registered 2026-06-17 |
| Table 2 | Methods data companion | §4 taxonomy data for Figure 2 | Registered 2026-06-17 |
| Figure 1 | Core | §3 source-family saturation map | Pre-existing |
| Figure 2 | Core | §4 taxonomy support heatmap | Pre-existing |
| Figure 3 | Core | §4 legal uncertainty matrix | Pre-existing |
| Figure 4 | Core | §4 duplicate-review QC graph | Pre-existing |
| Figure 5 | Core | §4 publication-safe evidence funnel | Pre-existing |
| Figure 6 | Core | §4 jurisdiction/language map | Pre-existing |
| Table A | Core | §4 authoritative document-depth | Pre-existing |
| Table B | Core | §4 public-sector disclosure | Pre-existing |
| Table C | Companion | §4 security crosswalk coverage | Pre-existing |
| Figure 7 | Companion | §4 security threshold ladder | Pre-existing |
| Figure 8 | Companion | §4 attestation readiness | Pre-existing |

## Denominator discipline verification

| Surface | Preprint denominator | Dashboard registry | Match |
| --- | --- | --- | --- |
| Figure 2 / Table 2 core | 39/29 | 39/29 | PASS |
| Figure 2 / Table 2 extended | 44/34 | 44/34 | PASS |
| Figure 2 / Table 2 legacy | 35/27 | 35/27 | PASS |
| Figure 5 funnel | 21 publication-safe lineages | 21 publication-safe lineages | PASS |
| Figure 7 threshold | 4 threshold rows | 4 threshold rows | PASS |
| Figure 8 attestation | 4 trust-surface rows | 4 trust-surface rows | PASS |
| S15 reviewed-core | 250 cases / 34 jurisdictions | 250 cases / 34 jurisdictions | PASS |

## Patch applied this cycle

1. Replaced boost-local path in Table 1 row "Legacy mechanical Figure 2 source"
   from `results/boost/limen-dashboard-paper-forge/taxonomy-heatmap.tsv`
   to `Historical provenance (reproducibility package)`.

2. Registered Table 1 (denominator registry) and Table 2 (taxonomy data companion)
   as legitimate manuscript tables in:
   - `dashboard/limen-dashboard-spec-v0.1.md` (Article-facing figure/table bundle + route-safe rules)
   - `papers/article-architecture-v0.1.md` (Figure and table registry + manuscript-routing rules)

## Reference and supplementary material counts

- Academic references (§7): 14 ([1]–[14])
- Supplementary table references: S1–S15
- Supplementary figure: Figure S1 (frozen 2026-06-14 snapshot)
- Supplementary note: Note 1
- Total SI objects: 17

## Caption control parity

All 11 figure/table surfaces have:
- explicit denominator class in the dashboard spec
- explicit "What this does not show" footnote in the dashboard spec
- caption-safe sentence starter in the article architecture
- corresponding TSV export in `results/dashboard/`

## Hostile-reviewer objection simulation

| Objection | Defense |
| --- | --- |
| "The authors conflate denominators across figures" | Table 1 and §5.1 explicitly separate Figure 2 (39/29), Figure 5 (21 lineages), and Figure 7 (4 rows) |
| "The corpus claims completeness" | Abstract, §1, §5, §6 all reject completeness; Figure 1 shows thin/blocked families |
| "Legal conclusions are overstated" | Figure 3 and §5 explicitly block legal/compliance/certification claims |
| "Country rankings are implied" | Figure 6 subtitle and §5 explicitly frame as visibility asymmetry, not ranking |
| "Security claims are inflated" | Table C and Figure 7 are bounded companions with explicit gap states |
| "Provenance is overstated" | Figure 8 and §7 explicitly state local-only witness; no external assurance |
| "References are internal pipeline paths" | §7 has 14 proper academic citations; §8 Data Availability uses directory-level paths only |
| "Supplementary tables are phantom references" | All 17 SI objects (S1–S15 + Figure S1 + Note 1) have standalone source files on disk |

## Verdict

The preprint manuscript passes the hostile-reviewer residue audit. All pipeline
artifacts are purged, all slots are registered, all denominators are
disciplined, and all SI references are materialized. The remaining blockers
are content-level (source-family gaps sf08/sf09/sf11, Route C witness state)
rather than manuscript-governance issues.

## Next smallest publishability move

No further manuscript-governance patches are needed from this lane. The next
move is either:
1. Regenerate Figure S1 from current 250-case data (optional polish), or
2. Proceed to submission packaging (cover letter finalization, SI PDF assembly), or
3. Venue-fit decision (Scientific Data vs. alternative).
