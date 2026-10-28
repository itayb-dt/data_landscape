# Product

Where product decisions for the Data Landscape blog are kept: what we want the site to do, and why we chose it.

- **Requirements** (`requirements/REQ-NNN-*.md`): something the site should do. Each has a status and acceptance criteria.
- **Decisions** (`decisions/DEC-NNN-*.md`): a choice we made between options, with the reasoning, so we don't re-argue it later.
- **Prompts** ([prompts/](prompts/)): one writing guide per article type (acquisition, funding round, concept, database review, tech review). They define each type's structure and rules, so changing how an article type is written means changing its prompt first.

To add one, copy the matching file from [_templates/](_templates/), use the next free number, and add a row below.

Statuses: `Proposed` → `Accepted` → `Done` (or `Rejected` / `Deferred`).

## Requirements

| ID | Title | Status |
|----|-------|--------|
| [REQ-001](requirements/REQ-001-search.md) | Search | Proposed |
| [REQ-002](requirements/REQ-002-compact-view.md) | Compact view of market events | Done |
| [REQ-003](requirements/REQ-003-ontology.md) | Ontology tab | Proposed (mockup) |

## Decisions

| ID | Title | Status |
|----|-------|--------|
| [DEC-001](decisions/DEC-001-events-file-is-source-of-truth.md) | One events file is the source of truth | Accepted |
| [DEC-002](decisions/DEC-002-acquisition-article-structure.md) | One structure for acquisition articles | Accepted |
