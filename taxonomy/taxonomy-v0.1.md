# LIMEN Taxonomy v0.1

Purpose: classify AI edge cases without forcing them into one moral, legal, or
technical bucket. LIMEN records multi-label observations with explicit evidence
tier and confidence.

## Evidence Tiers

| Tier | Meaning | Use |
|---|---|---|
| `T0_lead` | Search hit, rumor, unresolved social/media lead, or weak signal. | Queue only; do not cite as case evidence. |
| `T1_single_public_source` | One public source reports the case. | Candidate record; needs corroboration. |
| `T2_corroborated_public_sources` | Two or more independent public sources support core facts. | Usable for descriptive analysis with caveats. |
| `T3_authoritative_source` | Regulator, court, company notice, security advisory, official report, or peer-reviewed source supports core facts. | Strongest ordinary public evidence. |
| `T4_reproducible_technical_finding` | Bounded reproduction or technical validation exists. | Use carefully; redact dangerous details. |

## Primary LIMEN Categories

Use all that apply.

| Code | Label | Definition |
|---|---|---|
| `unlawful_or_allegedly_unlawful_use` | Unlawful or allegedly unlawful use | Public sources allege or authorities state use connected to fraud, extortion, impersonation, harassment, IP violation, discrimination, cybercrime, or other unlawful conduct. |
| `security_risk` | Security risk | AI system, agent, model, toolchain, or deployment creates or amplifies confidentiality, integrity, availability, identity, supply-chain, or abuse risks. |
| `agentic_control_failure` | Agentic control failure | Agent plans, delegates, uses tools, persists memory, invokes APIs, or acts across workflows in a way that creates unexpected harm or loss of control. |
| `institutional_absurdity` | Institutional absurdity | AI use exposes irrational, performative, or disproportionate institutional process. Includes bureaucracy, procurement theater, hollow oversight, and mismatched automation. |
| `public_sector_misuse_or_gap` | Public-sector misuse or evidence gap | Public authority use, procurement, disclosure, oversight, or register evidence is missing, misleading, opaque, or concerning. |
| `deepfake_or_synthetic_identity` | Deepfake or synthetic identity | Generated/manipulated image, audio, video, persona, voice, identity, or authorship is central. |
| `legal_procedural_contamination` | Legal/procedural contamination | AI affects legal, administrative, expert, academic, or evidentiary process through fake citations, false records, automated filings, or provenance confusion. |
| `health_medical_or_mental_health` | Health, medical, or mental-health misuse | AI use affects clinical, wellness, crisis, therapy, diagnosis, treatment, or mental-health contexts. |
| `education_workplace_or_hr` | Education, workplace, or HR | AI use affects grading, hiring, firing, monitoring, workplace allocation, school discipline, or student/staff records. |
| `finance_insurance_or_market` | Finance, insurance, or market | AI use affects credit, insurance, trading, scams, pricing, eligibility, benefits, or market manipulation. |
| `surveillance_biometrics_or_policing` | Surveillance, biometrics, or policing | AI use involves identification, border control, law enforcement, risk scoring, surveillance, or public-space monitoring. |
| `research_integrity` | Research integrity | AI affects papers, datasets, peer review, synthetic evidence, benchmark gaming, authorship, or citation integrity. |
| `ai_washing_or_false_ai_claim` | AI washing or false AI claim | Case involves exaggerating AI capability, hiding human labor as AI, or falsely claiming AI provenance. |
| `normative_or_moral_outlier` | Normative or moral outlier | Case is not clearly unlawful or technical but violates salient expectations of dignity, fairness, consent, responsibility, or common sense. |
| `residual_unclassified` | Residual/unclassified | The case is important precisely because current categories do not name it well. |

## Harm Types

- physical injury or death;
- psychological or dignitary harm;
- financial loss;
- privacy or data protection harm;
- discrimination or unequal treatment;
- democratic, civic, or public-trust harm;
- reputational harm;
- legal/process harm;
- cybersecurity harm;
- institutional accountability harm;
- research/scientific integrity harm;
- uncertain or no realized harm but credible hazard.

## Affected Domains

Public administration, justice, policing, border/migration, health, education,
employment, finance, insurance, media, elections, security operations,
software development, research, consumer services, social platforms, critical
infrastructure, and personal/non-professional use.

## Classification Discipline

- Classify what public evidence supports.
- Separate allegation, confirmed fact, interpretation, and legal conclusion.
- Never upgrade legal status without an authoritative source.
- Treat media volume as visibility, not frequency.
- Keep the residual bucket alive; LIMEN's novelty lives at category edges.

## Baltic Language Coverage 

- Definition: Evidence involving Baltic languages (Estonian, Latvian, Lithuanian) and associated governance.
- Subtypes:
  - Estonian digital identity frameworks
  - Latvian public-sector AI deployments
  - Lithuanian regulatory sandboxes
- Crosswalk: EU AI Act Art. 55 (Systemic Risk) → Baltic Language Coverage; OECD AI Principle 7.3 → Baltic Language Coverage.
- Visualization: dashboard_hook = dashboard/limen-dashboard-spec-v0.1.md#baltic-language-coverage
- Validation: requires at least two supporting source references before full activation.

