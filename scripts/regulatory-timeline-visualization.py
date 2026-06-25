# Regulatory Actions Visualization Script

## Purpose
Generate timeline visualization of enforcement actions across jurisdictions for LIMEN AI Edge-Case Atlas.

## Dependencies
- Python 3.8+
- matplotlib
- pandas

## Execution
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load enforcement data (example structure)
# This should map to your actual data source
data = pd.read_csv('enforcement-actions.csv')

date_mask = '%Y-%m-%d'  # Date format mask
data['date'] = pd.to_datetime(data['date'], format=date_mask)

# Set date as index for resampling
data.set_index('date', inplace=True)

# Group by action type and jurisdiction while resampling monthly
groups = data.resample('M').groupby([pd.Grouper(freq='M'), 'action_type', 'jurisdiction'])

# Plot configuration
plt.figure(figsize=(15, 8))
plt.title('Regulatory Enforcement Timeline by Type and Jurisdiction')
plt.xlabel('Date')
plt.ylabel('Number of Actions')

# Plot each action type with jurisdiction
categories = data['action_type'].unique()
for action_type in categories:
    for jurisdiction in data['jurisdiction'].unique():
        group = data[(data['action_type'] == action_type) & (data['jurisdiction'] == jurisdiction)]
        if not group.empty:
            counts = group.resample('M').size()
            counts.plot(label=f'{action_type} ({jurisdiction})')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('regulatory-timeline.png')
```

## Output
- Saves `regulatory-timeline.png` showing trends over time
- Can be integrated into dashboard via Markdown: 
```markdown
![Regulatory Timeline](regulatory-timeline.png)
```

## Notes
- Modify data loading based on actual source format
- Add jurisdiction color coding or action type grouping as needed
- Include data source metadata and uncertainty flags from taxonomy mapping