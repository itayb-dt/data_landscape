---
title: "AWS acquires DuckLabs to bring DuckDB's in-process analytics closer to S3"
---
On August 26, 2026, Amazon [announced](https://www.aboutamazon.com/news/company-news/aws-ducklabs) that AWS has signed a definitive agreement to acquire [DuckLabs](https://ducklabs.com/), the Amsterdam-based company behind the [DuckDB](https://duckdb.org/) analytical database. DuckLabs published its own [announcement](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) the same day, saying the move is expected to take effect in early September. Deal terms were not disclosed.

One point matters more than the price. Amazon states that it is "not acquiring the DuckDB open source project." DuckDB stays free and open source under the MIT license, governed by the independent, non-profit DuckDB Foundation.

Deal terms were not disclosed ([InfoWorld](https://www.infoworld.com/article/4214800/aws-acquires-ducklabs-but-what-does-it-want-from-the-team-behind-duckdb.html)), and no credible estimate has been published. For scale: the team is about 30 people ([InfoWorld](https://www.infoworld.com/article/4214800/aws-acquires-ducklabs-but-what-does-it-want-from-the-team-behind-duckdb.html)), and Dealroom's [profile](https://app.dealroom.co/companies/ducklabs_1) describes the company as bootstrapped, with no venture funding, living on support contracts and feature partnerships.

## The Problem: Analytics shouldn't require a warehouse

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

The deal also solves a sustainability question. A small company maintaining a project used by millions is hard to fund through support contracts. SiliconANGLE reports AWS will now fund the open source work. The [DuckDB announcement](https://duckdb.org/2026/08/26/ducklabs-to-join-aws) says the Foundation will set up a Technical Advisory Board that can influence the projects' direction, and DuckLabs plans to let DuckDB run extensions signed by other developers and organizations.

For users, nothing changes for now. The roadmap, licensing and governance model stay the same. The thing to watch is influence: who sits on the advisory board, who contributes, and whether the open extension model ends up opening the ecosystem or tilting it towards AWS services.

## Relevant Products and Companies

[MotherDuck](https://motherduck.com/): a managed cloud service built on DuckDB, and the company most tightly coupled to DuckLabs. It has [partnered](https://www.cwi.nl/en/news/cwi-spin-off-duckdb-labs-partners-with-motherduck-who-raises-47-5-million-1/) with DuckDB Labs since 2022.

[chDB](https://github.com/chdb-io/chdb): the closest equivalent on the ClickHouse side, an in-process OLAP SQL engine powered by ClickHouse that needs no server. It [joined ClickHouse](https://clickhouse.com/blog/chdb-joins-clickhouse-family) in March 2024.

## My Take

DuckDB is an amazing technology. It is also another example of how Postgres is the starting point for everything, including analytics: DuckDB speaks a familiar SQL, and there is now a Postgres extension that embeds it.

Users do not really care about any of this. They want three things:

1. **Fast reads on a large amount of data.**
2. **Cheap storage.** That is why S3 is great.
3. **Simplicity, through SQL.**

DuckDB, S3 and SQL deliver all three, and AWS has just bought the company that makes the first piece.
