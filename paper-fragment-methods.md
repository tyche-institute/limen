# Methods: Figure Dataset Generation and Crosswalk Validation

## 1. Figure 2: Edge-Case Coverage Heatmap Update
- Source: `candidate-cases.jsonl` (current boost output)
- Process: Aggregate by jurisdiction/language, map to LIMEN dashboard categories
- Output: `results/boost/limen-boost-016/figure-2-dataset.tsv` (update existing)

## 2. Figure 5: Crosswalk Coverage Matrix
- Source: `crosswalk-delta.tsv`, `source-family-saturation-ledger.tsv`
- Process: Merge with GAIA/PALLAS authority layers, flag low-confidence entries
- Output: `results/boost/limen-boost-016/figure-5-dataset.tsv`

## 3. Figure 7: Claim-Support Flow Validation
- Source: `security-claim-defense-crosswalk.tsv`, `peer-review-gap-frontier-contrast.tsv`
- Process: Validate claim-support links against dashboard implementation
- Output: `results/boost/limen-boost-016/figure-7-validation.md`

## 4. Crosswalk Coverage Matrix Validation
- Compare `crosswalk-table.tsv` against `source-family-saturation-ledger.tsv` for discrepancies
- Flag mismatched source families and authority scores
- Output: `results/boost/limen-boost-016/crosswalk-validation-report.tsv`