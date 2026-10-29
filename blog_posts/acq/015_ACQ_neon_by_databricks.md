---
title: "Databricks acquires Neon to put an agent-ready Postgres next to the lakehouse"
published: 2026-10-27
---
Databricks [agreed to acquire Neon](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems) on May 14, 2025. The companies did not disclose the price; it was reported at about $1 billion ([TechCrunch](https://au.finance.yahoo.com/news/databricks-buy-open-source-database-120751104.html)). Two weeks later its main rival Snowflake [bought Crunchy Data](https://www.businesswire.com/news/home/20250602455530/en/Snowflake-Acquires-Crunchy-Data-to-Bring-Enterprise-Ready-Postgres-Offering-to-the-AI-Data-Cloud), also a Postgres company, reportedly for about $250 million ([TechTarget](https://www.techtarget.com/searchdatamanagement/news/366625068/Snowflake-acquisition-of-Crunchy-Data-adds-Postgres-database), citing reports; not confirmed by Snowflake). Both data platforms wanted a transactional database, and both chose Postgres.

<figure class="shot">
  <img src="{{ '/assets/images/neon/hero.png' | relative_url }}" alt="Databricks and Neon logos" loading="lazy">
  <figcaption>Databricks and Neon. Source: <a href="https://www.databricks.com/blog/databricks-neon">Databricks</a>.</figcaption>
</figure>

## The Problem: Operational databases are slow to create, expensive to idle and hard to copy

A transactional database is the system an application writes to. Classic Postgres on a server is a long-lived thing: you size it, provision it, pay for it around the clock and treat it with care, because it holds the only copy of production data.

That model strains in two ways. First, cost: a team with dozens of dev, test and preview environments pays for databases that are idle most of the day. Second, safety: giving a developer realistic data to test against usually means a slow dump and restore, or a risky shared staging database.

AI agents make both worse. An agent that writes code needs a database to try it on, and it may need a fresh one for every attempt. It also needs real data as context, but it cannot be trusted with production. Humans create a few databases a week. Agents create them by the thousands.

## The Solution: Serverless Postgres with storage separated from compute

[Neon](https://neon.com/) is open-source-based Postgres that [separates storage from compute](https://neon.com/blog/neon-and-databricks) and puts a branchable, versioned storage layer underneath. That gives three practical properties:

- **Fast and cheap to start.** Databricks says Neon can spin up [a fully isolated Postgres instance in 500 milliseconds or less](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems). Compute scales automatically and can scale to zero when idle, so an unused database costs little.
- **Branching.** A branch is an instant copy of a database, [schema and data together](https://www.databricks.com/blog/databricks-neon), without copying the underlying files. Experiments never touch production.
- **A plain Postgres interface.** Existing drivers, tools and extensions work, and there is one connection string.

The benefit goes to developers who want a database per pull request, and to platforms that build apps on behalf of users. Neon says that [over 80% of the databases on its platform](https://neon.com/blog/neon-and-databricks) were being created by AI agents rather than humans, a figure Databricks repeats from Neon's internal telemetry.

<figure class="shot narrow">
  <img src="{{ '/assets/images/neon/agents-create-databases.png' | relative_url }}" alt="Chart: AI agents create 4x more databases than humans on Neon, from 30% in October 2024 to over 80% in May 2025" loading="lazy">
  <figcaption>Neon's own chart: the share of databases created by agents grew from about 30% to over 80%. Source: <a href="https://www.databricks.com/blog/databricks-neon">Databricks</a>.</figcaption>
</figure>

### Funding history

- Series A-1 - Jul 2022 - $30M - [BigDATAwire](https://bigdatawire.com/2022/07/27/neon-raises-30m-for-its-postgres-as-a-service)
- Series B - Aug 2023 - $46M, led by Menlo Ventures, $104M raised to date - [EdgeIR](https://edgeir.com/serverless-postgres-provider-neon-scores-46m-in-series-b-funding-round-20230803)

Sources disagree on later funding and on the total raised, so only the rounds above are listed.

## Understanding the Acquisition

Databricks built its business on analytics: the lakehouse, Spark and the warehouse. What it lacked was the other half of the stack, the operational database where applications live. Databricks frames the transactional (OLTP) database market as [large and dominated by older products](https://www.databricks.com/blog/databricks-neon), ready for change. Without an OLTP offer, an application's data always starts in someone else's database, and Databricks only meets it after it has been copied over.

Neon completes the basics. With it Databricks can offer the transactional store, the lakehouse and the governance layer in one platform. Within a month of the announcement Databricks [launched Lakebase](https://siliconangle.com/2025/06/11/following-neon-acquisition-databricks-launches-serverless-lakebase-database/), a serverless Postgres built on Neon's technology, and Lakebase became [generally available on AWS](https://www.dbta.com/Editorial/News-Flashes/Databricks-Lakebase-is-Now-Generally-Available-Delivering-Reliability-Performance-and-Governance-173362.aspx) in February 2026. It is governed by Unity Catalog and has sync tables that keep operational data aligned with lakehouse tables, so teams do not build a pipeline between the two worlds.

Why Neon and not another Postgres vendor? Databricks could have bought a conventional Postgres provider, or built its own. The agent story is what sets Neon apart. Ali Ghodsi said:

> "The era of AI-native, agent-driven applications is reshaping what a database must do. Neon proves it: four out of every five databases on their platform are spun up by code, not humans."

Instant, cheap databases suit agents that create many short-lived environments. Branching lets an agent receive a copy of real data as context, then test, fail and be thrown away without risk. The same properties serve human developers, but agents turn them into requirements.

Snowflake's logic with Crunchy Data was similar, but its emphasis differs. Snowflake [wants to fill the gap](https://www.techtarget.com/searchdatamanagement/news/366625068/Snowflake-acquisition-of-Crunchy-Data-adds-Postgres-database) left by its earlier Unistore and Hybrid Tables attempts, with a Postgres that is enterprise-ready and, per Snowflake, FedRAMP-capable. Crunchy brings security and compliance for regulated industries; Neon brings developer and agent ergonomics.

For existing customers, Databricks said it [will keep investing in Neon](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems) for new and current users. Neon's docs describe it as [continuing as its own product](https://neon.com/docs/introduction/neon-and-lakebase), aimed at developers, startups and agent platforms, on the same technology that powers Lakebase.

## Relevant Products and Companies

Postgres itself is not the differentiator: there are many Postgres providers, and every cloud vendor has one. What matters is how tightly a data platform integrates with it. Two other examples of that integration:

- [Snowflake Postgres (Crunchy Data)](https://www.snowflake.com/): Snowflake's parallel move, built on the Crunchy Data acquisition and aimed at regulated enterprises.
- [ClickHouse](https://clickhouse.com/): it [acquired PeerDB](https://clickhouse.com/blog/clickhouse-acquires-peerdb-to-boost-real-time-analytics-with-postgres-cdc-integration) in 2024 for real-time replication from Postgres, and in January 2026 [announced a native Postgres service](https://www.businesswire.com/news/home/20260122173204/en/ClickHouse-Announces-Native-Postgres-Service-Offering-a-Unified-Data-Stack-for-Real-Time-and-AI-Driven-Applications), built with Ubicloud, so Postgres and analytics sit side by side.

## My Take

Data is complicated, and agents make it even more complicated. I see two different directions.

The first is that data is stored everywhere: relational OLTP databases, document databases, and data lakes full of files. Integration, managing the catalog and consistency across all of it are real problems. When we look at the entire data landscape, which is what this blog is about, vendors need to address many of these aspects at once. That is true for Databricks, ClickHouse and Snowflake, and for the three main clouds.

The second is agents, which is a different and new story. How do you give an agent context? It starts a conversation, goes for lunch and comes back an hour later. How does it get access to tables, wherever they are stored, so it can give an answer? That is a separate problem from where the data lives.

Neon fits this vision. Databricks could have acquired any other Postgres provider, or built its own, and a billion dollars is a lot of money for that. Neon brings a good story about agents: databases that are cheap and fast to create, that scale to millions of databases a day, with vector search built in ([Lakebase supports pgvector](https://siliconangle.com/2025/06/11/following-neon-acquisition-databricks-launches-serverless-lakebase-database/)), and a branch that gives the agent real data as context. That goes beyond a classic Postgres vendor, and I think it is what justified the price.

It also fits a pattern I keep seeing: Postgres is the starting point for everything. Snowflake and Databricks each bought a Postgres company within two weeks of each other, ClickHouse is building its own Postgres story, and the reason is the same: analytics platforms now need the transactional side, and Postgres is what developers already use.
