# DEC-002: One structure for acquisition articles

- **Status:** Accepted
- **Date:** 2026-10-27
- **Related:** [acquisition prompt](../prompts/acquisition_blog_post_prompt.md)

## Context

Acquisition articles had drifted: different section names, an "Estimated Deal Amount" bullet that repeated what the site banner now shows, and generic headings ("Opening Context", "About <Company>", "Relevant Tools") that said nothing about the content.

## Options considered

1. Keep the original template and only restyle it.
2. A fixed skeleton with content-specific headings where the content varies, and fixed titles where company names are already clear.

## Decision

Option 2:

- Title: `<Acquirer> acquires <Target> to <short reason>`, matching the card headline.
- A lead paragraph with no heading, instead of "Opening Context". The banner carries the facts.
- `The Problem: <short problem>` and `The Solution: <short approach>`, written per article.
- `Understanding the Acquisition` and `Relevant Products and Companies`: fixed titles with no company names.
- `My Take`: required. The author's view if given, otherwise a draft for the author to rewrite. When an update shows the direction was right, My Take states that direction in advance and the update closes the loop.

## Consequences

- Readers know where to look in every article.
- Headings need a small amount of writing per article. The author edits the drafts.
- The four existing articles were rewritten to match; funding history sits inside The Solution.
