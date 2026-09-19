# Prompt: Write a DB Review Blog Post

Use this prompt to generate a structured review of a database product.

---

You are writing a DB review blog post for technical and business readers.

## Objective
Write a clear, opinionated review that explains:
1. What the database is and who built it
2. What problems it is designed to solve
3. What it is best suited for
4. How it compares to main competitors
5. A personal take on whether it lives up to the hype

## Required Tone and Style
- Technically grounded but accessible to engineering managers and architects
- Opinionated and direct — this is a review, not a press release
- Short paragraphs and explicit section titles
- No invented benchmarks or customer claims
- The personal thoughts section should be first-person and candid

## Naming Convention
- The output title should start with `DB`
- Example: `DB_DuckDB_Analytical_Queries_Local_First`

## Required Structure
Use exactly these H2 section titles in this order:

## Opening Context
- 2-4 lines introducing the database and why it is worth reviewing.
- State the vendor, open-source status, and the release or version being reviewed if relevant.
- Include inline links to the official website and documentation.

## What Is {{db_name}}?
- Short plain-language description.
- State the database category (relational, columnar, document, vector, graph, time-series, multi-model, etc.).
- List 3-5 core architectural properties as bullets.

## What Problems Does It Solve?
- Explain the operational or analytical gaps this database addresses.
- Describe the workflow pain points it targets.
- Keep this section about the industry problem, not just about the product.

## What It Is Best For
- List the top 2-4 use cases where this database shines.
- For each, explain concretely why this database fits better than the alternatives.
- Use this format: `**Use case**: why it fits.`

## What It Is Not Good For
- Be specific about the scenarios where this database is the wrong tool.
- Include architectural limits, operational complexity, or ecosystem gaps.
- Use this format: `**Scenario**: why it falls short.`

## Competitive Landscape
- Identify 3-5 direct competitors.
- For each, write one line comparing it to {{db_name}} on the dimension that matters most (speed, cost, ease of use, ecosystem, scalability, query model, etc.).
- Use this format: `**Competitor** — one-line comparison.`
- Include links to competitor official sites when available.

## My Take
- Write this section in first person.
- Give an honest, direct opinion on the database: is it worth adopting, who should seriously consider it, and what gives you pause.
- Address the hype vs. reality gap if one exists.
- End with one sentence on what you will be watching going forward.

## Further Reading
- Add 3-5 links to official docs, architecture papers, or credible technical sources.
- Prefer first-party links.

## Content Requirements
- Do not invent performance numbers, customer names, or funding data.
- If a comparison claim is uncertain, label it as an opinion.
- Ground technical claims in official documentation or well-known public benchmarks.
- Keep the focus on practical value, not feature checklists.

## Length Target
- 800-1300 words

## Input Variables
Use these inputs when provided:
- DB name: {{db_name}}
- DB website: {{db_website}}
- DB docs: {{db_docs}}
- Category: {{db_category}}
- Open source: {{open_source}}
- Version or release context: {{version}}
- Problems it solves: {{problems}}
- Best use cases: {{best_for}}
- Not good for: {{not_good_for}}
- Main competitors: {{competitors}}
- Personal notes / opinions: {{personal_notes}}
- Further reading: {{further_reading}}

Now write the full blog post.
