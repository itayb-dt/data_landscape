---
title: "Dremio acquired by SAP"
show_title: true
---
## Opening Context

On May 4, 2026, [SAP](https://www.sap.com/) announced that it has agreed to acquire [Dremio](https://www.dremio.com/) in a move aimed at unifying SAP and non-SAP data for analytics and agentic AI. The official announcement, [SAP to Acquire Dremio to Unify SAP and Non-SAP Data to Power Agentic AI](https://news.sap.com/2026/05/sap-to-acquire-dremio-unify-sap-and-non-sap-data-power-agentic-ai/), makes the strategic intent unusually clear: this is not just a product tuck-in, it is infrastructure for SAP's broader data and AI stack. The exact terms of the transaction were not disclosed, and SAP said the deal is expected to close in Q3 2026, subject to regulatory approvals.

- Estimated Deal Amount: Unknown (terms were not disclosed in the official SAP announcement).

## The Problem: Unified Data for Agentic AI

Most enterprise AI projects do not fail because the models are weak. They fail because the data is fragmented across operational systems, analytics platforms, data lakes, SaaS tools, and custom pipelines. Across the market, teams repeatedly run into the same pattern: data remains locked in incompatible formats, disconnected across systems, and stripped of the business context needed to make outputs trustworthy.

That problem gets harder when the goal shifts from dashboards to agents. A dashboard can tolerate some manual stitching and delayed refreshes. An agent cannot. If an agent is expected to answer questions, trigger workflows, or recommend actions, it needs fast access to both transactional context and broader enterprise data. It also needs a consistent understanding of meaning: what counts as revenue, which hierarchy is authoritative, who has access to what, and how data lineage should be interpreted.

A simple example is enough to show the challenge. Imagine an operations leader asking an AI system which suppliers are causing the highest margin risk this quarter. Part of that answer may live in ERP and finance systems. Another part may sit in a cloud warehouse, a support platform, or raw operational logs. If those sources have to be copied, remapped, and normalized before every serious question, the system becomes slow, brittle, and expensive. If they are not governed under a shared semantic model, the answer may be fast but wrong.

This is the core acquisition thesis: agentic AI needs a data layer that can work across heterogeneous enterprise systems without forcing everything through endless ETL and format conversion.

## About Dremio

[Dremio](https://www.dremio.com/) describes itself as an [Agentic Lakehouse](https://www.dremio.com/) built for agents and managed by agents. That positioning can sound like standard AI-era marketing until you look at the underlying product choices. The company has spent years building around open formats and high-performance query access rather than closed storage and migration-heavy architectures.

Based on Dremio's official product and company materials, the platform combines a few core capabilities.

First, Dremio is strongly aligned with open lakehouse standards, especially Apache Iceberg, and highlights its contributions to projects such as Apache Arrow and Apache Polaris. This matters for teams that want interoperability across engines and tools rather than lock-in to a single execution stack.

Second, Dremio focuses heavily on federation. Its [federated query capabilities](https://www.dremio.com/platform/sql-query-engine/federation/) are designed to query across multiple sources without requiring full data movement. For enterprise teams, that reduces the overhead of pipeline-heavy architectures and can shorten time-to-insight.

Third, Dremio positions its [AI Semantic Layer](https://www.dremio.com/ai-semantic-layer/) and [open catalog](https://www.dremio.com/platform/enterprise-data-catalog/) as a way to enforce shared business meaning, governance, and lineage across diverse data environments. That semantic consistency is increasingly important when analytics and AI systems are expected to produce auditable, business-aware outputs.

Finally, Dremio emphasizes operational automation and elasticity in its lakehouse architecture, including autonomous optimization patterns and managed service operation. In practical terms, that positioning targets two persistent pain points in data platforms: unpredictable performance and high operational burden.

### Public Funding Rounds

Series C - Mar 26, 2020 - $70M - [https://www.dremio.com/blog/announcing-our-series-c-fundraise/](https://www.dremio.com/blog/announcing-our-series-c-fundraise/)

Series D - Jan 8, 2021 - $135M - [https://www.dremio.com/blog/dremio-135m-series-d/](https://www.dremio.com/blog/dremio-135m-series-d/)

Series E - Jan 25, 2022 - $160M - [https://www.dremio.com/blog/dremios-2b-valuation/](https://www.dremio.com/blog/dremios-2b-valuation/)

## Understanding the Acquisition

The strategic logic is straightforward. SAP already owns a huge share of the world's business-critical operational data, but customers do not run their businesses on SAP data alone. They also depend on cloud warehouses, lakehouses, third-party SaaS platforms, industry systems, and bespoke internal applications. If SAP wants [SAP Business Data Cloud](https://news.sap.com/tags/sap-business-data-cloud-2/) to become the control plane for enterprise analytics and agentic workflows, it has to meet that heterogeneous reality directly.

That is why the Dremio acquisition matters. SAP is not just buying faster query performance. It is buying an architecture for open data access. In the official release, SAP says Dremio will complement SAP Business Data Cloud and SAP HANA Cloud to support seamless integration across SAP and non-SAP data with high performance and low cost. It also says Dremio will help deliver a universal, open catalog built on Apache Polaris and the Apache Iceberg REST Catalog API, which will serve as both the discovery layer and semantic layer of SAP Business Data Cloud.

That point deserves attention. A universal catalog is not a cosmetic feature. If SAP executes well, this becomes the system that tells agents and analytics tools what the data means, how entities relate to one another, who is allowed to use them, and how trust should be enforced. SAP explicitly links this to the future [SAP Knowledge Graph](https://news.sap.com/2026/05/sap-to-acquire-dremio-unify-sap-and-non-sap-data-power-agentic-ai/), embedding business relationships, organizational hierarchies, regulatory classifications, and lineage as native properties.

Philipp Herzig, CTO of SAP SE, summarized the rationale clearly in the official announcement: "Enterprise AI doesn't stall because the models aren't good enough; it stalls because the data isn't ready for AI agents. Dremio eliminates that bottleneck." That is the right framing. The hard part of enterprise AI is increasingly not model access. It is building a governed, performant, interoperable data substrate that agents can actually use.

Dremio's own announcement reinforces the same idea from the other direction. The company says the combination with SAP should help deliver one open platform where agents can reason over enterprise data, decide, and act. It also highlights SAP's data assets, knowledge graph work, and agent strategy as complementary to Dremio's lakehouse, federation, and semantic capabilities.

The open-source angle also matters. SAP explicitly says it will continue investing in projects central to Dremio's platform, including Apache Iceberg, Apache Polaris, and Apache Arrow. That commitment will be important to watch. If SAP preserves Dremio's credibility in open ecosystems while tightening integration into its own stack, this could strengthen SAP's position well beyond its installed base.

## Relevant Tools

[SAP acquisition announcement](https://news.sap.com/2026/05/sap-to-acquire-dremio-unify-sap-and-non-sap-data-power-agentic-ai/) - SAP's official statement of the deal, product rationale, and expected close timing.

[Dremio's official acquisition post](https://www.dremio.com/blog/sap-intends-to-acquire-dremio/) - Dremio's view of the deal and how it fits its agentic lakehouse roadmap.

[Dremio federation capabilities](https://www.dremio.com/platform/sql-query-engine/federation/) - Official explanation of how Dremio queries across disparate data sources.

[Dremio AI Semantic Layer](https://www.dremio.com/ai-semantic-layer/) - Useful context for understanding why SAP cares about semantics and governed context, not just query acceleration.
