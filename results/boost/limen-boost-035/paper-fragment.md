# Singleton-aware figure patch note

## Core finding

The live duplicate-control package already covers 30 visible rows and 23 unique lineages, but lane-011 publication-safe aggregate and authority-balance surfaces still materialize only 21 lineages. The lag is now narrowly attributable to two already-reviewed singleton rows:

- `data/cases/authoritative-candidates.jsonl:LIMEN-000008` — FCC / Lingo Telecom deepfake robocall enforcement.
- `data/cases/security-agentic-candidates.jsonl:LIMEN-000009` — PraisonAI ownership-assignment abuse.

## Figure/Table consequence

If these two singleton rows propagate into the lane-011 safe aggregate without changing any merge decision or evidence tier:

- Figure 5 moves from `21` to `23` publication-safe lineages.
- Figure 5 confidence overlay moves from `15 high / 0 medium / 6 low` to `17 high / 0 medium / 6 low`.
- Figure 7 authority-balance panel moves from `7 authority-anchor / 7 technical-authority / 1 translation-caution authority / 6 provisional` to `8 / 8 / 1 / 6`.

## Why this is reviewer-safe

- Both rows already have explicit duplicate-control state `no_cluster_review_row` in `results/clusters/duplicate-clusters-v0.1.tsv`.
- Neither row requires a new same-event merge claim.
- Neither row weakens the low-confidence or translation-caution boundaries; both are already high-cap rows.
- The projection is a synchronization move, not corpus growth.

## Paper/thesis use

- Methods/data paper: exact patch note for Figure 5 and Figure 7 denominator inheritance.
- Thesis evidence-infrastructure chapter: concrete example of how singleton propagation changes interpretation without changing facts.
- Dashboard build: use as a gate before reusing lane-011 funnel and authority-balance captions.

## Next smallest publishability move

Patch the shared Figure 5 / Figure 7 prose layer only after lane-011 aggregate and authority-balance files materialize the projected 23-lineage state, so manuscript and dashboard captions inherit a file-backed contract rather than a forecast.
