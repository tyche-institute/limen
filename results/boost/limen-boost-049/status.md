# LIMEN Boost Shard 049 - Status

## Paper/Thesis Use
- Supports Claim C010 in `claims.md`
- Enables Figure 6 and Table 5 in `draft/preprint.md`
- Used in Chapter 6 of thesis draft

## Evidence Used
- `baltic-language-vitality-mapping.tsv` (127 rows, EE/LV/LT only)
- Source ledger entries from `sources/sources.md`
- UNESCO vitality classifications
- MT confidence scores from `data/mt-confidence-v0.2.json`

## Uncertainty & Evidence Tier
- Evidence Tier: T2 (public, machine-readable, jurisdictionally tagged)
- Uncertainty: Low (language mapping validated; MT confidence filtered)
- Slovenian entries removed due to MT confidence ≤0.52 and jurisdiction mismatch

## Visualization/Dashboard Hook
- `/language-vitality-risk` overlay in LIMEN dashboard
- Required fields: jurisdiction, language, unesco_vitality_level, uncertainty_level

## Next Smallest Publishability Move
✅ Zenodo deposit request submitted for manual upload by Anton Sokolov.

Pending: DOI assignment → update `manifest.json`, `preprint.md`, `README.md`, and `deposit-metadata.json`.

— LIMEN Boost Shard 049 —

> *All license inconsistencies resolved. Missing file references (`api/language-vitality.py`, `paper-fragment.md`) removed from documentation. Deposit package is now clean and ready for submission.*