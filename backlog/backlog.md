# Backlog

## Interesting technologies 
https://github.com/rerun-io/rerun 

The data layer for physical AI
Log, query, visualize, and stream to training on shared columnar storage built for multimodal data.

What it does: Rerun ingests multi-rate, multimodal data (images, point clouds, transforms, time series, joint states, video) from many sources and formats (robot logs, human-data rigs, sim, web video; MCAP, rrd, LeRobot). The built-in viewer renders everything in sync, in realtime: scrub episodes, compare sensors side-by-side, watch CV pipelines run live. The same data is queryable with dataframes or SQL, and streams directly into training. Built in Rust on column-chunk storage purpose-built for multi-rate physical data. SDKs in Python, Rust, and C++.

Quickstart: pip install rerun-sdk — log your first multimodal data and see it in the viewer in under 2 minutes.

Run the Rerun Viewer in your browser
Read about what Rerun is and who it is for
Use cases
Ingest robot logs, egocentric/UMI rigs, sim, and web video into one substrate
Run CV pipelines (SLAM, hand tracking, motion retargeting) as table edits
Query raw, intermediate, and derived data with dataframes or SQL
Visualize multi-rate, multimodal sequences across the pipeline
Stream dataset mixes directly to training — no export jobs, no stale copies
Data types
Multi-rate, multimodal, spatial: images, point clouds, time series, tensors, transforms, joint states, video. Preserved end-to-end.

## Market events to review

Parsed from a list of deals. Eleven were added to `_data/events.yml` without analysis. These need a decision:

- **Andy Pavlo → ClickHouse** (announced Aug 3, 2026). A hire, not an acquisition: Pavlo becomes VP of Database Research and leads a new group, ClickHouse Labs. Not added to the events file, which only holds funding rounds and acquisitions. Official: https://clickhouse.com/blog/andy-pavlo-joins-clickhouse and https://clickhouse.com/blog/andy-pavlo-founding-clickhouse-labs
- **Supabase $150M round** (announced Oct 2, 2026, alongside the Turso deal). A funding event of its own. Not added yet; needs the official round announcement and valuation checked.

Already covered: Dremio → SAP has a full analysis ([003](../blog_posts/acq/003_ACQ_dremio_by_sap.md)).


## Article ideas (to discuss: worth publishing?)

Written down so they are not forgotten. None is researched or verified yet. Facts below are the author's notes.

- **Oxla → Redpanda** (October 2025). Redpanda acquired Oxla, a Polish deeptech startup building a distributed SQL/OLAP query engine. The idea: bring compute-on-storage technology into Redpanda for real-time analytics and its Agentic Data Plane. Type: acquisition.
- **Benthos → Redpanda** (May 2024). Redpanda acquired Benthos and rebranded it as Redpanda Connect, a high-performance data streaming and integration engine with 220+ pre-built connectors. Type: acquisition.
- **Redpanda funding.** Last round found: $100M Series D, announced April 3, 2025, led by GV with Lightspeed participating, at a $1B valuation (company press release: https://www.redpanda.com/press/redpanda-raises-100m-launches-enterprise-agentic-ai-platform). No newer round found as of Nov 2026. Total raised is reported as about $265M, but sources differ. Type: funding, and context for the two Redpanda acquisitions above. Possible angle: one Redpanda article covering Benthos, Oxla and the funding.
- **Tobiko → Fivetran.** Fivetran acquired Tobiko (the company behind SQLMesh and SQLGlot). Date and details not checked. Type: acquisition.
- **Census → Fivetran.** Fivetran acquired Census (reverse ETL). Date and details not checked. Type: acquisition.
- **RisingWave Labs funding.** Streaming database. Last round found: $36M Series A, announced October 18, 2022, led by Yunqi Partners (TechTarget: https://techtarget.com/searchdatamanagement/news/252526292/RisingWave-Labs-raises-36M-for-stream-processing-database). No Series B or later round found, but recent coverage is thin, so check RisingWave's own newsroom before ruling out a newer round. Total raised is reported as roughly $40M or more; sources differ. Type: funding. Weak candidate unless a newer round appears.
- **Turbopuffer funding.** Search and vector database on object storage. Last round found: seed in December 2025, amount undisclosed. Investors reported: Lachy Groom (existing) and Thrive Capital (new), per BetaKit (https://betakit.com/ex-shopify-engineers-raise-fresh-financing-to-scale-turbopuffers-ai-search/), which is the only source. Total raised conflicts across sources ($12M vs under $1M), so leave it out unless the company states it. A tracker (Dealroom) reports a $100M run-rate and profitability in March 2026; unverified, use only if the company says it. Type: funding. Better candidate than RisingWave, but the facts are thin.
- **Seemore Data funding.** New York data cost and performance optimization company, founded 2023. Only aggregators (Caplight, Hanaco VC profile) list a seed around November 2023 with Hanaco VC and State of Mind Ventures and about $5.6M total. No press release found, so none of this is verified. Needs the company's own announcement or a trusted outlet before writing. Type: funding (seed).
- **DataFlint funding.** Israeli startup (Petah Tikva) focused on Apache Spark performance optimization. Only aggregators list a pre-seed around April 2025, amount undisclosed. No announcement found, so nothing is verified. Not to be confused with Flint, an unrelated autonomous-website startup that raised a $5M seed. Type: funding (seed). Related to definity (Spark pipelines), see 041.

Related: Fivetran also has a missing logo in the Market Moves cards. Check if Fivetran already appears in `_data/events.yml` before writing.

## Idea: a separate category for seed rounds

Seed rounds are different from later rounds: there are usually no public numbers and no customers, so the funding template (Competitive Landscape, Previous Rounds, capital trajectory) has little to say. A seed article would focus on the idea: the problem, the approach, the founders and why it might matter. Open questions to discuss:

- Is it a new type in `_data/events.yml` and a new prompt, or a shorter variant of the funding prompt?
- What is the bar for writing one, given that facts are thin and the trusted-sources rule leaves little to say?
- Seed and Series A articles already share the Founder Background and Summary sections (see 010 Keewano, 040 Edelbyte). A seed type could start from those.
