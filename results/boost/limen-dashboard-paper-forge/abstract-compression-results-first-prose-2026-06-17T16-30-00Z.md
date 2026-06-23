# Verification note: abstract compression + results-first §4 prose

Timestamp (UTC): 2026-06-17T16:30:00Z
Lane: `limen-dashboard-paper-forge`
Project root: `/srv/tyche/projects/limen-ai-edge-case-atlas`

## What was done

Two editorial-only moves on `draft/preprint.md`:

1. **Abstract compression** (Scientific Data Data Descriptor format, ≤150 words):
   - Before: ~210 words
   - After: 138 words
   - Key denominators preserved: 15 categories, 39/29 core, 21 publication-safe lineages,
     15-row source-family map, 27-edge duplicate graph, 12-row jurisdiction/language,
     248 cases / 32 jurisdictions.
   - Removed: extended sidecar counts (44/34), security/provenance companion mention,
     "thesis chapters" mention, "translation ceilings" from problem statement.
   - Claim ceilings preserved: no completeness, no prevalence, no legal violation.

2. **Results-first §4 openings** (7 subsections rewritten):
   - §4.1: removed "Shared-control front door: CCR-009...", now opens with "LIMEN's
     authoritative-document routing separates at least five materially different
     support states..."
   - §4.2: removed "Shared-control front door: CCR-017...", now opens with "Across
     LIMEN's current eleven-row public security seed, evidence-layer asymmetry is
     the principal result..."
   - §4.3: removed "Shared-control front door: CCR-013...", now opens with "Deepfake,
     synthetic-identity, false-authorship, and provenance-confusion incidents are
     treated here as an evidence-class problem..."
   - §4.5: removed "Shared-control front door: CCR-010...", now opens with "LIMEN's
     procedural-contamination and research-integrity slice now supports a
     source-depth claim..."
   - §4.6: removed "Shared-control front door: CCR-003...", now opens with "The
     AI-washing posture sidecar is best read as a four-row ladder..."
   - §4.7: removed "Shared-control front door: CCR-001...", now opens with "Under
     LIMEN's live 39/29 duplicate-governed taxonomy contract..."
   - §4.8: removed "Shared-control front door: CCR-015...", now opens with "LIMEN's
     public-sector slice is best read as an institutional-asymmetry panel..."
   - §4.4 and §4.9 were already results-first (no change needed).

## Verification counts

- `grep -c "Shared-control front door" draft/preprint.md` → 0 (was 7)
- `wc -l draft/preprint.md` → 320 (was 345)
- Abstract word count → 138 (was ~210, target ≤150)

## What was NOT changed

- No denominator was changed
- No new collection was performed
- No claim ceiling was relaxed
- No figure/table counts were altered
- Provenance file paths within paragraph bodies were preserved (they remain
  as evidence anchors in the prose, just not as section openers)
- §1–§3, §5, §6 unchanged

## Remaining editorial blockers (from status.md)

1. sf08 court-depth, sf09 buyer-side, sf11 peer-reviewed gaps (documented,
   not fixable from this lane).
2. Route C remains local-bundle provenance only.
3. Reference extraction from boost-path inline citations not yet done.

## Next smallest publishability move

Extract a formal reference list from the boost-path inline citations in §4,
converting them to a numbered bibliography. This is editorial-only and does
not require new data.
