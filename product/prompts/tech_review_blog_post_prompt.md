# Prompt: Write a TECH REVIEW Blog Post

Use this prompt to generate a business-focused technical review blog post about a new technology, feature, or product capability.

---

You are writing a TECH REVIEW blog post for business and technical readers.

## Objective
Write a clear, practical review that explains:
1. What the new technology or feature is
2. What business problem it is trying to solve
3. How it should help the company or team using it
4. What the implementation looks like in practice
5. What tradeoffs, risks, or limitations should be considered

## Required Tone and Style
- Business-first, but technically credible
- Practical and outcome-oriented
- Clear and concise, without hype
- Use short paragraphs and explicit section titles
- Prefer the vendor’s official documentation, product pages, or announcement pages as the primary source

## Naming Convention
- The output title should start with `TECHREV`
- Example: `TECHREV_LangSmith_SmithDB_Agent_Observability_Data_Layer`

## Required Structure
Use exactly these H2 section titles in this order:

## Opening Context
- Start with 2-4 lines introducing the technology and why it matters.
- State the vendor/product name clearly.
- If available, include a short note about the source page or product area being reviewed.

## What Problem Is It Solving?
- Explain the business or operational problem in plain language.
- Focus on why this matters to the company using it.
- Describe what gets better if this technology works as intended.

## What It Does
- Explain the core capability in simple terms.
- Include the main workflow, architecture, or rollout path at a high level.
- Keep the explanation objective and grounded in the source material.

## How It Should Help the Company
- Focus on business outcomes and operational benefits.
- Describe how it may reduce friction, improve visibility, speed up delivery, lower risk, or improve decision-making.
- Connect the technology to the company’s goals or operating model.

## Implementation Notes
- Summarize the setup, architecture, or adoption path.
- Mention prerequisites, dependencies, rollout status, or production scope that appear in the official source.
- Keep this section practical and concise.

## Tradeoffs and Limitations
- Explain what can be difficult, expensive, or slow about adoption.
- Include cases where the solution may not be worth the effort.
- Be specific about operational, performance, security, or governance constraints.

## Who Should Care
- Identify the teams or roles that benefit most.
- Explain why they would care in one or two sentences.

## Further Reading
- Add 3-5 links to official documentation, product pages, or vendor resources.
- Prefer first-party links.

## Content Requirements
- Keep the focus on the business side of the technology.
- If the source is a product doc, translate technical details into business impact.
- Do not over-explain implementation mechanics unless they affect adoption or value.
- Do not invent outcomes, benchmarks, or customer claims.
- If facts are missing, say so rather than guessing.
- When possible, reference the official product documentation and any related vendor pages.

## Length Target
- 700-1200 words

## Input Variables
Use these inputs when provided:
- Title: {{title}}
- Vendor name: {{vendor_name}}
- Product or feature name: {{product_name}}
- Official source page: {{source_page}}
- Business problem: {{business_problem}}
- Expected company benefit: {{expected_benefit}}
- Implementation notes: {{implementation_notes}}
- Tradeoffs: {{tradeoffs}}
- Relevant teams: {{relevant_teams}}
- Further reading: {{further_reading}}

## Seed Example Input (LangChain SmithDB Announcement)
- Title: TECHREV_LangSmith_SmithDB_Agent_Observability_Data_Layer
- Vendor name: LangChain (LangSmith)
- Product or feature name: SmithDB, the data layer for agent observability
- Official source page: https://www.langchain.com/blog/introducing-smithdb
- Business problem: traditional observability data stores struggle with deeply nested, long-running, multimodal agent traces and complex query patterns at low latency
- Expected company benefit: faster trace analysis, better debugging velocity, and simpler enterprise deployment via object-storage-backed, compute-scalable architecture
- Implementation notes: object storage + Postgres metastore + stateless ingestion/query/compaction services; production traffic migration details included in source
- Relevant teams: AI platform engineering, observability teams, SRE, product engineering, data infrastructure

Now write the full blog post.
