---
title: "Separation of storage and compute"
show_title: true
---
## Opening Context

Separation of storage and compute is a core architectural pattern behind many modern analytics and cloud database platforms. Instead of tying data and processing to the same machines, it decouples them so each layer can scale independently.

This model is popular because it improves elasticity, simplifies operations for many workloads, and can align costs more closely with actual usage.

Last updated: Nov 4, 2025  
Created: Mar 3, 2025

## What Is Separation of Storage and Compute?

In plain language, separation of storage and compute means your data lives in one layer, while query/processing engines run in another. Compute can scale up or down without moving the data each time.

Technical definition: it is a decoupled architecture where persistent data storage is centralized (typically object storage or shared storage services), and stateless or semi-stateless compute clusters access that data over the network.

Core architectural properties:
- Compute and storage layers are decoupled.
- Storage is shared and accessible by multiple compute clusters.
- Compute can scale independently from storage capacity.
- Workloads can be isolated by spinning up separate compute resources against the same data.
- Billing often maps separately to storage consumption and compute usage.

This is the opposite direction of classic shared-nothing, co-located designs, where each node stores and processes its own local slice of data.

## What Problem Is It Designed to Solve?

Traditional co-located systems are often fast because data is local to compute, but they create coupling between capacity dimensions. If you need more CPU for bursty queries, you may also need to provision more storage nodes than necessary. If you need more storage, you may be forced to buy more compute than you need.

Separation addresses several practical bottlenecks:
- Inefficient scaling when storage growth and compute demand do not move together.
- Operational friction from resizing tightly coupled clusters.
- Cost inefficiency from overprovisioning one resource to get another.
- Multi-team contention when all workloads share the same fixed cluster.

The concept is designed to solve flexibility and elasticity problems first. It is not a magic performance optimization in every scenario.

## Main Advantages

In practice, teams adopt this model not for one abstract reason, but because it consistently improves how they scale, isolate workloads, and control spend as demand changes.

- **Independent scaling**: Teams can increase compute for a high-concurrency reporting window without changing storage footprint.
- **Better workload isolation**: Different departments or use cases can run on separate compute pools against shared data, reducing noisy-neighbor issues.
- **Cost control and transparency**: Storage and compute can be monitored and optimized separately, making usage patterns easier to understand.

## Real-World Use Cases

[Snowflake](https://www.snowflake.com/en/) is the clearest mainstream example of this model in practice, so its customer stories are a good way to see what the architecture changes operationally. In [AT&T's case study](https://www.snowflake.com/en/customers/all-customers/case-study/att/), Snowflake highlights self-service dashboards and major cost savings tied to caching and a unified data platform. The important architectural shift is not just faster reporting. It is that teams move away from provisioning around peak demand on one fixed system and toward an operating model where compute behavior can be tuned around query demand while storage remains shared and persistent.

The same pattern appears in [KFC's case study](https://www.snowflake.com/en/customers/all-customers/case-study/kfc/), where Snowflake says data sharing went from days to seconds and database operational costs fell. What changes here is the coordination model: instead of routing every team through one tightly coupled platform with more operational overhead, organizations can let multiple teams work against the same data foundation with less contention and less infrastructure coupling.

## Relevant Companies and Systems

[Snowflake](https://www.snowflake.com/) - a cloud data platform known for separating storage and virtual warehouses (compute).

[Google BigQuery](https://cloud.google.com/bigquery) - serverless analytics service with decoupled compute and storage economics.

[Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) - enables querying shared data in S3 with separate compute layers.

[ClickHouse Cloud](https://clickhouse.com/cloud) - managed deployment model that supports cloud decoupling patterns while ClickHouse roots remain performance-oriented.

[Neon](https://neon.tech/) - serverless Postgres architecture that separates storage from compute to enable elastic, ephemeral environments.

## Tradeoffs, Disadvantages, and Limits

Of course, there are also real disadvantages and tradeoffs to this approach, especially when data locality, simplicity, or predictable performance matter more than elasticity.

- **Network overhead**: Because storage is remote from compute, decoupled systems can add latency and bandwidth penalties compared with co-located architectures.
- **Higher system complexity**: Separate storage, compute, caching, and governance layers create more moving parts, which raises the operational bar for teams that want a simpler platform.
- **Not ideal for every workload**: If demand is stable or the workload depends on maximum local-disk and memory-first performance, a tightly coupled architecture may be a better fit.

## Practical Decision Framework

Use separation of storage and compute when most of these are true:
- Compute demand is bursty or unpredictable.
- Storage growth is steady but not tied to compute demand.
- Multiple teams need isolated workloads on shared datasets.
- You can enforce query governance and cost monitoring.
- You value operational elasticity over absolute peak local-disk speed.

Consider co-located models when most of these are true:
- You optimize for strict low-latency query performance.
- Workload shape is stable and predictable.
- You can efficiently operate tightly coupled clusters.
- Data locality is a first-order requirement.

## Co-located vs Decoupled: Practical Note

Systems like Druid and ClickHouse are often associated with co-located query performance characteristics. Even when architectures include different node roles, they still commonly emphasize high-speed data access paths for query execution.

Decoupled cloud data warehouse architectures prioritize elasticity and independent scaling. In many real systems, vendors also introduce caching and optimization layers to reduce the performance gap, but tradeoffs remain.

## Further Reading

[Snowflake Architecture Overview](https://docs.snowflake.com/en/user-guide/intro-key-concepts)

[Google BigQuery Architecture](https://cloud.google.com/bigquery/docs/introduction)

[Amazon Redshift Spectrum Documentation](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html)

[ClickHouse Cloud Documentation](https://clickhouse.com/docs/en/cloud/overview)

[Neon Architecture](https://neon.tech/docs/introduction/architecture-overview)
