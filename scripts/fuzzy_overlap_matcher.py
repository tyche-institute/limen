#!/usr/bin/env python3
import os
import argparse
from fuzzywuzzy import fuzz, process
from Levenshtein import ratio as levenshtein_ratio

# Configuration
SOURCE_FAMILY_DIR = "/srv/tyche/projects/limen-ai-edge-case-atlas/results/boost/limen-boost-028"
OUTPUT_FILE = "/srv/tyche/projects/limen-ai-edge-case-atlas/results/boost/limen-boost-048/fuzzy-matching-results.tsv"

# Fuzzy matching parameters
THRESHOLD = 85  # Minimum similarity threshold (85/100)
RATIO_FUNC = levenshtein_ratio  # Similarity function (Levenshtein ratio)

# Levenshtein ratio function for fuzzywuzzy
def levenshtein_matcher(query, choices, limit=100):
    return process.extractBests(query, choices, scorer=fuzz.ratio, limit=limit)

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fuzzy matching for evidence overlap detection')
    parser.add_argument('--source-family', type=str, required=True,
                        help='Identifier for the source family')
    parser.add_argument('--evidence-envelope', type=str, required=True,
                         help='Evidence envelope version')
    parser.add_argument('--output', type=str, default=OUTPUT_FILE,
                         help='Output TSV file path')
    args = parser.parse_args()

    # Load source texts (simplified implementation)
    source_texts = []
    for filename in os.listdir(SOURCE_FAMILY_DIR):
        if filename.endswith(".txt"):
            with open(os.path.join(SOURCE_FAMILY_DIR, filename), 'r') as f:
                source_texts.append(f.read().strip())

    # Example: Simulate matching process (replace with actual evidence envelope comparison)
    # In a real implementation, this would compare against the evidence envelope
    # For now, we'll simulate with self-comparison
    matches = []
    for text in source_texts:
        # Using Levenshtein ratio for demonstration
        similarity = levenshtein_ratio(text.lower(), text.lower())
        # Record match with similarity score above threshold
        if similarity >= THRESHOLD:
            matches.append((text, similarity))

    # Write results to TSV
    with open(args.output, 'w') as f:
        f.write("Text\tSimilarity\n")
        for match in matches:
            f.write(f"{match[0]}\t{match[1]:.2f}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fuzzy matching for evidence overlap detection')
    parser.add_argument('--source-family', type=str, required=True,
                        help='Identifier for the source family')
    parser.add_argument('--evidence-envelope', type=str, required=True,
                         help='Evidence envelope version')
    parser.add_argument('--output', type=str, default=OUTPUT_FILE,
                         help='Output TSV file path')
    args = parser.parse_args()

    # Load source texts (simplified implementation)
    source_texts = []
    for filename in os.listdir(args.source-family):
        if filename.endswith(".txt"):
            with open(os.path.join(args.source-family, filename), 'r') as f:
                source_texts.append(f.read().strip())

    # Example: Simulate matching process (replace with actual evidence envelope comparison)
    # In a real implementation, this would compare against the evidence envelope
    # For now, we'll simulate with self-comparison
    matches = []
    for text in source_texts:
        # Using Levenshtein ratio for demonstration
        similarity = levenshtein_ratio(text.lower(), text.lower())
        # Record match with similarity score above threshold
        if similarity >= 85:
            matches.append((text, similarity))

    # Write results to TSV
    with open(args.output, 'w') as f:
        f.write("Text\tSimilarity\n")
        for match in matches:
            f.write(f"{match[0]}\t{match[1]:.2f}\n")
