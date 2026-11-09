---
title: "Cloudflare acquires Arroyo to add SQL stream processing to its developer platform"
published: 2025-04-14
---
Cloudflare [announced on April 10, 2025](https://blog.cloudflare.com/cloudflare-acquires-arroyo-pipelines-streaming-ingestion-beta/) that it has acquired Arroyo, an open source stream processing engine, alongside the open beta of its new streaming product, Pipelines. The price was not disclosed. The one thing that matters: Pipelines launched as ingestion only, and Arroyo is how Cloudflare plans to add SQL processing on top.

<figure class="shot">
  <img src="{{ '/assets/images/arroyo/hero.png' | relative_url }}" alt="Cloudflare blog graphic: Just landed, streaming ingestion on Cloudflare with Arroyo and Pipelines" loading="lazy">
  <figcaption>Cloudflare's launch post for Pipelines and the Arroyo acquisition. Source: <a href="https://blog.cloudflare.com/cloudflare-acquires-arroyo-pipelines-streaming-ingestion-beta/">Cloudflare</a>.</figcaption>
</figure>

## The Problem: Streaming data needs state, and state is hard to run

Events arrive constantly: clicks, payments, sensor readings, logs. Most teams don't want each event on its own. They want "orders per minute by region", or "alert me when a card is used in two countries within ten minutes". That means remembering what already happened, in windows of time and across joins between streams.

Remembering is the hard part. The engine has to keep that state, save it so a crash doesn't lose it, and give the same answer after a restart. The established tool is Apache Flink, which is powerful but runs on the JVM, needs tuning and usually a dedicated team. Many teams that only need windows and aggregations end up either running Flink or writing the logic by hand in application code.

## The Solution: A streaming engine where SQL is the API

[Arroyo](https://www.arroyo.dev/) is a distributed stream processing engine written in Rust. Its [README](https://github.com/ArroyoSystems/arroyo) lists SQL pipelines, stateful windows and joins, checkpointing for fault tolerance, and connectors including Kafka and Iceberg. In Cloudflare's post, founder Micah Wylde says they built it in Rust for speed and operational simplicity ("no JVM tuning required!"), started with SQL as the API, and built an object-storage-native state backend. That last point means state is kept in cheap object storage instead of on local disks.

The engine is dual-licensed under Apache 2 and MIT. The post says dozens of companies run Arroyo pipelines, which is a vendor claim. Wylde names Lyft and Splunk, and Flink, as his earlier experience.

### Funding history

Pre-seed - April 2023 - about $500K - [VCBacked](https://www.vcbacked.co/company/arroyo), an aggregator, with Y Combinator among the investors. I could not confirm it from Arroyo or Y Combinator. No later round found.

## Understanding the Acquisition

Cloudflare's own words: the Pipelines beta lets you ingest high volumes of structured, real-time data and load it into R2, its object storage. Transformations, it says, are still to come. It plans "to bring the best parts of Arroyo into Pipelines and deeply integrate it with Workers, R2, and the rest of our Developer Platform", with a streaming SQL API on the way.

The pieces fit. Pipelines is the front door, R2 is the storage, and [R2 Data Catalog](https://blog.cloudflare.com/r2-data-catalog-public-beta/), launched the same week, manages Iceberg tables on R2. Cloudflare says it wants to ingest streams directly into Iceberg tables you can query immediately. Arroyo supplies the missing middle: filtering, enriching and aggregating events before they land. Cloudflare also lists Workers as user-defined functions, Kafka clients as a source, and sinks beyond R2.

What stays: Arroyo says the engine "will remain open-source and self-hostable". Cloudflare's post says nothing about the license, and neither source says what happens to Arroyo's own hosted service and its customers. The README now points to Cloudflare Pipelines as the managed option, noting that only stateless pipelines into R2 are supported so far. Stateful pipelines are described as coming.

The announcement states no terms and no team size.

## Relevant Products and Companies

- [Apache Flink](https://flink.apache.org/): the incumbent open source stream processor, and the system Arroyo is positioned against.
- [Confluent](https://www.confluent.io/): Kafka's commercial company, the other major home for streaming and stream processing.
- [Cloudflare R2](https://developers.cloudflare.com/r2/): the object storage where Pipelines lands its data.

## My Take

*Draft for the author to rewrite.*

This is a platform play, not a database play. Cloudflare has been assembling a data stack out of its own parts: storage in R2, tables in Iceberg, compute in Workers. Streaming ingestion was the missing entry point, and SQL processing is the next one. I expect Cloudflare to use Arroyo to make the simple case very simple: events in, a few lines of SQL, a queryable table out, with no cluster to run.

I don't expect it to replace Flink for heavy workloads. The people who gain most are teams already on Workers who would never have set up a streaming system. A small deeptech team with an open source engine and no hosted business of scale had a clear way out here, and joining a platform that already has the storage and the customers looks like a sensible outcome.
