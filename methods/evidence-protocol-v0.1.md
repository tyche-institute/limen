# LIMEN Evidence Protocol v0.1

## Scope

LIMEN records public-source evidence about AI edge cases and maps each record
to technical, legal, ethical, and governance frameworks. It is designed for
research, policy analysis, attestation experiments, and dashboard/publication
artifacts.

## Ingestion Stages

1. Source discovery: identify public source families, endpoints, reuse terms,
   and source authority.
2. Lead capture: create T0 leads with URLs, access date, language,
   jurisdiction, and source-family label.
3. Candidate record: promote to T1 only when at least one public source
   supports a concrete event, hazard, vulnerability, or anomalous use.
4. Corroboration: promote to T2 with independent public support.
5. Authority upgrade: promote to T3 when an authoritative source supports core
   facts.
6. Technical validation: promote to T4 only through bounded, non-dangerous
   reproduction or public technical evidence, with exploit details redacted.

## Safety Rules

- Do not collect or store credentials, tokens, private messages, or private
  victim material.
- Do not reproduce exploit payloads, malware, evasion steps, or operational
  cyber instructions.
- Do not scrape behind logins or bypass access controls.
- Do not make individual-targeting dossiers.
- Preserve public figures, minors, and private persons with extra caution.
- Keep non-consensual intimate media and similar material as metadata-only
  references to authoritative reporting; never mirror the content.
- Avoid bulk downloads until source rights, rate limits, and value are clear.

## Classification Rules

- Multi-label everything.
- Separate `source_claim`, `curator_interpretation`, and `legal_status`.
- Keep evidence tier and confidence visible.
- Do not infer AI Act high-risk status, non-compliance, illegality, or liability
  from weak public evidence.
- When in doubt, keep the record as a lead and create a verification task.

## Completeness Model

LIMEN cannot become 99% complete against all reality. It can become highly
complete against declared source families. Every source family should track:

- discoverability;
- access method;
- reuse constraints;
- language/jurisdiction;
- update cadence;
- last crawl date;
- records found;
- records rejected;
- duplicate rate;
- saturation estimate;
- unresolved verification queue.

## Minimum Case Artifact

Every candidate case needs:

- stable `case_id`;
- title and short summary;
- at least one source claim;
- evidence tier;
- source URL/path and access date;
- source language and jurisdiction if known;
- classification labels;
- confidence;
- uncertainty notes;
- crosswalk placeholders;
- provenance/run id.

