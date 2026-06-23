# Security issuer-notice subledger status

Date: 2026-06-07T00:35:02Z
Lane: `limen-continuous-experiments`
Project: `limen-ai-edge-case-atlas`
Sprint: `20260607-hostile-reviewer-pass`

## Artifact created

- `results/security/security-issuer-notice-subledger-v0.1.tsv`

## Paper-readiness delta

- Normalized the scattered security notice layer into one reviewer-legible subledger for Auto-GPT, Langflow, Claude Code, and CrewAI-linked cases.
- Made issuer-interest and authority differences explicit across vendor advisories, a repo issue, and a CERT/CC coordination notice so remediation-timing claims do not collapse into a single authority class.
- Added a table-ready basis for a remediation-timeline overlay and an issuer-vs-CVE comparison panel without changing any case evidence tier.

## Verified counts from the local package

- 5 notice-linked rows normalized.
- 2 rows have clear vendor security advisories.
- 1 row has only a vendor repo issue rather than a formal advisory.
- 2 rows rely on a third-party CERT/CC coordination notice rather than a direct vendor bulletin.
- Notice-presence status split: 4 `yes`, 1 `partial`, 0 `no` in the current local package.

## Claims verified, rewritten, or dropped

Verified:
- the local security package already contains enough public notice metadata to support a dedicated source-family-07 subledger;
- issuer/platform notices are useful for remediation timing and notice depth, but not for stronger comparative safety or prevalence claims;
- CrewAI currently has coordination-center notice depth without a direct vendor bulletin in the local package.

Rewritten into bounded form:
- Langflow remains a repo-issue-only notice layer in this package, so closed-issue status is treated as provenance metadata rather than proof of remediation.
- CERT/CC rows are treated as coordination evidence, not as substitutes for direct vendor fixed-version statements.

## Remaining blocker

Direct CrewAI vendor remediation/version notice depth is still missing, and Langflow still lacks a formal vendor advisory or release-note-grade public notice in the local package.

## Observatory hook

This subledger can feed:

- a remediation timeline overlay (`case_id`, `notice_published_at`, `notice_record_type`, `remediation_detail_visible`);
- an issuer-vs-independent notice comparison table (`issuer_type`, `authority_band`, `notice_exists_status`);
- a manuscript methods/results note on why notice depth should not automatically upgrade evidence tier.
