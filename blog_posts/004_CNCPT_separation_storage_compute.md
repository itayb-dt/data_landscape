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

Independent scaling
- Teams can increase compute for a high-concurrency reporting window without changing storage footprint.

Better workload isolation
- Different departments or use cases can run on separate compute pools against shared data, reducing noisy-neighbor issues.

Cost control and transparency
- Storage and compute can be monitored and optimized separately, making usage patterns easier to understand.

Operational elasticity
- Compute can be paused, resumed, or resized faster in many cloud-native systems.

Faster experimentation
- New workloads can start with dedicated compute against existing shared data, with less migration overhead.

## Real-World Use Cases

Burst analytics for business reporting
- A finance team can run heavy month-end queries on a temporary larger compute tier without re-architecting storage.

Multi-tenant analytics platforms
- Different internal teams or customers can get isolated compute resources while using a common data foundation.

Mixed BI and data science access
- BI dashboards and exploratory workloads can use different compute configurations against the same underlying datasets.

Cloud-native data platforms with variable demand
- Organizations with uneven query patterns benefit from scaling compute to demand while keeping storage stable.

Developer-friendly database branching and ephemeral environments
- Decoupled models can support fast creation of short-lived compute endpoints while reusing durable storage.

## Relevant Companies and Systems

[Snowflake](https://www.snowflake.com/) - a cloud data platform known for separating storage and virtual warehouses (compute).

[Google BigQuery](https://cloud.google.com/bigquery) - serverless analytics service with decoupled compute and storage economics.

[Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) - enables querying shared data in S3 with separate compute layers.

[ClickHouse Cloud](https://clickhouse.com/cloud) - managed deployment model that supports cloud decoupling patterns while ClickHouse roots remain performance-oriented.

[Neon](https://neon.tech/) - serverless Postgres architecture that separates storage from compute to enable elastic, ephemeral environments.

## Tradeoffs, Disadvantages, and Limits

Network distance penalties
- When data is remote from compute, access latency and bandwidth can become bottlenecks versus local-disk execution.

Potential performance gap for some OLAP patterns
- Co-located, memory-first architectures can still outperform decoupled designs on certain high-intensity workloads.

More moving parts
- You gain flexibility, but distributed coordination, caching behavior, and storage-service dependencies add complexity.

Cost surprises from poor governance
- While decoupling can lower costs, always-on warehouses, inefficient query patterns, or egress-heavy workflows can erase benefits.

Operational tuning is still required
- Decoupled does not remove the need for partitioning strategy, query optimization, and data layout discipline.

## When This Is Not a Good Solution

Ultra-low-latency workloads where every millisecond matters
- If your primary requirement is maximum local read speed and predictable tail latency, co-located architectures may be better.

Highly stable workloads with fixed capacity profiles
- If demand is constant and well-understood, the flexibility premium of decoupled architecture may not pay off.

Teams without cloud cost controls or performance observability
- Decoupling can create spend/performance drift without strong governance, query discipline, and monitoring.

Workloads heavily dependent on local-state optimizations
- Some systems benefit from tight data locality and in-memory patterns that are harder to replicate with remote storage.

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
