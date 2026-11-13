---
title: "EDB acquires Altinity to add ClickHouse analytics to its Postgres platform"
published: 2026-11-09
---
EDB [announced on November 5, 2026](https://altinity.com/news/altinity-and-enterprisedb) that it has acquired Altinity, a leading independent provider of software, services and support for ClickHouse. EDB did not disclose the price. The one thing that matters: EDB, a Postgres company, now owns the expertise to run the leading open source analytics database next to it.

<figure class="shot">
  <img src="{{ '/assets/images/altinity/hero.png' | relative_url }}" alt="Altinity and EnterpriseDB are joining forces to deliver sovereign AI data systems" loading="lazy">
  <figcaption>Altinity and EnterpriseDB. Source: <a href="https://altinity.com/news/altinity-and-enterprisedb">Altinity</a>.</figcaption>
</figure>

## The Problem: Running ClickHouse in production is hard, and the best features live in one vendor's cloud

ClickHouse is a column-oriented database built for fast analytics on very large tables. The engine is open source under the Apache 2.0 license, so any company can download it and run it. Running it well is another matter. A production cluster has shards and replicas, a coordination service, version upgrades, new nodes to add, and a schema that has to stay the same on every node. A team that wants to self-host ClickHouse on Kubernetes has to build and maintain all of that.

There is a second problem. ClickHouse, Inc. sells its own managed service, ClickHouse Cloud, and some of its features exist only there. ClickHouse's documentation lists, for example, compute-compute separation, which lets several groups of compute nodes work on the same data and is available in the Scale and Enterprise plans, and the SharedMergeTree table engine, which [ClickHouse built from scratch for ClickHouse Cloud](https://clickhouse.com/blog/clickhouse-cloud-boosts-performance-with-sharedmergetree-and-lightweight-updates). A company that runs the open source engine does not get them. Imagine a bank that must keep data in its own data center and cannot use a public cloud: it can run ClickHouse itself, but it needs someone to support it, and it gets the base engine only.

## The Solution: Support, a managed service and Kubernetes tooling for open source ClickHouse

[Altinity](https://altinity.com/) is built around that gap. Its tagline is "Run open source ClickHouse better". It sells:

- **Altinity.Cloud:** a managed ClickHouse service, either on Altinity's cloud or in the customer's own cloud account.
- **Support and training:** 24/7 support for ClickHouse, and training.
- **Altinity Stable Builds:** ClickHouse binaries based on the long-term-support releases, which Altinity maintains for up to three years. They are Apache 2.0 licensed, with "no hold-backs or closed source components" in Altinity's words.
- **Project Antalya:** an open source project that Altinity describes as a way to run ClickHouse queries on cheaper data lakes.

Altinity builds on open source ClickHouse. It is not affiliated with ClickHouse, Inc., and says so on its site. EDB says Altinity is the number two company contributor to ClickHouse, with 888 merged pull requests, and that it serves customers such as Samsung Electronics and Jump Trading, who are quoted on EDB's announcement page.

### The Kubernetes operator

Altinity also maintains the [Altinity Kubernetes Operator for ClickHouse](https://github.com/Altinity/clickhouse-operator). An operator is a piece of software that runs inside Kubernetes and does what a database administrator would otherwise do by hand. You describe the cluster you want, and the operator builds it and keeps it that way.

This one creates, configures and manages ClickHouse clusters on Kubernetes. A cluster is defined as a custom resource, and the operator handles scaling, including copying the schema to new nodes automatically, and version upgrades. It also configures users and exports metrics to Prometheus. It is Apache 2.0 licensed, has about 2.6k stars on GitHub, and Altinity is its primary maintainer. Altinity calls it the first Kubernetes operator for ClickHouse, or for any analytic database.

## Understanding the Acquisition

EDB sells Postgres, with support, tools and an enterprise distribution. What it lacked next to its transactional database was an analytics engine. [EDB's announcement](https://www.enterprisedb.com/announces/altinity) states the plan in two sentences: "Postgres writes the record. ClickHouse reads it." EDB says its Postgres AI analytics architecture uses ClickHouse as its real-time engine, and that the combined company serves more than 1,860 enterprise customers.

Altinity brings the know-how: the people who contribute to ClickHouse, run it for customers and have built the operator for Kubernetes.

What changes, according to the announcement:

- Altinity becomes the EDB Real-Time Analytics group and reports to EDB's CEO, Kevin Dallas. The management team stays.
- Customer contracts, SLAs, products and services stay the same.
- ClickHouse stays Apache 2.0. Altinity Stable Builds, the operator and Project Antalya stay open source under Apache 2.0.
- ClickHouse, Inc. is not part of the deal and remains independent.
- EDB plans to add integrated enterprise ClickHouse capabilities to its platform.

This is the same idea as ClickHouse's own recent moves, seen from the other side. ClickHouse bought a Postgres company, [Xata]({{ '/blog_posts/acq/037_ACQ_xata_by_clickhouse.html' | relative_url }}), to get a Postgres to sit next to its analytics engine. EDB bought a ClickHouse company to get an analytics engine to sit next to its Postgres.

## Relevant Products and Companies

- [ClickHouse Cloud](https://clickhouse.com/cloud): ClickHouse, Inc.'s own managed service, the direct alternative to Altinity.Cloud.
- [Altinity Stable Builds](https://altinity.com/altinity-stable/): the supported open source distribution at the center of Altinity's offer.
- [PeerDB]({{ '/blog_posts/acq/018_ACQ_peerdb_by_clickhouse.html' | relative_url }}): the Postgres replication that ClickHouse bought to connect the same two engines.

## My Take

ClickHouse made its base engine open source, and that let other companies build a business on top of it. Altinity is the clearest example. But I think companies like that do not grow too much. The features that matter most are in ClickHouse's own cloud, so a company around the open source version works at the edges.

EDB has done this before. It took open source Postgres and built an enterprise version of it. Now it has taken open source ClickHouse, and it may build an advanced version of that too. Time will tell.
