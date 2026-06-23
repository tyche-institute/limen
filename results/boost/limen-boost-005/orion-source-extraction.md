# ORION source extraction note

Cycle timestamp: 2026-06-07T01:13:59Z
Lane: `limen-boost-005`
Candidate: `LMWCS-20260606-004`
Source URL: `https://www.policija.si/delovna-podrocja/mednarodno-sodelovanje/crpanje-evropskih-sredstev/projekt-euccs-preparation-stage-4`
Access date (UTC): 2026-06-07
Language: Slovenian (`sl`)
Jurisdiction: Slovenia
Source family: `official_police_source`
Source authority: `national_police`
Rights/terms note: Public official police webpage; use as citation/metadata support only. No broader reuse-rights claim made.

## Why this artifact exists

This note converts the already resolved ORION police page into a reviewer-legible extraction artifact. It isolates what the page explicitly says, gives a bounded English gloss for the six listed sub-goals, and records which stronger interpretations still require caution.

## Source-bounded extraction

Title on page:
- `Projekt ORION: Umetna inteligenca za varno mejno kontrolo`

Opening project-purpose paragraph in Slovenian:
- `Projekt ORION (angl. Optimized Risk-based Intelligence-driven Operations for Next-generation Secure, Reliable and Privacy-preserving Border Management) je namenjen izboljšanju upravljanja meja, tudi s pomočjo umetne inteligence. Cilj je varna, zanesljiva in zasebnost ohranjajoča mejna kontrola naslednje generacije.`

Bounded English gloss:
- Project ORION is presented as aiming to improve border management, including with the help of artificial intelligence, toward next-generation border control described as secure, reliable, and privacy-preserving.

Main-goal paragraph in Slovenian:
- `Glavni cilj projekta je zagotoviti napredne rešitve za upravljanje zunanjih meja Evropske unije, ki povečujejo varnost in učinkovitost operacij, hkrati pa zagotavljajo močno etično in pravno skladnost ter zaščito osebnih podatkov potnikov na evropskih mejah. Šest ključnih podciljev projekta:`

Bounded English gloss:
- The page says the project seeks advanced solutions for managing the EU's external borders that increase operational security and efficiency while also ensuring strong ethical and legal compliance and protection of travelers' personal data.

## Six listed sub-goals

Original Slovenian list:
- 1. `izboljšanje koordinacije med mejnimi, carinskimi in varnostnimi kontrolami`
- 2. `optimizacija dodeljevanja virov za zmanjšanje čakalnih dob`
- 3. `izboljšanje zmožnosti za odkrivanje groženj, zlasti na trajektih tipa roll-on/roll-off (Ro-Ro)`
- 4. `zagotovitev interoperabilnosti z obstoječimi sistemi EU (npr. SIS, VIS, EES)`
- 5. `izboljšanje energetske učinkovitosti in zmanjšanje okoljskega vpliva (cilj je vsaj 15-odstotno zmanjšanje ogljičnega odtisa)`
- 6. `zagotovitev etične in pravne skladnosti ter zaščite osebnih podatkov potnikov.`

Bounded English gloss for manuscript/table use:
- 1. improve coordination among border, customs, and security controls
- 2. optimize resource allocation to reduce waiting times
- 3. improve threat-detection capability, especially on roll-on/roll-off (Ro-Ro) ferries
- 4. ensure interoperability with existing EU systems such as SIS, VIS, and EES
- 5. improve energy efficiency and reduce environmental impact, with a stated target of at least a 15% reduction in carbon footprint
- 6. ensure ethical and legal compliance plus protection of passengers' personal data

## Explicit technical and operational language on the page

Original Slovenian technology paragraph:
- `Projekt razvija napredne tehnologije, s ciljem doseganja stopnje TRL 7 (angl. Technology Readiness Level 7), kot so tehnologije za identifikacijo in preverjanje potnikov, tehnologije za pregled vozil, sistemi, ki bodo ohranjali zasebnost, omogočali iskanje in obdelavo šifriranih biometričnih podatkov, ter sistemi za zagotavljanje transparentnih in pravno skladnih priporočil mejnim organom.`

