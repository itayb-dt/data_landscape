---
title: "Workday to acquire Honeydew, a semantic layer for AI and BI"
published: 2026-11-18
---
<p class="disclaimer" style="color:#ff5a5a;font-weight:700;border-left:3px solid #ff5a5a;background:rgba(255,90,90,.1);padding:10px 14px;border-radius:0 8px 8px 0"><strong style="color:#ff5a5a">Disclosure: I am an investor in Honeydew. Everything here is my personal opinion and does not represent Dynatrace.</strong></p>

Workday [announced on November 18, 2026](https://newsroom.workday.com/2026-11-18-Workday-Announces-Intent-to-Acquire-Honeydew,-a-Semantic-Layer-for-AI-and-Business-Intelligence) that it intends to acquire Honeydew, a startup that gives AI agents and BI tools the same business definitions. The price was not disclosed. The one thing that matters: Workday wants its AI agents to compute a number the same way every time, and not to improvise it.

<figure class="shot">
  <img src="{{ '/assets/images/honeydew/hero.jpg' | relative_url }}" alt="Honeydew: Compiler and Memory" loading="lazy">
  <figcaption>Honeydew's homepage image. Source: <a href="https://honeydew.ai/">Honeydew</a>.</figcaption>
</figure>

## The Problem: The same business question gets different answers

Ask a company "what is our headcount?" and the answer depends on definitions. Does it count only full-time employees, or contractors too? Does it include roles that are approved but not yet filled? Workday uses this very example in its announcement. In most companies each dashboard, each report and each analyst has a private answer, written into their own query.

AI agents make this worse. An agent that is asked the question has to find the right tables, join them and decide what "headcount" means, and it does this from scratch on every request. Workday calls the common workaround "schema-stuffing": pasting the data dictionary and the join rules into every prompt. When the team changes the model or the platform, it starts over. The risk is a different answer to the same question from one run to the next, or a wrong number that nobody notices, in places as sensitive as payroll.

## The Solution: One place for business definitions, turned into queries by a compiler

A **semantic layer** is the place where a company defines its terms once: what revenue is, what a customer is, how headcount is counted. Every tool then asks for "headcount" and gets the same answer.

[Honeydew](https://honeydew.ai/) is a semantic layer for AI and BI. Its way of working, from its own [description](https://honeydew.ai/semantic-compiler/), is a compiler and not a text-to-SQL model: "The AI decides what to ask. It never decides how." The agent asks for a metric, and Honeydew resolves the definition, the joins and the filters from the semantic model and generates the SQL. The company says that compilation is deterministic, so the same question becomes the same SQL whether an agent, a dashboard or Excel asked it.

What it connects to, per Honeydew's site:

- **Data warehouses:** Snowflake, Databricks and Google BigQuery. Honeydew says it processes data inside the customer's own warehouse.
- **BI tools:** Power BI and Tableau, plus Excel.
- **AI agents:** through MCP, the standard protocol for connecting agents to tools, and through SQL and GraphQL APIs.
- **Governance:** changes to definitions are versioned in the customer's Git provider.

Named on its homepage as a customer is Pizza Hut, quoted saying that everyone gets the same answer. Honeydew is based in Tel Aviv and went through Y Combinator in the winter 2023 batch. [Y Combinator](https://ycombinator.com/companies/honeydew) lists David Krakov, Baruch Oxman and Liron Slonimsky-Shemy as the founders. Krakov previously founded Varada, a data lake acceleration company that Starburst acquired in 2022. A [Snowflake blog post](https://www.snowflake.com/en/blog/investment-honeydew-business-intelligence) is titled "Honeydew Revolutionizes Business Intelligence with Investment from Snowflake Ventures".

## Understanding the Acquisition

Workday sells HR and finance software, and its customers' most sensitive numbers sit in Workday. The company has been building agents for those customers, and its CTO, Gabe Monroy, put the problem plainly in the announcement: "An AI model shouldn't be improvising the calculation behind a payroll number."

The plan is to embed Honeydew's semantic compiler in **Workday Data Cloud**. According to Workday, the model says what it needs and Workday builds the exact query, the same way every time, and applies the customer's definitions to live data in Data Cloud. That differs from semantic layers that work on data already extracted into a warehouse or lake. Workday also says its permissions travel with the definitions, so an invalid or unauthorized request would be blocked before any query runs. Yasmeen Ahmad, who runs Workday Data Cloud, said that the biggest bottleneck in enterprise AI is not reasoning but context.

For Workday this is the trust layer for agents. It is not a new product line, and Workday describes it as part of its platform for HR, finance and IT.

What happens to Honeydew customers who are not Workday customers is not said in the announcement. Honeydew works with Snowflake, Databricks and BigQuery, and a Constellation Research analyst expects it to keep working beyond Workday data. That is the analyst's view, not a commitment from Workday.

## Relevant Products and Companies

- [dbt Semantic Layer](https://www.getdbt.com/product/semantic-layer): the semantic layer from dbt Labs, tied to its transformation tool.
- [Cube](https://cube.dev/): a semantic layer that sits between data sources and applications.
- [AtScale](https://www.atscale.com/): a semantic layer for BI and analytics.
- [Snowflake](https://www.snowflake.com/): Honeydew's first warehouse, and an investor through Snowflake Ventures.

## My Take

I am personally involved here, so read this with that in mind. One of the founders worked part time at my startup, Metis, which Dynatrace acquired, for a few months while he was going through the ideation process for Honeydew. That is why there was never a question that I would invest in his idea.

This is also a lesson. Ideation does not take five days a week. It takes time, and it is good to keep working while you take that time to decide what to build.

I think they played it right. They built on Snowflake, formed a partnership with Snowflake, and Snowflake Ventures invested in them. For an infrastructure startup, a strong partner or investor like that helps a lot with gaining trust from customers and with hiring good people. I know this from my previous startup, where Microsoft invested through M12.

There are open source semantic layers too. I think they are not as good, and a semantic layer that people trust with their numbers takes more than code: it takes people who know how to lead it. That is what Workday gets along with the product.
