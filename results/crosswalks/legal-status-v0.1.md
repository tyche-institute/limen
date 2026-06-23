# LIMEN legal/normative crosswalk status v0.1

Date: 2026-06-08
Project: `limen-ai-edge-case-atlas`
Cycle sync note: 2026-06-08T21:14:56Z
Canonical matrix/queue basis: `results/crosswalks/legal-normative-crosswalk-v0.1.tsv` + `results/crosswalks/legal-case-review-board-v0.1.tsv` checked at 2026-06-08T21:14:56Z
Primary lane this cycle: `limen-legal-normative-crosswalk`

## Why this status file changed

The canonical legal denominator remains stable, but the research-integrity blocker has now crossed from source-depth description into explicit admission logic. The legal matrix still correctly keeps `research_integrity` outside the seeded legal case board, yet the lane now also preserves a bounded rule for how one authority-scored exemplar could be admitted later without converting publisher notice text into a misconduct or legal-status finding.

This pass is a bounded admission-logic upgrade only. It does not add a new source, a new seeded row, a broader direct EU AI Act anchor, or any stronger legal/compliance/misconduct conclusion. It shifts the blocker from “the lane still needs explicit admission logic or stronger institutional evidence” to the narrower “the rule now exists, but no exemplar has yet been admitted under it and no stronger institutional record has displaced notice-text depth.”

## Legal/normative package covered by this index

Primary legal front door:
- `results/crosswalks/legal-status-v0.1.md`

Shared crosswalk index:
- `results/crosswalks/status.md`

Core package:
- `results/crosswalks/legal-normative-crosswalk-v0.1.tsv`
- `results/crosswalks/legal-frontier-priority-board-v0.1.tsv`
- `results/crosswalks/legal-safe-claim-board-v0.1.tsv`
- `results/crosswalks/legal-case-review-board-v0.1.tsv`
- `results/crosswalks/legal-document-depth-board-v0.1.tsv`
- `results/crosswalks/legal-category-document-depth-summary-v0.1.tsv`
- `results/crosswalks/legal-framework-anchor-pressure-board-v0.1.tsv`
- `results/crosswalks/legal-review-owner-load-board-v0.1.tsv`
- `results/crosswalks/legal-framework-family-directness-board-v0.1.tsv`
- `results/crosswalks/legal-framework-anchor-quote-register-v0.1.tsv`
- `results/crosswalks/legal-document-anchor-gap-board-v0.1.tsv`
- `results/crosswalks/legal-uncertainty-queue.md`
- `results/crosswalks/legal-review-frontier-v0.1.tsv`
- `results/crosswalks/framework-anchor-coverage-v0.1.tsv`
- `results/crosswalks/legal-claim-ceiling-board-v0.1.tsv`

## Package snapshot

- `legal-normative-crosswalk-v0.1.tsv` still contains 15 category rows.
- Seed posture remains explicit: 12 seeded rows and 3 zero-seed or shadow-package rows.
- Review priorities remain: High = 10; Medium = 5.
- The live extracted case-level review board currently contains 30 category-case rows spanning 17 unique sampled case references.
- Direct local EU AI Act primary-text anchoring remains narrow: `deepfake_or_synthetic_identity` only.
- Non-ISO direct framework-family coverage remains explicit in `results/crosswalks/legal-framework-family-directness-board-v0.1.tsv`: EU AI Act = 1 category, NIST AI RMF = 4, OECD = 7, UNESCO = 5.
- `results/crosswalks/legal-framework-anchor-quote-register-v0.1.tsv` still materializes 11 short bounded excerpts across the five already-used framework families so later prose can cite exact wording without re-opening the underlying public pages.
- `results/crosswalks/legal-document-anchor-gap-board-v0.1.tsv` now correctly shows 2 categories with `all_sampled_rows_have_direct_document_anchors`, 7 with `mixed_direct_document_and_gap_state`, and 6 with `no_direct_document_anchor_visible`.
- Category-depth front door remains stable in the canonical legal TSV: 9 categories show `document_grade_present`; 2 remain `summary_only` (`agentic_control_failure`, `security_risk`); 1 remains `no_local_authority_refs`; and 3 remain zero-seed/shadow-package placeholders.
- `research_integrity` remains one of those zero-seed/shadow-package rows, but it now also has an explicit bounded seed-admission rule at `results/boost/limen-legal-normative-crosswalk/research-integrity-seed-admission-rule-v0.1.md`: one archived NEJM direct notice plus two Springer direct notices exist locally, yet the lane still withholds seeded legal-family closure until one exemplar is actually admitted under that rule or a stronger institutional record lands.
- The repaired board now keeps `security_risk` and `agentic_control_failure` below direct legal/official document-anchor closure, keeps `public_sector_misuse_or_gap` mixed because the Danish row is still summary-page depth, and keeps ORION as an official-companion row rather than a document-grade closure claim.
- ISO/IEC 42001 overview anchoring still spans all 15 rows and should remain read as management-system framing rather than legality, compliance, or certification proof.
- The only row without any non-ISO direct framework-family anchor remains `residual_unclassified`.
- `institutional_absurdity` preserves the Finland mixed-authority explanation: direct Yle phenomenon text plus indirect official actor-role and ministry-governance context, still short of same-event official corroboration.

