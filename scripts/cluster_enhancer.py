["cluster_enhancer"]

import pandas as pd

def main(input_path, evidence_path, output_path):
    # Read input clusters and evidence tiers
    clusters = pd.read_csv(input_path, sep='\t')
    evidence = pd.read_csv(evidence_path, sep='\t')
    
    # Merge clusters with evidence tiers using correct column names
    # Use left merge on cluster_id (from clusters) and case_id (from evidence)
    enriched = pd.merge(clusters, evidence, left_on='cluster_id', right_on='case_id', how='left')
    
    # Assign enhancement score based on evidence tier
    enriched['enhancement_score'] = enriched['evidence_tier'].map({'high': 3, 'medium': 2, 'low': 1})
    
    # Save enhanced clusters
    enriched.to_csv(output_path, sep='\t', index=False)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print('Usage: python cluster_enhancer.py <input> <evidence> <output>')
        sys.exit(1)
    
    main(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )