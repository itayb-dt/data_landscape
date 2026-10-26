---
title: "Database types: a map of the landscape"
---
# Database Types: A Map of the Landscape

Databases are not interchangeable. Every category was built to solve a specific set of tradeoffs — and choosing the wrong one for a workload is one of the most expensive architectural mistakes a team can make. This page maps the major categories, explains what each one is optimized for, and links to reviews of specific products.

---

## Transactional (OLTP)

**Optimized for:** Many concurrent reads and writes on individual records, with strong consistency guarantees.

The classic database category. OLTP systems are row-oriented: they store all columns of a row together so that reading or updating a single record is fast. They enforce ACID properties (Atomicity, Consistency, Isolation, Durability), which makes them the right choice for anything where correctness of individual operations matters — banking, order management, user accounts, inventory.

The tradeoff: they are poor at analytical queries that scan millions of rows and aggregate across them. Running a monthly sales report on a transactional database will work — slowly and at the expense of operational performance.

**Common examples:** PostgreSQL, MySQL, Oracle, SQL Server, SQLite

---

## Analytical (OLAP)

**Optimized for:** Fast aggregation queries over large datasets.

OLAP systems are column-oriented: they store all values for a single column together, which makes it fast to read only the columns a query needs and compress them efficiently. A query like "total revenue by region for the last 12 months" reads two columns out of a table with 50 columns — a columnar engine skips the other 48.

The tradeoff: individual row writes and updates are expensive. OLAP databases are typically append-heavy (batch loads, streaming inserts) rather than point-update systems.

**Common examples:** ClickHouse, DuckDB, BigQuery, Snowflake, Amazon Redshift, Apache Druid

---

## Key-Value & Storage Engines

**Optimized for:** Fast point lookups and writes by key, often embedded inside another system.

The simplest data model: a key maps to a value. No schema, no joins, no secondary indexes (unless built on top). Key-value stores are either standalone (Redis, DynamoDB) or embedded as a storage engine inside another database (RocksDB inside CockroachDB, TiKV, Kafka Streams).

The tradeoff: the simplicity is also the limitation. Without a query layer on top, answering anything beyond "give me the value for this key" requires building it yourself.

**Common examples:** Redis, DynamoDB, RocksDB, LMDB, BadgerDB, etcd

**Reviews:**
- [RocksDB — The Storage Engine Behind Half the Databases You Use](007_DB_rocksdb_embedded_keyvalue.md)

---

## Document

**Optimized for:** Flexible, schema-free storage of structured and semi-structured data.

Document databases store data as self-contained documents (typically JSON or BSON). Each document can have a different shape — no migrations needed when a field is added. This flexibility makes them popular for content management, catalogs, user profiles, and any domain where the data model evolves frequently.

The tradeoff: without a fixed schema, maintaining data quality requires discipline at the application layer. Analytical queries across many documents are slower than in a columnar system.

**Common examples:** MongoDB, CouchDB, Firestore, Amazon DocumentDB

---

## Graph

**Optimized for:** Highly connected data where relationships are as important as the entities themselves.

Graph databases store data as nodes and edges. Traversing relationships — "find all friends of friends who also follow this account" or "what is the shortest path between these two entities?" — is a first-class operation, not an expensive series of joins. Fraud detection, knowledge graphs, recommendation engines, and network analysis are natural fits.

The tradeoff: graph databases are poor at bulk aggregation queries and at workloads where the relational structure is shallow. If your data is mostly tabular, a graph database adds complexity without benefit.

**Common examples:** Neo4j, Amazon Neptune, TigerGraph, Dgraph, FalkorDB

**Reviews:**
- [HelixDB — One Database for Graph, Vector, and Full-Text](011_DB_helixdb_graph_vector.md)

---

## Time-Series

**Optimized for:** Sequential data points indexed by time — metrics, sensor readings, events at regular intervals.

