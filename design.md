# Filter UI Mockup for Crosswalk Coverage Dashboard

## 1. Jurisdiction Selector
- Typeahead search for country names (Balkan, Baltic, Finno-Ugric, etc.)
- Group by language family and regional bloc
- Visual feedback when selection changes evidence coverage

## 2. Framework Toggle
- Checkboxes for each governance framework:
  [ ] AIID
  [ ] OECD AIM
  [ ] MITRE ATLAS
  [ ] CSET AI Risk
  [ ] EU AI Act
  [ ] ISO/IEC 42001
  [ ] OWASP AI
  [ ] NIST AI RMF
- Realm-time update of coverage map when frameworks are toggled

## 3. Evidence Tier Highlight
- Color-coded overlays matching SVG:
  - Green (#2ecc71): Tier 1 (Full)
  - Orange (#f39c12): Tier 2 (Partial)
  - Red (#e74c3c): Tier 3 (Initial)
  - Gray (#c0392b): Tier 4 (Gap)
- Legend with interactive tooltips

## 4. Legal Review Flags
- Red border emphasis on jurisdictions requiring review
- Click handler to open legal review queue in new panel

## 5. Publication Venue Mapping
- Dropdown to filter coverage by target venue:
  - AI Policy Review
  - Journal of AI Governance
  - International AI Law Review
  - NATO Science & Society
- Auto-adjust coverage thresholds based on venue requirements

## 6. Responsive Design
- Mobile-first approach with collapsible sections
- SVG scaling maintained at all breakpoint
- Touch-friendly controls for tablet use

## 7. Implementation Plan
1. Create React components for each control
2. Bind state to SVG visualization
3. Add URL parameter support for bookmarking views
4. Integrate with dashboard currentness audit system
5. Add accessibility labels and keyboard navigation

## 8. Dependency Requirements
- @types/react
- react-select for jurisdiction search
- d3.js for SVG interaction
- styled-components for theming
- jest for cross-browser testing