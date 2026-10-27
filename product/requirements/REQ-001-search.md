# REQ-001: Search

- **Status:** Proposed
- **Date:** 2026-10-26
- **Area:** Navigation

## Problem

The site has posts across six categories plus a list of funding and acquisition events. A reader who remembers a company ("what did SAP do with Dremio?") or a concept ("storage and compute") can only browse the timeline or the All Posts list and scan by eye. This gets worse as posts and events are added.

## Requirement

A reader can type a query and get matching posts and events, from any page.

## Acceptance criteria

- [ ] A search box is visible in the header on every page.
- [ ] Results include posts (matched on title and body) and events (matched on company, acquirer, target, stage).
- [ ] Each result shows its type (post or event, and category) and links to the post, or to the source for events without analysis.
- [ ] Events that have an analysis are marked as such in the results.
- [ ] Works on the GitHub Pages site, with no server.
- [ ] Results appear while typing, in under a second on the current content.

## Out of scope

- Filtering by date range or amount (the Market Moves tabs already filter by type).
- Search analytics.

## Open questions

- Client-side index at build time (for example Pagefind or Lunr) or a small custom index? Pages' built-in Jekyll build cannot run extra tools, so a build-time index means a GitHub Actions workflow or a committed index file.
- Should `product/` (including its prompts) and `backlog/` ever be searchable? Default: no.
