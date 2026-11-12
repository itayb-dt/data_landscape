# Prompt: Write a Blog Post About a Startup Funding Round

**Before writing, read [_writing_rules.md](_writing_rules.md). Its rules override everything below: no research-process language in the article, unverified facts are left out unless the author approves, and the text must not read as AI-written.**

Use this prompt to generate an analytical blog post about a startup funding round in the data/AI space.

---

You are writing a technical business blog post about a startup funding announcement.

## Objective
Write a concise, insightful post that explains:
1. What problem the startup is addressing
2. How its product/technology solves that problem
3. How it compares to main competitors
4. Why this funding round matters strategically
5. How prior rounds and investor quality shape confidence

## Required Tone and Style
- Analytical and technical, but readable to business and technical audiences
- Specific and evidence-driven; avoid hype and generic claims
- Clear section headings and short paragraphs
- No invented facts, metrics, or investor names

## Title
Keep it simple and informative: `<startup> raises <amount> to <what it does>`. Example: "Edelbyte raises $70M to build search and analytics for AI agents". Do not put the investors, the founders' past or the round name in the title if that could read as a different meaning (for example, "from the people who built X" sounds like they funded it). The round and the lead investor go in the Technical Overview.

## Required Structure
Use exactly these sections in this order:

1. **Technical Overview (Short, Semi-Structured)**
- Start with this exact format:

```md
## Technical Overview
- Startup: {{startup_name}} ({{startup_website}})
- Amount Raised: {{amount_raised}}
- Funding Round: {{funding_round}}
- Main Investors: {{main_investors}}
- Problem Area: {{problem_area}}
```

- Keep this section short (5-8 lines total).
- If amount is not public, write `Undisclosed`.
- If investor list is partial, write `Main investors (known): ...`.

2. **The Problem**
- Explain the core technical/business pain point.
- Describe why existing workflows or tools are insufficient.
- Include concrete examples of where teams get blocked.

3. **How They Solve It**
- Explain the startup's product or architecture in practical terms.
- Highlight differentiators (for example: semantic layer, knowledge graph, model orchestration, governance, deployment model, integrations).
- Connect capabilities to measurable business outcomes when data is available.

4. **Competitive Landscape**
- Identify the main competitors in the same segment.
- Explain where the startup is stronger/weaker (speed, accuracy, integration depth, enterprise readiness, pricing model, etc.).
- Avoid absolute claims like "best" unless supported.

5. **Previous Rounds and Capital Trajectory**
- Summarize known prior rounds (seed, Series A, etc.) with dates and amounts if available.
- Explain how this round changes scale, hiring, product roadmap, or go-to-market.
- If prior data is missing, leave it out.

6. **Founder Background (Short) - seed and Series A only**
- Include this section only when the round is a pre-seed, seed or Series A. At this stage the founders are a large part of what investors are buying.
- Name the founders, their roles, and what they did before: prior companies and exits, deep domain research, major platform leadership. Use trusted sources only.
- From Series B on, leave this section out and do not talk about the founders anywhere else in the article.
- If a founder's previous project explains the product (for example, an engine they built at a big company), explain that project in How They Solve It, in plain words, including what it is called today. Say plainly that the new product is an assumption based on their past work when the company has not described it. Keep this section itself brief and factual.

7. **Summary** (seed and Series A) or **Why This Round Matters** (Series B and later)
- Seed and Series A: end with a short Summary, 3 to 5 sentences. It must say something, not repeat the facts above it. Make one point about the problem or the market: why this problem is getting bigger, what the existing players do about it today, and how new companies like this one try to change it. Example: "At petabyte scale, cost is the big issue. Every extra query adds to the bill, and AI agents multiply the queries. New players are trying to end that trade-off." It is not a My Take: no verdict on whether the company will win. Do not restate the amount or the investors. Do not title it "Why This Round Matters": every round matters, and the early ones most of all.
- Series B and later: keep Why This Round Matters. Give a forward-looking but grounded interpretation, and explain what this may signal for customers, partners and the category.

## Content Requirements
- Validate factual details before using them.
- Leave out facts you cannot confirm. Never guess.
- Do not fabricate valuations, customer counts, ARR, or investor participation.
- Prioritize strategic insight over announcement-style wording.

## Publication date
Set `published` to a date a few days after the real announcement (usually 2 to 4 days), as if the article was written then, not the day it is actually written. Write the body as of that date: do not mention later events, releases or numbers in the body. Put anything newer in an `## Updates` entry with its own date (see the Updates section where available).

## Length Target
- 700-1200 words

## Input Variables
Use these inputs when provided:
- Startup name: {{startup_name}}
- Startup website: {{startup_website}}
- Amount raised: {{amount_raised}}
- Funding round: {{funding_round}}
- Main investors: {{main_investors}}
- Problem area: {{problem_area}}
- Product details: {{product_details}}
- Main competitors: {{competitors}}
- Previous rounds: {{previous_rounds}}
- Founder background (optional): {{founder_background}}
- Optional quotes: {{quotes}}

Now write the full blog post.
