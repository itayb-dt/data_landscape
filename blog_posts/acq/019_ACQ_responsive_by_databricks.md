---
title: "Databricks acquires Responsive to bring object-storage-native database engineering to Lakebase"
published: 2026-10-29
---
Responsive [announced on October 9, 2026](https://www.responsive.dev/) that it is joining Databricks, "to accelerate Lakebase and Neon development". The price was not disclosed, and I found no separate Databricks post, so the facts here come from Responsive's own announcement. The three founders, Apurva Mehta, Almog Gavra and Rohan Desai, are joining. The open source project they built, SlateDB, stays independent.

<figure class="shot">
  <img src="{{ '/assets/images/responsive/hero.png' | relative_url }}" alt="Responsive and Databricks logos" loading="lazy">
  <figcaption>Responsive is joining Databricks. Source: <a href="https://www.responsive.dev/">Responsive</a>.</figcaption>
</figure>

## The Problem: Online databases keep their data on local disks, which makes them costly and slow to change

A traditional database keeps its data on disks attached to the machine that serves it. That ties storage to compute. Adding capacity means moving data between machines. Making a copy for testing means copying the files. Durability means replicating every write across availability zones, and you pay for that traffic.

Object storage, such as S3, looks like the answer: it is cheap, almost unlimited and highly durable, and it lets different engines read the same data. The catch is that, as [Chris Riccomini explains](https://materializedview.io/p/slatedb-an-embedded-storage-engine), it has higher latency and a per-request price compared with a local disk. Most storage engines, RocksDB being the best known, are built on the assumption of a fast local disk. Building an online system on object storage means rethinking the engine, not just changing where the files go.

Take a team running a stateful service with terabytes of state. Scaling out means shipping terabytes to new nodes. Recovering from a failure means reloading them. Testing a change safely means a full copy. Each of those is slow and expensive because the state lives on one machine's disk.

## The Solution: Databases built to keep their state on object storage

Responsive began by building tooling for Kafka Streams applications, and that work is now [archived](https://www.responsive.dev/). Its current thesis is to [separate storage from compute](https://www.responsive.dev/), keep state on object storage in an open format that different engines (transactional, search, analytical) can share, and make checkpoints, branches and clones instant and cheap, so developers and agents can experiment without touching production.

Two open source projects carry that idea:

- **[SlateDB](https://slatedb.io/)**: an embedded key-value database and LSM engine built on object storage, under the Apache 2.0 license. It has a Rust core with Go, Java, Node.js and Python bindings. Data is written straight to object storage with no local disks, one writer is enforced by a fencing protocol on the manifest, many readers can scale reads, and checkpoints are zero-copy, which is the basis for clones. Its site shows logos of Dropbox, Prisma and HelixDB, among others. Rohan Desai [co-created it](https://materializedview.io/p/slatedb-an-embedded-storage-engine), and it was released as open source in August 2024.
- **[OpenData](https://www.opendata.dev/)**: a family of open source (MIT) object-native databases, all built on SlateDB: a vector database with full-text search, a durable ingestion buffer that works without Kafka, a Prometheus-compatible time series database, and a log for event streams.

The benefit goes to teams that want databases that scale and cost like object storage and still serve online workloads.

### Funding history

Public Funding Rounds: Not publicly available from credible sources.

## Understanding the Acquisition

Lakebase, Databricks' Postgres, is built on the same principles. Databricks describes a Lakebase as an architecture that [separates compute from storage, keeps data in open formats, and stores it in cloud object stores](https://www.databricks.com/blog/what-is-a-lakebase). Responsive says Lakebase shares the architectural principles behind its work, and that the team joins to help Lakebase move into its next phase.

The announcement names a term for that phase: LTAP, for lake transactional and analytical processing. In [The New Stack's description](https://thenewstack.io/databricks-is-rebuilding-the-data-stack-for-ai-agents/), the idea is to keep one copy of the data in open formats and let transactional and analytical engines work on it without a pipeline between them. That is the same job Mooncake was bought for (see my [Mooncake article]({{ '/blog_posts/acq/017_ACQ_mooncake_by_databricks.html' | relative_url }})), but from the storage side.

What is new is the team. Neon already separates storage and compute, so Databricks did not need Responsive for the idea. What the team has built is the hard part underneath: an engine that makes object storage fast and cheap enough for online workloads, and a way to share that state across engines. My reading, not stated in the announcement, is that this experience goes into the storage layer of Lakebase and Neon, and that OpenData's vector and search databases line up with the search and retrieval features Neon calls [Lakebase Search](https://neon.com/blog/lakebase-search-retrieval-agents).

For customers and the community: SlateDB [stays independently governed](https://www.responsive.dev/) by the Commonhaus Foundation, so it does not become a Databricks product. Responsive's Kafka Streams work is no longer actively developed, so any team still using it should plan for that. The announcement names no customers.

## Relevant Products and Companies

- [SlateDB](https://slatedb.io/): the embedded LSM engine on object storage at the center of the deal, staying independent.
- [OpenData](https://www.opendata.dev/): the family of object-native databases, built on SlateDB.
- [Lakebase](https://www.databricks.com/product/lakebase): Databricks' Postgres, built on Neon, where this engineering is going. The Postgres side of the story is in my [Neon article]({{ '/blog_posts/acq/015_ACQ_neon_by_databricks.html' | relative_url }}).
