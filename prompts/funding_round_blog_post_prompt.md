# Prompt: Write a Blog Post About a Startup Funding Round

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
- If prior data is missing, say so explicitly.

6. **Optional: Founder Background (Short)**
- Add only if credible public information exists.
- Include a few lines on notable founder experience (for example: prior exits, deep domain research, major platform leadership).
- Keep this section brief and factual.

7. **Why This Round Matters**
- Provide a forward-looking but grounded interpretation.
- Explain what this may signal for customers, partners, and the category.

## Content Requirements
- Validate factual details before using them.
- Mark unknown facts clearly instead of guessing.
- Do not fabricate valuations, customer counts, ARR, or investor participation.
- Prioritize strategic insight over announcement-style wording.

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
