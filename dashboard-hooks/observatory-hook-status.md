# Observatory Hook: Source Map Status

## Purpose
Provide a dashboard-level view of the latest status of the source-family coverage map, enabling real-time monitoring of coverage updates and authority scores.

## Data Source
- `results/source-map/status.md` – contains the latest source-family ledger update and coverage status.

## Integration
- The hook consumes the `status.md` file to generate a summary badge or indicator in the dashboard’s “Source Authority” panel.
- It maps the “latest update” timestamp and the “saturation_metric” values to a visual indicator (e.g., green/orange/red) reflecting coverage health.
- The hook can be extended to trigger alerts when new source families are added or when saturation metrics cross thresholds.

## Implementation Notes
- Parse the first line of `status.md` for the UTC timestamp to display “Last update: YYYY-MM-DD HH:MM UTC”.
- Extract the “saturation_metric” column values for the “Source Family Coverage” row to compute a simple health score.
- Use the `dashboard-hooks` processing pipeline to render a small badge component.
- Reference the hook from the main dashboard `index.html` by adding a `<meta>` tag or sidebar entry with link `observatory-hook-status.md`.

## Stakeholders
- @anton.sokolov (review)
- Dashboard maintainers
- Legal review team (for blocked source workflow)