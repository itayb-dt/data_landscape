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

### What Firebolt built

Firebolt calls its product a "Cloud Data Warehouse for Data-Intensive Applications", in its own [engineering post](https://www.firebolt.io/blog/how-we-built-firebolt). Strip away the description and it is a data warehouse: SQL over data in object storage, with compute separate from storage, plus indexes, caching and a query planner tuned for speed. Each of these ideas exists elsewhere. Firebolt combined them and aimed them at applications instead of analysts, but nothing in the description is a new kind of database.

Firebolt also has a free, self-hosted edition, Firebolt Core, since June 2025. It is not open source, and its license forbids only building a competing hosted service on it.

Customers named on Firebolt's site include Similarweb, which uses it for customer-facing analytics, along with Primer, IQVIA, Sweet Security and Bigabid. Firebolt has raised [about $270 million](https://www.calcalistech.com/ctechnews/article/anq8b3yg3) in total.

### Who Firebolt competes with

It is a crowded market. Firebolt's site has comparison pages against ClickHouse, Druid, Snowflake, Databricks, BigQuery, Redshift and Athena, so it sees open source databases, data platforms and the cloud vendors as its competitors. This article leaves benchmarks out on purpose, but the choice of whom Firebolt compares itself with shows who it thinks it is up against. ClickHouse is the closest, and it is free to run.

### Funding history

- Series A - Dec 2020 - $37M - [CTech](https://www.calcalistech.com/ctech/articles/0,7340,L-3928013,00.html)
- Series B - Jun 2021 - $127M - [CTech](https://www.calcalistech.com/ctech/articles/0,7340,L-3928013,00.html)
- Series C - Jan 2022 - $100M at a $1.4B valuation, led by Alkeon Capital - [CTech](https://www.calcalistech.com/ctech/articles/0,7340,L-3928013,00.html)

## Understanding the Acquisition

Every database ends up needing two jobs. The first is running the application: saving an order, updating an account, reading one customer's record. This is called OLTP. The second is answering big questions over a lot of data: sales by region, usage trends, which customers are at risk. This is called OLAP, or simply analytics. Most databases are built for the first job, and companies add the second one next to it, either inside the same database or in a separate system.

MongoDB is an operational database, so analytics is the job it has to solve. It already offers several ways to analyze data inside MongoDB: its aggregation pipeline, [analytics nodes](https://www.mongodb.com/docs/atlas/cluster-config/multi-cloud-distribution/) that keep heavy reports away from the application, and a [SQL interface](https://www.mongodb.com/docs/sql-interface/) for BI tools such as Tableau and Power BI.

The question is how fast they answer. When the market talks about analytics today, it means a query over a petabyte of data, or trillions of rows, that returns in seconds or less. That is what ClickHouse and other vendors claim. MongoDB has not said that its own tools reach that level. If they do not, which the purchase suggests, then MongoDB has analytics technically but not at the level the market expects.

The usual way out for a MongoDB customer is to copy the data into another database built for analytics. That means an ETL pipeline, a second system to pay for, more complexity and more things that can break. MongoDB calls this the "data-movement tax". This is the core of the deal: MongoDB buys an engine built for that speed and puts it next to its own database, so customers do not have to leave.

MongoDB's [announcement](https://www.mongodb.com/company/blog/news/mongodb-acquires-firebolt) says what changes. Firebolt's engine "will run right alongside your database", and MongoDB will "keep it in sync automatically, so there's no pipeline to build or manage". Customers will be able to turn on real-time analytics for their MongoDB data, and there is a waitlist. Over time, MongoDB says, they will also be able to analyze data from other sources and formats next to their MongoDB data.

MongoDB is not claiming to replace the warehouse. Its FAQ says traditional warehouses and lakes remain the right fit for internal BI, reporting and data science. Firebolt is for the other side: applications and agents that need answers on live data.

For existing Firebolt customers, MongoDB says nothing changes, with the same support and service. Firebolt CEO Benjamin Wagner told CTech: "Joining MongoDB puts our engine where millions of developers already build."

## Relevant Products and Companies

- [ClickHouse](https://clickhouse.com/): the open source analytical database most often used for the same real-time, high-concurrency workloads, and the main competitor named in this space.
- [Apache Druid](https://druid.apache.org/) and [Apache Pinot](https://pinot.apache.org/): open source real-time analytics databases that applications use for user-facing dashboards.
- [Snowflake](https://www.snowflake.com/) and [Databricks](https://www.databricks.com/): the warehouses that Firebolt says are not built for low-latency, high-concurrency applications.

## My Take

For a long time Firebolt was a zombie unicorn. It had the unicorn label from 2022, a $1.4 billion valuation, but in practice I think it was a zombie: a company with the status and without the momentum.

The first sign is the founders. CTech reported that both Eldad Farkash and Saar Bitner stepped down from management in 2025, long before this sale. When both founders are gone well before an exit, I think that is a very bad sign. The people who built the company and believed in it were not there at the end.

The second sign is the cuts. CTech reported two rounds of layoffs, in September 2022 and in February 2026. In 2022 Firebolt had more than 200 employees. Looking at LinkedIn today, I count no more than 30, maybe 50.

So this looks to me like a very sad exit. I read it as an acquihire with a bit of technology on top, not the purchase of a growing business. CTech's estimate that the price is significantly lower than $1.4 billion fits that picture.

The market itself was not the problem. MongoDB's reason for the deal is that applications and agents need real-time analytics, so the demand is real. What Firebolt lacked was a way to stand out against ClickHouse, the warehouses and the cloud vendors.
