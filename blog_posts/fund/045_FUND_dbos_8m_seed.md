---
title: "DBOS raises $8.5M seed to make cloud applications recover from failures"
published: 2024-03-16
---
# DBOS Raises $8.5M Seed to Make Cloud Applications Recover from Failures

<figure class="shot">
  <img src="{{ '/assets/images/dbos/hero.jpg' | relative_url }}" alt="DBOS: Durable Workflows Just Use Postgres" loading="lazy">
  <figcaption>The DBOS banner. Source: <a href="https://www.dbos.dev/">DBOS</a>.</figcaption>
</figure>

## Technical Overview

- Startup: DBOS ([dbos.dev](https://www.dbos.dev/)), Cambridge, Massachusetts
- Amount Raised: $8.5M
- Funding Round: Seed, [reported by Blocks and Files on March 13, 2024](https://www.blocksandfiles.com/public-cloud/2024/03/13/dbos-raises-85m-to-get-cloud-apps-off-the-dirt-roads/1591242)
- Main Investors: Engine Ventures and Construct Capital (leads), with Sinewave and GutBrain Ventures
- Problem Area: Applications that lose their place when something crashes (durable execution)

---

## The Problem

A program that does one thing and finishes is easy to run. Real applications do not work that way. A checkout takes a payment, reserves stock, sends an email and waits three days for an approval. An AI agent calls a model, calls a tool, waits for a person and calls another model. A data job runs for hours across many machines. Any of these can be cut in half by a crash, a deploy or a network failure.

When that happens, a plain program starts over, or it is left half done. Imagine a payment that was charged and a server that died before the order was saved: the customer paid for an order that does not exist, or is charged twice when the job retries. Teams solve this by hand with queues, retry code, status columns in a database and clean-up jobs. It works, but it is a lot of code that has nothing to do with the product, and it is where bugs hide.

The technique that addresses it is called **durable execution**: a program records its progress as it runs, so after a failure it continues from the last finished step instead of from the beginning.

---

## How They Solve It

DBOS came out of a research project at MIT and Stanford, started by Mike Stonebraker, the creator of Postgres. The original idea, as Blocks and Files describes it, was a "database-oriented operating system": run the services that an operating system provides on top of a distributed database, so state is stored and recoverable by design. The company launched with DBOS Cloud, a serverless platform for applications that are built from stateful functions and workflows.

According to the company, as relayed by Blocks and Files, the platform offers:

- Workflows that run once and only once, even through failures.
- Time-travel debugging, to replay what a program did.
- Observability in SQL, because the history of every run is data in a database.
- Detection of attacks on running applications.

The company's pitch is that developers write ordinary functions and the platform keeps their state, so an application that takes months to build the usual way can be built in days. That quote comes from Matei Zaharia, and it is a claim, not a measured result.

---

## Competitive Landscape

Durable execution is not new. The best-known product is **Temporal**, whose founders built a similar system called Cadence at Uber and started Temporal in 2019. The big clouds sell their own versions: **AWS Step Functions** and **Azure Durable Functions**. They all follow the same pattern: an application calls their API, and the state of the workflow is stored for it. DBOS has to show that a different place to keep that state, a database, is worth a new vendor.

---

## Previous Rounds and Capital Trajectory

- Seed - Mar 2024 - $8.5M, led by Engine Ventures and Construct Capital, with Sinewave and GutBrain Ventures - [Blocks and Files](https://www.blocksandfiles.com/public-cloud/2024/03/13/dbos-raises-85m-to-get-cloud-apps-off-the-dirt-roads/1591242)

This is the first disclosed round. DBOS says the money goes to growing the engineering team and improving the platform. Reed Sturtevant, a general partner at Engine Ventures, joins the board, which also includes Andy Palmer, Peter Kraft and Stonebraker.

---

## Founder Background

- **Mike Stonebraker**, architect. He created Postgres and received the Turing Award, according to Blocks and Files. DBOS lists him as a co-founder.
- **Matei Zaharia** co-led the research project. He created Apache Spark and is a co-founder and the CTO of Databricks. Blocks and Files called him a co-founder of DBOS in 2024, but DBOS's own site now lists him as a founding advisor.
- **Qian Li**, CEO, and **Peter Kraft**, CTO, are listed as co-founders on DBOS's site. **Andy Palmer** is chairman and a co-founder.

The team describes itself as a joint group of MIT and Stanford computer scientists. The company says it is the commercial form of that research.

---

## Summary

Every application that spans more than one step has to survive failure, and today most teams pay for that with their own retry and clean-up code. Durable execution turns it into a platform feature, and AI agents, which run long, call many tools and wait for people, make the need more visible. DBOS is a seed-stage bet from the people who built Postgres that the right foundation for it is a database.

---

## My Take

Durable execution is clearly important. Anything that runs for more than a few seconds, and an AI agent more than most, needs to survive a crash. I am less sure about the business.

How big is this market? There is no analyst figure that I can point to. The best signal is Temporal, and it comes from the company itself: in September 2026 it announced a $550M Series E at a $12.55B valuation, and says it has more than 4,300 paying customers, including OpenAI. If that is right, durable execution is a large market and growing quickly. But Temporal is also the reason it is hard to enter. AWS and Azure sell their own, and newer players such as Restate and Inngest raised their own rounds in 2025 and 2026. They differ in the details, but the pattern is similar: your code calls an API and the state is stored for you.

So is a dedicated product justified? DBOS has an answer, and it changed over time. It began as a new operating system on a database. Today it is a library that uses the Postgres you already run, so customers do not adopt a new database at all. That makes it cheaper and easier to try, and it is a smart move. It also raises the question of what exactly is left to sell. A library on Postgres is easy to copy, and durable execution looks to me more like a feature that every platform will have than a product by itself.

I do not know which way this goes. DBOS has raised far less than Temporal, and it has real customers. The test is whether companies pay for a durable library, or build the same thing on Postgres themselves.

---

## Updates

*Late additions, published after the original article and not part of the official announcements.*

### 2024 to 2026: A library on Postgres, case studies and enterprise features

- **The product moved.** DBOS's main product is now DBOS Transact, an open source library that uses Postgres to record the progress of workflows, with no separate orchestration server. It supports Python, TypeScript, Go and Java, and Rust is in a first preview. DBOS Cloud, the launch product, now appears only on the pricing page. A control plane called DBOS Conductor handles monitoring, alerts and recovery across workers.
- **How it works.** Functions are marked as workflows, and each step inside one is saved as it completes. After a failure the workflow runs again, and finished steps return their saved results instead of running twice. DBOS says plainly that this does not guarantee exactly-once effects outside the database: if a crash comes after a payment but before the step is saved, the step can run again, so such calls need idempotency keys.
- **Case studies,** all from DBOS's own customer page:
  - **Notion** moved the job system behind Notion Mail off a queue library onto DBOS.
  - **Orderful**, an EDI company, replaced RabbitMQ with DBOS for its transaction processing.
  - **BMS** runs genomic sequencing pipelines on durable queues.
  - **Supabase** has a case study, and DBOS lists support for Supabase Edge Functions.
  - **Walmart** is listed as having integrated DBOS into an internal agentic AI framework, with no details given.
  - DBOS says it has hundreds of customers.
- **Pricing and enterprise.** The library is free. Paid plans for the platform start at $99 a month and are billed by checkpoints, meaning workflow runs and steps. In October 2026 DBOS added a DBOS Transact Enterprise extension.
- **Funding.** DBOS's site still lists "$8.5m+ raised".
