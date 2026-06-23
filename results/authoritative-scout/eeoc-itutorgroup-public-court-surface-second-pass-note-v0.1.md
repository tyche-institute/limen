# EEOC / iTutorGroup public court-surface second pass note

Date: 2026-06-07T09:16:34Z
Case: `LIMEN-000002`
Lane: `limen-regulator-court-enforcement-scout`

## Why this cycle

`next.md` and the hostile-reviewer sprint both favored either one genuinely different public court-facing surface for `LIMEN-000002` or a shift away from repetitive same-route probing. This cycle took the bounded different-surface route.

## What was tested

- CourtListener REST dockets API
- CourtListener REST search API
- CourtListener web search page
- Justia federal dockets search
- Eastern District of New York official iQuery entry point

## Result

No open complaint, consent decree, docket entry, or judicial order text was captured.

The new negative result is narrower and more useful than the previous generic blocker note:

1. two separate CourtListener routes were inaccessible anonymously on this host (`401` / `403`),
2. Justia's search surface returned a Cloudflare interstitial (`403`), and
3. the official EDNY iQuery page exists but immediately routes the user to PACER login instead of exposing open court text.

## Paper/thesis use

This supports a reviewer-safe claim that `LIMEN-000002` remains agency-summary-level not because obvious public mirror routes were ignored, but because bounded anonymous host-side attempts across both mirror and official court surfaces still did not expose a reusable court-originating document.

## Observatory hook

Treat this as an `open_court_probe` / `access_barrier` artifact for the authority-depth dashboard and the legal-uncertainty or limitations panel.
