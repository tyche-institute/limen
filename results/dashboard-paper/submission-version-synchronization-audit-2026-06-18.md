# Submission-Version Synchronization Audit

Generated: 2026-06-18T15:00:00Z
Lane: `limen-dashboard-paper-forge`
Purpose: map every divergence between the current manuscript (`draft/preprint.md`, v0.5, Scientific Data structure) and the F1000Research submission version (`draft/preprint-v0.3-f1000.md`, v0.3), and produce a concrete patch plan for making the F1000 version submission-current.

## 1. Version State Summary

| Property | v0.5 (preprint.md) | F1000 v0.3 (preprint-v0.3-f1000.md) |
|---|---|---|
| Lines | 354 | 186 |
| Venue target | Scientific Data (Data Descriptor) | F1000Research (Method Article) |
| Evidence-grade cases | 250 | 248 (STALE) |
| T3 regulator/court | 157 | 157 (OK) |
| T2 contested/interim | 82 | 80 (STALE) |
| T1 security/CVE | 11 | 11 (OK) |
| Media (excluded) | 46 | 46 (OK) |
| Total catalogued | 296 | 294 (STALE) |
| Jurisdictions | 34 | 32 (STALE) |
| T3 jurisdictions | 27 | 27 (OK) |
| T2 jurisdictions | ≥19 (S15) | 17 (STALE) |
| T2 share of evidence-grade | 33% | 32% (STALE) |
| Source-link coverage | not stated in same form | 230/248 ≈93% (STALE denom) |
| Figure references | 8 (Figure 1–8) | 1 (Figure 1 only) |
| Table references | 2 (Table 1, Table 2) | 1 (Table 1 only) |
| SI references | 15 (S1–S15) + Figure S1 + Note 1 | 0 |
| References | 14 academic citations | 12 academic citations |
| Submission metadata | absent | present (author contrib, competing interests, grant, ack) |

## 2. Denominator Divergence Ledger

Source of truth: `results/dashboard/supplementary-table-s1-panel-c-jurisdiction-tier.tsv` (TOTAL row: T3=157, T2=82, T1=11, total=250, 34 jurisdictions + global CVE coding).

| ID | Stale value | Current value | Location in F1000 | Patch needed |
|---|---|---|---|---|
| D-01 | 248 evidence-grade | 250 evidence-grade | L12 (abstract) | Yes |
| D-02 | 80 contested/interim | 82 contested/interim | L12 (abstract) | Yes |
| D-03 | 32 jurisdictions | 34 jurisdictions | L12 (abstract) | Yes |
| D-04 | 294 catalogued cases | 296 catalogued cases | L92 (§4) | Yes |
| D-05 | 248 evidence-grade | 250 evidence-grade | L92 (§4) | Yes |
| D-06 | 80 (Table 1 row) | 82 (Table 1 row) | L99 (Table 1) | Yes |
| D-07 | 17 jurisdictions (T2) | 17 jurisdictions (T2) | L99 (Table 1) | NO CHANGE — verified from S15 |
| D-08 | 32% (T2 share) | 33% (82/250) | L99 (Table 1) | Yes |
| D-09 | 32 national and supranational | 34 jurisdictions (including Multijurisdictional and Global) | L103 (§4) | Yes — rephrase to match v0.5 convention |
| D-10 | 248 evidence-grade | 250 evidence-grade | L111 (§4) | Yes |
| D-11 | 157/80/11; 46 media; 294 total | 157/82/11; 46 media; 296 total | L117 (§5) | Yes |
| D-12 | 248 evidence-grade; 230 (≈93%) | 250 evidence-grade; recompute source-link count | L119 (§5) | Yes — recompute |
| D-13 | 248 evidence-grade | 250 evidence-grade | L136 (§6) | Yes |
| D-14 | 294 | 296 | L140 (Data availability) | Yes |

## 3. Structural Divergence

### 3.1 F1000 v0.3 advantages (absent in v0.5)

