# LIMEN AI Edge-Case Atlas

Status: launched 2026-06-07
Owner: Tyche Institute
Project id: `limen-ai-edge-case-atlas`

LIMEN is a Tyche evidence observatory for the long tail of AI reality:
obscure, absurd, unlawful, security-sensitive, institutionally strange,
agentic, and norm-breaking uses or misuses of AI that do not fit cleanly
inside ordinary risk categories.

The name comes from Latin `limen`, meaning threshold. The observatory studies
threshold cases: between accident and misuse, joke and harm, private action
and governance problem, software vulnerability and legal incident, novelty
and moral failure. As a working acronym, LIMEN expands to:

Long-tail Incidents, Misuse, Edge-cases, and Normative anomalies.

## Purpose

LIMEN records public-source evidence about AI edge cases, classifies them with
multi-label taxonomies, maps them to existing incident/risk/security/governance
frameworks, and prepares them for later legal, ethical, and attestation
analysis.

It is not a compliance authority, certification body, regulator, threat intel
vendor, or scandal feed. Its job is to make difficult cases observable,
traceable, and comparable without overstating what public evidence proves.

## Core Outputs

- public-source family map;
- LIMEN case schema and source schema;
- anomaly/misuse/security/normative taxonomy;
- crosswalks to AIID, OECD AIM, AVID, MIT AI Risk Repository, CSET AI Harm,
 MITRE ATLAS, NIST AI RMF, EU AI Act, ISO/IEC 42001, OWASP LLM/agentic
 security categories, RATS, VC, SCITT, and C2PA;
- evidence-grade case database;
- duplicate/cluster graph;
- legal and ethical mapping queue;
- attestation-ready evidence-envelope profile;
- dashboard-ready maps, timelines, matrices, and paper figures;
- article/data/method paper architecture.

## Evidence Boundary

LIMEN uses public/open sources and local Tyche artifacts. It must not collect
private communications, credentials, private personal data, exploit payloads,
malware, or non-public victim material. It records source claims, evidence
quality, and uncertainty. It does not declare illegality, liability,
non-compliance, guilt, or official incident status unless an authoritative
source has already done so.

Raw crawling and large data stay on the project's working infrastructure. This
public repository holds schemas, methods, taxonomies, source-family ledgers, an
example public-source case record, and other public-safe artifacts.

## Repository Files

- `schema/limen-case.schema.json` - case-record schema.
- `taxonomy/taxonomy-v0.1.md` - multi-label taxonomy and evidence tiers.
- `sources/public-source-families-v0.1.tsv` - source-family ledger.
- `methods/evidence-protocol-v0.1.md` - ingestion, review, and safety rules.
- `attestation/evidence-envelope-v0.1.md` - attestation evidence-envelope profile.
- `cases/` - example public-source case record(s).
- `claims.md`, `methods.md`, `manifest.json`, `publication-goal-card-current.md` - project notes.

## Project Status

- Local Git repository initialized and committed.
- GitHub repository `tyche-institute/limen-ai-edge-case-atlas` created manually via web UI.
- Repository URL added to `manifest.json` under `backup_remote` and `git_remote`.
- `next.md` updated to reflect completed action.
- Dashboard and paper artifacts are ready for integration.

## Contribution Guidelines

- Follow the existing structure and naming conventions.
- Document all changes and additions in `journal.md`.
- Ensure all data sources are properly cited in `sources/sources.md`.
- Push changes to the remote repository after review.
- For large changes, open an issue first for discussion.

## Contact

For questions or collaboration, contact Anton Sokolov at Anton.Sokolov@tyche-institute.org.
