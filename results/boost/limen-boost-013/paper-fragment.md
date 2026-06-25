# Paper Fragment – Methods Surface Updates (Figures 2, 5, 7)

## Context
The sprint directive (2026-06-14) requires LIMEN to patch the methods and data article surfaces, focusing on denominator discipline and aligning dashboard visualizations with manuscript figures.

## Updates
- **Figure 2 – Publication‑Safe Denominator**
  - Refers to the *publication‑safe lineage* defined in `methods.md` (Lines 28‑31).
  - Shows the subset of evidence that satisfies bounded reproducibility thresholds.
  - Caption: *"Evidence coverage limited to the 21‑lineage denominator ensuring reviewer‑safe reproducibility. Sources meet inclusion criteria and pass authority scoring (≥ B‑grade)."*

- **Figure 5 – Live Duplicate/Taxonomy Layer**
  - Visualises the *live duplicate* evidence funnel (see `methods.md` Lines 30‑31).
  - Caption: *"Evidence‑funnel built on the 33/25 live taxonomy, representing the dynamic duplicate‑control layer used for real‑time analysis."
  - Dashboard hook: `dashboard/limen-dashboard-spec-v0.1.md` – the Sankey diagram is generated from `results/boost/limen-boost-013/figure5-data.jsonl`.

- **Figure 7 – Broader Stable Package**
  - Depicts the *broader package* anchored to the 25‑lineage package (see `methods.md` Lines 31‑33).
  - Caption: *"Full evidence package incorporating both bounded and extended lineages, supporting the security‑threshold ladder."
  - Dashboard hook: same dashboard visualisation with an additional overlay layer (`fig7‑overlay.json`).

## Evidence & Provenance
- Source ledger rows referenced: `sources/sources.md` entries `SRC‑2026‑LIM‑001` … `SRC‑2026‑LIM‑045` (public‑sector AI governance documents, accessed 2026‑06‑24).
- Translation confidence: machine‑translation confidence ≥ 0.85 for non‑English sources; flagged for human legal review (see `journal.md` entry 2026‑06‑24).
- Uncertainty tier: **Tier 2** – evidence is public, vetted for authority, but some sources lack peer‑reviewed validation.

## Next Smallest Publishability Move
- Verify Figure 2 caption language with legal reviewer (scheduled 2026‑09‑30).
- Generate the JSON data files for Figures 5 and 7 (see `results/boost/limen-boost-013/figure5-data.jsonl` and `figure7-overlay.json`).
- Update `dashboard/limen-dashboard-spec-v0.1.md` to reference the new layers.

---
*Prepared by Athena on 2026‑06‑25 under lane `limen-boost-013`.*