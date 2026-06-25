# Dashboard Specification

## 1. Evidence-Tier Funnel
- **Purpose**: Visualize the distribution of cases across evidence tiers
- **Data Source**: seed_case_database.tsv (Evidence Tier column)
- **Visualization**: Stacked bar chart showing count of cases per tier

## 2. Source Family Saturation Map
- **Purpose**: Show coverage progress across source families
- **Data Source**: source_family_saturation_ledger.tsv
- **Visualization**: Heat map with color intensity indicating saturation level

## 3. Jurisdiction/Language Map
- **Purpose**: Geographic and linguistic distribution of cases
- **Data Source**: seed_case_database.tsv (Jurisdiction, Language columns)
- **Visualization**: World map with sized/cased markers + language pie chart

## 4. Taxonomy Heatmap
- **Purpose**: Identify emerging categories and gaps
- **Data Source**: seed_case_database.tsv (Case ID, Summary)
- **Visualization**: Clustered heatmap of case categories vs jurisdictions

## 5. Security/Agentic Crosswalk
- **Purpose**: Show overlaps between security failures and agentic issues
- **Data Source**: crosswalk_mapping.tsv
- **Visualization**: Bipartite network graph

## 6. Legal Uncertainty Matrix
- **Purpose**: Track uncertainty across jurisdictions
- **Data Source**: Legal uncertainty queue (to be created)
- **Visualization**: Matrix with jurisdictions vs uncertainty types

## 7. Duplicate Cluster Graph
- **Purpose**: Identify repetitive patterns
- **Data Source**: Seed case database (Summary, Source)
- **Visualization**: Cluster graph with strength indicators

## 8. Residual Category Queue
- **Purpose**: Highlight unclassified cases
- **Data Source**: Seed case database (unmapped cases)
- **Visualization**: Interactive list with filtering capabilities