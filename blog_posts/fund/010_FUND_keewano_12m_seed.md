---
title: "Keewano raises $12M seed to build a platform for AI agent memory"
---
# Keewano Raises $12M Seed to Build a Platform for AI Agent Memory

## Technical Overview

- Startup: Keewano (keewano.com)
- Amount Raised: $12M
- Funding Round: Seed
- Main Investors: Hetz Ventures (lead), a16z speedrun, Remagine Ventures, DIG Ventures, and angel investors
- Problem Area: Event history storage and retrieval for AI agents

---

## The Problem

AI agents need context. When an agent investigates why a customer churned, why a transaction looks suspicious, or why a device started failing, the answer lives in the sequence of events that led there — not in a pre-aggregated metric.

Traditional databases were not built to serve that sequence. A data warehouse stores current state or pre-computed aggregates. To answer "what happened before this customer cancelled?", a team must reconstruct the timeline from separate tables, time-ordered joins, and window functions — queries they had to design in advance. If nobody thought to model that question, the answer is weeks of engineering away.

The cost of serving raw sequences to agents is the other half of the problem. Pulling a user's full event history from a warehouse, serializing it, and stuffing it into a prompt context is slow, expensive in tokens, and breaks down quickly at scale. A user with 10,000 events can generate a 50,000-token context window — most of it noise — before the agent can ask a single question.

---

## How They Solve It

Keewano built KeewanoDB, a platform that organizes data around **entities** and their **event histories** rather than tables and rows. Every entity — a user, a device, an AI agent run — owns a chronological sequence of events that is stored in order and never aggregated away.

A concrete example from their documentation:

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

That full sequence is what the platform stores. When an agent asks "why did this customer cancel?", it does not join five tables — it reads `customer_123`'s complete story and reasons over it directly. The sequence itself is the answer. Patterns that no dashboard was designed to catch — like the gap between "purchased" and "contacted_support" — become visible without any upfront modeling.

Key capabilities:
- **In-platform compute via MCP**: agents query the data inside the platform using the Model Context Protocol; only the result, not the raw events, travels to the model
- **84% fewer LLM tokens** claimed in production compared to pulling raw rows into context
- **Quarter-billion-event scans in under half a second**
- **Schemaless ingestion**: new event types append without schema migrations
- Ingests from Kafka, Postgres, Snowflake, BigQuery, and Parquet

---

## Competitive Landscape

There is no direct drop-in competitor for what Keewano is doing. Teams currently approximate the same outcome by combining a data warehouse for historical events, a stream processor for freshness, and a vector database for semantic retrieval. Keewano's pitch is that the combination is the problem — and a purpose-built platform eliminates it.

Indirect competitors:

- **Amplitude / Mixpanel** — behavioral analytics platforms that store user events but pre-aggregate them into funnels and cohorts. Answer predefined questions fast; cannot serve arbitrary agent queries over raw sequences.
- **Apache Pinot / Druid** — real-time OLAP engines, aggregation-first and not designed for per-entity sequence reasoning.
- **InfluxDB / TimescaleDB** — time-series databases where time is the primary axis, not the entity. Not built for "tell me the full story of entity X."

---

## Previous Rounds and Capital Trajectory

This is Keewano's first disclosed round. The $12M seed is a meaningful size for an infrastructure company at launch — enough to fund a full engineering team and initial go-to-market without needing to raise again in the near term. The a16z speedrun participation is notable: that program moves fast and bets on category-defining infrastructure plays.

---

## Founder Background

CTO Pavel Bibergal previously ran data infrastructure at Plarium, a large cross-platform gaming company. Gaming generates some of the densest per-entity event streams anywhere — millions of players, thousands of events per session, years of behavioral history. Bibergal's team started building with agents and LLMs roughly two years ago, hit the same wall everyone hits (too many tokens, too much latency, too little context), and built KeewanoDB to solve it. That is a credible origin story: the product came from the problem, not the other way around.

---

## Why This Round Matters

AI agents are moving from demos to production, and production agents need memory — durable, queryable, cost-efficient memory at scale. The current answer is stitched-together pipelines. Keewano is betting there is a platform category to be won here before the warehouses and vector stores expand to absorb the problem.

A $12M seed with a16z speedrun on the cap table gives them the runway and the credibility to land early enterprise customers. Whether the category is real — or whether ClickHouse with good schema design turns out to be "good enough" — is the question the next 18 months will answer.
