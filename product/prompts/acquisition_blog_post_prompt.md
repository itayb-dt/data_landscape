# Prompt: Write a Blog Post About an Acquisition

Use this prompt to write an acquisition article. All acquisition articles share one structure, so a reader always knows where to find the problem, the solution and the strategic reasoning.

Reference articles: [Dremio / SAP](../../blog_posts/acq/003_ACQ_dremio_by_sap.md) and [DuckLabs / AWS](../../blog_posts/acq/013_ACQ_ducklabs_by_aws.md).

---

You are writing an analytical blog post about a company acquisition in the data/AI space.

## Objective
Write a clear, insightful post that explains:
1. The industry problem the acquired company solves
2. How the acquired company solves it
3. Why the acquisition matters strategically for the buyer
4. What this could mean for customers and the broader ecosystem

## Required Tone and Style
- Professional and opinionated, but not hype-driven
- Easy to read for technical and business audiences
- Concrete and specific; avoid generic AI buzzwords
- Short paragraphs and clear section headings
- Inline markdown links to official company sources when referencing the acquirer, the target, product pages, or the official announcement
- Prefer first-party links (acquirer and target domains) over third-party coverage

## Required Structure

The site renders a header above the article with the announcement date, deal value, category and official links. The article must not repeat those facts as a list.

Ignore the status of the deal. Assume it will close or has closed. Do not write about pending, expected or completed closing, regulatory approval, and do not set `status` in `_data/events.yml`.

### Title (front matter `title`)
Format: `<Acquirer> acquires <Target> to <short, specific reason>`

- Example: `SAP acquires Dremio to give AI agents one governed view of SAP and non-SAP data`
- The reason says what the buyer gets, not what the target is.
- Use the same text as `headline` in `_data/events.yml`.

### Lead paragraph (no heading)
Two or three sentences straight after the front matter:
- What was announced and when, with an inline link to the official announcement.
- The terms: say the price was not disclosed if that is the case. Do not mention closing.
- The one thing that matters most about the deal.

If a credible estimate of the deal value exists, state it here and put the source in parentheses with an inline link, for example `about $1 billion ([TechCrunch](https://...))`. Never invent an estimate. If there is none, say the price was not disclosed. Context that is sourced (team size, funding model) may be added.

### 1. `## The Problem: <short, specific problem>`
- Example: `The Problem: Enterprise AI can't reason over fragmented data`
- Phrase it as a problem, not as a solution or a wish. Write `Analytics needs a data warehouse, with all its complexity`, not `Analytics shouldn't require a warehouse`.
- Explain the industry-wide challenge in depth: why it is hard, and why validation, trust and context matter.
- Include at least one realistic example showing ambiguity in interpretation.
- Frame it as an industry problem, not a weakness of one company.
- Do not mention the acquirer unless needed for a neutral factual citation.

### 2. `## The Solution: <short description of the approach>`
- Example: `The Solution: An open lakehouse that queries data where it lives`
- Describe what the target does in practical terms and its technical differentiators.
- Show the business value and who benefits.
- Keep it objective and startup-centric. Do not analyze the target through the acquirer's perspective here; that belongs in Understanding the Acquisition.
- End with `### Funding history`, one line per round in this format:
  - `Round - Date - Amount - Link`
  - Example: `Seed - Nov 2021 - $3M - https://...`
- If no credible public funding data is found, write: `Public Funding Rounds: Not publicly available from credible sources.`

### 3. `## Understanding the Acquisition`
This title is fixed. Do not add company names.
- Analyze the strategic fit for the buyer.
- Explain how the technology likely integrates into the buyer's product stack.
- Cover the expected impact on end users, developers and enterprise teams.
- Include one short quote from a relevant executive if available.
- Link the official announcement and at least one official page from each company when available.
- Cover what happens to open source projects, customers and existing products, if relevant.

