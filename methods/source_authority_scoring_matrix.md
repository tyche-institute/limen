# Source Authority Scoring Matrix v0.1

This matrix defines criteria and weights for evaluating the authority of sources in the LIMEN AI Edge-Case Atlas. Scores are calculated on a 0-1 scale where 1 represents maximum authority.

## Scoring Criteria

| criterion                | weight | description                                                                 | example score |
|--------------------------|--------|-----------------------------------------------------------------------------|---------------|
| Official public portal   | 0.35   | Government or institutional website (.gov, .edu, etc.)                   | 0.9          |
| Regulatory mention       | 0.25   | Source is cited in legal/regulatory documents                           | 0.8          |
| Academic publication      | 0.15   | Peer-reviewed journal or conference paper                                | 0.7          |
| Media outlet (verified)   | 0.10   | Established news organization with verifiable editorial process          | 0.6          |
| Crowdsourced platform      | 0.05   | Wikipedia, crowdsourced databases                                        | 0.4          |

## Application Process

1. Identify source type
2. Evaluate against criteria
3. Calculate weighted score: Σ(criterion_score * weight)
4. Apply confidence multiplier based on language translation (0.7-1.0)

## Example Application

For a blocked Estonian government portal:
- Official public portal: 1.0 * 0.35 = 0.35
- Regulatory mention: 0.8 * 0.25 = 0.2
- Media mentions: 0.6 * 0.10 = 0.06
- **Total before translation: 0.61**
- Translation confidence: 0.85
- **Final score: 0.61 * 0.85 = 0.5185**

## Dashboard Integration

This matrix will populate:
1. Source Authority Matrix (Table 2)
2. Evidence Coverage Map (Map 3)
3. Confidence scoring in source ledger entries