Time-series databases are built around the assumption that time is always the primary query axis. They compress time-ordered data efficiently, support downsampling and retention policies natively, and handle high-frequency writes from many sources simultaneously. Monitoring, IoT telemetry, financial tick data, and infrastructure metrics are the core use cases.

The tradeoff: time is the primary index. Querying by entity first ("all readings from sensor X") is a secondary concern, and cross-entity comparisons require additional modeling.

**Common examples:** InfluxDB, TimescaleDB, Prometheus, Victoria Metrics, QuestDB

---

## Search & Full-Text

**Optimized for:** Relevance-ranked retrieval over unstructured or semi-structured text.

Search databases build inverted indexes: for every term in a document, they store which documents contain it and how often. This makes keyword search, fuzzy matching, BM25 relevance ranking, and faceted filtering fast. Log analysis and e-commerce search are the canonical use cases.

The tradeoff: traditional search engines are weak at analytical aggregations at scale. Several newer systems (SereneDB, OpenSearch) are closing this gap by combining search indexes with columnar storage.

**Common examples:** Elasticsearch, OpenSearch, Apache Solr, Typesense

**Reviews:**
- [SereneDB — A Unified Search and Analytics Database](006_DB_serenedb_search_analytics.md)

---

## Vector

**Optimized for:** Similarity search over high-dimensional embeddings.

Vector databases store numeric embeddings — dense representations of text, images, audio, or other data produced by machine learning models. Instead of exact key lookups, they find the nearest neighbors to a query vector using algorithms like HNSW or IVF. The primary use case is semantic search and retrieval-augmented generation (RAG) for AI applications.

The tradeoff: vector search is probabilistic, not exact. It finds approximate nearest neighbors fast, but it is not a general-purpose query engine — joining vectors with structured filters requires hybrid search capabilities that vary by product maturity.

**Common examples:** Pinecone, Weaviate, Qdrant, Milvus, pgvector (PostgreSQL extension)

---

## In-Memory

**Optimized for:** Sub-millisecond latency where the entire working dataset fits in RAM.

In-memory databases keep all data in RAM rather than on disk, eliminating I/O as a bottleneck. This makes them suitable for caching, session storage, real-time leaderboards, and any workload where speed matters more than durability. Most offer optional persistence (snapshots or write-ahead logs) to survive restarts.

The tradeoff: RAM is expensive and finite. In-memory databases are not the right choice when the dataset grows beyond available memory, or when durability is a hard requirement without operational complexity.

**Common examples:** Redis, Memcached, DragonflyDB, KeyDB

---

## NewSQL / Distributed SQL

**Optimized for:** ACID transactions at horizontal scale across many nodes.

NewSQL databases attempt to give you the correctness guarantees of traditional OLTP systems with the horizontal scalability of distributed NoSQL stores. They typically use consensus protocols (Raft, Paxos) to coordinate writes across nodes and partition data automatically. The goal: global scale without giving up SQL or ACID.

The tradeoff: distributed transactions are inherently more expensive than local ones. Latency increases with geographic distribution, and operational complexity is significantly higher than a single-node PostgreSQL instance.

**Common examples:** CockroachDB, TiDB, Google Spanner, PlanetScale, YugabyteDB

---

## Wide-Column (NoSQL)

**Optimized for:** High write throughput at massive scale with eventual consistency.

Wide-column stores organize data into rows with a large and flexible set of columns, distributed across many nodes with no single point of coordination. They sacrifice strong consistency for availability and partition tolerance (the CAP theorem tradeoff). They excel at write-heavy workloads that must stay up even when nodes fail.

The tradeoff: eventual consistency means different nodes may return different values for the same key at the same moment. Applications must be designed to tolerate this. Complex queries requiring joins or strict ordering are not a natural fit.

**Common examples:** Apache Cassandra, HBase, Google Bigtable, ScyllaDB

---

*This page is updated as new reviews are published.*
