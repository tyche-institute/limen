# AIID machine-readable field-family note v0.1

Date: 2026-06-07
Lane: `limen-boost-002`
Project: `limen-ai-edge-case-atlas`

## What was checked

- Public cite page: `https://incidentdatabase.ai/cite/1515/`
- Public page-data JSON: `https://incidentdatabase.ai/page-data/cite/1515/page-data.json`
- Public snapshots index: `https://incidentdatabase.ai/research/snapshots/`
- Latest public backup linked from the snapshots page: `backup-20260601120109.tar.bz2`

## Main finding

AIID is now stronger than a page-label-only comparator in the local shard-002 package. The public cite route for incident `1515` has a directly accessible machine-readable companion at `/page-data/cite/1515/page-data.json`, and that JSON exposes a richer field family than the older bounded snapshot checks alone:

- exact incident keys (`incident_id`, `title`, `description`, `date`);
- linked report identifiers (`report_number` values `7347`, `7348`, `7349`);
- linked report metadata (`source_domain`, `url`, `date_published`);
- structured actor/system arrays (`Alleged_developer_of_AI_system`, `Alleged_deployer_of_AI_system`, `Alleged_harmed_or_nearly_harmed_parties`, `implicated_systems`);
- visible taxonomy metadata (`CSETv1` namespace and public field-definition surfaces).

## Why this matters

This gives LIMEN one reviewer-safe machine-readable AIID route without needing a bulk API claim or a large archive mirror. It also sharpens the local methods caveat: the latest public backup linked from the snapshots page is `backup-20260601120109.tar.bz2`, but the incident's public `editor_notes` say the incident ID was created on `2026-06-04`, after that backup date. The absence of incident `1515` from the latest backup is therefore expected snapshot lag, not evidence that the public cite/page-data record is unstable.

## Paper/thesis use

- Methods appendix note on AIID interoperability layers: visible cite page, public page-data JSON, and lagged public snapshots should be modeled separately.
- Comparator-readiness table: AIID can now be described as a bounded public comparator with one direct machine-readable page-data route, while bulk/archive semantics remain only partially verified.
- Dashboard hook: add a comparator panel field showing `page_data_json_available=yes`, `snapshot_lag_visible=yes`, and exact actor/system/report-family slot availability.

## Claim ceiling

This note does not justify bulk AIID ingestion, complete archive equivalence, legal/compliance claims, or event-truth claims. It only justifies a stronger statement about public machine-readable field availability on one exact cite-page route plus a visible snapshot-lag caveat.
