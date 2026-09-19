# DB: KeewanoDB — A Database Built Around Entity Histories, Not Tables

## Opening Context

[KeewanoDB](https://www.keewano.com/) launched on September 15, 2026 — literally days ago — positioning itself as "the first database built for machine reasoning at scale." It raised a $12M seed round led by Hetz Ventures with participation from a16z speedrun, Remagine Ventures, and DIG Ventures.

The founders came out of the gaming industry. Keewano's CTO Pavel Bibergal previously ran data infrastructure for Plarium, a cross-platform gaming company, where a single player can generate thousands of events across years of sessions. That origin matters — it shaped every design decision in this database.

Official docs: [docs.keewano.com](https://docs.keewano.com/)

---

## What Is KeewanoDB?

KeewanoDB is an **event series database** — a category it is largely inventing for itself. It is not a time-series database, not an event streaming platform, and not a data warehouse. The distinction is in how data is organized: instead of tables and rows, everything is organized around **entities** and their **event histories**.

The fundamental unit is an **event**: an atomic action attached to a specific entity, stored in the order it happened. Events do not update previous state — they append to the history. Here is an example directly from their documentation:

```
Entity: customer_123

  signed_up
  searched
  viewed_product
  added_to_cart
  left
  returned
  purchased
  contacted_support
  cancelled
```

That sequence is what the database stores — all of it, in order. When an agent asks "why did this customer cancel?", it reads `customer_123`'s full story and reasons over it directly, rather than joining five tables and aggregating across cohorts. The sequence itself is the answer.

Core architectural properties:

- **Entity-centric storage**: every entity (user, device, agent) owns a chronological sequence of events — think of it as each entity getting its own timeline
- **No cross-entity joins**: queries operate within a single entity's history; the engine is not designed for joins across entities
- **4-byte event encoding**: compact on-disk format built for sequential reads, not random access
- **Semantic layer at ingestion**: LLMs enrich events with contextual labels as they arrive, persisting all historical states rather than overwriting them
- **In-database compute**: scripts run inside the database via MCP (Model Context Protocol), so agents query without moving data out
- **Schemaless ingestion**: new event types can be added without schema migrations

---

## What Problems Does It Solve?

**Traditional databases destroy event context.** A standard data warehouse stores current state or pre-computed aggregates. If you want to know the sequence of events that preceded a churn, a fraud event, or a device failure, you reconstruct it from separate tables, time-ordered joins, and window functions. That reconstruction is slow to build, expensive to maintain, and answers only the questions you thought to ask in advance.

**AI agents are expensive to feed raw data.** When an agent needs context about a user, the typical approach is to pull rows from a warehouse, serialize them, and stuff them into a prompt. A user with 10,000 events might generate a 50,000-token context window — most of which is noise. KeewanoDB claims up to 84% fewer tokens by processing at the data layer: the agent asks a question, the database computes the relevant summary, and only the answer travels to the model.

**Agents need to answer questions nobody anticipated.** Pre-built dashboards and aggregates work when you know the question ahead of time. Agents exploring why something happened need to follow a trail — and that trail is the event sequence. KeewanoDB stores data in a format where unanticipated questions are first-class, not afterthoughts.

---

## What It Is Best For

**AI agent memory and reasoning over behavioral histories**: An agent investigating a churned customer, a suspicious transaction, or a failing device needs the full event sequence for that entity. KeewanoDB is built exactly for this retrieval pattern.

**Behavioral analysis without pre-modeling**: Finding users who match a behavioral pattern (the "lookalike" query), identifying sequences that precede an outcome (churn, purchase, default), and comparing before/after behavior around a specific event — all without knowing those questions ahead of time.

**Gaming, fintech, and IoT where entities generate dense event streams**: A player generating 500 events per session, a bank account with years of transactions, a sensor emitting state changes every second — these are the workloads the founders designed for.

**Reducing LLM context costs in production AI systems**: If you are building agents that query user behavior at scale and hitting token budget limits, KeewanoDB's in-database processing model is directly targeting your problem.

---

## What It Is Not Good For

**Cross-entity aggregations and analytics**: "What is the average purchase value across all customers this month?" is not what this database is for. That is a warehouse query. KeewanoDB is optimized for deep, per-entity reasoning — not wide aggregations across the full dataset.

**Transactional workloads**: No ACID transactions, no primary-key updates, no "current state" model. If your application reads and writes the same record many times, this is the wrong tool.

**Teams that do not have AI agents in the architecture**: The MCP integration, the LLM semantic layer, and the token-efficiency story only matter if agents are actually querying the data. If your primary consumers are humans using dashboards, a standard analytical database will serve you better.

**Replacing your warehouse**: KeewanoDB ingests from Kafka, Postgres, Snowflake, and BigQuery. It sits alongside your warehouse, not instead of it.

---

## Competitive Landscape

**[Apache Kafka + ksqlDB](https://ksqldb.io/)** — handles event streaming and stream-time queries well, but designed for stream processing pipelines, not retrospective entity-history analysis. No entity-centric model, no agent interface.

**[Amplitude](https://amplitude.com/) / [Mixpanel](https://mixpanel.com/)** — product analytics platforms that store user events but pre-aggregate them into funnels and cohorts. Answer predefined questions fast; cannot serve arbitrary agent queries over raw sequences.

**[Apache Pinot](https://pinot.apache.org/) / [Apache Druid](https://druid.apache.org/)** — real-time OLAP engines. Strong at aggregation queries over event data, weak at per-entity sequence reasoning and native agent integration.

**[TimescaleDB](https://www.timescale.com/) / [InfluxDB](https://www.influxdata.com/)** — time-series databases. Time is the primary axis, not the entity. Efficient for sensor data aggregations; not built for "tell me the story of entity X."

**[Rockset](../acq/008_ACQ_rockset_by_openai.md)** (acquired, shut down) — the closest prior comparison. Rockset unified real-time ingestion + SQL + search; KeewanoDB narrows the focus specifically to entity event histories and agent-first querying. Different angle on a similar gap.

---

## My Take

I am still working through this one. The category claim is bold — "first database for machine reasoning at scale" is the kind of line that ages poorly if the product does not deliver. But the problem they are solving is real and genuinely underserved.

The entity-centric model is interesting. The insight that sequences are destroyed by aggregation, and that agents need sequences not summaries, is correct. Whether that insight requires a new database or whether it is something ClickHouse + good schema design could approximate is the question I cannot answer yet.

The gaming origin story gives me confidence they are solving a real engineering problem, not a whiteboard one. The 84% token reduction claim needs scrutiny — but if it holds, that is not a feature, that is a cost structure change for AI-native applications.

What I will be watching: whether the "no cross-entity joins" constraint turns out to be a principled design decision or a limitation that becomes painful in production. And whether they can show me a named customer in six months.

Verdict pending.

---

## Further Reading

- [KeewanoDB overview](https://www.keewano.com/overview)
- [KeewanoDB documentation](https://docs.keewano.com/)
- [Launch coverage — SiliconANGLE](https://siliconangle.com/2026/09/15/startup-keewano-launches-agent-focused-database-and-pulls-in-12m-in-funding/)
- [VentureBeat — data model deep dive](https://venturebeat.com/data/every-user-device-and-agent-gets-its-own-table-in-keewanodb-and-queries-never-join-across-them)
- [Funding announcement — PR Newswire](https://www.prnewswire.com/il/news-releases/keewano-raises-12m-and-launches-keewanodb-the-first-database-built-for-machine-reasoning-at-scale-302878769.html)
