# Prompt: Write a Blog Post About a Merger

**Before writing, read [_writing_rules.md](_writing_rules.md). Its rules override everything below: no research-process language in the article, unverified facts are left out unless the author approves, and the text must not read as AI-written.**

Use this prompt for a merger of two companies that combine as equals, so neither is the buyer. If one company buys the other, use the acquisition prompt instead.

---

You are writing for technical and business readers who follow the data and AI market.

## Objective
Explain what each company does, what the merger is, and why the two chose to merge instead of one buying the other. Keep it factual, with the companies' own announcements as the base and your analysis clearly labeled.

## Required Tone and Style
- Clear, practical, no hype. Short paragraphs.
- Facts come from the announcements of both sides. Where a number comes from one side only, say whose it is.
- Mark what is analysis. Anything the companies did not say is "my analysis" or "hypothesis".

## Required Structure
Title (front matter `title`): "<Company A> and <Company B> merge to <purpose>". Name both companies. Do not use "acquire".

Lead paragraph (no heading): the announcement date, with a link to one announcement, the form of the deal (for example all-stock), the headline number if one exists, and that it is a merger, not an acquisition. Leave out anything the announcements do not cover.

Hero image right after the lead, if a shared graphic exists.

### 1. `## What Each Company Does`
One short paragraph per company, in its own words where possible. Name the main products and the one or two earlier acquisitions that matter. Say how the two fit together today.

### 2. `## Understanding the Merger`
One section, three parts in this order. Do not add a separate "Why" heading.
- **The facts**: bullets, one line each: **Structure**, **Leadership** (who is CEO and who holds which role), **Scale** (combined revenue and customers, with whose figures they are), **Products and brands**, **Open source and licensing**, **Name of the combined company**. Leave out anything the announcements do not cover. Do not repeat the facts shown in the page header.
- **Why they say they merged**: a short paragraph with the reasons both sides give, with short quotes and attribution.
- **Why neither company simply bought the other**: your analysis, introduced with a sentence that says the companies do not state this. Consider price and who pays (all-stock vs cash), relative size, identity and trust (open source communities, neutral positioning), differences in business model and culture, and shared investors or board members. Present these as hypotheses, as short bullets.

### 3. `## Relevant Products and Companies` (optional)
One line each, with links.

### 4. `## The Announcements`
Links to the announcement of each side, one bullet each, with the author or title.

### 5. `## My Take` (required, written by or approved by the author)
Do not invent a personal view. Propose a draft in the chat and wait for approval.

### 6. `## Updates` (optional)
Dated entries for what happens later, such as closing, rebranding or product changes. Start the section with an italic line saying these are late additions, published after the original article and not part of the official announcements. Each entry is `### <Month Year>: <short title>`.

## Publication date
Set `published` to a date 2 to 4 days after the real announcement, as if the article was written then. Write the body as of that date and put anything newer in Updates.

## Images
Use the shared announcement graphic or an architecture diagram from the announcements. Download it (do not hotlink), save under `assets/images/<companies>/`, cap the longest side at about 1400px, and use the `<figure class="shot">` markup with a source link. No headshots.

## Events file (`_data/events.yml`)
Add an event with `type: merge`, `date` (announcement), `when`, `company_a`, `abbr_a`, `color_a`, `company_b`, `abbr_b`, `color_b`, `headline` (same as the title), `tldr` (facts only, one or two sentences), `signal` (why it was done, not a repeat of the tldr), `facts` (label/value pairs such as Announced, Structure, Combined ARR, Closed), `links` (the announcements of both sides) and `post`. Logos come from `_data/logos.yml` when the company is listed there, otherwise the abbreviation square is shown.

## Length Target
500 to 800 words, not counting My Take and Updates.

## Input Variables
- Companies: {{company_a}} and {{company_b}}
- Announcements of each side: {{sources}}
- Deal terms (structure, value, leadership, closing): {{deal_terms}}
- Author's view (optional): {{my_take}}
