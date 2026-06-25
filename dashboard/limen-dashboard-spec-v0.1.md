# LIMEN Dashboard Specification v0.1

## Purpose
Provide a reproducible, interactive dashboard that visualises the LIMEN AI Edge‑Case Atlas evidence pipeline. The dashboard must expose provenance, coverage, and uncertainty for each evidence item and support the article figures.

## Data Inputs
- `data/atlas-evidence.jsonl` – line‑delimited evidence records (source_path, language, jurisdiction, evidence_tier, uncertainty_flag).
- `results/taxonomy/taxonomy-delta-v0.2.md` – taxonomy updates and coverage heatmap data.
- `results/clusters/duplicate-clusters-v0.2.tsv` – duplicate‑cluster identifiers.
- `results/dashboard-paper/status.md` – current build status (auto‑updated).

## Core Views
1. **Source‑Family Coverage Map** – choropleth per jurisdiction showing count of evidence items per source family (legal, policy, standards, PKI).
2. **Evidence‑Tier Funnel** – stacked bar visualising raw counts → screened → validated → manuscript‑ready items.
3. **Taxonomy Heatmap** – matrix of edge‑case categories vs. language coverage, colour‑coded by evidence tier.
4. **Language‑Jurisdiction Matrix** – table with language, script, jurisdiction, evidence‑type, translation status.
5. **Uncertainty Matrix** – heatmap of uncertainty flags vs. source family.
6. **Duplicate Cluster Graph** – network graph of clusters, node size = cluster size, colour = evidence tier.

## Interactivity
- Filter by source family, jurisdiction, language, tier, uncertainty.
- Hover tooltip shows full provenance (source_path, access_date, checksum).
- Export selected view to SVG/PNG for article figures.

## Implementation
- Backend: Python (FastAPI) serving JSON to a lightweight React front‑end.
- Visualization library: Plotly/D3 for interactive maps and graphs.
- Dockerised for reproducibility (`docker build -t limen-dashboard`).

## Deliverables
- `dashboard/limen-dashboard-spec-v0.1.md` (this file)
- `dashboard/app/` (code base – to be added later)
- `results/dashboard-paper/status.md` (status report – created separately)
