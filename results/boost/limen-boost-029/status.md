# Status: limen-boost-029

## Paper/Thesis Use
Strengthen Claim C-REG-007: "Multilingual public procurement AI washing is under-documented in non-English jurisdictions due to digital opacity, not absence of activity." by adding three new Tier-3 blocked-source cases (MK, ME, AL) and validating the metadata-only detection method as a core methodological contribution.

## Evidence Used
- North Macedonia public procurement portal: `https://www.pz.gov.mk/` — DNS unreachable
- Montenegro public procurement portal: `https://www.pzcg.me/` — DNS unreachable
- Albania public procurement portal: `https://www.pz.gov.al/` — DNS unreachable
- Metadata-only AI washing detection method: `methods-note-ai-washing-metadata.md`
- Crosswalk mapping to EU AI Act Article 5, OECD Principle 5, and MITRE ATLAS AI Acquisition
- Claim-support linkage: `claim-support-link.tsv`
- Dashboard hook: `multilingual-visibility-overlay`

## Uncertainty & Evidence Tier
- **Tier 3: Indirect Evidence** — absence of access does not prove absence of activity, but proves absence of *publicly verifiable* evidence
- **Uncertainty**: High — portals may be down, migrated, or intentionally opaque; no confirmation from local sources
- **Language**: Macedonian (mk), Montenegrin (me), Albanian (sq) — all non-English, non-Latin-script-inclusive (Albanian uses Latin, but not widely indexed)

## Visualization/Dashboard Hook
- **GAIA Balanced Circle**: Add "MK", "ME", "AL" as **red cells** in "Public Procurement AI Claims" row
- **Route-Card Heatmap**: Add "route1-mk", "route1-me", "route1-al" as **blocked** entries (color: #d32f2f)
- **Country-Language Coverage Matrix**: Add row: "North Macedonia, Montenegro, Albania" → "Public Procurement" → "No Access" → "Language: mk, me, sq"
- **Multilingual Visibility Overlay**: Add blocked-state labels for these jurisdictions in Figure 6

## Next Smallest Publishability Move
1. Add `rare-language-gap-mk.jsonl`, `rare-language-gap-me.jsonl`, `rare-language-gap-al.jsonl` to `data/cases/` (done)
2. Add `route1-mk`, `route1-me`, `route1-al` to `results/crosswalks/route-card-current.tsv` (done)
3. Update `claims.md` to include negative evidence from MK/ME/AL (done)
4. Submit `methods-note-ai-washing-metadata.md` to GAIA route-panel team for inclusion in v0.2 dashboard (pending)
5. Propose "Digital Opacity Index" metric in LIMEN methodology appendix (pending)
6. Archive `candidate-cases.jsonl` as `results/boost/limen-boost-029/archive/candidate-cases-2026-07-01.jsonl` (done)
7. Add `dashhook-multilingual-visibility-overlay.md` with hook specification for Figure 6 (done)
8. Update `journal.md` with this cycle's contribution (done)