---
title: "MongoDB acquires Firebolt to bring real-time analytics to its database"
published: 2026-11-17
---
MongoDB [announced on November 17, 2026](https://www.mongodb.com/company/blog/news/mongodb-acquires-firebolt) that it has acquired Firebolt, an analytical database built for fast queries from many users at once. The price was not disclosed. Israeli business outlet CTech wrote that "the estimated acquisition price is significantly lower" than the $1.4 billion valuation Firebolt had in 2022.

<figure class="shot">
  <img src="{{ '/assets/images/firebolt/hero.png' | relative_url }}" alt="Firebolt: The Analytical Database for Engineers" loading="lazy">
  <figcaption>The Firebolt homepage banner. Source: <a href="https://www.firebolt.io/">Firebolt</a>.</figcaption>
</figure>

## The Problem: Operational data and analytics live in two separate systems

An operational database runs the application: orders, users, events. Analytics usually runs somewhere else, in a data warehouse, so the data has to be copied from one system to the other. MongoDB calls this "the data-movement tax": a pipeline to build and watch, a delay before the data arrives, and a second copy to pay for.

That was acceptable when the reader of the analytics was an analyst looking at a dashboard. It is a worse fit when the reader is a customer-facing feature or an AI agent. Imagine a support agent that is asked "is this customer's usage unusual this week?" while the customer is waiting. The answer has to come from live data, in well under a second, and many such questions arrive at the same time. A warehouse that is tuned for a handful of analysts running heavy queries is not built for that.

## The Solution: A cloud analytical database tuned for low latency and many concurrent queries

[Firebolt](https://www.firebolt.io/) describes itself as "a high performance analytical database". It runs as a single binary on a laptop and scales to hundreds of nodes and petabytes of data in the customer's cloud. Data sits in object storage, and compute is separate from storage, so any compute cluster can read any data. It speaks standard SQL, with a dialect aligned to Postgres.

### What was unique

Firebolt describes its product as a "Cloud Data Warehouse for Data-Intensive Applications", from its own [engineering post](https://www.firebolt.io/blog/how-we-built-firebolt). It kept the familiar warehouse model, SQL over data in object storage, and tuned it for applications that ask many small questions at once and cannot wait. Four things set it apart, all in Firebolt's own words and not tested by anyone else:

- **Built for applications, not analysts.** The design target is a customer-facing product or an agent, not a dashboard.
- **Indexes in a warehouse.** Most warehouses scan data. Firebolt lets you define indexes that pre-compute common answers, and the planner uses them automatically.
- **Real transactions.** Firebolt says it supports full ACID transactions, which it says several warehouses only partly offer.
- **Isolated engines.** Different workloads run on separate compute engines over the same data, so one heavy user does not slow the others.

Firebolt also has a free, self-hosted edition, Firebolt Core, since June 2025. It is not open source, and its license forbids only building a competing hosted service on it.

Customers named on Firebolt's site include Similarweb, which uses it for customer-facing analytics, along with Primer, IQVIA, Sweet Security and Bigabid. Firebolt has raised [about $270 million](https://www.calcalistech.com/ctechnews/article/anq8b3yg3) in total.

### Who Firebolt competes with

It is a crowded market. Firebolt's site has comparison pages against ClickHouse, Druid, Snowflake, Databricks, BigQuery, Redshift and Athena, so it sees open source databases, data platforms and the cloud vendors as its competitors. This article leaves benchmarks out on purpose, but the choice of whom Firebolt compares itself with shows who it thinks it is up against. ClickHouse is the closest, and it is free to run.

### Funding history

- Series A - Dec 2020 - $37M - [CTech](https://www.calcalistech.com/ctech/articles/0,7340,L-3928013,00.html)
- Series B - Jun 2021 - $127M - [CTech](https://www.calcalistech.com/ctech/articles/0,7340,L-3928013,00.html)
- Series C - Jan 2022 - $100M at a $1.4B valuation, led by Alkeon Capital - [CTech](https://www.calcalistech.com/ctech/articles/0,7340,L-3928013,00.html)

## Understanding the Acquisition

MongoDB's [announcement](https://www.mongodb.com/company/blog/news/mongodb-acquires-firebolt) says Firebolt's engine "will run right alongside your database", and that MongoDB will "keep it in sync automatically, so there's no pipeline to build or manage". It becomes part of MongoDB's Intelligent Data Platform. In the coming months, MongoDB customers will be able to turn on real-time analytics for their MongoDB data, and there is a waitlist.

MongoDB is not claiming to replace the warehouse. Its FAQ says traditional warehouses and lakes remain the right fit for internal BI, reporting and data science. Firebolt is for the other side: applications and agents that need answers on live data.

For existing Firebolt customers, MongoDB says nothing changes, with the same support and service. Firebolt CEO Benjamin Wagner told CTech: "Joining MongoDB puts our engine where millions of developers already build."

### Why Firebolt ended up here

Firebolt raised $270 million and was valued at $1.4 billion, and it is now being bought for less. The facts below come from CTech and from Firebolt's own pages. The reading of them is an analysis, not something either company has said.

**The company went through two rounds of cuts.** In September 2022, eight months after the Series C, CTech reported that Firebolt laid off dozens of employees. Then-CEO Eldad Farkash said at the time that the company had over $200 million in the bank and was reacting to the market slowdown. In February 2026, CTech reported more cuts, in Israel and abroad, with more than $100 million still in cash, and wrote that only a small team of developers would remain in Israel. CTech also reported that the founders, Eldad Farkash and Saar Bitner, stepped down from management in 2025.

**It was not a lack of demand.** Real-time analytics for applications has paying customers, and Firebolt's own customer list shows it. MongoDB's reason for the deal is that AI agents need exactly this. The demand looks real. The open question is who gets to serve it.

**The category is crowded, and some of the competition is free.** Firebolt had to win against open source engines (ClickHouse, Druid, Pinot, StarRocks), against warehouses that every customer already pays for (Snowflake, Databricks, BigQuery, Redshift) and against Azure's Kusto-based service. ClickHouse is the strongest of them: it is open source, and it now has its own cloud, Postgres and large funding rounds (see the [ClickHouse Series D]({{ '/blog_posts/fund/039_FUND_clickhouse_400m_series_d.html' | relative_url }})). Firebolt chose to keep its free Core edition closed source. Its own post explains why: "With GenAI accelerating software development, defensibility is more difficult than ever."

**A 2022 valuation set expectations that growth had to meet.** A $1.4 billion valuation that early assumed a large and fast-growing business. The cuts and the leadership change suggest that did not happen. Firebolt has not published revenue, and neither has MongoDB, so how far short it fell is unknown.

## Relevant Products and Companies

- [ClickHouse](https://clickhouse.com/): the open source analytical database most often used for the same real-time, high-concurrency workloads, and the main competitor named in this space.
- [Apache Druid](https://druid.apache.org/) and [Apache Pinot](https://pinot.apache.org/): open source real-time analytics databases that applications use for user-facing dashboards.
- [Snowflake](https://www.snowflake.com/) and [Databricks](https://www.databricks.com/): the warehouses that Firebolt says are not built for low-latency, high-concurrency applications.
