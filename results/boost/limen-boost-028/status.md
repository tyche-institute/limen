## Status Report – LIMEN Boost Shard 028 (Theme 4)

**Paper/Thesis Use:**  Section 4 (Methods) – “Security and Agentic‑Control Failure Cases” draft for the AI Edge‑Case Atlas.

**Evidence Used:**  Four source entries from `sources/security-agentic-failures.tsv` covering EU AI Act security provisions, MITRE Secure AI Framework, NIST AI RMF security controls, and a global case study of autonomous payment errors.

**Uncertainty & Evidence Tier:**
- Regulatory (EU AI Act) – Tier B (authoritative official regulation).
- Industry‑standard (MITRE) – Tier C (well‑known but not legally binding).
- Government guideline (NIST) – Tier B.
- Case study – Tier C, limited peer‑review.

**Visualization / Dashboard Hook:**  Add a “Security Failure Catalog” widget to the Tyche Dashboard (see `dashboard-hook.md`). It will ingest `candidate-cases.jsonl` to display sortable table with columns Title, Jurisdiction, Tier, and Notes.

**Next Smallest Publishability Move:**  Draft Table 2 for the manuscript (list of security‑related edge cases) and prepare a brief narrative paragraph linking each case to the broader claim that “AI systems lack robust agentic safeguards”.
