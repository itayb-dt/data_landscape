---
title: "LanceDB raises $57.5M to build a data platform for multimodal AI"
published: 2026-11-18
---
# LanceDB Raises $57.5M to Build a Data Platform for Multimodal AI

<figure class="shot">
  <img src="{{ '/assets/images/lancedb/hero.png' | relative_url }}" alt="LanceDB: AI-Native Multimodal Lakehouse" loading="lazy">
  <figcaption>The LanceDB banner. Source: <a href="https://www.lancedb.com/">LanceDB</a>.</figcaption>
</figure>

## Technical Overview

- Startup: LanceDB ([lancedb.com](https://www.lancedb.com/)), a Y Combinator company
- Amount Raised: $57.5M
- Funding Round: Series B, [announced November 17, 2026](https://www.lancedb.com/blog/lancedb-series-b-funding)
- Main Investors: Bessemer Venture Partners and Innovation Endeavors (co-leads), with Theory Ventures, Dimension, Swift Ventures, CRV and Y Combinator
- Problem Area: Storing, searching and training on images, video and other unstructured data for AI

---

## The Problem

The data stack that most companies use was built for tables: rows of customers, orders and events. AI research works on something else. A model that generates video, understands images or drives a car is trained on files such as video, pictures, audio and text, together with the embeddings (lists of numbers that describe their meaning) and the labels that go with them.

LanceDB's headline for the round says it directly: "AI research has outgrown the modern data stack." Imagine a team that trains an image model. The raw images sit in cloud storage, the descriptions in a table, the embeddings in a separate vector database, and the training job needs all of them in one stream. Every step in between is a pipeline that somebody has to build, and every copy of the data is another thing to keep in sync and pay for.

---

## How They Solve It

LanceDB is built on **Lance**, an open source file and table format for this kind of data. It is a columnar format, designed so that large and mixed data can be read quickly from cloud object storage, searched and updated without rewriting everything.

On top of the format, LanceDB sells what it calls a **multimodal lakehouse**: one place where the same table can be used for four jobs, according to its site:

- **Search:** vector, full-text and hybrid search with filters, over the same table.
- **Curation:** finding and selecting the right data in a very large collection.
- **Feature engineering:** adding new columns, such as embeddings or labels, without rewriting the table.
- **Training:** reading data straight from storage into the training job, with versioning so a model can be tied to the exact data it learned from.

The open source library is free, and LanceDB makes money from managed versions: LanceDB Cloud and LanceDB Enterprise. With the round, the company says it is adding to Enterprise a durable, memory-accelerated write path for real-time ingest, distributed indexing and managed compaction.

Customers named by the company in the announcement are Netflix, Microsoft AI, Runway, Luma AI and Midjourney. LanceDB also says that revenue has grown by more than ten times in a year since its Series A, without giving the base, so it is a growth claim and not a size.

---

## Competitive Landscape

LanceDB began as a vector database, and in that role a main competitor is **Pinecone**, a managed vector database. On its comparison page, LanceDB describes itself as "the end-to-end data layer for multimodal AI" and Pinecone as "a fully managed vector database". The difference it claims is scope: Pinecone does retrieval for AI applications as a proprietary managed service, while LanceDB covers retrieval together with curation, feature engineering and training, and has an open source core. That page is LanceDB's own marketing.

So the overlap with Pinecone is real but partial. For search over embeddings the two compete directly. For preparing and training on multimodal data, LanceDB is aiming at a job that a pure vector database does not do.

---

## Previous Rounds and Capital Trajectory

- Seed - May 2024 - $8M, led by CRV, Essence VC and Swift Ventures, with Y Combinator backing - [TechCrunch](https://techcrunch.com/2024/05/15/lancedb-which-counts-midjourney-as-a-customer-is-building-databases-for-multimodal-ai)
- Series A - June 2025 - $30M, led by Theory Ventures, with CRV, Y Combinator, Databricks Ventures and Runway - [LanceDB](https://www.lancedb.com/blog/series-a-funding)
- Series B - Nov 2026 - $57.5M, co-led by Bessemer Venture Partners and Innovation Endeavors - [LanceDB](https://www.lancedb.com/blog/lancedb-series-b-funding)

LanceDB says total funding to date is $98.5M. The valuation was not disclosed. The company says the money will go toward supporting AI research teams across the full flywheel for improving a model, from data to training.

---

## Why This Round Matters

LanceDB started as a vector database for developers, a crowded category, and this round funds a different bet: that the real money is in the data platform behind model training. Named customers such as Runway, Midjourney and Netflix suggest that frontier AI teams are already building on Lance, and that the open source format is how the company reaches them. The question for the category is whether vector search stays a product of its own, as Pinecone sells it, or becomes one feature of a platform for AI data. A Series B of this size says investors are betting on the platform.
