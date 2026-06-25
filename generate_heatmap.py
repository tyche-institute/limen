import pandas as pd
import matplotlib.pyplot as plt

tsv_path = '/srv/tyche/projects/limen-ai-edge-case-atlas/results/boost/limen-boost-036/crosswalk-delta-nist-sp80053.tsv'
output_path = '/srv/tyche/projects/limen-ai-edge-case-atlas/results/boost/limen-boost-036/coverage-heatmap.png'

df = pd.read_csv(tsv_path, sep='\t')

df['Control'] = df['notes'].str.extract(r'SP-800-53-(\d{4})[.]?\d*')[0].str.replace('.0', '')
df['Mapped'] = 1  # All entries have mappings based on notes

df_pivot = df.pivot_table(index='framework', columns='Control', aggfunc='sum', values='Mapped', fill_value=0)

plt.figure(figsize=(12, 8))
plt.imshow(df_pivot, cmap='viridis', aspect='auto')
plt.colorbar()
plt.xticks(range(len(df_pivot.columns)), df_pivot.columns)
plt.yticks(range(len(df_pivot.index)), df_pivot.index)
plt.savefig(output_path, bbox_inches='tight')
print(f'Coverage heatmap saved to {output_path}')
