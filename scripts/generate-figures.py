#!/usr/bin/env python3
"""Generate LIMEN publication figures (Figures 2-8) from dashboard TSVs.

Produces PNG (300 dpi) and SVG for each figure.
Output: results/boost/limen-dashboard-paper-forge/figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import csv
import os

# Output directory
out_dir = "/srv/tyche/projects/limen-ai-edge-case-atlas/results/boost/limen-dashboard-paper-forge/figures"
os.makedirs(out_dir, exist_ok=True)

base = "/srv/tyche/projects/limen-ai-edge-case-atlas/results/dashboard"

def parse_tsv(path):
    rows = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            rows.append(row)
    return rows

# Common style
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

def save_fig(fig, name):
    fig.savefig(f"{out_dir}/{name}.png", dpi=300)
    fig.savefig(f"{out_dir}/{name}.svg")
    plt.close(fig)
    print(f"  Saved: {name}.png + .svg")


# ============================================================
# FIGURE 2: Taxonomy Heatmap
# ============================================================
print("Generating Figure 2: Taxonomy Heatmap...")
taxonomy = parse_tsv(f"{base}/taxonomy-heatmap.tsv")

categories = [r['category_label'] for r in taxonomy]
seed_counts = [int(r['seed_case_count']) for r in taxonomy]
auth_counts = [int(r['authoritative_seed_count']) for r in taxonomy]
priorities = [r['review_priority'] for r in taxonomy]

# Sort by seed count descending
sorted_idx = sorted(range(len(seed_counts)), key=lambda i: seed_counts[i], reverse=True)
categories = [categories[i] for i in sorted_idx]
seed_counts = [seed_counts[i] for i in sorted_idx]
auth_counts = [auth_counts[i] for i in sorted_idx]
priorities = [priorities[i] for i in sorted_idx]

fig, ax = plt.subplots(figsize=(10, 7))

y_pos = np.arange(len(categories))
bar_width = 0.35

bars1 = ax.barh(y_pos - bar_width/2, seed_counts, bar_width, 
                label='Seed case count', color='#6baed6', edgecolor='#2171b5', linewidth=0.5)
bars2 = ax.barh(y_pos + bar_width/2, auth_counts, bar_width,
                label='Authoritative source count', color='#2ca25f', edgecolor='#006d2c', linewidth=0.5)

# Add priority markers
for i, (p, sc) in enumerate(zip(priorities, seed_counts)):
    marker = '●' if p == 'High' else '○'
    color = '#d73027' if p == 'High' else '#636363'
    ax.text(max(sc, auth_counts[i]) + 0.3, i, f'{marker} {p}', va='center', fontsize=7, color=color)

ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.set_xlabel('Count')
ax.set_title('Figure 2. LIMEN Taxonomy Heatmap\nDenominator: 39 governed record refs / 29 unique lineages (core); 44 / 34 (extended sidecar)')
ax.legend(loc='lower right', fontsize=8)
ax.set_xlim(0, max(seed_counts) + 3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.text(0.5, -0.08, '● High review priority  ○ Medium review priority\nDoes not represent prevalence or completeness of AI incidents globally.',
        transform=ax.transAxes, fontsize=7, ha='center', style='italic', color='#636363')

save_fig(fig, "figure-2-taxonomy-heatmap")


# ============================================================
# FIGURE 3: Evidence-Tier Funnel
# ============================================================
print("Generating Figure 3: Evidence-Tier Funnel...")
evidence = parse_tsv(f"{base}/evidence-funnel.tsv")

stages = [r for r in evidence if r['row_type'] == 'lineage_stage']
stage_labels = [r['stage_label'] for r in stages]
lineage_counts = [int(r['lineage_count']) for r in stages]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [1.2, 1]})

colors_funnel = ['#f0f0f0', '#fd8d3c', '#f0f0f0', '#2ca25f', '#66c2a4', '#f0f0f0']
bars = ax1.barh(range(len(stage_labels)), lineage_counts, color=colors_funnel[:len(stage_labels)], 
                edgecolor='#333333', linewidth=0.5)

for i, (label, count) in enumerate(zip(stage_labels, lineage_counts)):
    ax1.text(count + 0.2, i, str(count), va='center', fontsize=9, fontweight='bold')

ax1.set_yticks(range(len(stage_labels)))
ax1.set_yticklabels(stage_labels, fontsize=8)
ax1.set_xlabel('Lineage count')
ax1.set_title('Evidence-tier distribution\n(publication-safe lineages)')
ax1.set_xlim(0, max(lineage_counts) + 3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Confidence cap pie
conf_data = [r for r in evidence if r['row_type'] == 'confidence_cap']
conf_labels = [r['stage_label'].replace('publication confidence cap: ', '').capitalize() for r in conf_data]
conf_counts = [int(r['lineage_count']) for r in conf_data]
conf_colors = ['#2ca25f', '#fd8d3c', '#e31a1c']

non_zero = [(l, c, col) for l, c, col in zip(conf_labels, conf_counts, conf_colors) if c > 0]
if non_zero:
    labels_nz, counts_nz, colors_nz = zip(*non_zero)
    wedges, texts, autotexts = ax2.pie(counts_nz, labels=labels_nz, colors=colors_nz,
                                        autopct='%1.0f%%', startangle=90)
    for t in autotexts:
        t.set_fontsize(9)

ax2.set_title('Confidence cap distribution\nDenominator: 21 publication-safe lineages')

fig.suptitle('Figure 3. Evidence-Tier Funnel and Confidence Cap', fontsize=11, y=1.02)
plt.tight_layout()
save_fig(fig, "figure-3-evidence-funnel")


# ============================================================
# FIGURE 4: Source-Family Saturation Map
# ============================================================
print("Generating Figure 4: Source-Family Saturation Map...")
source_fam = parse_tsv(f"{base}/source-family-coverage.tsv")

fam_labels = [r['source_family'] for r in source_fam]
fam_priorities = [r['priority'] for r in source_fam]
fam_saturation = [r['saturation_state'] for r in source_fam]

# Sort by priority
priority_order = {'P0': 0, 'P1': 1, 'P2': 2}
sorted_idx = sorted(range(len(fam_labels)), key=lambda i: (priority_order.get(fam_priorities[i], 9), fam_labels[i]))
fam_labels = [fam_labels[i] for i in sorted_idx]
fam_priorities = [fam_priorities[i] for i in sorted_idx]
fam_saturation = [fam_saturation[i] for i in sorted_idx]

fig, ax = plt.subplots(figsize=(10, 8))

y_pos = np.arange(len(fam_labels))

# Color by saturation state
sat_colors = {'seeded': '#2ca25f', 'planned': '#bdbdbd'}
bar_colors = [sat_colors.get(s, '#cccccc') for s in fam_saturation]

# Priority markers
pri_colors = {'P0': '#d73027', 'P1': '#fc8d59', 'P2': '#fee090'}

bars = ax.barh(y_pos, [1]*len(fam_labels), color=bar_colors, edgecolor='#333333', linewidth=0.5, height=0.7)

# Add priority badges
for i, (p, s) in enumerate(zip(fam_priorities, fam_saturation)):
    ax.plot(-0.05, i, 's', color=pri_colors.get(p, '#cccccc'), markersize=10, transform=ax.get_yaxis_transform())

ax.set_yticks(y_pos)
ax.set_yticklabels([f"{l} ({p})" for l, p in zip(fam_labels, fam_priorities)], fontsize=8)
ax.set_xlim(-0.15, 1.1)
ax.set_xticks([])
ax.set_title('Figure 4. Source-Family Saturation Map\n15 source families, seeded vs. planned state')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#2ca25f', edgecolor='#333', label='Seeded (active)'),
    mpatches.Patch(facecolor='#bdbdbd', edgecolor='#333', label='Planned (not yet seeded)'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='#d73027', markersize=8, label='P0 (critical)'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='#fc8d59', markersize=8, label='P1 (important)'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='#fee090', markersize=8, label='P2 (frontier)'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=7, ncol=2)

ax.text(0.5, -0.05, 'Seeded state reflects local package readiness, not external completeness.\nThin-family flags (sf08, sf09, sf11, sf13) documented in Appendix.',
        transform=ax.transAxes, fontsize=7, ha='center', style='italic', color='#636363')

save_fig(fig, "figure-4-source-family-saturation")


# ============================================================
# FIGURE 5: Jurisdiction/Language Coverage
# ============================================================
print("Generating Figure 5: Jurisdiction/Language Coverage...")
jurisdiction = parse_tsv(f"{base}/jurisdiction-language-coverage.tsv")

jur_names = [r['jurisdiction'] for r in jurisdiction]
jur_langs = [r['language'] for r in jurisdiction]
jur_counts = [int(r['record_count']) for r in jurisdiction]
jur_tiers = [r['strongest_evidence_tier'] for r in jurisdiction]
jur_translation = [int(r['translation_review_needed_count']) for r in jurisdiction]

# Sort by record count descending
sorted_idx = sorted(range(len(jur_names)), key=lambda i: jur_counts[i], reverse=True)
jur_names = [jur_names[i] for i in sorted_idx]
jur_langs = [jur_langs[i] for i in sorted_idx]
jur_counts = [jur_counts[i] for i in sorted_idx]
jur_tiers = [jur_tiers[i] for i in sorted_idx]
jur_translation = [jur_translation[i] for i in sorted_idx]

fig, ax = plt.subplots(figsize=(10, 6))

y_pos = np.arange(len(jur_names))

# Color by tier
tier_colors = {'T3_authoritative_source': '#2ca25f', 'T1_single_public_source': '#fd8d3c'}
bar_colors = [tier_colors.get(t, '#cccccc') for t in jur_tiers]

bars = ax.barh(y_pos, jur_counts, color=bar_colors, edgecolor='#333333', linewidth=0.5)

# Add language and translation badges
for i, (lang, transl) in enumerate(zip(jur_langs, jur_translation)):
    label_parts = [lang.upper()]
    if transl > 0:
        label_parts.append(f'⚑{transl}')
    ax.text(jur_counts[i] + 0.1, i, ' '.join(label_parts), va='center', fontsize=7, color='#333333')

ax.set_yticks(y_pos)
ax.set_yticklabels(jur_names, fontsize=8)
ax.set_xlabel('Record count')
ax.set_title('Figure 5. Jurisdiction and Language Coverage\nDenominator: 12 jurisdiction/language rows from reviewed-core corpus')
ax.set_xlim(0, max(jur_counts) + 1.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

legend_elements = [
    mpatches.Patch(facecolor='#2ca25f', edgecolor='#333', label='T3 authoritative source'),
    mpatches.Patch(facecolor='#fd8d3c', edgecolor='#333', label='T1 single public source'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=7)

ax.text(0.5, -0.08, '⚑ = translation review needed. Shows visibility surface, not prevalence or completeness.\n21 publication-safe lineages across jurisdictions.',
        transform=ax.transAxes, fontsize=7, ha='center', style='italic', color='#636363')

save_fig(fig, "figure-5-jurisdiction-language")


# ============================================================
# FIGURE 6: Legal Uncertainty Matrix
# ============================================================
print("Generating Figure 6: Legal Uncertainty Matrix...")
legal_unc = parse_tsv(f"{base}/legal-uncertainty-matrix.tsv")

cat_labels = [r['category_label'] for r in legal_unc]
cat_counts = [int(r['seed_case_count']) for r in legal_unc]
cat_priorities = [r['review_priority'] for r in legal_unc]

# Sort by count descending
sorted_idx = sorted(range(len(cat_labels)), key=lambda i: cat_counts[i], reverse=True)
cat_labels = [cat_labels[i] for i in sorted_idx]
cat_counts = [cat_counts[i] for i in sorted_idx]
cat_priorities = [cat_priorities[i] for i in sorted_idx]

fig, ax = plt.subplots(figsize=(10, 7))

y_pos = np.arange(len(cat_labels))

# Use heatmap-style coloring: priority determines color
pri_color_map = {'High': '#d73027', 'Medium': '#fc8d59'}
bar_colors = [pri_color_map.get(p, '#cccccc') for p in cat_priorities]

bars = ax.barh(y_pos, cat_counts, color=bar_colors, edgecolor='#333333', linewidth=0.5)

# Add count labels
for i, c in enumerate(cat_counts):
    if c > 0:
        ax.text(c + 0.15, i, str(c), va='center', fontsize=9, fontweight='bold')
    else:
        ax.text(0.15, i, '0 (guardrail)', va='center', fontsize=7, color='#636363', style='italic')

ax.set_yticks(y_pos)
ax.set_yticklabels(cat_labels, fontsize=8)
ax.set_xlabel('Seed case count')
ax.set_title('Figure 6. Legal Uncertainty Matrix\nCategories by seed count and review priority')
ax.set_xlim(0, max(cat_counts) + 2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

legend_elements = [
    mpatches.Patch(facecolor='#d73027', edgecolor='#333', label='High review priority'),
    mpatches.Patch(facecolor='#fc8d59', edgecolor='#333', label='Medium review priority'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=8)

ax.text(0.5, -0.06, 'Zero-count rows are methods guardrails, not evidence of absence.\nLegal conclusions cannot be drawn from public-source counts alone.',
        transform=ax.transAxes, fontsize=7, ha='center', style='italic', color='#636363')

save_fig(fig, "figure-6-legal-uncertainty")


# ============================================================
# FIGURE 7: Security Threshold Ladder
# ============================================================
print("Generating Figure 7: Security Threshold Ladder...")
security_thr = parse_tsv(f"{base}/security-threshold-ladder-panel.tsv")

thr_labels = [r['threshold_class'].replace('_', ' ').title() for r in security_thr]
thr_counts = [int(r['member_count']) for r in security_thr]
thr_buckets = [r['publication_buckets_present'] for r in security_thr]

# Reverse for bottom-up ladder
thr_labels = thr_labels[::-1]
thr_counts = thr_counts[::-1]
thr_buckets = thr_buckets[::-1]

fig, ax = plt.subplots(figsize=(8, 5))

y_pos = np.arange(len(thr_labels))

# Gradient: stronger ceiling = darker green
ladder_colors = ['#fee08b', '#a6d96a', '#66bd63', '#1a9850']
if len(thr_labels) <= len(ladder_colors):
    bar_colors = ladder_colors[:len(thr_labels)]
else:
    bar_colors = ['#cccccc'] * len(thr_labels)

bars = ax.barh(y_pos, thr_counts, color=bar_colors, edgecolor='#333333', linewidth=0.5, height=0.6)

# Add bucket labels
for i, (count, bucket) in enumerate(zip(thr_counts, thr_buckets)):
    ax.text(count + 0.1, i, f'n={count}  [{bucket}]', va='center', fontsize=7, color='#333333')

ax.set_yticks(y_pos)
ax.set_yticklabels(thr_labels, fontsize=8)
ax.set_xlabel('Member count')
ax.set_title('Figure 7. Security Threshold Ladder\nDenominator: 4 threshold classes, 11 total security rows')
ax.set_xlim(0, max(thr_counts) + 3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.text(0.5, -0.10, 'Bounded companion to Figures 2 and 5; not a core count surface.\n[publication_buckets_present] indicates where members appear in the manuscript.',
        transform=ax.transAxes, fontsize=7, ha='center', style='italic', color='#636363')

save_fig(fig, "figure-7-security-threshold-ladder")


# ============================================================
# FIGURE 8: Duplicate-Review Graph
# ============================================================
print("Generating Figure 8: Duplicate-Review Graph...")
duplicate = parse_tsv(f"{base}/duplicate-review-graph.tsv")

# Count edge types
edge_types = {}
for r in duplicate:
    et = r['edge_type']
    edge_types[et] = edge_types.get(et, 0) + 1

# Count cluster basis categories
cluster_bases = {}
for r in duplicate:
    cb = r['cluster_basis']
    cluster_bases[cb] = cluster_bases.get(cb, 0) + 1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left: Edge type distribution
et_labels = [k.replace('_', ' ').title() for k in edge_types.keys()]
et_counts = list(edge_types.values())
et_colors = ['#e31a1c' if 'collision' in k.lower() else '#33a02c' for k in edge_types.keys()]

bars1 = ax1.barh(range(len(et_labels)), et_counts, color=et_colors, edgecolor='#333333', linewidth=0.5)
for i, c in enumerate(et_counts):
    ax1.text(c + 0.1, i, str(c), va='center', fontsize=9, fontweight='bold')

ax1.set_yticks(range(len(et_labels)))
ax1.set_yticklabels(et_labels, fontsize=8)
ax1.set_xlabel('Edge count')
ax1.set_title('Edge type distribution')
ax1.set_xlim(0, max(et_counts) + 2)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Right: Decision summary
decisions = {'Reviewed not duplicate': 0, 'Identifier collision': 0}
for r in duplicate:
    if 'nomerge' in r['edge_id'].lower() or r['edge_type'] == 'reviewed_not_duplicate':
        decisions['Reviewed not duplicate'] += 1
    elif 'collision' in r['edge_type']:
        decisions['Identifier collision'] += 1

dec_labels = list(decisions.keys())
dec_counts = list(decisions.values())
dec_colors = ['#33a02c', '#e31a1c']

wedges, texts, autotexts = ax2.pie(dec_counts, labels=dec_labels, colors=dec_colors,
                                     autopct='%1.0f%%', startangle=90)
for t in autotexts:
    t.set_fontsize(10)
for t in texts:
    t.set_fontsize(8)

ax2.set_title('Review decision summary\nDenominator: 27 duplicate-review edges')

fig.suptitle('Figure 8. Duplicate-Review Graph\n27 edges, 0 merge decisions, all reviewed as distinct', fontsize=11, y=1.02)
plt.tight_layout()
save_fig(fig, "figure-8-duplicate-review-graph")


# ============================================================
# Summary
# ============================================================
print("\n" + "="*60)
print("Figure generation complete.")
print(f"Output directory: {out_dir}")
files = sorted(os.listdir(out_dir))
for f in files:
    fpath = os.path.join(out_dir, f)
    size_kb = os.path.getsize(fpath) / 1024
    print(f"  {f}: {size_kb:.1f} KB")
print(f"Total files: {len(files)}")
