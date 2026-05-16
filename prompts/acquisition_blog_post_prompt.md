# Prompt: Write a Blog Post About an Acquisition (Modeled on Post 002)

Use the following prompt to generate a blog post in the same structure and tone as post 002.

---

You are writing an analytical blog post about a company acquisition in the data/AI space.

## Objective
Write a clear, insightful post that explains:
1. The industry problem the acquired company solves
2. Why the acquired company matters
3. Why the acquisition is strategically important for the buyer
4. What this could mean for customers and the broader ecosystem

## Required Tone and Style
- Professional and opinionated, but not hype-driven
- Easy to read for technical and business audiences
- Concrete and specific; avoid generic AI buzzwords
- Use short paragraphs and clear section headings
- Use explicit markdown section titles for every major section (for example: `## The Problem: ...`, `## About ...`).
- Include inline markdown links to official company sources when referencing the acquirer, target, product pages, or official announcement

## Required Structure
Use exactly these sections in this order:

Formatting rule: render each section name below as a markdown H2 title in the output.

1. **Opening Context**
- Start with a short paragraph announcing the acquisition.
- Mention that deal terms may be undisclosed if that is the case.
- Add a bullet immediately after the opening paragraph:
	- `- Estimated Deal Amount: ...`
- The value can be:
	- `Unknown` (if no credible estimate exists), or
	- a range compiled from sources (for example: `$X-$Y based on Source A and Source B`).
- If a range is used, include inline markdown links to each source used for the range.

2. **The Problem: [Domain] Challenges**
- Explain the core technical/business challenge in depth.
- Include why validation, trust, and context are hard problems.
- Use at least one realistic example showing ambiguity in interpretation.
- Frame this section as an industry-wide challenge, not a company-specific weakness.
- Do not reference the acquiring company in this section unless it is required for a neutral factual citation.

3. **About [Acquired Company]**
- Describe what the company does in practical terms.
- Explain its technical differentiators (for example: metadata graph, semantic layer, compiler/orchestration, governance features).
- Show the business value and who benefits.
- Keep this section objective and startup-centric.
- Do not analyze the startup through the acquiring company's perspective in this section.
- Reserve acquirer-specific benefits, synergies, and integration impact for **Understanding the Acquisition** only.
- If public funding history is available, include a short subsection named `### Public Funding Rounds` using this exact line format:
	- `Round - Date - Amount - Link`
- Example format:
	- `Seed - Nov 2021 - $3M - https://...`
- If no credible public funding data is found, write: `Public Funding Rounds: Not publicly available from credible sources.`

4. **Understanding the Acquisition**
- Analyze strategic fit for the acquiring company.
- Explain how the technology likely integrates into the buyer's product stack.
- Include expected impact on end users, developers, and enterprise teams.
- Add one short quote from a relevant executive if available.
- Link the official acquisition announcement and at least one official page from each company when available.

5. **Relevant Tools**
- List 2-4 related products/companies in the same problem space.
- For each, include one short line on why it is relevant.

## Content Requirements
- If specific facts are provided (names, timeline, product names), use them accurately.
- If a fact is unknown, explicitly say it is not publicly disclosed.
- Keep claims grounded; do not invent financial terms or performance metrics.
- Prioritize strategic insight over press-release language.
- Use markdown links sourced from the relevant official company domains for factual references.
- Prefer first-party links from the acquiring company and acquired company over third-party coverage.
- Never invent an estimated deal amount. Use `Unknown` unless credible sources provide an estimate or range.

## Length Target
- 700-1200 words

## Input Variables
Use these inputs when provided:
- Acquiring company: {{acquirer}}
- Acquired company: {{target}}
- Official acquiring company links: {{acquirer_links}}
- Official acquired company links: {{target_links}}
- Estimated deal amount: {{estimated_deal_amount}}
- Deal amount estimate sources (optional): {{deal_amount_sources}}
- Domain/problem area: {{problem_area}}
- Closing timeline: {{timeline}}
- Integration products/platforms: {{integration_points}}
- Optional quote(s): {{quotes}}
- Relevant tools list: {{related_tools}}

## Example Input (From Post 002)
- Acquiring company: Salesforce
- Acquired company: Waii
- Official acquiring company links: https://www.salesforce.com
- Official acquired company links: https://waii.ai
- Estimated deal amount: Unknown
- Problem area: Text-to-SQL for enterprise analytics
- Timeline: Expected close in Q3 FY26
- Integration points: Data Cloud, Tableau Next, Agentforce

Now write the full blog post.