## Why this matters for review

- Reviewer-facing legal front doors now tell the same truthful anchor-depth story and the same truthful admission-logic story.
- This reduces the risk that later manuscript, dashboard, reviewer-response, or thesis prose either overstates where direct legal/official document text exists or improvises an unsafe promotion rule for research-integrity rows.
- The package remains claim-conservative: this is an admission-logic upgrade, not a seeded-row promotion or doctrinal-closure upgrade.

## Durable delta this cycle

1. Wrote `results/boost/limen-legal-normative-crosswalk/research-integrity-seed-admission-rule-v0.1.md`, `results/boost/limen-legal-normative-crosswalk/research-integrity-seed-admission-audit-2026-06-08T21-14-56Z.tsv`, and `results/boost/limen-legal-normative-crosswalk/cycle-2026-06-08T21-14-56Z.md` as the machine-readable and narrative audit trail for this threshold-changing rule.
2. Refreshed `results/crosswalks/legal-normative-crosswalk-v0.1.tsv`, `results/crosswalks/framework-anchor-coverage-v0.1.tsv`, `results/crosswalks/legal-frontier-priority-board-v0.1.tsv`, `results/crosswalks/legal-safe-claim-board-v0.1.tsv`, and `results/crosswalks/legal-claim-ceiling-board-v0.1.tsv` so the legal package now states that the rule exists while keeping the row zero-seed.
3. Refreshed `results/crosswalks/legal-uncertainty-queue.md`, `results/crosswalks/status.md`, project `journal.md`, `next.md`, and the lane status/journal pair so the blocker shift is visible from the front doors.

## Paper-readiness delta this cycle

LIMEN's legal package is safer for hostile-reviewer reuse because the research-integrity row and its helper surfaces no longer stop at source-depth description alone. Methods, appendix notes, dashboard panels, reviewer response, and thesis prose can now say that bounded non-Springer direct notice text exists locally and that a lane-local bounded admission rule exists, while still preserving the stronger caution that legal-family seeding and misconduct conclusions remain out of scope until a named exemplar is admitted or stronger institutional evidence lands.

## Claims verified, rewritten, or dropped

Verified / retained:
- The legal package still contains 15 category rows.
- The live extracted legal case board now verifies at 30 category-case review rows and 17 unique sampled case references.
- The sampled Langflow row still appears consistently as an authority-summary `T3_authoritative_source` row backed by reviewed-advisory plus CVE/OSV support.
- The quote register still carries 11 short direct excerpts across EU AI Act, NIST AI RMF, OECD, UNESCO, and ISO/IEC 42001 overview surfaces.
- `research_integrity` now correctly states that the local shadow package already contains one archived NEJM direct notice plus two Springer direct notices, and that a bounded admission rule now exists while seeded legal-family closure remains withheld.
- `security_risk` and `agentic_control_failure` remain summary-only in the direct-document board despite direct public CVE/advisory text.
- `public_sector_misuse_or_gap` remains mixed because the Danish AI-SU row is still summary-page depth.
- ORION remains a bounded police-plus-CORDIS-plus-partner public chain and official-companion row, not procurement, deployment, legality, proportionality, or effectiveness proof.
- The Finland appeals row remains mixed-authority support only: direct broadcaster text plus indirect official context, not same-event official corroboration.

Rewritten / clarified:
- The primary legal front door now matches the live research-integrity blocker state rather than the older no-non-Springer-direct-notice wording.
- Queue-pressure prose now separates bounded direct publisher notice depth from actual seeded legal admission.
- The package now exposes an explicit bounded rule for future exemplar admission instead of leaving that logic implicit.

Dropped / avoided:
- no new crawl;
- no new multilingual-authority bridge row;
- no new seeded-case promotion;
- no widening of misconduct, procurement, deployment, legality, proportionality, effectiveness, compliance, or liability claims;
- no claim that rule creation implies seeded legal admission.

## Remaining blocker

The next substantive gain still requires one threshold-changing companion rather than another packaging pass: one ORION-specific procurement/register/technical, audit, evaluation, or court-facing document; one later official operational/DPIA/procurement/evaluation surface for the Danish AI-SU row; one phenomenon-specific Finnish police/court/ombudsman/ministry companion for `LMWCS-20260606-001`; one document-grade legal-text improvement for the unlawful/deepfake/procedural/education frontier; one provider/deployer postmortem or stronger technical-authority layer for the security/agentic frontier; and, for research integrity, either one actual rule-applied exemplar or one stronger institutional investigation/provenance record beyond direct publisher notice text.