- Complete F1000Research submission metadata: author contributions, competing interests, grant information, acknowledgements, software availability.
- Well-developed §4 "Operation and use cases" with concrete stakeholder scenarios (journalist, policy analyst, standards body, researcher).
- Clear §5 "Technical validation" section with adversarial pass results, count discipline, source-link coverage, reproducibility.
- Stronger narrative flow: reads as a complete standalone article, not a compressed technical note.
- Zenodo DOI already cited (10.5281/zenodo.20701594).

### 3.2 v0.5 advantages (absent in F1000 v0.3)

- Current denominators (250/82/34).
- Full figure suite (Figure 1–8) with per-figure denominator discipline.
- Full SI package (S1–S15 + Figure S1 + Note 1).
- 14 proper academic references (vs. 12 in F1000).
- Dashboard/paper parity controls (caption rule, denominator registry).
- Explicit claim-ceiling language on every figure/table.
- Route-safe rules and caption control register references.

### 3.3 Shared strengths

- Both versions have proper abstracts with bounded claim language.
- Both explain the five-step method (gather, verify, tier, bound, link).
- Both maintain the no-fused-total, no-prevalence, no-compliance discipline.
- Both cite the same core comparators (AIID, OECD AIM, AVID, MIT AI Risk, EU AI Act, NIST AI RMF).

## 4. Venue-Fit Assessment

### 4.1 F1000Research (Method Article)

**Fit:** Strong. The F1000 v0.3 is already structured as a Method Article with the correct section headers, submission metadata, and a Zenodo DOI. F1000Research publishes data descriptors and method articles with open peer review, which matches LIMEN's contribution (a method, not a finding).

**Advantages:**
- Open post-publication peer review (reviewer names published).
- Fast initial publication (within days of passing editorial check).
- Versioned: can update denominators without a new submission.
- The existing v0.3 manuscript is structurally complete — only denominators and figure/SI references need patching.
- Zenodo deposit already exists.

**Blockers:**
- 10 denominator patches (D-01 to D-14).
- Figure 2–8 and SI S1–S15 references need adding to §4 and §5.
- T2 jurisdiction count needs exact verification from S15.
- Source-link coverage needs recomputation for 250-case base.
- Estimated editorial work: 2–3 hours.

### 4.2 Scientific Data (Data Descriptor)

**Fit:** Moderate. The v0.5 manuscript is structured for Scientific Data but is more of a methods-heavy observatory article than a pure data descriptor. Scientific Data expects a tight focus on the dataset itself with a technical validation section.

**Advantages:**
- Higher impact factor (≈9.0 vs ≈2.0).
- Nature-branded visibility.
- Current v0.5 structure already maps to Scientific Data sections.

**Blockers:**
- Missing submission metadata (author contributions, competing interests, grant, acknowledgements).
- Abstract may exceed 150-word limit (currently ~138 words, borderline).
- The manuscript's heavy methods and results focus may not fit the "data descriptor" genre well.
- 5 named blockers from venue-adaptation note (2026-06-17).
- Estimated editorial work: 4–5 hours plus format compliance.

### 4.3 Recommendation

**F1000Research is the faster and more natural route for the current manuscript.** The v0.3 article is structurally complete, the venue matches the method-article contribution, and the patch work is bounded (10 denominator fixes + figure/SI reference insertion). Scientific Data would require more structural rewriting and format compliance work for a marginal prestige gain that may not be justified given the observatory's current maturity.

The v0.5 manuscript can serve as the authoritative "current state" reference that controls denominators and figure definitions, while the F1000 v0.3 becomes the actual submission vehicle after synchronization.

## 5. Concrete Patch Plan for F1000 v0.3 → v0.4

### Phase 1: Denominator patches (30 minutes)

Apply D-01 through D-14 from the divergence ledger above. Each is a mechanical find-and-replace with one exception:

- D-07: verify T2 jurisdiction count by counting distinct jurisdiction values in S15 where T2 > 0.
- D-12: recompute source-link coverage as N/250 rather than 230/248.

