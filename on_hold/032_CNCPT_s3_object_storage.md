---
title: "S3 and object storage: not a database, but databases are built on it"
published: 2026-11-05
show_title: true
---
## Opening Context

Almost every modern data platform keeps its data in object storage, and the reference implementation is Amazon S3. It is simple, very durable and cheap. It is also where a growing share of the market is moving its tables.

This is the first post in a series. It covers the basics: what S3 is, whether it is a database, and the move to separate storage from compute.

## What Is S3?

S3 stores objects in buckets. An object is a file plus metadata, and you read or write it through an HTTP API. There are no directories in the file system sense, no in-place edits and no query language.

Two numbers are worth getting right:
- **Durability**: AWS says S3 is [designed to provide 99.999999999% (11 nines) data durability](https://aws.amazon.com/s3/storage-classes/), with data stored across a minimum of three Availability Zones by default. This is about not losing data, not about uptime.
- **Availability**: S3 Standard is designed for 99.99% availability, with an availability SLA of 99.9% ([AWS](https://aws.amazon.com/s3/storage-classes/)).

The S3 API has also become the common language of object storage. Many other products copy it.

## Cheaper Than Any Database

Storing a terabyte in object storage costs a fraction of storing it in a database or on block storage. That is my general view, not a benchmark, and the exact price depends on the region and storage class, so check the [AWS pricing page](https://aws.amazon.com/s3/pricing/).

The price comes with trade-offs. Every read and write is a network request that AWS bills, and reading data out to the internet costs money, while data transferred in is free. Latency is much higher than local disk.

## Is S3 a Database?

Not by itself. S3 has no query engine, no schema, no indexes and no transactions across objects. You can put a file in and get it back, and that is the whole contract. AWS does say S3 now gives [strong read-after-write consistency](https://aws.amazon.com/s3/faqs/): a read right after a write sees the latest version. That is a useful building block, but it is not a database.

What is changing is the layer above. Open table formats such as [Apache Iceberg](https://iceberg.apache.org/) and [Delta Lake](https://docs.delta.io/latest/index.html) add table metadata on top of plain files, so many engines can work on the same tables. Iceberg says engines like Spark, Trino, Flink, Presto, Hive and Impala can "safely work with the same tables, at the same time". A catalog then tells the engine where the tables are.

AWS is moving into this layer itself:
- [S3 Tables](https://aws.amazon.com/s3/features/tables/): fully managed Apache Iceberg tables in S3, exposed through the Iceberg REST Catalog API, with engines such as Spark, Trino, Flink, Athena, Redshift and Snowflake.
- [S3 Metadata](https://aws.amazon.com/s3/features/metadata/): object metadata stored in read-only Iceberg tables you can query.
- [S3 Vectors](https://aws.amazon.com/s3/features/vectors/): which AWS calls "the first cloud object store with native support to store and query vectors".

So S3 is not a database, but it keeps picking up database features, and many databases now use it as their storage layer.

## Separate Storage From Compute

This is the pattern behind that shift. Data lives in one shared layer, usually object storage, and the engines that process it run separately and can scale on their own. I explain the idea in more detail in [Separation of storage and compute]({{ '/blog_posts/cncpt/004_CNCPT_separation_storage_compute.html' | relative_url }}).

The advantages:
- **Independent scaling**: add compute for a heavy query without buying more storage, and the reverse.
- **Isolated workloads**: several compute clusters can read the same data without slowing each other. ClickHouse Cloud, for example, lets [multiple compute node groups use the same shared object storage](https://clickhouse.com/docs/cloud/reference/architecture).
- **One copy, many engines**: with open table formats, different tools query the same files.

Products built this way:
- [Snowflake](https://docs.snowflake.com/en/user-guide/intro-key-concepts): "Snowflake separates storage and compute".
- [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction): its "separation of compute and storage layers" is a core design point.
- [Amazon Redshift](https://aws.amazon.com/redshift/features/): RA3 instances let you pay for compute separately from storage.
- [ClickHouse Cloud](https://clickhouse.com/docs/cloud/reference/architecture) and [Firebolt](https://docs.firebolt.io/overview/architecture-overview.md): tables in object storage, compute on top.
- [Databricks](https://docs.databricks.com/aws/en/lakehouse/): compute decoupled from storage, with Delta Lake on cloud object storage.
- Neon, now part of Databricks as Lakebase Postgres: [Postgres with compute and storage split](https://neon.com/docs/introduction/architecture-overview). See my [Neon article]({{ '/blog_posts/acq/015_ACQ_neon_by_databricks.html' | relative_url }}).

The price is latency. Neon's own documentation puts it well: object storage is "optimal for durability, scale, and cost, not latency", so these systems rely on caches to avoid slow reads.

## Alternatives to S3

S3 is not the only object store, and the API is not tied to AWS.
- **On other clouds**: Azure Blob Storage and Google Cloud Storage are the native services on Azure and GCP. I have not checked how closely each speaks the S3 API.
- **S3-compatible software you run yourself**: [MinIO](https://www.min.io/), which raised a $103M Series B in 2022. It restricted the admin console of its open source community edition in 2025, and reports say the repository was archived in 2026 while the company pushes its paid AIStor.
- **S3-compatible managed services**: [Tigris](https://www.tigrisdata.com/), a globally distributed store built for AI workloads that says customers can move across clouds without egress fees.

The reason these exist is mostly cost and control, and egress fees are a big part of both.

## My Take

This is just the basic understanding. I will write more posts about using files as tables and how to query them.

Separating storage from compute is not a new concept, but it has become much more popular as the amount of data has grown. When data is huge, copying it between systems stops making sense, and keeping one cheap copy that many engines can read does.
