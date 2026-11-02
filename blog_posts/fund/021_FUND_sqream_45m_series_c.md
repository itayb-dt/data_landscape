---
title: "SQream raises $45M Series C to push its GPU analytics engine into enterprise AI and ML"
published: 2026-11-02
---
SQream [announced a $45M Series C](https://en.globes.co.il/en/article-israeli-data-analytics-co-sqream-raises-45m-1001457706) on September 12, 2023, led by World Trade Ventures. The company said it would use the money to expand in North America, extend its strategic partnerships and advance its AI and ML enterprise capabilities. The valuation was not disclosed. This article describes the round as announced then. The company's later insolvency is covered separately (see [Updates](#updates)).

## Technical Overview

- Startup: SQream ([sqream.com](https://sqream.com/))
- Amount Raised: $45M
- Funding Round: Series C
- Main Investors (known): World Trade Ventures (lead), Schusterman Investments, George Kaiser Foundation, Icon Continuity Fund, Blumberg Capital, Freddy & Helen Holdings, and others
- Problem Area: Analytics and data preparation at very large scale, using GPUs

## The Problem

Companies in manufacturing, telecom and finance generate data at a rate that strains CPU-based warehouses. Loading, cleaning and querying tens of terabytes means large clusters, long jobs and a bill that grows with the data.

A realistic case: a semiconductor maker collects sensor data from production lines, up to 100TB a day by [one example SQream gave](https://venturebeat.com/business/sqream-nabs-45m-to-accelerate-data-analytics-with-gpus). To find why yield drops, analysts need to join and scan that history repeatedly, and every slow query delays a decision on the line. The same pain appears when the data is meant for machine learning: preparing it is often the slowest and most expensive step before any model runs.

## How They Solve It

SQream, founded in 2010 by CEO Ami Gal and CTO Razi Shoshani ([Globes](https://en.globes.co.il/en/article-israeli-data-analytics-co-sqream-raises-45m-1001457706)), built a patented GPU-based query optimization engine. [According to VentureBeat](https://venturebeat.com/business/sqream-nabs-45m-to-accelerate-data-analytics-with-gpus), it runs two products:

- **SQreamDB**: a SQL database that uses GPUs to scan large datasets with fewer machines.
- **SQream Blue**: a cloud-native, managed data preparation lakehouse.

The company's benchmarks, as reported by [Globes](https://en.globes.co.il/en/article-israeli-data-analytics-co-sqream-raises-45m-1001457706), claim a 90% reduction in ingestion and preparation times and in footprint, and an 80% reduction in cost. These are SQream's own figures for some cases, not independent tests.

One customer case in the coverage: an unnamed electronics manufacturer replaced a Hadoop-based setup with three compute nodes accelerated by 12 GPUs, running more than 280 automated daily reports, and reported production yield rising from 50% to 90%. Named customers include Samsung, LiveAction, Sinch, Orange, AIS and LG. Revenue was not shared.

CEO Ami Gal said in the announcement: "As Generative AI shines a light on the importance of leveraging AI and ML within enterprises, as well as the value of GPUs as part of the analytics process, we have seen interest in our technology skyrocket."

## Competitive Landscape

SQream competes on two fronts.

- **Cloud warehouses and query engines** such as [Snowflake](https://www.snowflake.com/), [Databricks](https://www.databricks.com/) and [ClickHouse](https://clickhouse.com/): CPU-based, broadly adopted and integrated with the surrounding tooling. SQream's argument is cost and speed at very large scale, not breadth.
- **GPU data processing** such as [NVIDIA RAPIDS](https://rapids.ai/), the open source libraries for running dataframe and SQL workloads on GPUs. They address the same hardware advantage without a separate database.

Where SQream is stronger, by its own account, is very large data volumes and heavy preparation workloads. Where it is weaker is ecosystem: a separate database engine has to win a place next to the platforms customers already run, and to prove its cost advantage against engines that keep improving.

## Previous Rounds and Capital Trajectory

[VentureBeat reports](https://venturebeat.com/business/sqream-nabs-45m-to-accelerate-data-analytics-with-gpus) that this round took SQream's total raised to $135M. Other trackers show lower totals, for example [CB Insights](https://www.cbinsights.com/company/sqream-technologies/financials) at about $121.8M. Earlier rounds, as listed in my research notes:

- Series A - Jun 2015 - ~$9M, led by Blumberg Capital - not linked (to be verified)
- Series B - May 2018 - $26M, led by Alibaba Group and Hanaco Venture Capital - not linked (to be verified)
- Series B extension - Jun 2020 - $39.4M, led by Mangrove Capital Partners and Schusterman Family Investments - [Globes](https://en.globes.co.il/en/article-israeli-big-data-analytics-co-sqream-raises-394m-1001333580)
- Series C - Sep 2023 - $45M, led by World Trade Ventures - [Globes](https://en.globes.co.il/en/article-israeli-data-analytics-co-sqream-raises-45m-1001457706)

Blumberg Capital and Schusterman, who backed earlier rounds, took part again. [Globes quotes](https://en.globes.co.il/en/article-israeli-data-analytics-co-sqream-raises-45m-1001457706) the CEO describing the funding climate as tight.

## Why This Round Matters

For the category, the round was a bet that the generative AI wave would create demand for GPU-based data preparation and analytics. The company framed it that way itself: the use of funds names AI and ML enterprise capabilities first. For customers, it meant a vendor with funding to expand support in North America.

## Updates

*Late additions, published after the original article and not part of the official announcements.*

### May 2026: SQream enters insolvency

In May 2026 the company, then named Scailium (formerly SQream), asked the Tel Aviv District Court to open rehabilitation proceedings and the court authorized a trustee to seek a sale. The full story is in [my article on the shutdown]({{ '/blog_posts/shutdown/020_SHUTDOWN_sqream_insolvency.html' | relative_url }}).
