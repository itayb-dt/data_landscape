---
title: "Salesforce acquires Waii to let anyone query enterprise data in plain language"
---
Salesforce has acquired Waii, a natural-language-to-SQL startup. The exact details of the deal were not disclosed. Once it closes, expected in Q3 FY26, Waii's capabilities will be integrated into Salesforce Data Cloud.

<figure class="shot">
  <img src="{{ '/assets/images/waii/hero.png' | relative_url }}" alt="Salesforce announcement graphic for the Waii acquisition" loading="lazy">
  <figcaption>Salesforce's announcement of the Waii deal. Source: <a href="https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-waii/">Salesforce</a>.</figcaption>
</figure>

## The Problem: Text-to-SQL can't see business context

Text to SQL technology represents one of the most complex challenges in enterprise AI. Unlike traditional software features where testing is straightforward, authentication either works or fails when given wrong credentials, but SQL query validation is inherently ambiguous. When a system returns "$45M in sales for the top 5 categories in the South region," how do you verify if that's correct?

The fundamental problem isn't just translating English to SQL syntax; it's understanding business context, data relationships, and implicit assumptions. In practice, three analysts looking at the same dataset can arrive at different conclusions based on how they interpret "South region" (geographic boundaries? sales territories?), "top categories" (by revenue? units? margin?), or even basic time periods. Poor documentation compounds this challenge. If humans struggle to understand data schemas and business rules, how can AI systems be expected to navigate these complexities reliably?

As Waii's CEO Gunther Hagleitner puts it: "In a world where every database speaks a different dialect of SQL, we built Waii to close the gap between what people want to ask and what their data systems can understand." This highlights why advanced solutions need to go beyond simple language translation; they must encode not just technical relationships but business context and governance rules that traditional text to SQL approaches often miss.

## The Solution: A knowledge graph that maps the data landscape

Waii is an enterprise grade natural language to SQL platform that translates plain language questions into production ready SQL queries. The startup's key innovation is a dynamic metadata knowledge graph that maps an organization's entire data landscape, representing not just database schemas, but the intricate relationships between tables, columns, business metrics, and governance rules.

Waii's platform goes beyond prompt to SQL basics with a dialect aware SQL compiler, built in query optimization, and full stack enterprise integration all powered by its knowledge graph foundation. This rich, contextual understanding allows its core engine to translate natural language questions into highly accurate, deeply contextual SQL queries.

The problem Waii addresses is universal across enterprises: the disconnect between people who need data insights and those who can technically access it. Enterprises are generating more data than ever, but its value remains locked behind technical and semantic complexity, creating bottlenecks where business decisions are delayed while waiting for technical teams.

## Understanding the Acquisition

The acquisition makes perfect strategic sense for Salesforce's AI powered enterprise vision. The Salesforce ecosystem includes millions of non technical users who currently rely on technical teams to translate data queries or navigate disconnected data silos.

By acquiring Waii, Salesforce aims to "democratize" data access and remove technical barriers. As Raveendrnathan Loganathan, EVP of Salesforce Data Cloud, stated: "The future of business isn't about having the most data; it's about making that data speak a common language. Our vision is to empower every employee, from the boardroom to the frontline, to have a trusted conversation with their data. With Waii, we're not just augmenting our stack; we're acquiring the catalyst that makes this vision a reality for our customers."

Once the deal closes in Q3 FY26, Waii's capabilities will integrate into Data Cloud, enabling AI driven workflows across Salesforce's offerings including Tableau Next and Agentforce. Waii's technology will form the foundation of Tableau's next generation semantic engine, powered by a live knowledge graph that enables faster, more relevant analytics through true language driven exploration, where the system understands the user's intent, not just their words.

## Relevant Products and Companies

- **SkySQL**: how SkySQL enables smarter text-to-SQL agents with LlamaIndex.
- **[Vanna.ai](https://vanna.ai/)**: a personalized AI SQL agent.
