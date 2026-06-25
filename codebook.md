## LIMEN Edge-Case Atlas Codebook

### Figure 2: Denominator Calculation
**Description**: Methodology for computing denominators in Figure 2 (Dashboard/Paper Parity Check)

**Data Sources**:
1. `crosswalk-delta.tsv` (Evidence distribution)
2. `source-crosswalk-v0.2.tsv` (Source metadata)

**Calculation Steps**:
1. Aggregate evidence counts by source family
2. Filter sources with complete jurisdiction metadata
3. Compute total usable evidence pool = Σ(evidence counts) where source has both jurisdiction and evidence tier
4. For each visualization unit (country/jurisdiction):
   - Numerator = Evidence count matching unit
   - Denominator = Total usable evidence pool
   - Display Ratio = Numerator / Denominator

**Adjustments**:
- Exclude entries with `jurisdiction: unknown`
- Weight adjustment for multilingual sources (see Language Coverage Matrix)

**Validation Checks**:
1. Check total evidence pool consistency across Figures 2, 5, 7
2. Verify jurisdiction-source mapping in source-crosswalk-v0.2.tsv
3. Cross-reference with dashboard-spec.md Figure 2 requirements
