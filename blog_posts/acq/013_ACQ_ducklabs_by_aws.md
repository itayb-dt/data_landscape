---
title: "AWS acquires DuckLabs to bring DuckDB's in-process analytics closer to S3"
published: 2026-09-02
---
AWS is acquiring DuckLabs, the Amsterdam company behind DuckDB, but [not the DuckDB project itself](https://www.aboutamazon.com/news/company-news/aws-ducklabs), which stays open source under the MIT license and the independent DuckDB Foundation. DuckLabs is small: about 30 people ([InfoWorld](https://www.infoworld.com/article/4214800/aws-acquires-ducklabs-but-what-does-it-want-from-the-team-behind-duckdb.html)) and, according to [Dealroom](https://app.dealroom.co/companies/ducklabs_1), bootstrapped, living on support contracts rather than venture capital.

## The Problem: Analytics needs a data warehouse, with all its complexity

Most analytical questions are not big data problems. They are medium data problems: a few hundred gigabytes to a few terabytes of events, orders or logs that someone wants to slice quickly. The standard answer has been a cloud data warehouse or a cluster: load the data, size the compute, wait for it to start, and pay for it while it sits idle.

That is a poor fit for a growing share of work. Analysts want answers in seconds on a laptop. Application developers want to embed analytics inside a product without running a separate system. Data engineers want to test a transformation on real files before it goes to production.

The cost is not only money. Every copy of the data into a warehouse is another pipeline to maintain and another place where numbers can drift. Take a simple question: "How many active users did we have last week?" Does "active" mean logged in, or performed a billable action? The answer depends on definitions, and the more systems the data passes through, the harder it is to agree on which number is right.

The industry has been moving towards a simpler pattern: keep the data once, in open file formats on object storage, and bring a fast query engine to it, wherever the user happens to be.

## The Solution: A database that runs inside the application

DuckLabs is the company behind DuckDB, an open source analytical SQL database that runs inside the application as a library: no server, no cluster. It is columnar and vectorized, so scans and aggregations over large tables are fast. It reads Parquet, CSV and JSON files directly, and runs on a laptop, in a serverless function, or in the browser.

According to the [DuckDB announcement](https://duckdb.org/2026/08/26/ducklabs-to-join-aws), the projects around it, DuckDB, DuckLake and Quack, all remain MIT-licensed. [SiliconANGLE](https://siliconangle.com/2026/08/26/aws-buys-ducklabs-to-bring-duckdbs-embeddable-analytics-to-more-enterprises/) reports that DuckLabs earned its revenue from commercial support contracts and feature development partnerships, and that the company was founded just over five years ago by Hannes Mühleisen and Mark Raasveldt, who still lead its core engineering.

The adoption numbers explain the deal. The DuckDB team [reported](https://duckdb.org/2026/08/05/github-40k-stars) on August 5, 2026 that DuckDB has "50M+ monthly downloads in PyPI, more than double the 20M we reported last time," and that its GitHub repository passed 40,000 stars. [PyPI Stats](https://pypistats.org/packages/duckdb) currently shows about 54.9 million downloads in the last month, roughly 16.6 million in the last week and 1.5 million in the last day (7-day smoothing). SiliconANGLE reports that DuckLabs said downloads reached more than three million a day at one point. PyPI counts include automated installs, so read them as a sign of reach rather than a count of users.

The differentiators are practical:

- **Zero operations.** There is nothing to deploy. It is a library.
- **SQL as the interface.** Anyone who knows SQL can use it immediately.
- **Files as tables.** It queries data where it already lives, without a load step.
- **Open source with a foundation.** The project's governance is separate from the company.

### Funding history

Public Funding Rounds: Not publicly available from credible sources.

## Understanding the Acquisition

The strategic logic is about where analytics runs. AWS already holds a very large share of the world's data in S3. The more queries run directly against that data, the more AWS wins. Constellation Research analyst Michael Ni put it to SiliconANGLE plainly: "AWS wins if more of that work happens directly against S3 and inside its AWS services."

The two companies already worked together. AWS and DuckLabs collaborated on DuckDB support for Amazon S3 Tables and Amazon SageMaker Lakehouse, according to SiliconANGLE. Amazon says the relationship goes back further: Andy Warfield, an AWS VP and distinguished engineer, said in the announcement, "We've been working closely with the DuckLabs team for the past two years."

AWS was explicit about the direction on day one. In its [announcement post](https://aws.amazon.com/blogs/big-data/aws-and-ducklabs-building-the-future-of-analytics-together/) on August 26, Mai-Lan Tomsen Bukovec, an AWS technology VP, wrote that AWS will "continue to invest in deep integration between DuckDB and our building block services" and will look at how to "integrate DuckDB's performance and simplicity in our other AWS services." The stated aim is to combine DuckDB's strength on everyday queries of a terabyte or less with AWS scale. The first concrete example arrived more than a month later: Aurora PostgreSQL now runs lake queries on DuckDB's engine (see [Updates](#updates)).

The deal also solves a sustainability question. A small company maintaining a project used by millions is hard to fund through support contracts. SiliconANGLE reports AWS will now fund the open source work. The [DuckDB announcement](https://duckdb.org/2026/08/26/ducklabs-to-join-aws) says the Foundation will set up a Technical Advisory Board that can influence the projects' direction, and DuckLabs plans to let DuckDB run extensions signed by other developers and organizations.

For users, nothing changes for now. The roadmap, licensing and governance model stay the same. The thing to watch is influence: who sits on the advisory board, who contributes, and whether the open extension model ends up opening the ecosystem or tilting it towards AWS services.

## Relevant Products and Companies

[MotherDuck](https://motherduck.com/): DuckDB as a serverless cloud service, and the company most tightly coupled to DuckLabs. It was [started in partnership with the DuckLabs team](https://motherduck.com/blog/duckdb-amazon/), has submitted hundreds of patches to DuckDB, and has three engineers among the project's top 10 outside contributors. It raised a [$52.5M Series B at a $400M valuation](https://theregister.com/2023/09/21/motherduck_funding/) in 2023. Its pitch after the AWS deal is the product around the engine: developer ergonomics, collaboration, governance and a home for analysts and agents ([MotherDuck podcast](https://motherduck.com/explain-analyze/0010-aws-bought-ducklabs/)).

[chDB](https://github.com/chdb-io/chdb): the closest equivalent on the ClickHouse side, an in-process OLAP SQL engine powered by ClickHouse that needs no server. It [joined ClickHouse](https://clickhouse.com/blog/chdb-joins-clickhouse-family) in March 2024.

## My Take

DuckDB is an amazing technology. It is also another example of how Postgres is the starting point for everything, including analytics: DuckDB speaks a familiar SQL, and there is now a Postgres extension that embeds it.

Users do not really care about any of this. They want three things:

1. **Fast reads on a large amount of data.**
2. **Cheap storage.** That is why S3 is great.
3. **Simplicity, through SQL.**

DuckDB, S3 and SQL deliver all three, and AWS has just bought the company that makes the first piece.

Embedding DuckDB in Aurora (see [Updates](#updates)) is the next reasonable step. Postgres is where an application's data already lives, DuckDB reads the lake directly from S3, and SQL is the one interface everyone knows. Putting DuckDB inside Postgres gives users all three without a pipeline in between.

What about MotherDuck? It is now a partner that AWS could compete with. Its CEO saw this coming: ["Some day, Amazon will likely release their own service based on DuckDB... We welcome the competition."](https://motherduck.com/blog/duckdb-amazon/) Will a company that uses both Aurora and MotherDuck drop MotherDuck and pay only AWS? Mostly no, though some will.

Aurora covers the simplest case: joining your Postgres data with Parquet or Iceberg files in S3. Teams that use MotherDuck for exactly that, especially ones already fully on AWS, may consolidate. Aurora is not a shared analytics workspace, though. The scans run on the same cluster as production, and AWS itself suggests materializing the data when you need low latency. Analysts who want collaboration, their own compute, or a setup that isn't tied to AWS have little reason to leave. MotherDuck is betting on [the product around the engine](https://motherduck.com/explain-analyze/0010-aws-bought-ducklabs/), not on owning DuckDB.

The bigger threat to MotherDuck is not Aurora but the stand-alone DuckDB service that AWS may launch next. I have no data on how many customers use both, so this is my judgment, not a measurement.

## Updates

*Late additions, published after the original article as the market evolves. They are not part of the official announcements listed at the top.*

### Sep 30, 2026: Aurora PostgreSQL runs lake queries on DuckDB

AWS announced that [Aurora PostgreSQL can query Apache Iceberg and Parquet data directly](https://aws.amazon.com/about-aws/whats-new/2026/09/aurora-postgresql-query-apache-iceberg-and-parquet/). Aurora runs these queries on "DuckDB's high-performance query engine, embedded in PostgreSQL," against data in Amazon S3, S3 Tables or the AWS Glue Data Catalog, exposed as foreign tables.

A single query can combine live operational data, including uncommitted writes, with data in the lake, so there is no ETL copy into Aurora. For workloads that need low latency, the lake data can be materialized into native Aurora tables.

The feature is generally available from Aurora PostgreSQL 17.11 and 18.6, in all commercial and GovCloud (US) regions. There is no additional feature charge, but Aurora compute and S3 request costs still apply. Setup needs the `aurora_analytics` extension and an IAM role. More details are in AWS's [launch post](https://aws.amazon.com/blogs/aws/amazon-aurora-postgresql-now-supports-direct-querying-of-apache-iceberg-and-parquet-data-in-your-data-lake/) and [NeoTeo's coverage](https://www.neoteo.com/en/aws-brings-duckdb-powered-lake-queries-to-aurora-postgresql).
