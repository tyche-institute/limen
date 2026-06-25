# Legal Uncertainty Matrix
| Case ID       | Claim Type               | Legal Framework       | UNCERTAINTY | Resolution Status |
|---------------|--------------------------|----------------------|--------------|-------------------|
| C-036-001     | AI Washing - Overclaim  | EU AI Act (Article 3) | Medium       | Pending Review    |
| C-036-002     | AI Washing - Mislabel   | OECD AI Principles    | High         | Under Verification|
| C-036-003     | Human-as-AI            | MITRE ATLAS          | Low          | Resolved (Human) |

## Matrix Interpretation
- **Likelihood Categories**: 
  - High: Clear discrepancy between claim and technical reality
  - Medium: Ambiguous language requiring further verification
  - Low: Minor inconsistency with low impact
- **Impact Categories**: 
  - Regulatory: Affects compliance with AI governance frameworks
  - Contractual: Affects procurement terms
  - Reputational: Affects public perception

## Update Script Skeleton
```python
from pathlib import Path
import pandas as pd

def update_legal_uncertainty():
    # Load uncertainty queue
    uncertainty = pd.read_csv("data/uncertainty-queue.tsv", sep='\t')
    
    # Filter relevant cases
    legal_cases = uncertainty[uncertainty['category'].str.contains('AI Washing|Human-as-AI')]
    
    # Group by claim type and framework
    matrix = legal_cases.groupby(['claim_type', 'legal_framework']).size().unstack().fillna(0)
    
    # Write to markdown
    with open("dashboard/legal-uncertainty-matrix.md", 'w') as f:
        f.write(matrix.to_markdown())
```

This file was auto-generated from the current uncertainty queue.
Last updated: 2026-06-24T14:45:00Z