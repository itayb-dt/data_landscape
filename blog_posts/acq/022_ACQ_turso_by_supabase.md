---
title: "Supabase acquires Turso to give every AI agent its own database"
published: 2026-11-02
---
Supabase [announced on October 2, 2026](https://supabase.com/blog/supabase-is-acquiring-turso) that it is acquiring Turso, the company behind an open source rewrite of SQLite. The price was not disclosed. Press coverage says the deal came with a [$150M funding round](https://pulse2.com/supabase-raises-150-million-and-acquires-turso/), which I did not find in Supabase's own post. Glauber Costa, Turso's founder, joins Supabase as Head of Agentic Services, with co-founder Pekka Enberg and the rest of the team.

<figure class="shot">
  <img src="{{ '/assets/images/turso/hero.png' | relative_url }}" alt="Turso is joining Supabase" loading="lazy">
  <figcaption>Turso is joining Supabase. Source: <a href="https://turso.tech/blog/turso-is-joining-supabase">Turso</a>.</figcaption>
</figure>

## The Problem: AI agents need many small databases, and servers are built for a few large ones

A typical database server is sized and operated as a long-lived system. One Postgres instance serves one application, with a connection pool, backups and a person who knows how it was set up.

Agents work differently. A coding agent that builds an app for a user needs a place to keep that app's data. An assistant that remembers each customer needs state per customer. Multiply that by thousands of users and you need thousands, or millions, of isolated databases, created in seconds and mostly idle. Supabase says it is already [launching over one million databases per week](https://supabase.com/blog/supabase-is-acquiring-turso).

Take a platform where users generate small apps by prompt. Each app needs its own tables and its own isolation so one customer's data never leaks into another's. Provisioning a full database server for each one is slow and expensive, and sharing one database among all of them puts the isolation on the application developer.

## The Solution: SQLite, rebuilt in Rust, in a form that runs embedded or in the cloud

[Turso](https://turso.tech/) has three parts, and the names are easy to mix up:

- **[Turso Database](https://github.com/tursodatabase/turso)**: an in-process SQL database compatible with SQLite, written in Rust and licensed under MIT. Its README lists a Postgres frontend too, and marks some features as experimental, including Postgres compatibility, encryption at rest and full-text search. Turso's FAQ says it has not reached 1.0.
- **libSQL**: Turso's earlier fork of SQLite. Turso's FAQ says the Rust rewrite "replaces libSQL as our intended direction", though libSQL has been in use for longer.
- **Turso Cloud**: the hosted platform, [designed for](https://turso.tech/) database-per-user, database-per-agent and database-per-tenant setups. Turso says it is built on a diskless, WAL-on-S3 architecture and also offers bring-your-own-cloud.

The product claims, per Turso's homepage, include concurrent writes (MVCC), full-text search, vector search, local-first sync with explicit push and pull, and a design for millions of lightweight databases. Named users include Superhuman, Sauna.ai and Mastra.

The benefit goes to developers building agents or multi-tenant products who want a database to be as cheap and quick to create as a file.

### Funding history

Public Funding Rounds: Not publicly available from credible sources.

## Understanding the Acquisition

Supabase is a Postgres platform. Turso is SQLite. The two posts say so plainly: [Supabase will keep building around Postgres, and Turso will keep working on SQLite](https://supabase.com/blog/supabase-is-acquiring-turso). What Supabase wants is the ability to ["provision a database for each agent on demand"](https://supabase.com/blog/supabase-is-acquiring-turso), on Turso Cloud or in the customer's own cloud.

The path is also described in Turso's announcement, which promises a ["clear graduation path"](https://turso.tech/blog/turso-is-joining-supabase): start with a lightweight database per agent, move to standard Postgres through Supabase as the workload grows, and eventually reach petabyte scale with Multigres. Multigres is Supabase's project for scaling Postgres, which I have not covered here. Turso also says to expect deeper integration between the two in the coming months.

For existing users, both companies say nothing changes. Turso Cloud keeps running and Turso Database stays open source and actively developed. Neither post says anything about pricing or contracts, and I found no customer terms to report. Turso's own roadmap is a point to watch: the Rust engine is pre-1.0, so the team joins with significant engineering still ahead of it.

## Relevant Products and Companies

- [Supabase](https://supabase.com/): the open source Postgres platform that is the buyer.
- [Turso](https://turso.tech/): the SQLite-compatible database and its cloud, the target.
- [Neon](https://neon.com/): serverless Postgres bought by Databricks, another Postgres-for-developers deal. See my [Neon article]({{ '/blog_posts/acq/015_ACQ_neon_by_databricks.html' | relative_url }}).
- [SQLite](https://sqlite.org/): the embedded database all of this builds on.

## My Take

Another step in making Supabase a great platform for developers. Supabase started with Postgres, auth and storage in one place, and it keeps adding the pieces a developer needs to build an application without assembling them. Turso adds a piece that agents need: a database that is quick and cheap enough to create for each user or agent.
