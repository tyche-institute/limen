# Taxonomy Validation Note: Security Failure Categories (Theme 004)

## Schema Version
- Version: 2.3
- Date: 2026-06-23

## Category Definitions
1. **Data Poisoning**
   - Description: Malicious alteration of training data to degrade model performance
   - Verification Status: Schema validated
   - Example Count: 15 cases
   - Notes: Requires explicit evidence of intent

2. **Model Inversion**
   - Description: Extracting training data through model queries
   - Verification Status: Schema validated
   - Example Count: 8 cases
   - Notes: Often overlaps with privacy violations

3. **Adversarial Examples**
   - Description: Crafted inputs causing unintended model behavior
   - Verification Status: Schema validated
   - Example Count: 22 cases
   - Notes: Must demonstrate real-world impact

## Verification Progress
- Total Cases Reviewed: 45
- Cases Needing Further Verification: 12 (marked in candidate-cases.jsonl)
- Schema Validation Status: ✅ Green

## Next Steps
- Complete original source verification for remaining 12 cases
- Generate "Agentic-Control Failures by Regulatory Domain" table
- Crosswalk with OECD AI Risk Matrix (planned for 2026-06-24)

## Stakeholders
- Primary: LIMEN Manuscript Authors
- Secondary: GAIA/PALLAS Integration Team