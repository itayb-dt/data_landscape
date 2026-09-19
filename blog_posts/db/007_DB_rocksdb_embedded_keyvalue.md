# DB: RocksDB — The Storage Engine Behind Half the Databases You Use

## Opening Context

[RocksDB](https://rocksdb.org/) is an embeddable, persistent key-value store built and open-sourced by Meta (formerly Facebook). It is written in C++ and designed around one core idea: make writes to flash storage as fast as physically possible. It is not a database you talk to directly. It is the engine other databases are built on top of — and that distinction is what makes it worth understanding.

Version history goes back to 2012 when Meta forked Google's LevelDB. As of 2026 it is under active development with a steady stream of performance improvements coming from Meta, Bytedance, and the broader community.

---

## What Is RocksDB?

RocksDB is an embedded key-value storage engine in the LSM-tree (Log-Structured Merge-tree) family. "Embedded" means it runs as a library inside your process — there is no server, no port, no separate daemon. Your application links against it and calls its API directly.

Core architectural properties:

- **LSM-tree structure**: all writes go to an in-memory buffer (memtable), then flush sequentially to disk. No random writes.
- **Compaction**: background threads periodically merge and sort on-disk files (SSTables) to keep reads efficient and reclaim space.
- **Tunable for hardware**: separate configurations for HDD, SSD, and in-memory deployments — not a one-size-fits-all default.
- **Column families**: logical partitions within a single RocksDB instance, each with independent compaction and compression settings.
- **Key-value only**: keys and values are arbitrary byte arrays. There is no schema, no SQL, no secondary indexes built in.

---

## What Problems Does It Solve?

Flash storage (SSDs) fundamentally penalizes random writes. The hardware is fast at sequential reads and writes but expensive on random write patterns because of how NAND erase cycles work. B-tree storage engines (the classic alternative) perform random in-place updates — fine for spinning disk, punishing for SSD endurance and throughput at scale.

RocksDB was built to exploit the sequential write behavior of LSM trees to maximize SSD throughput while keeping the storage engine embeddable and tunable for diverse workloads. At Meta's scale — billions of writes per day across social graph, messaging, and other systems — the difference between "ok at writes" and "optimized for sequential writes" was worth building a purpose-specific engine.

The problems it solves:

- **Write-heavy workloads that saturate traditional B-tree engines**: ingestion pipelines, event logs, time-series, changelog data.
- **Building a custom database without writing a storage layer from scratch**: CockroachDB, TiKV, and others use RocksDB so they could focus on the distributed and query layers.
- **SSD endurance at high write volume**: lower write amplification compared to B-trees extends hardware lifetime in storage-constrained environments.

---

## What It Is Best For

**Embedded storage engine for a database you are building**: If you are building a distributed database, a stream processor state store, or a specialized data engine, RocksDB saves you from implementing your own durable storage layer. This is its most common real-world use. CockroachDB, TiKV (the storage layer behind TiDB), MyRocks (MySQL with RocksDB storage), and Apache Flink's state backend all use it this way.

**Write-heavy workloads on SSD**: Applications that ingest continuously and read occasionally — event stores, audit logs, ledger systems — fit the LSM model well. Writes are fast and sequential; reads are slower but acceptable.

**Key-value lookups in performance-critical services**: When you need durable, low-latency point lookups by key and do not need SQL or secondary indexes, RocksDB outperforms most general-purpose databases. LinkedIn uses it for feed ranking signals, Meta for social graph edges.

**Stream processing state**: Apache Kafka Streams and Flink use RocksDB as their default state backend for exactly this reason — fast writes during event processing, durable across restarts.

---

## What It Is Not Good For

**Direct application use without a query layer**: RocksDB gives you `Get(key)` and `Put(key, value)`. There is no SQL, no joins, no aggregations, no secondary indexes. If your application needs those things, you need to build them or use a database that already has.

**Read-heavy workloads with wide scans**: LSM-tree read amplification is a real cost. A single point read may touch multiple SSTable levels before finding the right version. Heavy scan workloads — full table scans, range aggregations — perform better on B-tree or columnar engines. The compaction process helps, but it is fundamentally a write-optimized structure.

**Large values**: RocksDB is optimized for small-to-medium values. Storing large blobs (multi-MB values) causes compaction to read and rewrite more data than necessary. There is a BlobDB extension that partially addresses this, but it adds complexity.

**Teams without C++ expertise managing the engine directly**: Tuning RocksDB for production is non-trivial. Compaction strategy, memtable sizing, block cache configuration, compression per level — these levers matter and misconfiguring them causes real performance problems. Most teams consume it through a database that has already done this tuning.

---

## Competitive Landscape

**LevelDB** — RocksDB's direct ancestor, also from Google/open-source. Simpler, less configurable, lower performance ceiling. RocksDB is the reason most people have moved on from LevelDB for anything serious.

**LMDB** — memory-mapped B-tree engine. Faster for read-heavy workloads and simpler operational profile, but write performance falls behind RocksDB at high write rates. Used in OpenLDAP and some embedded scenarios.

**WiredTiger** — the storage engine MongoDB uses. B-tree based (with some LSM options). A direct alternative for embedded storage use cases. Stronger at mixed read/write; RocksDB wins on pure write throughput.

**BadgerDB** — RocksDB-inspired LSM engine written in Go. Used by Dgraph. Lower C++ dependency cost for Go shops, but smaller community and less production hardening.

**Apache Cassandra's storage engine** — Cassandra uses its own LSM implementation. Same conceptual model as RocksDB, purpose-built for Cassandra's data model and not embeddable.

---

## My Take

RocksDB is infrastructure in the same way that Linux is infrastructure — most people using it do not know they are using it, and that is exactly the point. It won the embedded storage engine category convincingly. When CockroachDB, TiKV, Kafka Streams, and Flink all converge on the same storage engine, that is not a coincidence — it is validation.

If you are building something at the layer where RocksDB is a choice, it is probably the right default. The tuning complexity is real but manageable, and the community is large enough that most production problems have been solved before.

If you are using it indirectly through a database — which is how most people encounter it — then what matters is whether the database on top of it is well-designed. RocksDB will not save a bad design, but it will not be the bottleneck either.

I'll be watching the async coroutine read work. The 29–305% throughput gains in batched read scenarios are significant and could change the calculus on some read-heavy use cases where RocksDB has historically been a weaker choice.

---

## Further Reading

- [RocksDB official documentation](https://rocksdb.org/)
- [RocksDB: Evolution of Development Priorities — ACM paper](https://dl.acm.org/doi/10.1145/3483840)
- [The Fundamentals of RocksDB — GetStream](https://getstream.io/blog/rocksdb-fundamentals/)
- [B-Tree vs LSM-Tree — TiKV deep dive](https://tikv.org/deep-dive/key-value-engine/b-tree-vs-lm/)
- [MyRocks: RocksDB storage engine for MySQL — Meta Engineering](https://engineering.fb.com/2016/08/31/core-infra/myrocks-a-space-and-write-optimized-mysql-database/)
