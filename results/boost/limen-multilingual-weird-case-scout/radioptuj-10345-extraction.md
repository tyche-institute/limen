# Radio Ptuj source extraction note

Cycle timestamp: 2026-06-07T04:49:30Z
Lane: `limen-multilingual-weird-case-scout`
Candidate: `LMWCS-20260606-005`
Source URL: `https://radioptuj.svet24.si/podravje-na-moji-dlani/lokalne-novice/10345-pri-sveti-trojici-namesto-tajnice-ze-umetna-inteligenca`
Access date (UTC): 2026-06-07
Language: Slovenian (`sl`)
Jurisdiction: Slovenia
Source family: `local_news`
Source authority: `regional_radio`
Rights/terms note: Public Radio Ptuj article page; use as citation/metadata and narrow quotation support only. No broader reuse-rights claim made.

## Why this artifact exists

This note upgrades a Google-News-discovered title-gloss lead into a direct-source-resolved, reviewer-legible extraction artifact. It records only what the Radio Ptuj page itself supports and keeps stronger claims about municipal automation, staffing substitution, legality, or effectiveness out of scope.

## Source-bounded extraction

Title on page:
- `Pri Sveti Trojici namesto tajnice (že) umetna inteligenca`

Meta description / lead signal on page:
- `Kot ena prvih občin v Sloveniji, ki uvaja takšno rešitev v vsakodnevno delo občinske uprave.`

Bounded English gloss:
- The page presents the Municipality of Sveta Trojica as among the first municipalities in Slovenia to introduce this kind of solution into the everyday work of the municipal administration.

## Direct municipal-service signals captured from the article page

Original Slovenian excerpts:
- `Župan občine Sveta Trojica David Klobasa je na veliko noč razkril, da se od petka naprej ob klicu na številko tajništva občine oglaša njihova nova tajnica Klara, ki deluje ob pomoči umetne inteligence.`
- `Z občani se pogovarja na naraven način, prepozna vsebino klica in ga usmeri v pristojno pisarno.`
- `Vedno se oglasi, pazljivo posluša, razume in vas brez zapletov usmeri tja, kjer boste najhitreje prišli do odgovora.`
- `Njena naloga je preprosta, poskrbeti, da noben klic ne ostane spregledan in da vsaka zadeva dobi jasno pot obravnave.`
- `Po njihovi oceni so ena prvih občin v Sloveniji, ki uvaja takšno rešitev v vsakodnevno delo občinske uprave.`
- `Cilj je boljša organizacija dela, večja preglednost in predvsem hitrejša obravnava pobud občanov.`
- `Foto: Občina Sveta Trojica.`

Bounded English glosses:
- The article says the mayor of the Municipality of Sveta Trojica announced that, from Friday onward, calls to the municipal secretariat number are answered by a new secretary named Klara that operates with the help of AI.
- The article says Klara speaks with citizens in a natural way, recognizes the content of a call, and routes the caller to the competent office.
- The mayor's quoted framing presents the system as a no-missed-call / clearer-routing service channel rather than, on this page alone, proof of full human replacement.
- The article says the municipality views itself as among the first in Slovenia to introduce such a solution in everyday municipal-administration work.
- The article frames the municipal goal as better work organization, greater transparency, and faster handling of citizens' initiatives.
- The photo credit ties the article's illustration to the Municipality of Sveta Trojica, but the page alone does not yet provide a direct municipal document or procurement record.

## Claim ceiling after this extraction

Supported now:
- A direct Radio Ptuj article names the Municipality of Sveta Trojica and its mayor in connection with an AI-assisted municipal-secretariat phone-answering / routing channel called Klara.
- The article supports narrow descriptive claims that the system is presented as speaking naturally with callers, recognizing call content, and routing them to the appropriate office.
- The article supports a bounded institutional-absurdity / public-administration case framing because the source explicitly places the solution inside ordinary municipal-administration work.

Still not supported strongly enough for stronger manuscript claims without more checking:
- any claim that human secretarial staff were fully replaced rather than supplemented;
- any claim about the vendor, technical stack, accuracy, uptime, privacy posture, legality, procurement basis, or measured service benefit;
- any claim that the municipality was literally the first in Slovenia rather than self-describing as among the first;
- any final legal or policy conclusion based on machine-assisted reading alone.

## Paper/thesis use

- Reviewer-safe multilingual row for an institutional-absurdity / public-administration appendix table.
- Methods note showing direct-source recovery from a Google News RSS lead via Radio Ptuj's own public site-search surface.
- Comparator row for a municipal service-channel automation claim that may represent AI theater, workflow substitution, or both, pending stronger official documentation.

## Dashboard/visualization hook

Recommended fields:
- candidate_id
- jurisdiction
- language
- source_authority
- direct_source_resolved
- institution_named
- ai_use_phrase
- call_routing_signal
- self_described_first_mover_signal
- translation_review_required
- claim_ceiling

Suggested interpretation:
- Distinguish direct-source-resolved local-news municipal rows from unresolved title-only leads.
- Show how under-covered-language local media can surface public-administration AI theater or workflow-change claims before official procurement or municipal-document traces are captured.

## Next smallest publishability move

Look for one direct municipal page, procurement record, or mayor post that confirms whether Klara is a call-routing assistant, a broader administrative workflow tool, or primarily a publicity-facing deployment claim. If no official document is captured quickly, keep this row at the direct-source-resolved local-news ceiling.
