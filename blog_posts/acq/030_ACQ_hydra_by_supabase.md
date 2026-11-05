---
title: "Supabase brings in the Hydra team, maintainers of pg_duckdb"
published: 2026-02-13
---
Supabase [announced on February 10, 2026](https://supabase.com/blog/hydra-joins-supabase) that "the Hydra team" is joining it. Hydra is a small Y Combinator startup (Winter 2022) and a co-developer of [pg_duckdb](https://github.com/duckdb/pg_duckdb), an MIT-licensed extension that runs DuckDB analytics inside Postgres. Supabase's post never uses the word "acquisition", and no price or terms were given. [Crunchbase](https://www.crunchbase.com/organization/supabase/company_overview/overview_timeline) lists it as one.

<figure class="shot">
  <img src="{{ '/assets/images/hydra/hero.png' | relative_url }}" alt="Supabase Warehouse: Joseph Sciarrino joins Supabase, with the Hydra and DuckDB logos" loading="lazy">
  <figcaption>Supabase Warehouse: Joseph Sciarrino joins Supabase. Source: <a href="https://supabase.com/blog/hydra-joins-supabase">Supabase</a>.</figcaption>
</figure>

## The Problem: Postgres is a row store

Analytical queries scan many rows but touch few columns, which is what column stores are built for. Postgres's native storage is row-oriented. Hydra started with an open-source column-oriented Postgres, then moved to pg_duckdb.

## The Solution: Analytics that stay inside Postgres

Supabase's post shows pg_duckdb running an analytics query on Parquet files about 447x to 658x faster than plain PostgreSQL, depending on the machine. It is a vendor chart, and the query and data are not described in the post.

<figure class="shot">
  <img src="{{ '/assets/images/hydra/benchmark.png' | relative_url }}" alt="Benchmark chart: pg_duckdb on Parquet is about 447x to 658x faster than PostgreSQL" loading="lazy">
  <figcaption>Relative query time, pg_duckdb vs PostgreSQL. Vendor benchmark. Source: <a href="https://supabase.com/blog/hydra-joins-supabase">Supabase</a>.</figcaption>
</figure>

Supabase says Joe Sciarrino, Hydra's co-creator, will "build Supabase Warehouse: an open data warehouse architecture for developers", keeping Postgres at the center. It lists tighter Postgres and object storage integration, serverless analytics workflows, and a base for open table formats. Supabase will also take over maintenance of Hydra's repositories, help [MotherDuck](https://motherduck.com/) with pg_duckdb, and says everything stays open source.

<figure class="shot">
  <img src="{{ '/assets/images/hydra/open-warehouse-architecture.png' | relative_url }}" alt="Open Warehouse Architecture: Postgres synced with Iceberg, between transactional workloads and analytical tools" loading="lazy">
  <figcaption>Supabase's Open Warehouse Architecture: Postgres kept in sync with Iceberg. Source: <a href="https://supabase.com/blog/hydra-joins-supabase">Supabase</a>.</figcaption>
</figure>

### Funding history

Reported: about $3.1M in seed funding, roughly $3.6M in total, per aggregator sites. I could not confirm it from a primary source.

## Understanding the Acquisition

This looks more like an acqui-hire than a company purchase. The post names one person, Joe, and says the team is "joining". It does not say whether the Hydra company itself was bought, or what happens to its product and customers. That is my reading, not something either side has stated.

## Relevant Products and Companies

- [Supabase](https://supabase.com/): the buyer. It also took in the [Oriole team]({{ '/blog_posts/acq/029_ACQ_oriole_by_supabase.html' | relative_url }}) for storage work.
- [MotherDuck](https://motherduck.com/): the DuckDB company that also contributes to pg_duckdb.

## My Take

Great technology. There is a real need for a column store in Postgres. But I don't think it justifies a startup: a Postgres extension is a feature, and it is hard to build a standalone business on one. Joining a platform that can ship it to millions of developers seems a sensible outcome, and I wish the team well.

---

## Updates

*Late additions, published after the original article and not part of the official announcements.*

### November 2026: AWS still has no columnar extension

As of November 5, 2026, Amazon RDS for PostgreSQL does not offer a columnar extension: none is on AWS's [list of supported extensions](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-extensions.html), and neither is pg_duckdb. Aurora PostgreSQL's list doesn't have one either.
