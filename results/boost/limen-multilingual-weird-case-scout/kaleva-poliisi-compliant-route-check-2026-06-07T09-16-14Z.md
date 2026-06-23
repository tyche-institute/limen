# Kaleva / Poliisi compliant route check — 2026-06-07T09:16:14Z

Lane: `limen-multilingual-weird-case-scout`
Project: `limen-ai-edge-case-atlas`
Candidate focus: `LMWCS-20260606-002` (Kaleva / Finland)

## What was checked

- Confirmed `https://www.kaleva.fi/robots.txt` returns `User-agent: * Allow: /` while separately disallowing named AI crawlers.
- Confirmed `https://www.kaleva.fi/` is publicly reachable (`HTTP 200`).
- Checked `https://www.kaleva.fi/haku` and query variants; the page is reachable, but the server-rendered HTML did not expose the target article title or a clear query-resolved result surface from this shell context.
- Confirmed `https://poliisi.fi/robots.txt` publicly disallows `/search/`, `/haku/`, `/sok/`, `/-/q/`, and `/web/` for `User-agent: *`, so a shell-only official-site search follow-up would not be a compliant next move here.
- Confirmed `https://poliisi.fi/sitemap.xml` is public, but a bounded pass over sitemap-visible URLs did not yield an obvious AI/intimate-image companion page slug from this shell context.

## Result

No new compliant direct-source upgrade route emerged for `LMWCS-20260606-002` during this pass. The Kaleva row remains a reachable-but-search-friction-limited queue item rather than a newly resolved article or official police record.

## Paper/thesis use

- Methods/limitations note on why reachable host state does not automatically imply a reviewer-safe or robots-compliant verification route.
- Supports keeping the Finnish Kaleva lead in `search_surface_friction` rather than silently retrying blocked or disallowed routes.
- Helps justify why Lithuania/Estonia remain lower-priority shell follow-ups while Finland is still the least-bad unresolved route.

## Next smallest publishability move

Either:
1. use a clearly compliant non-search discovery surface that exposes the Kaleva article or a police companion record directly, or
2. keep exploiting the current multilingual package in figures/tables without promoting the Kaleva row beyond queue-only title-level status.
