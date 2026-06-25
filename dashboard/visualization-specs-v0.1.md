# LIMEN Dashboard Visualization Specifications v0.1

## 1. Evidence Tier Distribution
- Type: Bar chart
- Data Sources: Source ledger evidence tiers (Primary, Secondary, Tertiary)
- Axes: X = Jurisdiction, Y = Count
- Purpose: Visualize geographic distribution of evidence quality

## 2. Source Authority Matrix
- Type: Heatmap
- Data Sources: Source authority scores vs jurisdiction relevance
- Axes: X = Source Type, Y = Jurisdiction
- Color: Authority score (0.0-1.0)

## 3. Duplicate Cluster Network
- Type: Graph network
- Data Sources: Candidate duplicate pairs from limen-boost-011
- Nodes: Sources, Edges: Similarity scores

## 4. Language Coverage Map
- Type: Choropleth map
- Data Sources: Language distribution across jurisdictions
- Color: Intensity of language presence

## 5. Crosswalk Completion Tracker
- Type: Progress donut
- Data Sources: Crosswalk framework status per jurisdiction
- Segments: Complete, In Progress, Not Started

## 6. Temporal Distribution
- Type: Timeline
- Data Sources: Source publication dates
- Axes: X = Date, Y = Count

## 7. Authority Score Distribution
- Type: Histogram
- Data Sources: Source authority scores
- Bins: 0.0-0.2, 0.2-0.4, ..., 0.8-1.0"