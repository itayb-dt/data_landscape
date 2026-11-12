---
title: "Edelbyte raises $70M to build search and analytics for AI agents"
published: 2026-11-11
---
# Edelbyte Raises $70M to Build Search and Analytics for AI Agents

<figure class="shot">
  <img src="{{ '/assets/images/edelbyte/hero.png' | relative_url }}" alt="Edelbyte homepage: What would you build if cost wasn't a problem?" loading="lazy">
  <figcaption>The Edelbyte homepage. Source: <a href="https://edelbyte.io/">Edelbyte</a>.</figcaption>
</figure>

## Technical Overview

- Startup: Edelbyte ([edelbyte.io](https://edelbyte.io/)), Tel Aviv and San Francisco, founded in 2025 according to its press release
- Amount Raised: $70M, announced as combined seed and Series A funding
- Funding Round: Seed and Series A, [announced November 11, 2026](https://www.financialcontent.com/article/accwirecq-2026-11-11-sequoia-backs-microsoft-veterans-edelbyte-with-70m-to-challenge-data-infrastructure-giants)
- Main Investors: Sequoia and Quiet Capital (lead), with Greenoaks, Swish Ventures and Startpoint Capital ([Globes](https://en.globes.co.il/en/article-israeli-data-infrastructure-co-edelbyte-raises-70m-1001563008))
- Problem Area: Search and analytics over very large data, built for AI agents as well as people

---

## The Problem

Data platforms were designed for people. A person can only type so many questions a day, so the system could be priced and sized for that. An AI agent does not work that way. [Sequoia](https://sequoiacap.com/article/partnering-with-edelbyte-data-infrastructure-that-keeps-up-with-ai-s-curiosity) puts it this way: "One agent might fire off fifty queries where a person would run one."

That breaks the economics. Sequoia lists the trade-offs companies make today: keeping less history so queries stay fast, asking fewer questions so the bill stays reasonable, and building the product inside whichever cloud the database happens to run in. Imagine a security team that wants an agent to investigate every alert across a year of logs. If each question costs real money, the team has to limit the agent, or delete the history it would need.

Search and analytics are also usually separate systems. Finding a specific event (search) and summing a million events (analytics) have often been stitched together from different products, according to Sequoia.

---

## How They Solve It

Edelbyte describes its product as "a unified data platform for search and analytics, built for a new generation of builders and AI applications", with "an architecture designed for performance and cost efficiency at scale". Sequoia says it keeps detailed history queryable at interactive speed, scales as data and query volume grow, and gives people, applications and AI agents governed access to the same data. It runs in any public or private cloud and on premises, managed or self-hosted.

The company's claims are about cost: lower platform costs and, "in some cases, ten times as many queries within the same budget". It says it already runs petabyte-scale deployments with Fortune 500 customers.

The announcement does not describe how the engine works. The four founders built **Kusto** at Microsoft, so it is reasonable to assume that Edelbyte is something similar, rebuilt for AI workloads. That is my assumption, not something the company has said.

Kusto was [named after the oceanographer Jacques Cousteau](https://sequoiacap.com/article/partnering-with-edelbyte-data-infrastructure-that-keeps-up-with-ai-s-curiosity), "because it was built for diving into oceans of data". It started more than a decade ago as a small incubation project inside Microsoft, and it was built to query very large volumes of fast-arriving data, such as logs, telemetry and security events, in seconds instead of hours. Its query language was meant to be simple enough for anyone, not only big-data engineers. It became the data engine under Microsoft Sentinel, Microsoft Defender and Azure Monitor.

Customers know it as **Azure Data Explorer**, the name under which Microsoft offered it, and that service still exists. Microsoft Fabric added a second product on the same engine, [Eventhouse](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/create-eventhouse) in Real-Time Intelligence, and Microsoft documents a path for [moving to it](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/migrate-api-to-eventhouse). The Kusto name lives on in the Kusto Query Language.

---

## Competitive Landscape

The press release says Edelbyte is taking on Snowflake, Databricks and ClickHouse. These are the platforms where companies run analytics today, and all three face the same jump in query volume from AI agents.

Edelbyte's pitch is that a platform designed for AI workloads from the start can keep more history and answer more questions for the same money.

---

## Previous Rounds and Capital Trajectory

- Seed and Series A - Nov 2026 - $70M combined, led by Sequoia and Quiet Capital - [press release](https://www.financialcontent.com/article/accwirecq-2026-11-11-sequoia-backs-microsoft-veterans-edelbyte-with-70m-to-challenge-data-infrastructure-giants), [Globes](https://en.globes.co.il/en/article-israeli-data-infrastructure-co-edelbyte-raises-70m-1001563008)

Sequoia says it led the seed round. Globes reports about 40 employees in Israel, the US and Europe.

---

## Founder Background

- **Avner Aharoni**, CEO. [Sequoia](https://sequoiacap.com/article/partnering-with-edelbyte-data-infrastructure-that-keeps-up-with-ai-s-curiosity) says he spent a quarter century at Microsoft and "hustled Kusto from project to a globally beloved product".
- **Evgeney Ryzhyk**, CTO. Sequoia says he "invented the Kusto engine and its query language, then rebuilt it three times", making it faster and cheaper each time.
- **Alexander Sloutsky**, VP Engineering.
- **Yoni Leibowitz**, VP Platform Engineering.

They spent more than a decade together building data systems behind dozens of Microsoft products and services.

---

## Summary

At petabyte scale, cost is the big issue. Every extra query and every extra month of history adds to the bill, and AI agents multiply both. Today companies answer by keeping less data or asking fewer questions. Edelbyte is one of the new players trying to end that trade-off, and it is built by the team that made a data engine for exactly this kind of data at Microsoft.
