# Regulatory Enforcement Timeline Generation Script

import pandas as pd
import matplotlib.pyplot as plt

# Load enforcement actions CSV
DF = pd.read_csv('data/taxonomy-enforcement-actions.csv', parse_dates=['date'], dayfirst=True)

# Validate dates and filter valid entries
DF = DF.dropna(subset=['date'])
DF = DF[DF['date'].dt.year == 2026]  # Focus on current year

# Group by jurisdiction and type for plotting
grouped = DF.groupby(['jurisdiction', 'type']).size().unstack()

# Plot timeline
fig, ax = plt.subplots(figsize=(12, 6))
DF.set_index('date').groupby(pd.Grouper(freq='M'))['type'].count().plot(ax=ax, title='Monthly Enforcement Actions by Type', legend=False)

# Annotate key points
annotations = {
    '2026-02-28': 'EU AI Ethics Audit Framework',
    '2026-04-15': 'Meta DSA Transparency Warning',
    '2026-05-03': 'US FTC Google Safety Requirements',
    '2026-06-10': 'Tesla AI Risk Assessment Investigation'
}

for date, text in annotations.items():
    x = pd.to_datetime(date)
    ax.annotate(text, (x, ax.get_ylim()[1] - 0.1*ax.get_ylim()[1]), ha='left', va='top', fontsize=8)

# Save figure
plt.tight_layout()
plt.savefig('results/boost/limen-boost-051/regulatory-timeline.png')

print("Timeline visualization saved to regulatory-timeline.png")