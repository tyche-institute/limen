# Source-Family Saturation Map
## Coverage Overview
- **Total Sources**: 302
- **By Family**:
  - News: 121 (40%)
  - Policy: 75 (25%)
  - Academic: 60 (20%)
  - Other: 46 (15%)
## Geographic Distribution
- **Europe**: 65% of news sources
  - Top Countries: Germany (25%), UK (15%), France (10%)
- **Asia**: 35% of news sources
  - Top Countries: China (12%), India (8%), Japan (5%)
## Language Breakdown
- **English**: 50% of total sources
- **German**: 20%
- **French**: 15%
- **Other Languages**: 15%

## Update Script Integration
```python
from pathlib import Path
import pandas as pd

def update_source_saturation():
    sources = pd.read_csv("sources/sources.csv")
    family_counts = sources['family'].value_counts(normalize=True) * 100
    geo_distribution = sources[sources['family'] == 'News'].groupby('country').size()
    # Write to this markdown file
    with open("dashboard/source-saturation-map.md", 'w') as f:
        f.write(f"""{format_content(family_counts, geo_distribution)}""")
```

This file was auto-generated from the current source index.
Last updated: 2026-06-24T14:30:00Z