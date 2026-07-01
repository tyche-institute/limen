# Figure 2: Taxonomy Heatmap of AI Edge Cases in Public-Sector Contexts

## Description

The taxonomy heatmap visualizes AI edge cases in public-sector systems, showing support counts (N) and evidence tier information. Each cell represents a category of edge cases with the following details:

- **Support Count (N)**: Number of evidence instances for the category.

- **Evidence Tier**: Tier of the evidence (Tier I, II, or III) indicating its authority and reliability.

- **Fragility Flag**: Indicates whether the category is considered "fragile" (e.g., based on low redundancy or single-source evidence).

- **Caption Sentence**: A concise description of the category for use in figures and tables.

## Table 2 Support-State Ledger

A detailed ledger providing additional context for each category in the heatmap:

| taxonomy_surface_id                | support_count | aid_authority_tier | translation_burden | fragility_flag | table2_visible | caption_sentence |
|----------------------------------|---------------|--------------------|--------------------|----------------|----------------|------------------|
| legal_procedural_contamination    | 3             | Tier II           | high              | true           | true           | Procurement processes with legal procedural contamination |
| ai_washing_or_false_ai_claim      | 6             | Tier I            | low               | false          | true           | Claims of AI usage that are overstated or unspecified      |
| health_medical_or_mental_health    | 0             | Tier 3            | N/A               | false          | false          | (Zero-seed: No evidence found in Baltic jurisdictions 2020–2026) |
| research_integrity                 | 0             | Tier 3            | N/A               | false          | false          | (Zero-seed: No evidence found in Baltic jurisdictions 2020–2026) |
| residual_unclassified               | 2             | Tier 2            | medium            | true           | true           | Unclassified AI edge cases not fitting primary categories       |

## Denominator Synchronization

The heatmap is synchronized with the live taxonomy contract at 33 visible rows / 25 lineages as of 2026-06-30. This ensures alignment between the visual representation and the underlying evidence base.