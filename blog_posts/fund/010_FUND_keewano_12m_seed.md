# Keewano Raises $12M Seed to Build a Database for AI Agent Memory

## Technical Overview

- Startup: Keewano (keewano.com)
- Amount Raised: $12M
- Funding Round: Seed
- Main Investors: Hetz Ventures (lead), a16z speedrun, Remagine Ventures, DIG Ventures, and angel investors
- Problem Area: Event history storage and retrieval for AI agents

---

## The Problem

AI agents need context. When an agent investigates why a customer churned, why a transaction looks suspicious, or why a device started failing, the answer lives in the sequence of events that led there — not in a pre-aggregated metric.

The problem is that traditional databases were not built to serve that sequence cheaply or quickly. Getting an agent full event context from a warehouse typically means pulling large volumes of raw rows, serializing them, and pushing them into a prompt. That is slow, expensive in tokens, and scales poorly across millions of entities and thousands of concurrent agent queries.

---

## How They Solve It

Keewano built KeewanoDB, an event series database organized around entities rather than tables. Every user, device, or AI agent gets its own chronological event history — stored in order, never aggregated away. When an agent needs to reason about an entity, it queries the sequence directly inside the database, and only the result travels to the model.

The company claims up to 84% fewer LLM tokens compared to pulling raw data into context, and quarter-billion-event scans in under half a second. The database exposes a native MCP interface so agents can query it without external data pipelines.

---

## Competitive Landscape

There is no direct drop-in competitor in the event series category. Teams currently approximate the same outcome by combining a data warehouse for historical events, a stream processor for freshness, and a vector database for semantic retrieval. Keewano's pitch is that the combination is the problem — and a purpose-built engine eliminates it.

Indirect competitors include Amplitude and Mixpanel for behavioral analytics (pre-aggregated, not agent-queryable), Apache Pinot and Druid for real-time OLAP (aggregation-first, not sequence-first), and time-series databases like InfluxDB and TimescaleDB (time-centric, not entity-centric).

---

## Previous Rounds and Capital Trajectory

This is Keewano's first disclosed round. The $12M seed is a meaningful size for a database infrastructure company at launch — enough to fund a full engineering team and initial go-to-market without needing to raise again in the near term. The a16z speedrun participation is notable: that program typically moves fast and bets on category-defining infrastructure.

---

## Founder Background

CTO Pavel Bibergal previously ran data infrastructure at Plarium, a large cross-platform gaming company. The gaming industry generates some of the densest per-user event streams anywhere — millions of players, thousands of events per session, years of history. That operational background is a credible foundation for a database built around exactly that workload.

---

## Why This Round Matters

The timing is deliberate. AI agents are moving from demos to production, and production agents need memory — durable, queryable, cost-efficient memory. The current answer is stitched-together pipelines. Keewano is betting there is a database category to be won here before the warehouses and vector stores expand to absorb the problem.

A $12M seed with a16z speedrun on the cap table gives them the credibility to land early enterprise customers. Whether the category is real — or whether ClickHouse with good schema design turns out to be "good enough" — is the question the next 18 months will answer.

For a deeper look at what KeewanoDB actually does, see our [full DB review](../db/009_DB_keewanodb_event_series.md).
