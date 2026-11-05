---
title: "Supabase acquires Oriole to build a faster storage engine for Postgres"
published: 2024-04-18
---
Supabase [announced on April 15, 2024](https://supabase.com/blog/supabase-acquires-oriole) that the Oriole team is joining it "to build a faster storage engine for Postgres". The price was not disclosed. The product is OrioleDB, a Postgres storage engine that is still early-stage software.

## The Problem: Postgres's default storage was built for another era

Every Postgres table is stored in the default engine, called the heap. When rows are updated, old versions stay behind until a background process, VACUUM, cleans them up. On busy databases that means bloat, wasted disk and tuning. The storage layer is also tied to local disks, which makes separating storage from compute hard.

## The Solution: A drop-in storage engine

[OrioleDB](https://github.com/orioledb/orioledb) is an extension that replaces the heap through Postgres's Table Access Method interface, so a table is created with `using orioledb`. It uses an undo log and copy-on-write checkpoints, which, per its docs, remove the need for vacuuming in most cases. The license is Apache 2.0 or the PostgreSQL license.

One limit: it still [requires a patched Postgres](https://github.com/orioledb/postgres). Supabase says it has no timeline for getting the patches upstream, and that it could be a few major versions away.

### Funding history

Public Funding Rounds: Not publicly available from credible sources.

## Understanding the Acquisition

Supabase says the team will build a faster storage engine, help develop pluggable storage in Postgres, and work on decoupled storage and compute. The announcement gives no price and no timeline for a production release.

## Relevant Products and Companies

- [Supabase](https://supabase.com/): the buyer, and the only managed service offering OrioleDB that I know of.
- [Neon](https://neon.com/): separates storage and compute in Postgres by another route. See my [Neon article]({{ '/blog_posts/acq/015_ACQ_neon_by_databricks.html' | relative_url }}).

## My Take

A nice acquihire of a small deeptech team. Good luck.

---

## Updates

*Late additions, published after the original article and not part of the official announcements.*

### October 2026: OrioleDB public beta

Supabase [launched the OrioleDB public beta](https://supabase.com/blog/orioledb-public-beta) on October 28, 2026. It says OrioleDB is "not ready for production yet", has no point-in-time recovery and no SLA. Its own benchmark shows about 1.8x more transactions per minute than Supabase Postgres on heap storage, on an 8XL instance when data does not fit in memory. It is a vendor figure, and results depend on the workload.
