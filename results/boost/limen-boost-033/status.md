## Boost 033 Status – AI Washing Cases

**Artifact**: `candidate-ai-washing-cases.jsonl`

**Paper/Thesis Use**: Supports the *LIMEN AI Edge‑Case Atlas* manuscript section on deceptive AI marketing (AI‑washing) and provides concrete case studies for the *AI Washing* table (Table 3) and dashboard hook.

**Evidence Used**
- Wikipedia summary of AI washing (2026 revision) – provenance recorded.
- Primary sources:
  - Washington Post article via Yahoo Finance (layoff narrative) – media report.
  - Coca‑Cola product press release – media report.
  - SEC enforcement press release – regulatory enforcement.

**Uncertainty / Evidence Tier**
- All sources are publicly verifiable, English language, US jurisdiction. Tier 1 (high confidence) – direct statements from reputable outlets and regulator.

**Visualization / Dashboard Hook**
- Dashboard view `ai-washing-cases` in `limen-dashboard` (see `dashboard/limen-dashboard-spec-v0.1.md`).
- Columns: ID, Title, Claim Summary, Source URL, Evidence Tier, Notes.
- Intended for interactive filtering by jurisdiction, evidence tier, and claim type.

**Next Smallest Publishability Move**
- Draft *Table 3 – AI Washing Case Studies* for inclusion in the manuscript (see `draft/preprint.md` placeholder).
- Verify URLs and archive with perma.cc; add DOI placeholders.
- Prepare a short narrative linking AI washing to policy implications (e.g., SEC enforcement) for the *Policy Implications* subsection.
