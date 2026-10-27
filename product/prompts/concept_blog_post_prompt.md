# Prompt: Write a Blog Post Explaining a Data/AI Concept

Use this prompt to generate a structured, practical explainer about a technical concept.

---

You are writing a concept explainer blog post for technical and business readers.

## Objective
Write a clear blog post that explains:
1. What the concept is (short definition)
2. What problem it is designed to solve
3. Main advantages and why teams adopt it
4. Real-world use cases and relevant companies
5. Key disadvantages and when the concept is not a good fit

## Required Tone and Style
- Clear, practical, and precise
- Strong technical grounding without unnecessary jargon
- No hype language
- Short paragraphs and explicit section titles
- Use concrete examples whenever possible

## Required Structure
Use exactly these H2 section titles in this order:

## Opening Context
- Start with 2-4 lines introducing the concept and why it matters now.
- Add one line with update metadata when available:
  - Last updated: {{last_updated}}
  - Created: {{created_date}}

## What Is [Concept]?
- Give a short definition in plain language.
- Add a compact technical definition.
- Include 3-5 bullet points describing core architectural properties.

## What Problem Is It Designed to Solve?
- Explain the bottlenecks in older approaches.
- Clarify the tradeoffs this concept addresses.
- Keep this section generic and industry-wide, not vendor-specific.

## Main Advantages
- List only 1-3 top advantages.
- Use one line per bullet in this exact format: `**Advantage**: practical implication.`
- Do not use sub-bullets in this section.

## Real-World Use Cases
- First identify the main company most associated with implementing the concept, then find 1-2 use cases from that company's official site.
- Prefer first-party customer stories, solution pages, or product use-case pages from that company.
- Write this section as short explanatory paragraphs, not bullets.
- For each example, explain how the concept changes the operating approach, not just what the company does.
- Include inline markdown links to the official source pages used.

## Relevant Companies and Systems
- List well-known examples with one line each.
- Include links to official company or product pages when available.
- Example style:
  - Snowflake - cloud data warehouse with separated storage and compute.
  - Neon (Postgres) - serverless Postgres architecture with decoupled storage and compute.

## Tradeoffs, Disadvantages, and Limits
- Start this section with a short narrative sentence such as: `Of course, there are also real disadvantages and tradeoffs to this approach.`
- Merge drawbacks and "not a good fit" guidance into this single section.
- Use only 2-3 bullets in this section.
- Each bullet must be one line in this exact format: `**Subject**: explanation.`
- Include both architectural drawbacks and scenarios where another approach may be a better fit.

## Practical Decision Framework
- Provide a short checklist to decide whether to adopt this concept.
- Keep this actionable and concise.

## Further Reading
- Add 3-6 links to credible references.
- Prefer official docs, architecture papers, or primary technical sources.

## Content Requirements
- Clearly separate facts from opinion.
- If a claim is uncertain, label it as a hypothesis or viewpoint.
- Do not invent benchmarks, numbers, customer names, or quotes.
- If comparing architectures (for example: co-located vs decoupled), describe both fairly.

## Length Target
- 900-1400 words

## Input Variables
Use these inputs when provided:
- Concept: {{concept}}
- Last updated: {{last_updated}}
- Created: {{created_date}}
- Short definition notes: {{definition_notes}}
- Problem to solve: {{problem_to_solve}}
- Advantages: {{advantages}}
- Use cases: {{use_cases}}
- Relevant companies: {{relevant_companies}}
- Disadvantages: {{disadvantages}}
- Not-a-fit scenarios: {{not_a_fit}}
- References: {{references}}

## Seed Example Input (Separation of Storage and Compute)
- Concept: Separation of Storage and Compute
- Last updated: Nov 4, 2025
- Created: Mar 3, 2025
- Problem to solve: inability to scale compute and storage independently in co-located systems
- Relevant companies: Snowflake, Google BigQuery, Amazon Redshift Spectrum, ClickHouse Cloud, Neon

Now write the full blog post.
