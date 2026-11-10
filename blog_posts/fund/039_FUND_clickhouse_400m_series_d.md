---
title: "ClickHouse raises $400M Series D at a reported $15B valuation and buys Langfuse and a Postgres service"
published: 2026-01-19
---
# ClickHouse Raises $400M Series D at a Reported $15B Valuation

## Technical Overview

- Startup: ClickHouse ([clickhouse.com](https://clickhouse.com/))
- Amount Raised: $400M
- Funding Round: Series D, [announced January 16, 2026](https://www.businesswire.com/news/home/20260116008883/en)
- Valuation: $15B, according to [SiliconANGLE](https://siliconangle.com/2026/01/16/database-maker-clickhouse-raises-400m-acquires-ai-observability-startup-langfuse/) and other press coverage. I could not read the press release itself, so I treat the valuation as reported, not confirmed.
- Main Investors: Dragoneer (lead), with GIC, Index Ventures, Khosla Ventures, Lightspeed Venture Partners, Bessemer Venture Partners, and accounts advised by T. Rowe Price and WCM Investment Management. Bessemer comes from press coverage, not from the SiliconANGLE list.
- Problem Area: Real-time analytics, now extended to AI observability and transactional Postgres
- Announced with the round: the acquisition of Langfuse, and a managed Postgres service

---

## The Problem

Analytics used to mean a nightly report. Now an application shows live dashboards to its own customers, and an AI agent queries data many times a minute. Both need answers in milliseconds over billions of rows, and a traditional data warehouse is built for something slower and more occasional.

At the same time, AI systems create a new kind of data: every prompt, response and tool call of an LLM application is a record worth storing and querying, so teams can see what the model did and what it cost. The data lives in different systems, and each added system is one more pipeline to maintain.

---

## How They Solve It

ClickHouse is a column-oriented database built for fast analytical queries, open source and also sold as the managed ClickHouse Cloud. Its pitch is speed at scale: scanning and aggregating very large tables quickly, which suits real-time dashboards, observability data and now AI workloads.

SiliconANGLE reports that ClickHouse's annualized recurring revenue grew by more than 250% in the year before the round, and that the cloud service has over 3,000 customers, among them Meta, Sony and Lyft. These are company figures reported by the press. No absolute revenue figure was given in the coverage I could read.

---

## What Was Announced With the Round

Large rounds often come with a product story. This one came with two moves, both of which push ClickHouse beyond the analytics engine.

**1. The acquisition of Langfuse.** [Langfuse](https://langfuse.com/) is an open source platform for LLM observability, evaluations and prompt management. ClickHouse [announced that it acquired it](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability), and [Langfuse published its own post](https://langfuse.com/blog/announcing-acquisition). The price and the deal terms were not disclosed. What ClickHouse says:

- Langfuse already runs entirely on ClickHouse, in the cloud and when self-hosted.
- It remains open source under its MIT license for core features, Langfuse Cloud continues as a standalone service, and nothing changes for existing deployments.
- Deeper integrations are promised "over the coming months", without dates or features.
- The metrics are Langfuse's own claims: more than 20k GitHub stars, 23.1M SDK installs a month, and use by 19 of the Fortune 50.

**2. A managed Postgres service.** SiliconANGLE says ClickHouse will roll out a managed transactional database based on PostgreSQL, integrated with its columnar store. ClickHouse then [described it in detail on January 22, 2026](https://clickhouse.com/blog/postgres-managed-by-clickhouse): built with Ubicloud, running on local NVMe storage, in private preview on AWS. See my [PeerDB article]({{ '/blog_posts/acq/018_ACQ_peerdb_by_clickhouse.html' | relative_url }}) for the replication that connects it to ClickHouse.

### Use of the money

I could not read the press release, so I do not quote ClickHouse on this. Press coverage says the money goes to expanding in real-time analytics, data warehousing, observability and AI and machine learning. Treat that as a summary by journalists.

---

## Previous Rounds and Capital Trajectory

- Series A - Sep 2021 - about $50M, led by Index Ventures and Benchmark, with Yandex participating - [ClickHouse](https://clickhouse.com/blog/en/2021/clickhouse-inc/), [Business Wire](https://businesswire.com/news/home/20210920005219/en/ClickHouse-Inc.-Announces-Incorporation-Along-With-$50M-In-Series-A-Funding). This was the spin-out of ClickHouse, Inc. from Yandex.
- Series B - Oct 2021 - $250M at a $2B valuation, led by Coatue and Altimeter, with Index, Benchmark, Yandex, Almaz and Lead Edge, and new investors Lightspeed, Redpoint and FirstMark - [ClickHouse](https://clickhouse.com/blog/click-house-raises-a-250m-series-b-at-a-2b-valuationand-we-are-hiring), [Business Wire](https://www.businesswire.com/news/home/20211028005287/en). The date comes from the Business Wire release number and its search listing, not from the blog post.
- Series C - May 2025 - $350M at $6.35B, led by Khosla Ventures - [Business Wire](https://www.businesswire.com/news/home/20250529254399/en/ClickHouse-Raises-%24350-Million-Series-C-to-Power-Analytics-for-the-AI-Era), [Bloomberg](https://bloomberg.com/news/articles/2025-05-29/khosla-led-deal-values-data-startup-clickhouse-at-6-35-billion). Press summaries also list Index, Lightspeed, Benchmark, Coatue, BOND, IVP, Battery and Bessemer, and a $100M credit facility next to the equity. I could not open the release, so the investor list is secondary.
- Series D - Jan 2026 - $400M at a reported $15B, led by Dragoneer.

Adding the four rounds gives about $1.05B raised in equity, which matches the lowest tracker estimate. Other trackers show more, up to about $1.15B over more rounds, and one lists the Series D at $475M. I use the figure that most coverage agrees on. I did not verify possible extensions of earlier rounds.

---

## Why This Round Matters

The valuation went from $6.35B to a reported $15B in about eight months, more than double, and the Series D came only about six months after the Series C. Investors are pricing ClickHouse as one of the central databases of the AI era, not as a niche analytics engine.

The use of the money is visible in what was bought and launched alongside it: observability for LLM applications and a Postgres database, both next to the analytics engine. The company is building a stack around the engine, and it did so with acquisitions, as it did earlier with PeerDB.

---

## Updates

*Late additions, published after the original article and not part of the announcement.*

### May 2026: 4,000 customers and over $250M ARR

ClickHouse [reported](https://clickhouse.com/blog/clickhouse-tops-250m-arr-and-4000-customers) that it passed 4,000 customers and more than $250M in annual recurring revenue, which it describes as more than triple the year before. These are the company's figures.

### Nov 9, 2026: ClickHouse acquires Xata

On the day its Managed Postgres became generally available, ClickHouse acquired Xata, a Postgres platform known for instant database branching. See my [Xata article]({{ '/blog_posts/acq/037_ACQ_xata_by_clickhouse.html' | relative_url }}).
