---
title: "Snowflake acquires Crunchy Data to bring enterprise Postgres into the AI Data Cloud"
published: 2026-11-02
---
Snowflake [announced on June 2, 2025](https://www.snowflake.com/en/news/press-releases/snowflake-acquires-crunchy-data-to-bring-enterprise-ready-postgres-offering-to-the-ai-data-cloud/), at its Summit conference, that it is acquiring Crunchy Data, a Postgres company. Snowflake did not state a price. [TechTarget](https://www.techtarget.com/searchdatamanagement/news/366625068/Snowflake-acquisition-of-Crunchy-Data-adds-Postgres-database) cites multiple reports of about $250 million, which Snowflake did not confirm. The deal came less than three weeks after its rival Databricks agreed to buy Neon, and the product it enables is called Snowflake Postgres.

<figure class="shot">
  <img src="{{ '/assets/images/crunchy/hero.png' | relative_url }}" alt="Snowflake Postgres announcement header" loading="lazy">
  <figcaption>Snowflake Postgres. Source: <a href="https://www.snowflake.com/en/blog/snowflake-postgres-enterprise-ai-database/">Snowflake</a>.</figcaption>
</figure>

## The Problem: Analytics platforms have no transactional database next to them

A data platform such as Snowflake is built for analytics: large scans, aggregations, and machine learning over data that has already landed. The applications that produce that data, and the AI applications that act on it, need something different. They need a transactional database that handles many small reads and writes with low latency.

Today those live in separate systems. Application data sits in Postgres, MySQL or another operational database, and a pipeline copies it into the platform. Each copy adds delay, cost and another thing that can break, and the team that owns the application is rarely the team that owns the pipeline.

A realistic case: a retailer runs its orders in Postgres and its analysis in a warehouse. A pricing agent that needs the latest order state reads from a copy that is minutes or hours old, or the team builds a second path to the live database. Either the agent decides on stale data, or the team maintains a second path to production.

## The Solution: Enterprise-grade Postgres, run as a managed service

[Crunchy Data](https://www.crunchydata.com/) is a company built around Postgres. Its products include [Crunchy Bridge](https://www.crunchydata.com/blog/crunchy-data-joins-snowflake), a fully managed Postgres service, and its Postgres Operator (PGO) for running Postgres on Kubernetes. It is based in Charleston, South Carolina, and Snowflake's release highlights its record of enterprise readiness in FedRAMP-compliant environments.

The company's own announcement describes working at the intersection of Postgres and Apache Iceberg, and its current website lists a Postgres-native data warehouse with Iceberg support. That later product was not mentioned in the June 2025 announcements, so I do not know when it launched.

Customers named in the announcement posts include YNAB and Moneytree for Crunchy, and Blue Yonder and LandingAI on the Snowflake side. Crunchy's customer, employee and revenue numbers were not disclosed.

The benefit goes to enterprises that want Postgres with operational support, security and compliance, and to teams that want it from a vendor they already use.

### Funding history

Public Funding Rounds: Not publicly available from credible sources.

## Understanding the Acquisition

Snowflake says it will integrate Crunchy's capabilities into Snowflake Postgres, which [will complement Unistore](https://www.snowflake.com/en/news/press-releases/snowflake-acquires-crunchy-data-to-bring-enterprise-ready-postgres-offering-to-the-ai-data-cloud/), its earlier transactional offering. It was to be available soon in private preview. The [Snowflake blog](https://www.snowflake.com/en/blog/snowflake-postgres-enterprise-ai-database/) says Snowflake Postgres "will bring transactional Postgres data to Snowflake". It does not describe how the data moves.

TechTarget notes that Crunchy's Postgres engine will not work in concert with Snowflake's existing SQL engine, which means this is a second engine next to the first, not a replacement for it.

Snowflake's executives frame it as customer demand. Vivek Raghunathan, SVP of Engineering, called it ["a massive $350 billion market opportunity"](https://www.snowflake.com/en/news/press-releases/snowflake-acquires-crunchy-data-to-bring-enterprise-ready-postgres-offering-to-the-ai-data-cloud/). CEO Sridhar Ramaswamy, quoted by TechTarget, said it helps users have access to a transactional store right within Snowflake.

For customers: Snowflake says it will support existing Crunchy customers and make a strong commitment to the Postgres community. The announcements do not say whether Crunchy Bridge, PGO or other products will continue as they are, and no later announcement answers that in what I read. Crunchy's CEO, Paul Laurence, co-wrote the Snowflake blog post, so the team continues inside Snowflake.

The comparison with Neon is the obvious one, and I cover that deal in my [Databricks and Neon article]({{ '/blog_posts/acq/015_ACQ_neon_by_databricks.html' | relative_url }}).

## Relevant Products and Companies

- [Neon](https://neon.com/): serverless Postgres, bought by Databricks weeks earlier and now part of Lakebase.
- [Snowflake Postgres](https://www.snowflake.com/en/blog/snowflake-postgres-enterprise-ai-database/): the product Snowflake builds from the deal.
- [Crunchy Data](https://www.crunchydata.com/): the target.

Postgres is offered by every cloud and many specialists, so I do not list them all.

## My Take

A few weeks after its competitor Databricks acquired Neon, we see this announcement. Of course, a process like this started many months ago. I would not be surprised if Snowflake somehow knew about the Neon deal, or if Databricks approached Crunchy first and Crunchy said no. After all, the reported price is about 25% of what was reported for Neon. A lot of money, if true.

The goals are the same for both companies: add a relational engine, and get good sync between the analytics and the transactional side. Both also add very talented people who know how to build databases. That is true for both deals.
