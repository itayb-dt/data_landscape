# DEC-001: One events file is the source of truth

- **Status:** Accepted
- **Date:** 2026-10-26
- **Related:** REQ-002

## Context

The first version of Market Moves had one data file holding only analysed events, each with full card content. The compact view needs to list events that have no analysis too.

## Options considered

1. Keep the cards file and add a second file for bare events. Two files can disagree, and an event that gains an analysis has to move between them.
2. One file for all events, where analysis fields are optional.

## Decision

Option 2: `_data/events.yml`. Every event has the basic fields. An event is "analysed" when it has a `post` field, and only those get a card in the Detailed view. Promoting an event to analysed means adding fields to its existing entry.

## Consequences

- Adding an unanalysed event is a five-line entry.
- The overview strip, the compact view and the cards cannot drift apart.
- The file mixes short and long entries. The header comment in the file documents the fields.
