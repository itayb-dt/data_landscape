---
title: "TigerBeetle raises $24M to build a database for financial transactions"
published: 2024-07-26
---
# TigerBeetle Raises $24M to Build a Database for Financial Transactions

<figure class="shot">
  <img src="{{ '/assets/images/tigerbeetle/hero.png' | relative_url }}" alt="TigerBeetle: The Financial Transactions Database" loading="lazy">
  <figcaption>The TigerBeetle banner. Source: <a href="https://tigerbeetle.com/">TigerBeetle</a>.</figcaption>
</figure>

## Technical Overview

- Startup: TigerBeetle ([tigerbeetle.com](https://tigerbeetle.com/)), spun out of Coil in 2022
- Amount Raised: $24M
- Funding Round: Series A, closed May 30, 2024 according to the [company timeline](https://tigerbeetle.com/company) and [reported by TechCrunch on July 23, 2024](https://techcrunch.com/2024/07/23/tigerbeetle-is-building-database-software-optimized-for-financial-transactions/)
- Main Investors: Spark Capital (lead), Amplify Partners and Coil
- Problem Area: Recording the movement of money and other things of value at high volume, without errors

---

## The Problem

Every payment, wallet top-up, usage bill or stock trade comes down to the same operation: take an amount from one account and add it to another. Accountants have a rule for this, double-entry bookkeeping: every debit has an equal and opposite credit, so nothing appears or disappears.

Most companies record this in a general-purpose database such as Postgres. The database stores rows. The rules of bookkeeping (no negative balances, no double spending, both sides of a transfer or neither) are written by the company's own developers in application code. TigerBeetle's founder describes the result in [the seed announcement](https://tigerbeetle.com/blog/2023-01-30-series-seed-announcement) as ledgers built from "Postgres and duct tape", where one transfer of money needs several round trips to the database.

That works until volume grows. Imagine a payments company where every transaction also pays a fee into one company account. Every transfer wants to update that same account, and a normal database makes them wait for each other, one at a time. TigerBeetle says that high-volume payment switches and large startups were hitting this wall because of lock contention on "hot accounts". Making the database bigger does not fix a queue that is about one row.

The other half of the problem is trust. When a bug in the accounting code loses money, the cost is not a slow page but a reconciliation failure, and in a regulated business, much worse.

---

## How They Solve It

TigerBeetle is an open source database (Apache 2.0) built for one job: online transaction processing of financial data. In the company's words, it is "a specialized transactions database". Instead of tables and SQL, it has two things, accounts and transfers, and one rule built into the engine: every debit has an equal and opposite credit.

What that means in practice, from the [company's description](https://tigerbeetle.com/):

- **The accounting rules live in the database.** Limits on balances, transfers that must succeed or fail together, and two-step payments (authorize first, complete later, with timeouts handled by the database) are features of the engine. Developers do not rebuild them in application code.
- **It copies every write across several servers.** TigerBeetle replicates data across a group of machines using a published consensus protocol, so a single failure does not lose or corrupt a record.
- **It is tested by simulation.** The company says it tests TigerBeetle in a simulator that can replay failures deterministically, for a system whose main promise is that it does not lose money.
- **It sits next to the general database, not instead of it.** The company's advice is to keep a general-purpose database for everything else, and to use TigerBeetle only for the part that moves money. Data can be streamed to an analytics system.

The company claims large speed advantages over general-purpose databases. Those are its own figures, and this article leaves them out.

The use cases go beyond banks. CEO Joran Dirk Greef told [TechCrunch](https://techcrunch.com/2024/07/23/tigerbeetle-is-building-database-software-optimized-for-financial-transactions/) that it is "ideal for use cases where you need to count anything of value", from usage-based billing with spend caps to energy smart meters, gaming and instant payments. The company says it has had paying customers since day one. At the time of the round, its managed cloud service was available by invitation only.

---

## Competitive Landscape

TigerBeetle's main competitor is not another product but the default: a general-purpose SQL database such as Postgres, plus a ledger written by the company's own developers. For many companies that is good enough, and it keeps all the data in one familiar place. TigerBeetle has to convince them that money movement is special enough to deserve its own database.

It also has to win trust. A new database that holds money is judged on correctness and years of operation, not on features. Open source helps with that, because anyone can read the code.

---

## Previous Rounds and Capital Trajectory

- Seed - Jan 2023 - $6.4M, led by Amplify Partners with Coil as equal partners - [TigerBeetle](https://tigerbeetle.com/blog/2023-01-30-series-seed-announcement)
- Series A - May 2024 - $24M, led by Spark Capital with Amplify Partners and Coil - [TigerBeetle](https://tigerbeetle.com/company), [TechCrunch](https://techcrunch.com/2024/07/23/tigerbeetle-is-building-database-software-optimized-for-financial-transactions/)

Total raised is more than $30M. TechCrunch quotes Greef saying the round was brought forward from later in the year, and that the money goes to engineering, go-to-market and the cloud platform that is under development. TechCrunch reported about eight employees at the time, with plans to double the team by 2025.

---

## Founder Background

Joran Dirk Greef, founder and CEO, was consulting for Coil, a web payments company, when he did a safety and performance analysis of Mojaloop, a payments switch supported by the Gates Foundation. He says in the seed announcement that he gave up the startup he was working on and joined Coil full time to build TigerBeetle as Apache 2.0 open source. TechCrunch adds that he had earlier consulted for Microsoft on protections against zero-day exploits, and that TigerBeetle became a company after customers asked Coil for enterprise support.

Two engineers from Coil, known by their GitHub names, joined him when it was spun out in August 2022.

---

## Summary

Money movement is the oldest data problem there is, and most companies still solve it with a general database and their own accounting code. That is fine until volume or risk grows: a busy account turns into a queue, and a bug turns into lost money. TigerBeetle is a bet that this one job is important enough to have a database designed only for it, sitting beside the general-purpose database instead of replacing it.

---

## My Take

Most database companies try to be the one database for everything. TigerBeetle does the opposite: it is a database for one use case, counting things of value, and it is built only for that. I usually say that a new database needs a very good reason to exist, because Postgres is the default and keeps getting better.

Money movement may be that rare reason. The rules are fixed and old, mistakes are expensive, and one hot account is a problem that a general database handles badly. The risk is the size of the market. A database for one job is only as big as that job, and it has to live next to Postgres and not replace it. I will watch whether TigerBeetle becomes the standard way to keep a ledger, or stays a tool for the few companies that hit the wall.

---

## Updates

*Late additions, published after the original article and not part of the official announcements.*

### 2025 to 2026: Jepsen test, a cloud service and named customers

- **Independent testing, June 2025.** Jepsen, a firm known for testing database correctness, published an analysis of TigerBeetle funded by TigerBeetle. It covered versions 0.16.11 to 0.16.30. Jepsen says that as of version 0.16.45, TigerBeetle had addressed every issue it found, except indefinite retries. [Report](https://jepsen.io/analyses/tigerbeetle-0.16.11).
- **TigerBeetle Cloud, August 26, 2026.** The company's timeline says the managed service launched, "operated by the authors". Each customer gets a dedicated cluster, available in AWS, Azure and Google Cloud regions, with published monthly prices. [TigerBeetle Cloud](https://tigerbeetle.com/cloud).
- **Customers.** TigerBeetle's site names Super Payments, Pesawise, Straddle and Okto Payments among its users, with quotes from their engineering leaders. These are the company's own testimonials. It also released a connector for the Redpanda streaming platform in September 2025.
- **Still before 1.0.** The latest release is 0.17.9 from July 2026. A feature added in 0.17.5 was removed again in 0.17.9 because it caused compatibility problems.
- **Funding.** TigerBeetle's site still lists "over $30M raised".
