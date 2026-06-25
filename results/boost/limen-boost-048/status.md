## LIMEN Boost Shard 048 – Dashboard & Figure Readiness

**Paper/Thesis use**: Provides two new dashboard‑ready figures for the manuscript –
- **Figure 5**: Rare‑Language Coverage Gap bar chart, supporting the *Coverage Gaps* subsection of the Methods chapter and the *Evidence Gaps* table in the Results.
- **Figure 7**: Blocked Sources Sankey diagram, supporting the *Source Access Barriers* subsection of the Results.

**Evidence used**:
- `results/boost/limen-boost-048/language-coverage-gap.tsv` – language‑coverage gap data derived from the source ledger (estimates for Estonian, Latvian, Lithuanian).
- `results/boost/limen-boost-048/blocked-sources-sankey.tsv` – aggregated blocked‑source categories derived from `sources/sources.md`.

**Uncertainty / Evidence tier**: Tier 2 – curated public records; language‑coverage numbers are based on the current source ledger and may miss obscure low‑resource sources (marked as provisional). Sankey categories are based on manual categorisation of blocked entries.

**Visualization / dashboard hook**: Updated `dashboard-hook.md` now includes entries for Figure 5 and Figure 7 with Mermaid specifications. The dashboard build script will ingest the TSV files and generate PNG exports at `results/dashboard-paper/fig5-rare-language-gap.png` and `results/dashboard-paper/fig7-blocked-sources.png`.

**Next smallest publishability move**:
1. Add a reference to `language-coverage-gap.tsv` in `methods.md` (as Table X).
2. Insert a caption and citation for Figure 5 in `draft/preprint.md` (Section 5.5 Rare‑Language Coverage).
3. Insert a caption and citation for Figure 7 in `draft/preprint.md` (Section 6.2 Source Access Barriers).
4. Run the dashboard build (`./dashboard/build.sh`) to generate PNGs for Figures 5 and 7 and record checksums in `results/dashboard-paper/checksums.tsv`.

**Cycle**: limen-boost-048 bounded harvest (2026-06-25T22:45:00Z)
**Paper‑readiness delta**: Added two ready‑to‑publish figures and associated data tables, advancing the manuscript toward the *Results* and *Methods* completeness milestones.
**Route status**: dashboard‑paper lane active; awaiting Anton’s go‑ahead to integrate figures into manuscript.