Bounded extraction:
- states an ambition to reach TRL 7
- mentions technologies for passenger identification and verification
- mentions vehicle-inspection technologies
- mentions privacy-preserving systems able to search and process encrypted biometric data
- mentions systems intended to provide transparent and legally compliant recommendations to border authorities

Original Slovenian pilot-scenarios paragraph:
- `Tehnologije bodo testirane v realnih pilotnih scenarijih, ki se osredotočajo na dinamična okolja z velikim prometom, in sicer v Romuniji (pilotni scenarij "Inteligentno upravljanje procesov vkrcavanja na trajekte Ro-Ro"), Bolgariji (pilotni scenarij "Optimizirano izkrcavanje potnikov s trajektov Ro-Ro") in Sloveniji (pilotni scenarij "Izboljšana ocena tveganja in dodeljevanje virov na kopenskih mejnih prehodih").`

Pilot-scenario gloss:
- Romania: intelligent management of boarding processes on Ro-Ro ferries
- Bulgaria: optimized disembarkation of passengers from Ro-Ro ferries
- Slovenia: improved risk assessment and resource allocation at land border crossings

Consortium/funding paragraph signal:
- `Konzorcij vključuje 21 partnerjev iz 14 držav, med njimi pet mejnih organov in dva operaterja (Eurostar, UIC). Slovenski partnerji so Univerza v Mariboru (UM), Inštitut za korporativne varnostne študije Ljubljana (ICS) in Ministrstvo za notranje zadeve, Policija (MNZ).`
- `Gre za projekt v okviru HORIZON Innovation Action (HORIZON-IA), ki ga financira Evropska unija prek Izvršne agencije za raziskave (REA). Projekt se je začel 1. septembra 2025 in traja 36 mesecev. Skupni znesek dodeljenih sredstev znaša 5.240.093,75 evra. Projekt je za slovensko policijo 100-odstotno financiran iz finančnega vira Horizon. Za projektno implementacijo je planiranih okoli 99.000 evrov. Projekt koordinira UBITECH LIMITED (UBI) s Cipra.`

## Claim ceiling after this extraction

Supported now:
- The Slovenian police publicly host an ORION project page with explicit AI-assisted border-management framing.
- The page explicitly lists six project sub-goals.
- The page explicitly mentions privacy-preserving systems, encrypted biometric-data search/processing, transparent recommendations to border authorities, and pilot scenarios in Romania, Bulgaria, and Slovenia.
- The Slovenian pilot scenario is described as improved risk assessment and resource allocation at land border crossings.

Still not supported strongly enough for stronger manuscript claims without more checking:
- any claim that the system is already operational in production rather than pilot/testing form;
- any claim that ORION proves legality, compliance, effectiveness, necessity, or proportionality;
- any claim that biometric processing is deployed at scale rather than described as a project technology objective;
- any downstream legal conclusion based on machine-assisted translation alone.

## Paper/thesis use

- Reviewer-safe appendix row for a multilingual public-sector AI deployment case.
- Table support for a policing/border-control topology or language-coverage appendix.
- Methods note showing a concrete upgrade path from redirect-dependent discovery to direct-source extraction.

## Dashboard/visualization hook

Recommended fields for a deployment-map or evidence card:
- candidate_id
- jurisdiction
- language
- source_authority
- direct_source_resolved
- ai_use_phrase
- biometric_signal_present
- pilot_scenario_present
- risk_assessment_signal_present
- privacy_preserving_signal_present
- claim_ceiling
- translation_review_required

Suggested interpretation:
- Distinguish official multilingual project-purpose pages from weaker news-only leads.
- Show which rows contain explicit biometric, pilot, or risk-assessment language but still require caution before legal interpretation.

## Linked public content found on-page

- `Črpanje evropskih sredstev` -> `https://www.policija.si/delovna-podrocja/mednarodno-sodelovanje/crpanje-evropskih-sredstev`

## Next smallest publishability move

Check whether the linked police funding-section page or project-partner pages expose a direct project document, then decide whether ORION belongs in a manuscript paragraph on public-sector AI border pilots, biometric/privacy tension, or multilingual evidence-resolution method.
