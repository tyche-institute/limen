# Blocked Sources Report limen-boost-036

This report documents blocked sources identified during the LIMEN AI Edge-Case Atlas boost phase 036, focusing on Baltic public-sector sources.

## Blocked Source Inventory

| Source URL | Jurisdiction | Access Pattern | Blocked Reason | Contact Form Available |
|------------|--------------|----------------|----------------|------------------------|
| https://www.x-gov.ee/data/ai-reg | Estonia | IP geofence | .ee TLD access restrictions | Yes (Estonian only) |
| https://www.aidij-ai.lv | Latvia | CAPTCHA + JS challenge | Non-browser access blocked | No |
| https://mke.lva.lv/publications | Latvia | Basic auth + SSO | Institutional access required | Yes (Latvian only) |
| https://aiportal.environ.gov.sk | Slovakia | Redirect chain failure | Pending GDPR compliance check | Yes (Slovak) |

## Compliance-Safe Routing Process

1. Source classification: Public portal + regulatory mention
2. Contact form submission:
   - Language: Original source language
   - Channel: Official contact form + email backup
   - Content: Standardized request template (see Template 3b)
3. Monitoring: Response tracker in sources/tracking.tsv

## Next Actions

1. Translate contact form content for Estonian/Latvian sources (priority: 0.8)
2. Establish response monitoring pipeline (due 2026-07-01)
3. Update source ledger with routing status (lane 037)

## Dashboard Hook

Feeds into:
1. Evidence Coverage Map (Map 3) - blocked locations
2. Source Authority Matrix (Table 2) - access status column
3. Response Tracker (Table 4)

Status: Ready for routing (requires translation support)