### 4. `## Relevant Products and Companies`
This title is fixed.
- List 2-4 related products or companies in the same problem space, as a bulleted list.
- Each gets one short line on why it is relevant, with a link to its official site.
- Include tools that are tightly coupled to the target or the buyer, or close alternatives. Do not list extensions or features of other products.
- When the space is crowded with commodity providers (for example Postgres, which every cloud offers), say so in one sentence instead of listing them, and list only the examples that matter for the point of the article.

### 5. `## My Take` (required)
Every acquisition article has one. It is the author's own view in first person, and it is what makes the article more than a summary of announcements.
- Use the author's opinion when they give one. Keep their points and wording close.
- When they have not given one, draft it from the themes they repeat across the blog (data is complicated and agents make it more so, data is stored everywhere, Postgres as the starting point, what users actually want) and the direction in the announcements. Hand it over as a draft for the author to rewrite. Never present a draft as final.
- State a direction, not a summary: where the buyer is heading, what it will likely build next, and why it fits. Write it as an expectation ("I expect...", "the next reasonable step is..."), grounded in sourced facts from the article.
- If the article has an `## Updates` entry that shows what the buyer actually shipped, My Take must describe that direction in advance, as the author's analysis, and the update entry then closes the loop with a sentence such as "This is the direction described in My Take." My Take must not mention the update's facts as already known. Link to `#updates` only from the update entry, not from My Take.
- Do not invent facts, numbers or quotes in My Take. Opinions are the author's to rewrite; facts need sources.

### 6. `## Updates` (optional)
Articles are live. When the market moves (for example, the buyer ships the integration), add a dated entry here instead of rewriting the article.
- Start the section with an italic line saying these are late additions, published after the original article, and not part of the official announcements.
- Each entry is `### <Date>: <short title>`, newest last, with sourced facts and inline links.
- Do not add update sources to the `links` list in `_data/events.yml`. That list is for the original announcements only.
- Mention the update from Understanding the Acquisition with a link to `#updates` when it changes the picture. My Take does not link to it (see My Take).

## Images
Every article has a hero image and, where they exist, one or two images that explain something.
- **Hero**: the announcement graphic from the buyer's or target's own post (usually its `og:image`). Place it right after the lead paragraph, before `## The Problem`.
- **Explanatory**: an architecture diagram, a chart or a product screenshot from the original sources, placed next to the paragraph it supports. Do not use headshots, stock photos or decorative backgrounds.
- Download them (do not hotlink), save under `assets/images/<target>/` with a descriptive file name, and cap the longest side at about 1400px.
- Use this markup so the page gets a caption with the source link (add `narrow` to the class for tall diagrams):

```html
<figure class="shot">
  <img src="{{ '/assets/images/<target>/<file>.png' | relative_url }}" alt="Describe what it shows" loading="lazy">
  <figcaption>What it shows. Source: <a href="https://original.page/">Site</a>.</figcaption>
</figure>
```

## Content Requirements
- Use specific facts provided (names, timeline, product names) accurately.
- If a fact is unknown, say it is not publicly disclosed.
- Keep claims grounded. Do not invent financial terms, performance metrics or download counts.
- Cite numbers with inline links to the source.
- Prioritize strategic insight over press-release language.

## Length Target
700-1200 words, not counting My Take and Updates.

## Input Variables
- Acquiring company: {{acquirer}}
- Acquired company: {{target}}
- Official acquiring company links: {{acquirer_links}}
- Official acquired company links: {{target_links}}
- Deal value and sources (if any credible estimate exists): {{deal_value_sources}}
- Domain / problem area: {{problem_area}}
- Integration products / platforms: {{integration_points}}
- Optional quote(s): {{quotes}}
- Relevant products and companies: {{related_products}}
- Author's take (optional, a draft is written when missing): {{my_take}}

## After Writing
1. Save the article as `blog_posts/acq/NNN_ACQ_<target>_by_<acquirer>.md` with front matter containing `title` and `published` (the date the article was written, `YYYY-MM-DD`). The page header shows both the announcement date (from the event) and the written date, so readers can tell them apart.
2. Add or update the event in `_data/events.yml`: set `post` to the article's `.html` path, and add the card fields (see the other analysed events). Keep `headline` identical to the title.
