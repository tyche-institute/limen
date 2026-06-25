#!/usr/bin/env python3
"""
Small script to detect duplicate source titles in sources/sources.md.
Normalizes titles by lowercasing and stripping punctuation.
Reports any duplicates found.
"""
import re
import sys
from collections import defaultdict

def normalize(title):
    # Lowercase and remove punctuation (keep alphanumerics and spaces)
    title = title.lower()
    title = re.sub(r'[^\w\s]', '', title)
    return title.strip()

def main():
    path = "/srv/tyche/projects/limen-ai-edge-case-atlas/sources/sources.md"
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        sys.exit(1)

    # Pattern to capture bolded title: **Title**
    title_pattern = re.compile(r"\*\*(.+?)\*\*")

    titles = []
    # Each source entry appears to have a line like " 6|6. **EU AI Act Enforcement Mechanisms**..."
    # We'll collect the bolded part from each line that contains it.
    for line in lines:
        m = title_pattern.search(line)
        if m:
            raw_title = m.group(1)
            titles.append(raw_title)

    # Count occurrences
    counts = defaultdict(list)
    for title in titles:
        norm = normalize(title)
        counts[norm].append(title)

    # Find duplicates (normalized count > 1)
    duplicates = {norm: titles for norm, titles in counts.items() if len(titles) > 1}

    if duplicates:
        print("=== Duplicate Source Titles Detected ===")
        for norm, orig_titles in duplicates.items():
            print(f"Normalized title: '{norm}'")
            for orig in orig_titles:
                print(f"  - {orig}")
        print("\nDuplicate detection complete.")
    else:
        print("No duplicate source titles found.")
        print("Duplicate detection complete.")

if __name__ == "__main__":
    main()