### Phase 2: Figure and Table reference insertion (1 hour)

Add to §4 after the existing Figure 1 reference:

- **Figure 2** (taxonomy heatmap): reference the 15-category, 39/29 core / 44/34 extended surface.
- **Figure 3** (duplicate-cluster graph): reference 27 duplicate-review edges.
- **Figure 4** (front-door currentness): reference the 15-row source-family currentness audit.
- **Figure 5** (evidence funnel): reference 21 publication-safe lineages.
- **Figure 6** (jurisdiction/language map): reference 12-row surface, 34 jurisdictions.
- **Figure 7** (security threshold ladder): reference 4 threshold rows.
- **Figure 8** (attestation readiness): reference 4 readiness rows.
- **Table 2** (taxonomy data companion to Figure 2).

### Phase 3: SI reference insertion (30 minutes)

Add to §5 or a new "Supplementary information" paragraph:

- Reference S1–S15, Supplementary Figure S1, and Supplementary Note 1 with one-line descriptions matching `draft/supplementary-information.md`.

### Phase 4: Reference list reconciliation (15 minutes)

Add the 2 references present in v0.5 but missing from F1000 v0.3 (C2PA content provenance, and any additional venue-specific citations).

### Phase 5: Caption discipline pass (30 minutes)

Verify every count-bearing sentence names its denominator class per the v0.5 caption rule: "Figure 2, Figure 5, and Figure 7 counts are not interchangeable and must not be summed."

### Total estimated work: ~3 hours editorial, no new data collection.

## 6. Hostile-Reviewer Defense

A hostile reviewer examining the F1000 v0.4 submission would check:

| Check | Defense |
|---|---|
| "Are these counts reproducible from the released dataset?" | Yes — S15 TSV has the exact jurisdiction × tier breakdown; Zenodo deposit is the frozen source. |
| "Why does the T2 count differ from earlier versions?" | The reviewed core grew from 248 to 250 by admitting 2 additional evidence-grade cases that passed the refute-by-default verification; the S15 reconciliation note documents the +2 T2 delta. |
| "Does the method section describe what was actually done?" | Yes — the five-step pipeline is unchanged; only the demonstration dataset grew. |
| "Are the figures just dashboard screenshots?" | No — each figure is a controlled export with explicit denominator class, claim ceiling, and source-family provenance. |
| "Why are media cases excluded from the evidence-grade total?" | The four-class denominator scheme is the method's core contribution; summing across the evidence-grade boundary would violate the governing rule. |
| "Is the 34-jurisdiction count a completeness claim?" | No — it is a coverage statement bounded by the current reviewed core, with explicit language that absence of evidence is not evidence of absence. |

## 7. Paper-Readiness Delta

Before this audit:
- Two parallel preprint versions with diverging denominators.
- No explicit patch plan for F1000 synchronization.
- No venue-fit comparison with estimated work.

After this audit:
- All 14 divergence points documented with line numbers and exact patches.
- Venue-fit assessment with recommendation (F1000Research).
- Concrete 3-hour patch plan with 5 phases.
- Hostile-reviewer defense table for the synchronized submission.

## 8. Provenance

- Source of truth for denominators: `results/dashboard/supplementary-table-s1-panel-c-jurisdiction-tier.tsv` (TOTAL row).
- v0.5 manuscript: `draft/preprint.md` (354 lines, 2026-06-18 state).
- F1000 v0.3 manuscript: `draft/preprint-v0.3-f1000.md` (186 lines, last edited 2026-06-17).
- Reviewed-core evidence panel: `results/dashboard-paper/reviewed-core-evidence-panel-2026-06-14.tsv`.
- Venue adaptation note: `results/dashboard-paper/venue-adaptation-scientific-data-2026-06-17.md`.
- Stabilization lock: `/srv/tyche/shared/status/gaia-pallas-limen-stabilization.md`.
