## LIMEN Methods Draft: Evidence-Tier Synchronization and Claim-Ceiling Architecture

### 1. Evidence-Tier Synchronization
LIMEN employs a multi-tiered evidence framework to ensure traceability and robustness:

#### 1.1 Evidence Tier Definitions
- **Tier 0 (Direct Source)**: Public/open records with verbatim text from authority sources (e.g., regulator orders, publisher notices)
- **Tier 1 (Derivative)**: Structured representations derived from Tier 0 sources
- **Tier 2 ( Aggregated)**: Crosswalks and composite views

#### 1.2 Synchronization Process
1. **Source Capture**: Use Crossref/DOI lookups and public API harvesting
2. **Tier Alignment**: Ensure semantic consistency across tiers
3. **Drift Detection**: Regularly check for stale or mismatched entries
4. **Propagation**: Update downstream consumers when Tier 0 sources change

### 2. Claim-Ceiling Architecture

#### 2.1 Claim Classification
- **Type A**: Directly supported by Tier 0 sources
- **Type B**: Supported by Tier 1/2 with traceability
- **Type C**: Methodological assertions

#### 2.2 Ceiling Enforcement
1. **Bound Checking**: Prevent overstatement beyond evidence tiers
2. **Confidence Levels**: high/medium/highCaution
3. **Boundary Markers**: Explicit warnings for non-authoritative claims

### 3. Validation Procedures
- Regular integrity checks between tiers
- Automated flagging of violated claim ceilings
- Manual review of high-importance claims

### 4. Current Implementation
See `nejm-archive-propagation-audit.tsv` for recent synchronization examples.