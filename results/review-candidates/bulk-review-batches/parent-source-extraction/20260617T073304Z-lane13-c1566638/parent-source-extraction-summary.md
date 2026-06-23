# Parent source extraction summary

Batch: 20260617T073304Z-lane13-c1566638
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073304Z-lane13-c1566638/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T073304Z-lane13-c1566638/parent-source-extraction-results.tsv

Reviewed rows: 24
Output rows: 24

Verdict counts:
- source_url_extracted: 1
- country_gap_no_parent_source: 23

Notes:
- Used local metadata/source files only.
- Most rows were generated country query/profile/score placeholders without a concrete parent source URL.
- BPSE-03074 had an explicit local I03 source entry and URL in the country object.
