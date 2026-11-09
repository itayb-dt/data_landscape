---
title: "ClickHouse acquires Xata to add instant branching and agent-ready Postgres to its managed service"
published: 2026-11-10
---
ClickHouse [announced on November 9, 2026](https://clickhouse.com/blog/managed-postgres-ga-xata-acquisition) that it has acquired Xata, a Postgres platform known for instant database branching, on the day its own Managed Postgres became generally available. Xata [says it is "joining" ClickHouse](https://xata.io/blog/xata-is-joining-clickhouse). No price was disclosed. The one thing that matters: ClickHouse now owns the Postgres side of its stack, not only the analytics side.

<figure class="shot">
  <img src="{{ '/assets/images/xata/hero.png' | relative_url }}" alt="ClickHouse Managed Postgres goes GA and Xata acquisition" loading="lazy">
  <figcaption>ClickHouse Managed Postgres goes GA and the Xata acquisition. Source: <a href="https://clickhouse.com/blog/managed-postgres-ga-xata-acquisition">ClickHouse</a>.</figcaption>
</figure>

## The Problem: Copying a production database is slow, so developers and agents don't

Developers need a realistic copy of the database to test a change: the real schema, real data volumes, real edge cases. Copying a database of several terabytes takes hours and costs the same storage again. So teams test on a small fake dataset, share one staging database, or skip it, and migrations break in production.

AI coding agents make this worse. An agent that writes code and runs migrations needs its own disposable database for every task, and may create dozens a day. Nobody wants to pay for fifty full copies of a one-terabyte database, or wait for them.

## The Solution: Copy-on-write branches of a real Postgres

[Xata](https://xata.io/) is a Postgres platform that creates a branch of a database the way Git creates a branch of code. A branch shares the storage of its parent and only stores what changes, which is called copy-on-write. Xata lists these capabilities:

- **Instant branching:** it says a branch of a multi-terabyte database takes about 3 seconds, and that 50 branches of a 1TB database are billed for "something much closer to 1TB than 50TB".
- **Scale to zero:** idle databases stop their compute and wake on the next connection, which Xata says takes about a second.
- **Anonymized production data:** branches can be made from production data with sensitive columns masked.
- **Agent workflows:** "a database branch for every pull request and agent run".

The numbers are Xata's own claims. Customers it names include Sapien, Enginy, David AI, Runner AI and LoopAI. Under the hood it uses its own storage engine, Xatastor, which exposes ZFS volumes over the network using NVMe over TCP.

### Open source: pgstream and the platform

Xata also publishes open source. [pgstream](https://github.com/xataio/pgstream) is a change data capture tool and library for Postgres: it replicates data and schema changes (DDL) to targets such as another Postgres, OpenSearch, Kafka or webhooks, takes initial snapshots, and can anonymize column values on the way. It is Apache 2.0 licensed, with about 1.2k GitHub stars. That anonymizing replication is what makes branches from production data safe to hand out, so it supports Xata's main feature, branching. The [Xata platform](https://github.com/xataio/xata) itself is also on GitHub under Apache 2.0, built on Kubernetes and CloudNativePG, with about 1.1k stars. Its README says some security features for multi-tenant use are kept closed source.

### Funding history

- Seed - Sep 2021 - $5M - [aggregators](https://startupintros.com/news/2021-09-01-xata-io-seed), with investors including Operator Collective, SV Angel and Index Ventures.
- Series A - Mar 2022 - $30M - [aggregators](https://www.caplight.com/company/xata), led by Redpoint Ventures and Index Ventures according to most sources.

I could not confirm either round from a primary source, and aggregators disagree on the investor lists. About $35M in total.

## Understanding the Acquisition

ClickHouse says Xata "accelerates our roadmap for instant branching, cloning, and scale-to-zero environments". It lists two things coming to Managed Postgres: instant branches and clones with automatic idling, as one experience inside ClickHouse Cloud, and a dedicated tier for agents with sandboxing and memory. No dates are given. ClickHouse says it will integrate Xata fully "in the coming months". The team, led by Xata's founders Monica Sarbu and Tudor Golubenco, joins ClickHouse.

For Xata customers, Xata says nothing changes in the short term and new sign-ups continue, but "we will eventually migrate Xata customers to ClickHouse Managed Postgres", once there is feature parity. No date is given. Neither post says what happens to pgstream, so for now it stays under its Apache 2.0 license and its future is open.

**How it fits with PeerDB.** [PeerDB]({{ '/blog_posts/acq/018_ACQ_peerdb_by_clickhouse.html' | relative_url }}), bought in 2024, moves data out of Postgres into ClickHouse. It became the Postgres connector in ClickPipes, and the replication between ClickHouse's Postgres and ClickHouse itself. Xata is on the other side of that line: it improves the Postgres database where the data starts. Together the picture is complete: a managed Postgres for transactions, branching for developers and agents, PeerDB replication to ClickHouse for analytics, and the pg_clickhouse extension to query ClickHouse from Postgres. One caveat: PeerDB is source-available under the Elastic License v2, which is not an OSI open source license, while pgstream and the Xata platform are Apache 2.0. Overlap between pgstream and PeerDB (both do Postgres change capture) is possible, but neither post says anything about it.

## Relevant Products and Companies

- [Neon](https://neon.com/): Postgres with copy-on-write branching, now part of Databricks. See my [Neon article]({{ '/blog_posts/acq/015_ACQ_neon_by_databricks.html' | relative_url }}).
- [Snowflake Postgres](https://www.snowflake.com/): built on Crunchy Data. See my [Crunchy Data article]({{ '/blog_posts/acq/023_ACQ_crunchy_data_by_snowflake.html' | relative_url }}).
- [PeerDB]({{ '/blog_posts/acq/018_ACQ_peerdb_by_clickhouse.html' | relative_url }}): the Postgres replication that connects ClickHouse's Postgres to ClickHouse.

## My Take

Three analytics giants now have a good Postgres OLTP offering of their own: Snowflake with Crunchy Data, Databricks with Neon, and ClickHouse with its managed Postgres, now with Xata. That is no coincidence. Each of them sells an analytics engine, and the data they analyze starts in an operational database, so each wants to own it. Once both sit in the same vendor, what matters is how well the two stores sync, and how smooth the path is between them. That is where PeerDB fits for ClickHouse.

Of the three, I think ClickHouse leads the open source offering. The engine is open source, and the Postgres side is built from parts like pgstream and the Xata platform, under Apache 2.0.
