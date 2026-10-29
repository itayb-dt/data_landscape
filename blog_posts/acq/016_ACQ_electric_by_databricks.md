---
title: "Databricks acquires Electric to give AI agents a local Postgres that syncs with Lakebase"
published: 2026-08-14
---
Electric, the team behind the PGlite embedded Postgres and the Electric sync engine, [is joining Databricks](https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes) (the deal is reported as an [acquisition](https://aimagazine.com/articles/databricks-acquires-electric-to-power-blazing-fast-agents), and the price was not disclosed). The team joins [Neon](https://neon.com/blog/electric-joins-neon), which Databricks bought last year, with a clear goal: [add Electric's "data primitives and reactivity to Lakebase"](https://electric.ax/blog/2026/08/11/electric-joining-databricks), Databricks' serverless Postgres.

<figure class="shot">
  <img src="{{ '/assets/images/electric/hero.jpg' | relative_url }}" alt="Electric and Databricks logos" loading="lazy">
  <figcaption>Electric joins Databricks. Source: <a href="https://electric.ax/blog/2026/08/11/electric-joining-databricks">Electric</a>.</figcaption>
</figure>

## The Problem: Agents work in sandboxes, far from the data they need

A classic application talks to one database server. Agents work differently. According to [Databricks](https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes), they decide what data they need at runtime, run in sandboxed environments, and often work in groups.

Picture three agents handling a customer's refund. One reads the order, one checks the payment, and one drafts the reply. If every read is a round trip to a remote database, each step is slow. If each agent keeps its own copy of the data, the copies drift apart: the reply agent writes "refund approved" while the payment agent still sees the old state.

The same problem exists in collaborative apps. Keeping many clients consistent with a central database is hard: it takes conflict resolution, partial replication of only the rows a client may see, and reconnection logic ([Neon](https://neon.com/blog/electric-joins-neon)). Most teams end up building a fragile sync layer of their own.

## The Solution: Postgres that runs inside the app, plus a sync engine

Electric built two things that fit together:

- **[PGlite](https://pglite.dev/)**: Postgres compiled to WebAssembly, small enough to run inside an application, a browser tab, a user's device or an agent's sandbox. Databricks says it grew [from 1M to 13M weekly downloads in twelve months](https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes). It builds on WASM Postgres work by Stas Kelvich, a co-founder of Neon.
- **A real-time sync engine** (known as [Postgres Sync](https://electric.ax/sync/postgres-sync)): it keeps a subset of a central Postgres database continuously aligned with its clients, so developers do not write their own sync layer.

Together they give each agent a lightweight Postgres right where it runs, with local, low-latency reads, and keep it consistent with a central database. The same architecture powers collaborative apps like Google Docs, Figma and Notion, as Databricks notes.

Two production examples show what this looks like in practice:

- **Trigger.dev**, a platform for running background jobs, [uses Electric to power Trigger.dev Realtime](https://electric.ax/blog/2025/03/17/electricsql-1.0-released). When a user's task runs, the web app shows its status, progress and metadata as they change, [without polling](https://trigger.dev/docs/realtime/overview). CEO Matt Aitken: "We use ElectricSQL to power Trigger.dev Realtime, a core feature of our product."
- **Otto**, a spreadsheet where each cell runs as its own AI agent, uses Electric to stream agent updates to the sheet. Co-founder Sully Omar says it lets them ["reliably stream agent updates to our spreadsheet in real-time"](https://electric.ax/blog/2025/03/17/electricsql-1.0-released).

Both quotes are from Electric's own 1.0 announcement, so they are vendor-sourced.

Electric also maintains [TanStack DB](https://tanstack.com/db) and [Durable Streams](https://durablestreams.com/). Everything Electric has open sourced [stays open source](https://electric.ax/blog/2026/08/11/electric-joining-databricks). Electric Cloud, its hosted service, is shutting down, and its users must self-host or move to another provider.

### Funding history

Public Funding Rounds: Not publicly available from credible sources.

## Understanding the Acquisition

Databricks already owns the central database. It bought Neon and turned it into Lakebase, a [production-scale Postgres](https://www.databricks.com/product/lakebase). Electric adds the other end of the wire: a Postgres on the device or in the agent, and the machinery that connects the two. In Databricks' words, [sync keeps the two consistent](https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes). It is also an easy fit: Neon is Electric's most popular Postgres integration, and it powered most of Electric Cloud's sync services.

The more interesting part is what comes next. Neon says the two teams are [already at work on new backend capabilities](https://neon.com/blog/electric-joins-neon) and wants real-time sync to be a primitive that agents reach for by default, alongside Postgres, Auth, Storage and Functions. Electric says it will take sync [to the next level on Neon](https://electric.ax/blog/2026/08/11/electric-joining-databricks). Neither names a feature, but the direction points to live queries inside Lakebase: you subscribe to a SQL query, and its result stays current as the data changes, with no polling and no hand-built sync code.

This is important because agents depend on fresh context. An agent that answers from a stale copy gives a wrong answer with confidence, and a team of agents needs a shared, current view of the state they are changing.

It is also hard to build, and my reading is that these are the hard parts:

- **Arbitrary SQL.** Re-running a query on every change does not scale. The engine has to work out which live queries a write affects and update only those results, including joins and aggregates.
- **Consistency.** A client must never see half of a transaction. Updates have to arrive in commit order, and a writer must be able to tell when its own write has come back.
- **Who can see what.** Each client should receive only the rows it is allowed to see, so permissions have to be part of the design.
- **Cost and scale to zero.** Thousands of open subscriptions should not keep a database awake. That goes against Neon's pitch of cheap databases that sleep when idle.

Electric spent years on the sync side of this. Neon has the storage and branching side. The acquisition puts both teams in one building. For customers, the open source projects continue, but the hosted Electric Cloud does not, so users of it face a migration.

## Relevant Products and Companies

- [PGlite](https://pglite.dev/): the embeddable WASM Postgres at the center of the deal.
- [TanStack DB](https://tanstack.com/db): a client-side database layer maintained by Electric, used for local state that syncs with a backend.
- [Durable Streams](https://durablestreams.com/): an open source streaming protocol from Electric, for sending data to clients reliably.

## My Take

Data is complicated, and agents make it more complicated. An agent starts a conversation, goes for lunch and is back an hour later, and in the meantime its context and the data it works on must still be there and still be right. That is a different problem from where the data is stored, and nobody has solved it for the many places data now lives.

I read this acquisition as Databricks' answer to the agent side of that problem. Postgres is the starting point again: PGlite puts a real Postgres next to each agent, Lakebase holds the shared source of truth, and sync keeps them aligned. The part I find most interesting is not the local database. It is what Neon and Electric say they will build together, a real-time primitive inside the database. I expect that to be live queries: you subscribe to any SQL query and the result stays current as the data changes, without polling and without a sync layer you build yourself. It is the next reasonable step after branching, because an agent that can copy a database for context also needs to see it change.

It will be hard to get right, which is why this team was worth buying. Anyone can demo live data. Doing it for arbitrary SQL, with consistency, permissions and a bill that does not grow while the database sleeps is the real work. If they manage it on top of scale to zero, Neon becomes more than a cheap Postgres, and that is the story that justified the price of the Neon deal in the first place.

## Updates

*These entries were added after the original article. They are not part of the announcements.*

### Oct 15, 2026: Neon Realtime brings live queries to Lakebase Postgres

The feature the acquisition pointed to has shipped as a public beta, which is the direction described in My Take. [Neon Realtime](https://neon.com/blog/neon-now-has-realtime), written by Electric co-founder James Arthur, now at Databricks, puts it simply: "Any SQL query can now be a live query."

<figure class="shot">
  <img src="{{ '/assets/images/electric/neon-realtime.jpg' | relative_url }}" alt="Neon now has realtime: cover art with a live row counter" loading="lazy">
  <figcaption>Neon's announcement of Realtime. Source: <a href="https://neon.com/blog/neon-now-has-realtime">Neon</a>.</figcaption>
</figure>

- **What it does.** Any read-only, deterministic SQL query can be subscribed to, including joins, aggregates, window functions and subqueries. The result updates as the underlying data changes. Clients use the CLI, an SDK, or a React hook (`useLiveQuery`), and writes can be applied optimistically through [TanStack DB](https://neon.com/docs/realtime/guides/mutations).
- **How it works.** Enabling Realtime [installs an incremental live query engine inside Lakebase Postgres](https://neon.com/docs/realtime/how-it-works). It consumes logical replication, matches each write to the live queries it affects, and streams only the changes. A subscription starts with the full result, then changes arrive in batches, one per committed transaction, so a client never sees a partial write. Each batch carries transaction IDs, which lets `awaitTxId()` confirm that a write has synced.
- **Scale to zero and branching.** Clients connect to Neon's ingress layer, not to Postgres, so [open subscriptions don't keep the database awake](https://neon.com/blog/neon-now-has-realtime). Realtime is enabled per branch and child branches inherit it.
- **Security.** Queries are defined on the backend and sealed, so a client cannot forge or change them. Row-level security is not supported yet.
- **Replaces Electric's shapes.** The docs describe live SQL queries as [a drop-in replacement for Electric's role](https://neon.com/docs/realtime/overview), where shapes were used before.

The live-query pattern behind Trigger.dev and Otto, a database change reaching the browser at once, is now a feature of the database itself. I found no named Neon Realtime customers yet, which is normal for a beta. Existing Electric users such as Trigger.dev run on Electric's own engine.

It is free during the beta, though compute and egress are billed. It runs in four AWS regions, the protocol is still changing, and no benchmarks are published. It works on Neon, not yet on Lakebase inside Databricks.

The earlier [interview with James Arthur](https://neon.com/blog/electrifying-neon-building-the-realtime-backend) (Sep 24, 2026) explains why this took a dedicated team: "The thing about realtime is it demos well but tends to fall over in production," and there is "a fundamental tension between expressiveness and performance." That matches the list of hard parts above. Neon's [backend GA post](https://neon.com/blog/neon-backend-is-ga) listed realtime as the next primitive.

<figure class="shot">
  <img src="{{ '/assets/images/electric/electrifying-neon.jpg' | relative_url }}" alt="Electrifying Neon: building the realtime backend" loading="lazy">
  <figcaption>The interview with Electric co-founder James Arthur (Sep 24, 2026). Source: <a href="https://neon.com/blog/electrifying-neon-building-the-realtime-backend">Neon</a>.</figcaption>
</figure>
