---
title: "ParadeDB raises $12M Series A to turn Postgres into the search engine"
published: 2026-11-04
---
# ParadeDB Raises $12M Series A to Turn Postgres Into the Search Engine

## Technical Overview

- Startup: ParadeDB ([paradedb.com](https://www.paradedb.com/))
- Amount Raised: $12M
- Funding Round: Series A, [announced July 14, 2025](https://www.paradedb.com/blog/series-a-announcement)
- Main Investors (known): Craft Ventures (lead), Y Combinator and other existing investors
- Problem Area: Full-text, vector and analytical search inside Postgres

---

## The Problem

Most applications keep their data in Postgres, and most need search: find a product, a document, a transaction. Postgres has basic full-text search, but ranking and speed at scale are weak. Teams therefore add Elasticsearch next to it and copy the data over.

That copy is the pain. ParadeDB lists it as three problems: [syncing Postgres and Elastic is error-prone for update-heavy workloads](https://www.paradedb.com/blog/series-a-announcement), Elastic is not a reliable data store, and it can become very expensive at scale. A fintech with updating balances sees it clearly: a search index that lags the transaction table shows wrong results.

---

## How They Solve It

ParadeDB ships [pg_search](https://github.com/paradedb/paradedb), a Postgres extension with a custom index for full-text and vector search, BM25 scoring, filters, facets and aggregations. It is built in Rust on Tantivy for search and Apache DataFusion for analytics, and it adds a columnar index for some analytical queries. The search runs inside Postgres, so there is no second system to keep in sync.

**Is it open source?** The community edition is, under the AGPL-3.0 license, which ParadeDB says it [chose from day one](https://www.paradedb.com/). AGPL is an OSI-approved open source license, but a strict one: anyone who offers the software as a service must release their changes or buy a commercial license. ParadeDB sells that commercial license, plus support and physical replication for its indexes, as its Enterprise edition, and runs ParadeDB Cloud.

Named customers in the Series A post include Alibaba Cloud, Bilt Rewards and Modern Treasury. The post reports 100K+ installs and 7K+ GitHub stars. Performance claims, such as Bilt cutting query timeouts by 95%, come from the company.

---

## Competitive Landscape

- **Elasticsearch and OpenSearch**: the incumbents, which ParadeDB replaces by removing the second system.
- **Postgres built-in full-text search**: free and already there, but weaker at ranking.
- **Other Postgres search extensions**: [pg_textsearch](https://github.com/timescale/pg_textsearch) from Timescale adds BM25 ranking under the permissive PostgreSQL license, with a generally available v1.0. Its README says combining Boolean filtering with BM25 ranking is [not yet optimized as a single index scan](https://github.com/timescale/pg_textsearch), which is where ParadeDB claims an edge.

Where it runs matters, because an extension only helps if your database allows it. I checked the extension lists in the AWS documentation. [RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-extensions.html) and [Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Extensions.html) do not list pg_search, nor any BM25 extension, though both list pgvector. [Google Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extensions) lists pg_textsearch and not pg_search. [Neon](https://neon.com/docs/extensions/pg-extensions) marks pg_search unavailable and points to its own search feature.

---

## Previous Rounds and Capital Trajectory

- Seed - 2023 - about $2M, implied by the $14M total, not stated - [ParadeDB](https://www.paradedb.com/blog/series-a-announcement)
- Series A - Jul 2025 - $12M, led by Craft Ventures - [ParadeDB](https://www.paradedb.com/blog/series-a-announcement), [Craft Ventures](https://www.craftventures.com/articles/why-we-invested-in-paradedb)

The round brings the total raised to $14M. The founders are Philippe Noël and Ming Ying. I found no round after July 2025.

---

## Why This Round Matters

It is a bet that search belongs inside the main database, not next to it. The money funds a company that has to prove a business can be built on an extension, with a cloud and an enterprise license.

---

## My Take

ParadeDB is the kind of company I find easier to believe in. It does not ask you to adopt a new database. It adds search and analytics to Postgres, where people already are. "Just use Postgres" is right more often than not, and ParadeDB's job is to make it right more often.

The open question is the moat. Is this a whole product, or a Postgres extension? An extension can be replaced by another extension. What if tomorrow a new open source search extension is fast enough to compete? That is not hypothetical: Timescale's pg_textsearch already exists, under a permissive license. And the managed Postgres services matter more than the code. As of the AWS documentation I read, RDS and Aurora offer neither pg_search nor a BM25 extension. If a good-enough open source extension lands on RDS, most of the market will take it, and ParadeDB will be left with those who need more than good enough, or who run outside RDS.

The license is the other side of this. AGPL stops a cloud from simply reselling the code, which protects the business, and it also keeps the cloud from adding it to its list. So ParadeDB's path is to be so much better that customers go out of their way to run it. Is that enough? I am not sure, and I would watch which managed Postgres services add it.
