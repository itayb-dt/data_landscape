---
title: "SQream, the GPU database that raised over $120M, enters insolvency and heads for a court-run sale"
published: 2026-11-02
---
On May 18, 2026, SQream, now operating as Scailium, [asked the Tel Aviv District Court](https://www.calcalistech.com/ctechnews/article/ryl6vtdyfl) to open proceedings to examine its economic rehabilitation and to appoint a temporary trustee. A week later the court [authorized the trustee to start a sale](https://www.calcalistech.com/ctechnews/article/hynpbfflgx) of the company or its operations. The filing puts its debts at about 13.6 million shekels (about $4.7M), against losses reported at $100M or more. No buyer has been announced.

## What happened

The company said in its filing that it "is currently facing a breaking point and can no longer continue its operations." On May 7, employees were told that operations were suspended and were placed on unpaid leave, because the company could not meet payroll. About 50 people still worked there.

The debts are small next to what the company raised. [Calcalist's breakdown](https://www.calcalistech.com/ctechnews/article/ryl6vtdyfl) lists roughly $828K owed to employees, $515K to Mizrahi Tefahot Bank, $172K to suppliers, $103K in rent, $138K in royalties to the Israel Innovation Authority, plus unpaid pension contributions, income tax deductions and National Insurance. The company said it tried efficiency measures, strategic changes, rebranding, fundraising and a sale, and that none produced a binding agreement. It also blamed the difficulty of raising money from foreign investors on the war of the past two and a half years.

The loss figures are not consistent in the coverage: over 300 million shekels ($103M) as of 2023, and about $145M (420.5 million shekels) by 2024. Either way, this was a company that spent a lot more than it earned for a long time.

## The Problem: Analytics at the petabyte scale was expensive, and CPUs were the bottleneck

SQream, founded in 2010, started from a real problem. Scanning, joining and aggregating tens or hundreds of terabytes on CPU clusters needs many servers, and the cost grows with the data. Telecom, finance and manufacturing companies had that data and wanted to query it without a warehouse bill that scales the same way.

A realistic example: a telecom operator keeps years of call records and wants to join them to network events for fraud analysis. On a CPU warehouse the query touches billions of rows and needs a large cluster for hours. The business question is simple. The infrastructure under it is not.

## The Solution: A SQL engine that runs on GPUs

SQream built a [GPU-accelerated SQL database](https://sqream.com/) that used the parallelism of graphics processors to scan very large datasets with fewer machines. The pitch was petabyte-scale analytics at lower cost, sold mainly to large enterprises, with commercial activity [mostly in North America and South Korea](https://www.calcalistech.com/ctechnews/article/ryl6vtdyfl). Later it repositioned around GPU-accelerated data preparation for machine learning pipelines, and in December 2021 it bought Panoply, a no-code ELT service, for an estimated [$60-70M](https://www.calcalistech.com/articles/0,7340,L-3925096,00.html) (not disclosed by the companies).

### Funding history

- Series A - Jun 2015 - ~$9M, led by Blumberg Capital - not linked (to be verified)
- Series B - May 2018 - $26M, led by Alibaba Group and Hanaco Venture Capital - not linked (to be verified)
- Series B extension - Jun 2020 - $39.4M, led by Mangrove Capital Partners and Schusterman Family Investments - https://en.globes.co.il/en/article-israeli-big-data-analytics-co-sqream-raises-394m-1001333580
- Series C - Sep 2023 - $45M, led by World Trade Ventures - see [my article on the round]({{ '/blog_posts/fund/021_FUND_sqream_45m_series_c.html' | relative_url }})

[VentureBeat reported](https://venturebeat.com/business/sqream-nabs-45m-to-accelerate-data-analytics-with-gpus) a total of $135M after the Series C. Other trackers show about $120M.

## Understanding the Shutdown

No post-mortem has been published, so what follows is my reading of the public facts, not something the company has said.

**The product was a niche inside a niche.** A GPU database has to beat the CPU warehouses it competes with on cost, not just on speed, and those warehouses kept getting faster and cheaper while moving to object storage. GPUs were scarce and expensive for much of this period, and the buyers who needed the scale were few.

**The pivot came late.** The Series C in September 2023 was raised on an AI and ML data-preparation story. By then the company had [cut more than 15% of its workforce](https://www.calcalistech.com/ctechnews/article/ryl6vtdyfl) at some point and had been through a CEO change after 14 years of Ami Gal's leadership ([Calcalist](https://www.calcalistech.com/ctechnews/article/r100nuceske)). The AI story was a hard one to tell against vendors that already owned the data.

**The end was cash, not debt.** The liabilities are modest. A company with 50 people and a few million in obligations is not crushed by its creditors; it ran out of runway and out of investors willing to continue.

## What happens next

The trustee is [inviting bids](https://www.calcalistech.com/ctechnews/article/hynpbfflgx) for the company or its operations. The company says there is interest in its technology and assets. A buyer would get GPU-execution IP, a customer base and a small team. For existing customers, the practical risk is support and roadmap, and anyone running SQream should plan an exit path now.

## Relevant Products and Companies

- [NVIDIA RAPIDS and cuDF](https://rapids.ai/): open source GPU data processing, the direction GPU analytics took without a dedicated database vendor.
- [Voltron Data](https://voltrondata.com/): a GPU-accelerated query engine company built on open standards, in the same space.
- [ClickHouse](https://clickhouse.com/) and [Snowflake](https://www.snowflake.com/): the CPU-based engines that GPU databases had to beat on cost.

## My Take

This is sad, of course. Behind the numbers are about 50 people who were put on unpaid leave, and a team that built real technology.

But it is also a pattern. We see so many databases with special capabilities, and I am not sure all of them justify a new product. "Just use Postgres" is a joke that is right more often than not: for most workloads, Postgres or a warehouse you already run is good enough, and the special capability gets absorbed into the platforms customers already trust. A GPU engine is a clever way to get speed. Whether it is a reason to buy and operate a separate database is another question.

For a new database vendor, I think there must be a very clear business justification. Not "faster" in a benchmark, but a reason a customer cannot get what it needs from what it already has. [Firebolt](https://www.firebolt.io/) is the kind of example I have in mind, a vendor with a clear story about who the product is for and why.

If SQream's technology and customers find a buyer, they may do well as a feature of a bigger platform. As a stand-alone database company, the market did not leave room for it.
