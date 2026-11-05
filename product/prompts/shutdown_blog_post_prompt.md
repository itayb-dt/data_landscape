# Prompt: Write a Blog Post About a Startup Shutdown

Use this prompt to write a shutdown article. The article answers two questions: what exactly was the company trying to do, and why did it fail. Keep it short.

Reference articles: [SQream](../../blog_posts/shutdown/020_SHUTDOWN_sqream_insolvency.md) and [Explorium](../../blog_posts/shutdown/026_SHUTDOWN_explorium_external_data.md).

---

You are writing a short analytical blog post about a data or AI startup that shut down, entered insolvency or was wound down.

## Objective
Explain:
1. What the company was trying to do, in practical terms, and what problem it addressed
2. Why it failed, first in the company's own words, then in the reporters' words, then in the author's analysis

## What this article is not
Do not write about customers, employees, creditors, severance, debts or the sale process, beyond one clause where it helps the story (for example, "a court-run sale of the assets began"). No lists of who is owed what. No wind-down logistics (refunds, data deletion dates, export deadlines).

## Required Tone and Style
- Professional, restrained and respectful. A company shut down; do not gloat.
- Concrete and specific; avoid buzzwords.
- Short paragraphs and clear section headings.
- Inline markdown links to the sources. Prefer first-party sources (the company's own farewell post), then court filings, then reporters (Calcalist/CTech, Globes, TechCrunch).

## Required Structure

The site renders a header above the article with the status and area. Do not repeat them as a list.

### Title (front matter `title`)
Format: `<Company>, <what it was or raised>, <what happened>`

- Example: `Explorium, the external data platform that raised over $127M, shuts down after almost nine years`
- Use the same text as `headline` in `_data/events.yml`.

### Lead paragraph (no heading)
Two or three sentences straight after the front matter:
- What happened and when, with an inline link to the company's announcement or the first report.
- One fact that shows scale (money raised, years of operation).

### 1. `## The Problem: <short, specific problem>`
- The industry problem the company addressed, phrased as a problem.
- Include one realistic example.
- Frame it as an industry problem, not a weakness of the company.

### 2. `## The Solution: <what they built>`
- What the product did, in practical terms, and for whom.
- State how the direction changed over time, if it did (for example, repositioning for AI agents). Say whether the core stayed the same. Be honest: AI labels are often added on top of an unchanged core, and say so if that is the author's view.
- End with `### Funding history`, one line per round:
  - `Round - Date - Amount - Link`
  - If a round has no credible source, write "not linked (to be verified)".
- If no credible public funding data is found, write: `Public Funding Rounds: Not publicly available from credible sources.`

### 3. `## Why It Failed`
This title is fixed. It has three parts, in this order, and each is labeled by its voice so the reader knows who is speaking:
1. **The company's words.** Quote the founders' explanation, with a link. Keep quotes short, under 25 words each. Do not paraphrase them into something stronger.
2. **The reporters' words.** What the press says, with the outlet named. Mark it as the reporter's wording.
3. **Analysis.** The author's reading of the facts, introduced as such ("Reading the facts..."). Keep it to a short paragraph. Do not state speculation as fact.

If the company gives no reason, say so, then give the reporters' view and the analysis.

### 4. `## Relevant Products and Companies` (optional)
- 2-3 companies in the same space, one short line each with an official link. Skip if the space is crowded with commodity providers.

### 5. `## My Take` (required)
The author's own view, in first person.
- Use the author's opinion when they give one, close to their wording.
- When they have not given one, draft it from the blog's recurring themes (a new database vendor needs a clear business justification, "just use Postgres" is often right, data is complicated) and hand it over as a draft for the author to rewrite. Never present a draft as final.
- Short: two to four small paragraphs.
- Do not invent facts. Mention only facts that are sourced in the article.

### 6. `## Updates` (optional)
Dated entries for late news, for example a buyer for the assets. Start with an italic line saying these are late additions.

## Funding Rounds
- If there is an article about the last funding round, link to it from the funding history. Old rounds do not get their own article.
- Mention an old acquisition by the company in one clause only (for example, "bought Panoply for an estimated $60-70M"), with a source.

## Images
- No headshots, stock photos or decorative backgrounds. A hero image is optional; use the company's own announcement graphic if one exists.
- Download images, save under `assets/images/<company>/`, cap the longest side at about 1400px.

## Events file (`_data/events.yml`)
Add an entry so the shutdown shows on Market Moves:
- `type: shut`, `date`, `when`, `company`, `abbr`, `color`, `stage` (for example "Insolvency" or "Ceasing operations"), `headline`, `tldr`, `nums` (three label and value pairs of known facts, such as Raised, Founded, Last round), `signal`, `area`, `post`.
- `tldr` is a subtitle with facts only. `signal` is one or two short sentences saying the basic reason it failed, with no facts repeated from the subtitle.

## Content Requirements
- Use specific facts accurately. If a fact is unknown, say it is not disclosed.
- When sources disagree (for example on losses or totals raised), quote both and say so.
- Do not invent financial figures, causes or quotes.
- Cite numbers with inline links.

## Publication date
Set `published` to a date a few days after the real announcement (usually 2 to 4 days), as if the article was written then, not the day it is actually written. Write the body as of that date: do not mention later events, releases or numbers in the body. Put anything newer in an `## Updates` entry with its own date (see the Updates section where available).

## Length Target
500-800 words, not counting My Take and Updates.

## Input Variables
- Company: {{company}}
- What happened and when: {{event}}
- Official announcement and reports: {{sources}}
- Author's view (optional): {{my_take}}
