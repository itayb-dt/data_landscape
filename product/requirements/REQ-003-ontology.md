# REQ-003: Ontology

- **Status:** Proposed (hard-coded mockup only)
- **Date:** 2026-10-28

## What we want
A top-level **Ontology** tab: a visual vocabulary of the data landscape. Terms emerge from and dissolve into smoke, and one day each term explains itself and links to the articles and companies that matter for it.

## Mockup (done)
- Page `/ontology/` ([ontology.html](../../ontology.html)), nav tab after Market Moves.
- Dark browser-window frame titled ONTOLOGY, with drifting smoke (SVG turbulence filter plus animated blurred shapes).
- DATA LAKE and SPARK glow brightly on the left. OLAP, OPEN TABLE FORMAT, SQL, DAG, METADATA, STREAMING, HADOOP and a few more fade in and out across the screen.
- The page and the frame both say it is a mockup and not ready.
- Terms fade in and out, and reappear at a new random position each time (a small inline script).
- All terms are hard-coded in the HTML. Pure CSS, no scripts. Animation is off with `prefers-reduced-motion`.

## Open questions
- Where do the terms live? Likely a data file like `_data/ontology.yml`, with a definition and links to articles per term.
- Is clicking a term a definition card, a filtered article list, or a graph of related terms?
- Should the layout stay free-floating, or should related terms sit closer together?
