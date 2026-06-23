# LIMEN full-manuscript sentence-level denominator lint v0.6

Updated UTC: 2026-06-18T19:10:00Z
Lane: `limen-dashboard-paper-forge`

## Purpose

Run the v0.5 next-step lint against `draft/preprint.md`, focusing on Figure 2, Figure 5, Figure 7, count-bearing sentences, and forbidden-overread language. This is a manuscript safety artifact, not a new evidence collection pass.

## Canonical denominator source

- `results/boost/limen-dashboard-paper-forge/figure2-5-7-denominator-binding-register-v0.4.tsv`
- Figure 2: live core `39 governed record refs / 29 unique lineages`; extended `44 / 34`; mechanical `35 / 27` legacy/provenance only.
- Figure 5: `21` collapsed publication-safe lineages; confidence/translation bands are ceilings, not weights.
- Figure 7: threshold ladder is `4` rows; authority-balance sidecar is default visible `21` lineages with projected `23` lineages only.

## Lint result

- Count-bearing / figure / denominator candidate sentences scanned: `117`.
- Sentences requiring rewrite or explicit guardrail before lint patch: `18`.
- Draft patched in this cycle: `yes`.

## Findings and actions

| line | finding | action |
|---:|---|---|
| 50 | Possible forbidden-overread term without local negation/ceiling language<br><br>Instead of claiming completeness or prevalence, LIMEN makes its processing stages, denominator classes, source-family blockers, and claim ceilings explicit enough for a hostile reviewer to audit. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 120 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register<br><br>security crosswalk (Table 5, Figure 7) maps local evidence rows to these frameworks without claiming framework-level coverage. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 146 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register; Figure 7 threshold-row language must be explicitly separated from 21/23 sidecar lineage denominator; Figure 2/Table 2 sentence should name 39/29 live core when count-bearing<br><br>The main package is a controlled visibility stack: a source-family saturation map (Figure 1), a taxonomy heatmap (Figure 2, Table 2), a legal-uncertainty matrix (Figure 3), a duplicate-control graph (Figure 4), a publication-safe lineage funnel (Figure 5), a jurisdiction/language visibility map (Figure 6), and bounded Route B (Figure 7) and Route C (Figure 8) companions for security-threshold routing and attestation trust-surface readiness. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 155 | Figure 2/Table 2 sentence should name 39/29 live core when count-bearing<br><br>/ Surface / Authority file / Denominator class / Manuscript role / / --- / --- / --- / --- / / Figure 2 / Table 2 live taxonomy core / \`results/dashboard/taxonomy-heatmap. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 158 | Figure 2/Table 2 sentence should name 39/29 live core when count-bearing<br><br>tsv\` / 44 governed record refs / 34 unique lineages / Explicitly labeled extended sidecar only / / Legacy mechanical Figure 2 source / Historical provenance (reproducibility package) / 35 visible rows / 27 lineages / Historical provenance only / / Figure 5 publication-safe funnel / \`results/dashboard/evidence-funnel. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 160 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register<br><br>tsv\` / 21 publication-safe lineages / Evidence-maturity and publication-ceiling discussion / / Figure 7 security / agentic threshold ladder / \`results/dashboard/security-threshold-ladder-panel. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 165 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register; Figure 2/Table 2 sentence should name 39/29 live core when count-bearing; Figure 5 sentence should name separate 21 publication-safe lineages or explicitly defer to register<br><br>Figure 2, Figure 5, and Figure 7 counts are not interchangeable, and none of them supports incident prevalence, corpus completeness, legal violation, compliance, certification, safety, or truth claims. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 167 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register; Figure 7 threshold-row language must be explicitly separated from 21/23 sidecar lineage denominator<br><br>Figure 7 remains the bounded 4-row security/agentic threshold companion rather than part of the Route A denominator. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 189 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register; Figure 7 threshold-row language must be explicitly separated from 21/23 sidecar lineage denominator<br><br>Across LIMEN's current eleven-row public security seed, evidence-layer asymmetry is the principal result (Table 5, Figure 7): three rows (LIMEN-000001, LIMEN-000003, LIMEN-000008) sit in the core results bucket because they combine primary CVE text with vendor-authored advisory visibility and exact fix language; eight rows (LIMEN-000002, LIMEN-000004, LIMEN-000005, LIMEN-000006, LIMEN-000007, LIMEN-000009, LIMEN-000012, LIMEN-000016) belong in appendix-supporting results because they depend on reviewed-advisory or source-qualified wording, coordination-plus-CVE-linked fix visibility below formal vendor-bulletin certainty, independent-lab remediation language, a bounded identity-boundary exemplar, or a three-row trust-boundary slice spanning PraisonAI, Playwright MCP, and ToolHive; and one explicit gap row keeps the need for peer-reviewed security case support visible until a live row gains incident-specific support. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 205 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register; Figure 7 threshold-row language must be explicitly separated from 21/23 sidecar lineage denominator<br><br>The Route B threshold ladder (Figure 7, Table 5) remains bounded at 4 rows and is not part of the Route A denominator. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 231 | Figure 2/Table 2 sentence should name 39/29 live core when count-bearing<br><br>The security overlay remains useful because repeated mechanism families can support a Figure 2 or a Route B security inset without implying ecosystem prevalence. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 231 | Possible forbidden-overread term without local negation/ceiling language<br><br>The methods guardrail is that none of these overlays converts into a new top-level category, a prevalence finding, or a corpus-completeness argument. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 250 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register; Figure 2/Table 2 sentence should name 39/29 live core when count-bearing; Figure 5 sentence should name separate 21 publication-safe lineages or explicitly defer to register<br><br>Denominator separation Figure 2, Figure 5, and Figure 7 carry three different denominators that are not interchangeable. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 255 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register; Figure 7 threshold-row language must be explicitly separated from 21/23 sidecar lineage denominator<br><br>Figure 7 uses the bounded 4 threshold rows. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 256 | Possible forbidden-overread term without local negation/ceiling language<br><br>None of these denominators supports incident prevalence, corpus completeness, legal violation, compliance, certification, safety, or truth claims. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 291 | Figure 2/Table 2 sentence should name 39/29 live core when count-bearing<br><br>Several taxonomy categories in Figure 2 remain queue-only or singleton-watch material: \`procedural_hallucination_in_public_process\`, \`detector_governance_and_false_detection_claims\`, \`deepfake_intimate_image_local_abuse\`, and \`residual_unclassified\`. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 304 | Figure 7 citation lacks default 21-lineage / projected 23-lineage sidecar denominator language from v0.4 register<br><br>threshold, Figure 7) retains the explicit gap for peer-reviewed security case support. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |
| 306 | Possible forbidden-overread term without local negation/ceiling language<br><br>scholarly consensus, or ecosystem-wide security prevalence claims. | Patched where the issue concerned Figure 7 4-row threshold versus 21/23 sidecar language; leave other negated ceiling sentences intact. |

## Patch summary

- Patched `draft/preprint.md` Table 1 so Figure 7 names both the 4-row threshold ladder and the separate 21-default / 23-projected sidecar.
- Patched the Figure 7 paragraph in Section 3.1 to expose the authority-balance sidecar denominator wherever Figure 7 is exported.
- Patched Section 4.4 and Limitation 5.1 so Figure 7 threshold rows cannot be silently mistaken for the 21/23 sidecar lineage denominator.

## Negative/limitation record

This cycle did not add new sources, incidents, legal conclusions, compliance conclusions, safety claims, deployment claims, country rankings, or a fused GAIA/PALLAS/LIMEN denominator. The lint only strengthened manuscript denominator grammar.

## Observatory hook

The dashboard export path should attach the v0.4 denominator register as a machine-readable tooltip source for Figures 2, 5, and 7. For Figure 7, the UI should display two stacked labels: `threshold ladder: 4 rows` and `authority-balance sidecar: 21 default / 23 projected` so manuscript exports cannot lose the distinction.

## Post-patch verification

- Figure 7 / Route B candidate sentences scanned after patch: `14`.
- Figure 7 / Route B candidate sentences retained for human review after patch: `5` (all are non-count/general route, table-row split, or data-availability mentions; no additional rewrite was applied in this cycle).

| line | status | sentence |
|---:|---|---|
| 120 | ok | security crosswalk (Table 5, Figure 7 threshold ladder; authority-balance sidecar default 21 / projected 23 lineages) maps local evidence rows to these frameworks without claiming framework-level coverage. |
| 146 | ok | The main package is a controlled visibility stack: a source-family saturation map (Figure 1), a taxonomy heatmap (Figure 2, Table 2), a legal-uncertainty matrix (Figure 3), a duplicate-control graph (Figure 4), a publication-safe lineage funnel (Figure 5), a jurisdiction/language visibility map (Figure 6), and bounded Route B (Figure 7 threshold ladder, with authority-balance sidecar default 21 / projected 23 lineages) and Route C (Figure 8) companions for security-threshold routing and attestation trust-surface readiness. |
| 161 | review | / Figure 7 security / agentic threshold ladder and authority-balance sidecar / `results/dashboard/security-threshold-ladder-panel. |
| 161 | ok | tsv` / 4 threshold rows; sidecar default visible 21 lineages with projected 23-lineage sidecar only / Route B threshold-change logic and sidecar-visible authority-balance transport; not a live 23-lineage default / *Table 1. |
| 165 | ok | Figure 2 live 39/29 and extended 44/34 counts, Figure 5 21-lineage counts, and Figure 7 threshold/sidecar counts (4 threshold rows; 21 default / 23 projected sidecar lineages) are not interchangeable, and none of them supports incident prevalence, corpus completeness, legal violation, compliance, certification, safety, or truth claims. |
| 167 | ok | Figure 7 remains the bounded 4-row security/agentic threshold companion rather than part of the Route A denominator, and any Figure 7 export must separately expose the authority-balance sidecar as default visible 21 lineages with a projected 23-lineage sidecar only. |
| 189 | ok | Across LIMEN's current eleven-row public security seed, evidence-layer asymmetry is the principal result (Table 5, Figure 7 threshold ladder; sidecar default 21 / projected 23 lineages): three rows (LIMEN-000001, LIMEN-000003, LIMEN-000008) sit in the core results bucket because they combine primary CVE text with vendor-authored advisory visibility and exact fix language; eight rows (LIMEN-000002, LIMEN-000004, LIMEN-000005, LIMEN-000006, LIMEN-000007, LIMEN-000009, LIMEN-000012, LIMEN-000016) belong in appendix-supporting results because they depend on reviewed-advisory or source-qualified wording, coordination-plus-CVE-linked fix visibility below formal vendor-bulletin certainty, independent-lab remediation language, a bounded identity-boundary exemplar, or a three-row trust-boundary slice spanning PraisonAI, Playwright MCP, and ToolHive; and one explicit gap row keeps the need for peer-reviewed security case support visible until a live row gains incident-specific support. |
| 191 | review | The Route B threshold contract (Supplementary Table S2) travels with this finding whenever the paper shifts from generic asymmetry prose to venue-fit claims, and the threshold-change matrix (Supplementary Table S3) travels with it whenever the prose shifts from safe current-state interpretation to exact row-level upgrade conditions. |
| 205 | ok | The Route B threshold ladder (Figure 7, Table 5) remains bounded at 4 rows and is not part of the Route A denominator; the Figure 7 authority-balance sidecar must stay captioned as default visible 21 lineages with a projected 23-lineage sidecar only. |
| 231 | review | The security overlay remains useful because repeated mechanism families can support a Figure 2 or a Route B security inset without implying ecosystem prevalence. |
| 252 | ok | Figure 2, Figure 5, and Figure 7 denominator separation is now a single count-bearing sentence with 39/29, 44/34, 21, 4, and 21/23 contracts immediately attached. |
| 255 | ok | Figure 7 uses the bounded 4 threshold rows, with the separate authority-balance sidecar shown as default visible 21 lineages and projected 23-lineage sidecar only. |
| 304 | ok | Route B (security threshold, Figure 7 threshold ladder; sidecar default 21 / projected 23 lineages) retains the explicit gap for peer-reviewed security case support. |
| 394 | review | The reproducibility package — including dashboard exports (taxonomy heatmaps, evidence funnels, source-family coverage maps, security threshold ladders, jurisdiction/language surfaces), the caption-control register, the figure-route registry, and the source-family evidence-policy matrix — is available in the project repository under `results/dashboard/` and `results/dashboard-paper/`. |

## Remaining blocker

Before submission packaging, rerun this lint after any caption, abstract, or figure-number change; also verify that Supplementary Methods and any PDF-rendered captions carry the same 39/29, 21, and 21/23 contracts.
