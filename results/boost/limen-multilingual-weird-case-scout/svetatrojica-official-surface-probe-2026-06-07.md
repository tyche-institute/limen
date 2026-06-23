# Sveta Trojica official-surface probe

Cycle timestamp: 2026-06-07T05:31:48Z
Lane: `limen-multilingual-weird-case-scout`
Candidate: `LMWCS-20260606-005`
Target surface: Municipality of Sveta Trojica official portal (`https://www.sv-trojica.si/`; canonical variant observed as `https://www.svetatrojica.si/`)
Access date (UTC): 2026-06-07
Language: Slovenian (`sl`)
Jurisdiction: Slovenia
Source family tested: `official_municipal_portal`
Rights/terms note: public municipal web surface; this artifact records bounded access-state and discovery results only.

## Why this artifact exists

The previous cycle left `LMWCS-20260606-005` at a direct-source-resolved local-news ceiling and recommended one bounded official corroboration pass. This note records that pass even though it did not yield a new official-document upgrade.

## Probe summary

Observed in the bounded shell pass:

- Initial root checks on `https://www.sv-trojica.si/`, `https://svetatrojica.si/`, and `https://www.svetatrojica.si/` returned HTTP 200 and the municipal title `Občina Sveta Trojica v Slovenskih goricah`.
- `https://www.sv-trojica.si/robots.txt` returned HTTP 200 and exposed a public robots file that named `https://www.svetatrojica.si/sitemapxml` as the sitemap location.
- Search-style query URLs such as `https://www.sv-trojica.si/?s=Klara`, `?s=umetna inteligenca`, `?s=tajnica`, and `?s=David Klobasa` returned HTTP 200 but only surfaced the generic municipal shell metadata in the bounded fetches, not a case-specific result snippet or article text.
- A deeper discovery attempt against `https://www.svetatrojica.si/sitemapxml` later returned HTTP 403 with the page title `Dostop do strani trenutno ni mogoč`.
- Follow-up requests to candidate municipal content paths (for example `/objave/176`, `/objave/230`, `/objave/53`, and `/objave/404`) also returned the same HTTP 403 access-denied shell.

## What this does and does not support

Supported now:

- The Municipality of Sveta Trojica maintains a public official web surface reachable from this host at least at the root and robots-file level.
- In this cycle's bounded shell context, deeper official corroboration was not captured because discovery/content requests became access-gated before any municipal page about `Klara` or AI call-routing could be extracted.
- The failed upgrade is useful negative evidence for methods/limitations: the case remains stronger than a title-only lead, but still lacks an official municipal document captured from this shell.

Not supported by this probe:

- any official municipal confirmation that `Klara` exists or was deployed;
- any official confirmation of vendor, procurement, privacy, legality, human fallback, or measured service impact;
- any claim that the absence of a captured official page means the municipality never published one.

## Claim ceiling after this probe

`LMWCS-20260606-005` remains a direct-source-resolved local-news row. The official-corroboration state improves only as a limitations/methods note: partial municipal-site reachability existed, but deeper pages became access-gated before a confirming municipal document was captured.

## Next smallest publishability move

Prefer one cooled-off or browser-mediated official pass on the municipal portal, mayor post, or procurement/council-document surface. If that still fails, freeze the row at the current direct-source-resolved local-news ceiling and cite this probe as explicit negative evidence rather than implying an official corroboration that was not obtained.
