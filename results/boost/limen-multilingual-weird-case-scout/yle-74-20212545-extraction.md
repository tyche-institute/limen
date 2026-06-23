# Yle source extraction note

Cycle timestamp: 2026-06-07T01:56:40Z
Lane: `limen-multilingual-weird-case-scout`
Candidate: `LMWCS-20260606-001`
Source URL: `https://yle.fi/a/74-20212545`
Access date (UTC): 2026-06-07
Language: Finnish (`fi`)
Jurisdiction: Finland
Source family: `public_broadcaster_news`
Source authority: `local_public_broadcaster`
Rights/terms note: Public Yle article page; use as citation/metadata and narrow quotation support only. No broader reuse-rights claim made.

## Why this artifact exists

This note upgrades a Google-News-discovered title-gloss lead into a direct-source-resolved, reviewer-legible extraction artifact. It records only what the Yle article page itself supports and keeps stronger prevalence or legal-conclusion language out of scope.

## Source-bounded extraction

Title on page:
- `Tekoäly laatii nyt täysin järjettömiä valituksia – poliisilakimies turhautui: ”Viitataan tapauksiin, joita ei ole”`

Meta description / lead signal on page:
- `Sisä-Suomen poliisissa ja Itä-Suomen hallinto-oikeudessa on huomattu ilmiö, että valituksia tehdään nyt tekoälyn avulla.`

Bounded English gloss:
- The article says Internal Finland Police and the Eastern Finland Administrative Court have noticed a phenomenon in which appeals are now being made with the help of AI.

## Direct procedural signals captured from the article page

Original Finnish excerpts:
- `Hallintovalituksia tehdään nyt tekoälyllä, ja se työllistää viranomaisia.`
- `Kun joku valittaa poliisilaitoksen päätöksestä hallinto-oikeuteen, Porvali laatii poliisilaitoksen lausunnot hallintovalituksiin.`
- `Niissä viitataan sellaisiin oikeustapauksiin, joita ei ole olemassa, tai vedotaan oikeuskäytäntöihin sellaisesta näkökulmasta, joissa käytäntö on oikeasti täysin erilainen kuin tekoäly hallusinoi.`
- `Viranomaisen kannalta tämä on kiusallista, koska kaikkiin asioihin, joihin valituksessa viitataan, täytyy ottaa kantaa. Tämä työllistää viranomaista paljon.`
- `Meilläkin voi olla joitakin valituksia, jotka on mahdollisesti tehty tekoälyllä, mutta kysymys on vielä hyvin pienestä ilmiöstä.`
- `2024 ei tullut yhtään, viime vuonna useita ja nyt vauhti on kiihtynyt.`
- `Hän arvioi vastanneensa viime vuoden aikana 10–20 valitukseen, jotka hän erotti tekoälyn laatimiksi.`

Bounded English glosses:
- AI is being used to produce administrative appeals, and this creates work for authorities.
- The specific filing context is appeals against police decisions before the administrative court.
- According to the quoted police lawyer, some filings cite non-existent cases or invoke legal practice from angles that differ sharply from reality.
- Authorities still have to answer each argument raised, which creates a substantial workload burden.
- The chief judge quoted in the article frames the phenomenon as still small.
- The police lawyer is quoted as saying none were seen in 2024, several in 2025, and the pace has now accelerated.
- He estimates answering 10–20 appeals in the previous year that he identified as AI-drafted.

## Claim ceiling after this extraction

Supported now:
- A direct Yle article names Internal Finland Police and the Eastern Finland Administrative Court as institutions that have noticed AI-assisted administrative appeals.
- The article supports a narrow procedural-contamination claim: some filings reportedly contain fabricated case references or distorted legal support, while still consuming official response labor.
- The article provides a bounded frequency signal through quoted estimates, but those estimates remain journalistic-source reporting rather than official statistics.

Still not supported strongly enough for stronger manuscript claims without more checking:
- any claim that the observed filings amount to widespread abuse across Finland;
- any claim about adjudicated misconduct, sanctions, or formal court findings against specific filers;
- any claim that the article's quoted estimates are official system-wide counts;
- any final legal or policy conclusion based on machine-assisted reading alone.

## Paper/thesis use

- Reviewer-safe multilingual row for a public-sector/legal-process contamination table.
- Methods note showing direct-source recovery from a Google News RSS lead via Yle's own public search surface.
- Appendix support for a bounded discussion of administrative-workload contamination from AI-generated filings.

## Dashboard/visualization hook

Recommended fields:
- candidate_id
- jurisdiction
- language
- source_authority
- direct_source_resolved
- filing_type
- institution_named
- fabricated_case_reference_signal
- response_burden_signal
- translation_review_required
- claim_ceiling

Suggested interpretation:
- Distinguish direct-source-resolved broadcaster records from unresolved title-only leads.
- Show how non-English public-broadcaster reporting can surface public-sector procedural anomalies before any official document is captured.
