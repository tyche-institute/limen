## Dashboard Hook: Source Authority vs Cluster Size

### Visualization Type
Scatter Plot

### Data Sources
- X-axis: `cluster_size` (from source-authority-assessment.tsv)
- Y-axis: `source_authority_score` (from source-authority-assessment.tsv)
- Color: `language` (from source-authority-assessment.tsv)

### Required Fields
| Field | Description |
|---|---|
|cluster_id | Identifier for the cluster|
|source_authority_score | Calculated authority score (0-1)
|cluster_size | Number of documents in the cluster|
|language | Language of the source material|

### Implementation Notes
- Use hexbin smoothing for large cluster sizes
- Include interactive tooltips showing cluster_id and specific scores
- Filter controls for language and authority score thresholds

### Paper Integration
Figure 3: Source Authority Distribution Across Cluster Sizes

### SAMR Compliance Matrix Integration
Add new dimension to existing compliance matrix showing authority-weighted cluster distribution in China's regulatory environment