---
title: "Databricks acquires Mooncake Labs to mirror Lakebase Postgres into the lakehouse in real time"
published: 2025-10-04
---
Mooncake Labs, a small startup that mirrors Postgres data into open lakehouse tables, [is joining Databricks](https://www.databricks.com/blog/mooncake-labs-joins-databricks-accelerate-vision-lakebase) to accelerate Lakebase, Databricks' Postgres database. The price was [not disclosed](https://www.techtarget.com/searchdatamanagement/news/366631950/Mooncake-acquisition-boosts-Databricks-database-capabilities), and the team is the point: it is a very small company with three founders.

<figure class="shot">
  <img src="{{ '/assets/images/mooncake/hero.jpg' | relative_url }}" alt="Databricks and Mooncake logos" loading="lazy">
  <figcaption>Mooncake Labs joins Databricks. Source: <a href="https://www.databricks.com/blog/mooncake-labs-joins-databricks-accelerate-vision-lakebase">Databricks</a>.</figcaption>
</figure>

## The Problem: Operational data and analytical data live in different worlds

An application writes to Postgres. Analysts and AI agents read from a data lake. Between them sits a pipeline, usually built from change data capture and a stream or batch job, that copies the rows over. These pipelines are costly to build, break when a schema changes, and always add delay, so the lake is never quite current.

Take an agent that answers "where is my order?" The order status changes in Postgres every few seconds, while the lake still shows yesterday's state. The agent can answer from the fast but narrow database, or from the broad but stale lake. It cannot easily use both, and each team ends up owning its own copy of the truth.

## The Solution: Postgres changes mirrored into open tables, in real time

Mooncake built the bridge from the Postgres side. Databricks describes the result as making Postgres data ["immediately usable across workloads"](https://www.databricks.com/blog/mooncake-labs-joins-databricks-accelerate-vision-lakebase): transactions, analytics and AI on the same data, without ETL pipelines. Postgres changes are mirrored to the lakehouse in real time.

The best-known part is the open source [pg_mooncake](https://github.com/Mooncake-Labs/pg_mooncake) extension (MIT license). It keeps a columnstore mirror of Postgres tables in Apache Iceberg. A companion project, moonlink, handles the ingestion, and queries are accelerated by DuckDB. Because the data lands in an open table format, other engines can read it too. The project claims a top-10 place on ClickBench, which is the project's own claim.

The benefit goes to teams that want one copy of operational data feeding analytics and agents, instead of a pipeline per use case.

<figure class="shot">
  <img src="{{ '/assets/images/mooncake/pg-mooncake.jpg' | relative_url }}" alt="pg_mooncake: columnstore tables in Postgres" loading="lazy">
  <figcaption>The pg_mooncake extension. Source: <a href="https://github.com/Mooncake-Labs/pg_mooncake">pg_mooncake on GitHub</a>.</figcaption>
</figure>

### Funding history

- Seed - Undisclosed - Undisclosed, investor Khosla Ventures - [Crunchbase](https://www.crunchbase.com/funding_round/mooncake-labs-seed--ac46143c)

## Understanding the Acquisition

Databricks is assembling a Postgres of its own. It bought Neon in 2025, and Neon's technology is now the base of Lakebase. Neon gives it the transactional database. Mooncake gives it the link back to the lakehouse. Together they let Databricks say that an application database and the analytics platform are one system. Nikita Shamgunov, a Databricks VP of engineering and former Neon CEO, describes Mooncake's team as having deep expertise in ["Postgres internals, distributed systems and open table formats"](https://www.techtarget.com/searchdatamanagement/news/366631950/Mooncake-acquisition-boosts-Databricks-database-capabilities).

Why buy and not build? [TechTarget](https://www.techtarget.com/searchdatamanagement/news/366631950/Mooncake-acquisition-boosts-Databricks-database-capabilities) notes that few startups work on this approach, so rivals may have to build it themselves, and that Databricks chose to acquire it partly to bring in the founders. That makes it look like an acqui-hire for talent and open source technology, not for a business with scale. I could not find any public revenue or customer numbers for Mooncake.

Analysts are positive but careful. Sanjeev Mohan called it ["a great acquisition for Databricks, which is building out this new category of a lakebase"](https://www.techtarget.com/searchdatamanagement/news/366631950/Mooncake-acquisition-boosts-Databricks-database-capabilities), and added that the concept is new and "we don't know how successful it will be." Donald Farmer questioned whether this buying spree adds up to a coherent strategy.

For customers, the open source extension is MIT-licensed, but the company's own address, mooncake.dev, now redirects to Databricks. Expect the product to continue inside Lakebase, not as a separate service. The Postgres side of the story is in my [Neon article]({{ '/blog_posts/acq/015_ACQ_neon_by_databricks.html' | relative_url }}).

## Relevant Products and Companies

- [Lakebase](https://www.databricks.com/product/lakebase): Databricks' Postgres database, built on Neon, where Mooncake's technology is going.
- [Snowflake's Postgres and lake integration](https://www.snowflake.com/en/engineering-blog/pg-lake-postgres-lakehouse-integration/): the same bridge between Postgres and Iceberg, from the Snowflake side.
- [PeerDB](https://clickhouse.com/blog/clickhouse-acquires-peerdb-to-boost-real-time-analytics-with-postgres-cdc-integration): Postgres change data capture, bought by ClickHouse in 2024 to feed its analytics engine.

## My Take

Mooncake is more of a feature of Postgres than a standalone company. It solves one real problem, getting Postgres data into the lake, and does it well. But as a company it sells a single capability, in a very competitive market, at a time when AI lowers the effort of building something new. A feature like this can be copied, and a team of this size would have had to keep out-building bigger vendors on its own.

Inside Databricks the same piece becomes valuable. In Lakebase, the mirror is not another product to buy and wire up. It is a property of the database: switch it on and the operational data shows up in the lakehouse. That is a much better position than a startup with a connector.

It also fits a pattern I keep seeing at Databricks. Neon is the Postgres, Electric is the sync to the edge, and Mooncake is the bridge to the lake. Each is something Postgres vendors will be expected to offer, and Databricks is collecting them around one database. I expect the Mooncake bridge to show up in Lakebase as a built-in sync from Postgres to Delta tables, with no pipeline to run.

## Updates

*These entries were added after the original article. They are not part of the announcements.*

### May 12, 2026: Native Lakehouse Sync in public preview

Databricks launched native Lakehouse Sync for Lakebase in public preview, which is the direction described in My Take. According to [StartupHub.ai](https://www.startuphub.ai/ai-news/technology/2026/databricks-syncs-postgres-to-lakehouse-natively), it replicates Lakebase Postgres tables into Unity Catalog managed tables by decoding the write-ahead log, with no separate pipeline or external compute.

- **Setup.** It is enabled with a schema-level toggle, after which existing and new tables appear in Unity Catalog within about a minute.
- **History.** Every insert, update and delete is captured as slowly changing dimension (SCD) Type 2 history by default, and schema changes propagate automatically.
- **Scale to zero.** The sync scales down with the database and resumes from its last recorded state.
- **Claims.** Databricks says there is no impact on Postgres performance and no extra cost. These are Databricks' claims, as reported.

The Databricks documentation lists the related [change data feed](https://docs.databricks.com/aws/en/oltp/projects/use-cases) of Postgres changes into Delta tables as public preview. None of the sources I found says this is Mooncake's work, so I don't claim it is. It is the job Mooncake was bought to do.
