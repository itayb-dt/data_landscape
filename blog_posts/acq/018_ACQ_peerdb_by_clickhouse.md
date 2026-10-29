---
title: "ClickHouse acquires PeerDB to make Postgres a first-class source for real-time analytics"
published: 2024-08-02
---
ClickHouse [announced](https://clickhouse.com/blog/clickhouse-acquires-peerdb-to-boost-real-time-analytics-with-postgres-cdc-integration) on July 30, 2024 that it is acquiring PeerDB, a startup founded in 2023 by Kaushik Iska and Sai Srirampur that specializes in change data capture (CDC) for Postgres. The price was not disclosed. PeerDB is small and focused: its one job is moving data out of Postgres, fast and safely.

<figure class="shot">
  <img src="{{ '/assets/images/peerdb/hero.png' | relative_url }}" alt="ClickHouse and PeerDB logos" loading="lazy">
  <figcaption>ClickHouse acquires PeerDB. Source: <a href="https://clickhouse.com/blog/clickhouse-acquires-peerdb-to-boost-real-time-analytics-with-postgres-cdc-integration">ClickHouse</a>.</figcaption>
</figure>

## The Problem: Moving data from Postgres to an analytical database is slow and risky

Most applications keep their data in Postgres, and most analytics run somewhere else, in an engine built for scanning large tables. Connecting the two means copying data continuously. Change data capture reads the changes Postgres writes to its log and replays them in the destination.

<figure class="shot narrow">
  <img src="{{ '/assets/images/peerdb/postgres-vs-clickhouse.png' | relative_url }}" alt="Diagram: transactions go to row-based Postgres, real-time analytics run on columnar ClickHouse, with replication between them" loading="lazy">
  <figcaption>Row-based Postgres for transactions, columnar ClickHouse for analytics, and the replication in between. Source: <a href="https://clickhouse.com/blog/postgres-cdc-connector-clickpipes-ga">ClickHouse</a>.</figcaption>
</figure>

That sounds simple and is not. The first copy of a large table can take hours. Postgres keeps its log until the reader catches up, so a stalled reader can fill the disk of a production database. Schemas change, data types do not map cleanly, and the source is usually a critical operational system that must not be disturbed. As ClickHouse puts it, a fast and reliable CDC experience at its scale ["is not an easy problem to solve"](https://clickhouse.com/blog/clickhouse-welcomes-peerdb-adding-the-fastest-postgres-cdc-to-the-fastest-olap-database).

A customer example shows the scale of the pain. Vueling Airlines reports cutting its Postgres-to-ClickHouse snapshot time from [10+ hours to 15 minutes](https://clickhouse.com/blog/clickhouse-welcomes-peerdb-adding-the-fastest-postgres-cdc-to-the-fastest-olap-database) with PeerDB. That is a customer's own figure.

## The Solution: A CDC engine that does one thing, Postgres

[PeerDB](https://github.com/PeerDB-io/peerdb) is laser-focused on Postgres as the source. Its features, as ClickHouse describes them, include fast snapshots, schema evolution, rich data type mapping, resync, monitoring and alerting on replication slot growth, and cost control on the destination. It also takes care to keep the CDC process [non-invasive](https://clickhouse.com/blog/clickhouse-welcomes-peerdb-adding-the-fastest-postgres-cdc-to-the-fastest-olap-database) for the source database.

Before the deal, PeerDB moved Postgres data to [warehouses such as Snowflake and to queues like Kafka](https://www.businesswire.com/news/home/20240411109971/en/PeerDB-Raises-3.6-Million-Seed-Round-Funding-to-Revolutionize-Data-Movement-for-PostgreSQL). The code stays available under the Elastic License v2, which is source-available and not an OSI open source license, and ClickHouse says PeerDB Enterprise is now released under the same license.

### Funding history

- Seed - Apr 2024 - $3.6M, led by 8VC - [Business Wire](https://www.businesswire.com/news/home/20240411109971/en/PeerDB-Raises-3.6-Million-Seed-Round-Funding-to-Revolutionize-Data-Movement-for-PostgreSQL), [8VC](https://8vc.com/resources/announcing-our-investment-in-peerdb)

## Understanding the Acquisition

ClickHouse is built to answer analytical questions quickly, but the data it needs usually starts in Postgres. Until now users had to bring their own pipeline for that. By buying PeerDB, ClickHouse owns the path in: a new Postgres CDC connector in ClickPipes, its managed ingestion service, [powered by PeerDB](https://clickhouse.com/blog/clickhouse-welcomes-peerdb-adding-the-fastest-postgres-cdc-to-the-fastest-olap-database) and integrated into ClickHouse Cloud. ClickHouse also promises deeper integration with PeerDB Cloud and more CDC sources later.

Sai Srirampur says the deal ["bridges the gap between Postgres and ClickHouse"](https://clickhouse.com/blog/clickhouse-acquires-peerdb-to-boost-real-time-analytics-with-postgres-cdc-integration), and says the two companies already share many users. Aaron Katz, ClickHouse's CEO, says it empowers Postgres developers to move faster when building real-time data-driven applications.

This is also a sensible build-or-buy call. CDC is a specialist problem with many edge cases, and a team that has already solved them is worth more than a connector built from scratch.

For existing PeerDB Cloud customers, the service stays available on current terms until an equivalent ClickPipes connector is generally available. Customers using non-ClickHouse destinations on a paid plan will be wound down, with end of life set for [July 30, 2025](https://clickhouse.com/blog/clickhouse-welcomes-peerdb-adding-the-fastest-postgres-cdc-to-the-fastest-olap-database).

## Relevant Products and Companies

- [ClickPipes](https://clickhouse.com/cloud/clickpipes): ClickHouse Cloud's managed ingestion service, where the PeerDB-based connector will live.
- [Debezium](https://debezium.io/): the best-known open source CDC platform, commonly used to stream database changes into Kafka. The closest do-it-yourself alternative.
- [Mooncake Labs](../acq/017_ACQ_mooncake_by_databricks.md): a similar bridge from Postgres to the lakehouse, bought by Databricks.

## My Take

Everyone wants Postgres integration. Postgres is where applications start, so every analytics engine, warehouse and lake needs a way to get at its data. Each engine has its own advantages and disadvantages: ClickHouse is very fast at analytics, Postgres is excellent for transactions, and a lake is cheap and open. No one engine does everything well, so the integration between them is where the value is.

PeerDB helps with exactly that. It does not replace Postgres and it does not replace ClickHouse. It moves the data between them, reliably, and for the Postgres users who are ClickHouse's best prospects, that removes the biggest obstacle to trying it. ClickHouse is buying a way in.

I expect this to be only the first step. Once ClickHouse owns the CDC path, the next reasonable step is to make Postgres a first-class citizen in the product: replication that just works, then deeper integration, and eventually Postgres itself living next to ClickHouse.

## Updates

*These entries were added after the original article. They are not part of the announcements.*

### May 29, 2025: The Postgres CDC connector in ClickPipes is generally available

The first step arrived as expected. ClickHouse says PeerDB is now [fully integrated into ClickHouse Cloud](https://clickhouse.com/blog/postgres-cdc-connector-clickpipes-ga) as the Postgres CDC connector in ClickPipes. After a six-month beta, it supports hundreds of production workloads and moves more than 100TB of data a month, by ClickHouse's own numbers. Parallel snapshots are said to make initial loads and resyncs 10x faster, and replication latency can be as low as 10 seconds. Reference customers named are Ashby, Seemplicity and AutoNation. Billing started on September 1, 2025.

### Jan 22, 2026: ClickHouse launches its own managed Postgres

The second step went further, which is the direction described in My Take. ClickHouse [announced a managed Postgres service](https://clickhouse.com/blog/postgres-managed-by-clickhouse), built with its partner Ubicloud and running on local NVMe storage, in private preview on AWS and free during the preview. It describes a unified data stack: Postgres for transactions, ClickHouse for analytics, and PeerDB-powered replication between them, which syncs data in real time with an initial load followed by incremental change capture. Each service also includes the pg_clickhouse extension, so users can query ClickHouse from Postgres.

<figure class="shot narrow">
  <img src="{{ '/assets/images/peerdb/managed-postgres.png' | relative_url }}" alt="Architecture of ClickHouse managed Postgres: transactions in Postgres, CDC replication and pg_clickhouse queries to ClickHouse" loading="lazy">
  <figcaption>Managed Postgres next to ClickHouse: CDC replication one way, pg_clickhouse queries the other. Source: <a href="https://clickhouse.com/blog/postgres-managed-by-clickhouse">ClickHouse</a>.</figcaption>
</figure>
