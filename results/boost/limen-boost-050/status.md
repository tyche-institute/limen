## LIMEN Boost Shard 050 — Caucasus/Central Asia Language Vitality Delta

Cycle start: 2026-06-25
Lane rule load: hostile-reviewer-pass sprint lock (`current-publication-sprint.md` 20260607-hostile-reviewer-pass)
Sprint override: parole‑bounded harvesting only; no fused denominators; no rankings; no claims beyond source evidence.

### Status
- Paper/Thesis Fit: LIMEN Chapter 6 (Language Vitality) + ISO/IEC 42001 Annex D snippet
- Evidence Base: 5 Caucasus/Central Asia edge-case pointers (Armenian, Georgian, Kazakh, Uyghur, Kurdish Kurmanji) drawn from public sources; translation confidence proxies included; UNESCO vitality tiers mapped
- Visualization hooks: Language Vitality Risk Overlay (`languageRiskOverlay`) with new `language_risk_status` field for Jurisdiction/Language Matrix; hook specified in `dashboard-hook.md`
- Uncertainty & Tier: Tier 2–3 (moderate→low); uncertainty due to machine-translation proxies, redacted text, paywalls; documented in `language-vitality-delta-caucasus-central-asia.tsv` and `sources/sources.md`

### Artifacts delivered in this cycle
- new TSV: `data/caucasus-central-asia-language-vitality-delta.tsv`
- new TSV: `data/translation_review_queue.tsv` (added flagged rows for hostile‑reviewer route)
- ledger: `sources/sources.md` updated
- dashboard: `results/boost/limen-boost-050/dashboard-hook.md`
- paper frag: `results/boost/limen-boost-050/paper-fragment.md`
- cycle journal: `results/boost/limen-boost-050/journal.md`
- status: this file

### Next Hostile-Reviewer-safe publishability move (tight scope)
1. Submit `data/caucasus-central-asia-language-vitality-delta.tsv` to Zenodo with minimal schema; flag dataset as work-in-progress under copyright license CC-BY-4.0 (INTERNAL-LIMEN only).  
2. Patch `draft/preprint.md` Subsection 6.2 with Caucasus/Central Asia sample and uncertainty footnotes. Include the five sample IDs and vitality risk flags inline.
3. Patch `dashboard-specification.md` to register the new overlay schema key `language_risk_status` and color map.
4. Hostile-reviewer proof: keep every causal sentence bounded by "indicates" or "suggests"; provide evidence tier table and provenance footnote.

### Compliance & boundaries checklist  
- [x] Only public/open sources used
- [x] No private victim data
- [x] No credentials/tokens stored
- [x] No compliance/certification claims made
- [x] Machine translation clearly labeled; translation confidence capped at <=0.5 as flag threshold
- [x] No bulk download expansion; corpus frozen for sprint
- [x] Datasets carry provenance, access date, language, jurisdiction, rights notes
- [x] Hostile-reviewer prose drafted with uncertainty guardrails
- [x] Sprint lock boundaries respected (hostile reviewer pass, no fused denominators)

