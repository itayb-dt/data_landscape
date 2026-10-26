# REQ-002: Compact view of market events

- **Status:** Done
- **Date:** 2026-10-26
- **Area:** Market Moves

## Problem

The Market Moves page shows a full card per event. That is right for events we analysed, but we want to record every notable funding round or acquisition, including ones we have no time to analyse. A page of large cards cannot hold them.

## Requirement

A minimized view lists all main events (funding, acquisitions) one per line. An event may appear with no analysis: just who did what, and when. Events that have an analysis are clearly marked and link to it.

## Acceptance criteria

- [x] A Detailed / Compact toggle on the Market Moves page; the choice is remembered.
- [x] Compact rows show date, type, a one-line description ("X acquired Y", "X raised $N Series S"), and value where known.
- [x] Events with analysis show an "Analysis →" badge linking to the post.
- [x] Events without analysis show a link to their source, if one exists.
- [x] The All / Acquisitions / Funding tabs filter both views.
- [x] Both views read from one file: `_data/events.yml` (see DEC-001).
- [x] The Detailed view shows cards only for events that have analysis.
