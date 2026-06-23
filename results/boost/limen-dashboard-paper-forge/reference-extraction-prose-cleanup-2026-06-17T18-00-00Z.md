# LIMEN preprint v0.5: reference extraction and inline-path cleanup

Date: 2026-06-17T18:00:00Z
Lane: `limen-dashboard-paper-forge`
Action: editorial-only manuscript hygiene pass (no new data collection)

## What was done

Converted `draft/preprint.md` from v0.4 (320 lines, 64 inline file-path
citations, pipeline jargon) to v0.5 (354 lines, 14 proper academic
references, 14 Supplementary Table references, 0 pipeline jargon in prose).

## Specific changes

### Inline path removal
- Removed all 18 `results/boost/...` paths from §4 prose → replaced with
  "Supplementary Table SX" references (S1–S14) or figure/table references
- Removed all 11 `results/security/...` paths → replaced with "(Table C,
  Figure 7)" or supplementary table references
- Removed all 12 `results/dashboard-paper/...` paths → removed as governance
  metadata or replaced with "(see Caption Control Register, Supplementary
  Methods)"
- Removed all 3 `results/multilingual/...` paths → replaced with "(Figure 6,
  Table D)"
- Removed all 4 `claims.md:LIMEN-C-XXX` references → replaced with "(see
  Claims Register, Supplementary Methods)"
- Removed all 8 `CCR-XXX` references → replaced with "(see Caption Control
  Register, Supplementary Methods)"
- 1 `results/boost` path remains in Table 1 denominator registry (legacy
  mechanical provenance row — acceptable as methods-table provenance
  documentation)
- 1 `results/dashboard-paper/` path remains in §8 Data Availability (required
  for reproducibility pointer)

### Pipeline jargon removal
- "shard" → "evidence group" or removed
- "boost" → removed from prose
- "lane" → removed from prose
- "shared-control front door:" → removed (already done in prior cycle)

### New sections added
- **§7 References** — 14 proper academic citations:
  [1] AIID (McGregor 2021)
  [2] MIT AI Risk Repository (Schuett et al. 2024)
  [3] CSET AI Harm Index
  [4] OECD AI Policy Observatory
  [5] AVID
  [6] MITRE ATLAS
  [7] NIST AI RMF 1.0
  [8] EU AI Act (Regulation 2024/1689)
  [9] ISO/IEC 42001:2023
  [10] C2PA Technical Specification v2.0
  [11] SEC Delphia/Global Predictions (2024)
  [12] DOJ SDNY nate/Saniger (2024)
  [13] FTC DoNotPay (2024)
  [14] FCC Lingo Telecom (2024)
- **§8 Data Availability** — reproducibility package pointer to
  `results/dashboard/` and `results/dashboard-paper/`

## What was preserved

- Abstract: 138 words, unchanged
- All substantive findings, case IDs (LIMEN-000001–LIMEN-000016), denominators
  (39/29, 21, 4, 15, 27, 12, 248/32), and claim ceilings
- §1 Introduction (clean, unchanged)
- §2 Related Work (clean, unchanged)
- §3.1 denominator registry table (methods-appropriate, file paths in table
  column kept)
- §5 Limitations structure (7 subsections, paths removed from prose)
- §6 Conclusion (unchanged)

## Verification

- `grep -c 'results/boost' draft/preprint.md` → 1 (Table 1 only)
- `grep -c 'results/security' draft/preprint.md` → 0
- `grep -c 'claims.md:' draft/preprint.md` → 0
- `grep -c 'CCR-' draft/preprint.md` → 0
- `grep -c 'shard' draft/preprint.md` → 0
- Line count: 354 (under 400 target)

## Paper-readiness delta

Prior blocker #3 resolved:
> "Reference extraction from boost-path inline citations not yet done
> (boost file paths still appear in §4 paragraph bodies as evidence anchors)."

The manuscript is now readable by a hostile reviewer without encountering
internal pipeline artifacts. Every evidence discussion either cites a
numbered reference [N], a figure/table, or a supplementary table.

## Remaining blockers

1. sf08 court-depth, sf09 buyer-side, sf11 peer-reviewed gaps remain
   (documented, not fixable from this lane).
2. Route C remains local-bundle provenance only.
3. Supplementary Tables S1–S14 need actual content (currently referenced but
   not yet assembled as a supplementary-information file).
