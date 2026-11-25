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

- **ReductStore profile.** Storage and streaming layer for robot and machine data (reduct.store, ReductSoftware UG, Hamburg; founders Alexey Timin and Anthony Cavin). It stores timestamped records of any size, batches them into blocks and keeps them on local disk or S3-compatible storage, with FIFO retention and filtered replication from the machine to the cloud. Open source core (Apache-2.0), paid Pro and Enterprise tiers. Not a general database and not a data platform. No equity round found. Aggregators (Crunchbase, Tracxn) list only an IFB Innovationsstarter grant, April 2025, amount unknown. The founding year (2024 per Tracxn) is unverified. Performance and adoption figures are the company's own claims. Type: technology profile (not funding). Best written together with the physical-AI data items below.
- **Foxglove Series B.** Robotics data and observability platform. $40M Series B announced November 12, 2025, led by Bessemer with Eclipse and Amplify Partners, more than $58M raised in total (Business Wire: https://www.businesswire.com/news/home/20251112126106/en/Foxglove-Raises-%2440-Million-Series-B-to-Power-the-Future-of-Physical-AI). A year old now, so it needs an angle. Type: funding. The best-funded ReductStore competitor.
- **Eventual (Daft) funding.** Daft is an open source Python data engine for multimodal data (images, audio, video), and Eventual also sells a robot fleet data curation product. $20M Series A in June 2025, led by Felicis with M12 and Citi. Total funding conflicts across sources (about $30M in most). Everything found came from FinSMEs and aggregators, so check Eventual's own announcement first. Type: funding.
- **Rerun funding.** Open source visualization toolkit plus a database and cloud for physical AI data. $17M seed, March 20, 2025, led by Point Nine, $20.2M total (TechCrunch: https://techcrunch.com/2025/03/20/reruns-open-source-ai-platform-for-robots-drones-and-cars-revs-up-with-17m-seed/). Newer rounds not checked. Type: funding. Related to the Rerun entry in "Interesting technologies" above.
- **Theme: the data layer for physical AI.** One possible article across Foxglove, Rerun, Eventual, LanceDB (see 047) and ReductStore at the edge: who stores and queries robot data, where the open source projects overlap, and who is funded. Daft and ReductStore are neighbours more than substitutes: Daft processes multimodal data in the cloud, ReductStore records it on the machine.

- **FalkorDB funding (Series A?) - ON HOLD, do not publish.** The author wants an article on the A round, with a mention of the seed, the technology versus Neo4j, customer stories, the business model and a My Take. The Series A is not confirmed, so nothing was written. Research is kept here for later.
  - **Funding.** Seed: $3M, announced June 20, 2024 in a company press release on PRLog, led by Angular Ventures with K5 Tokyo Black and angels (Aryeh Mergi, Jerry Dischler, and Eldad Farkash and Saar Bitner of Firebolt). That is about 2.4 years ago, so it is inside the 3-year window and gets a mention only. Series A: no announcement found on falkordb.com or in the press. PitchBook (https://pitchbook.com/profiles/company/561275-02, blocks automated reads) lists a $7M early-stage deal dated February 27, 2026 and $10M raised in total, with no series name, lead or investors. Single aggregator, not approved for use. Needs the author's paste of the deal row or a trusted source.
  - **Company.** FalkorDB, Inc. Founders Guy Korland (CEO, PhD Tel Aviv University, previously led Redis' incubation arm), Roi Lipman (CTO, creator of RedisGraph) and Avi Avni (Chief Architect), all ex-Redis. The press release is datelined Tel Aviv and the job listings are in Tel Aviv, so the Israeli angle for My Take holds (rule 9 in the writing rules). The site does not state a headquarters.
  - **Technology.** Graph database stored as sparse matrices, with queries run as linear algebra. Runs as a module inside Valkey (announced November 23, 2026, Valkey 9.2 or later). Version 6.0 (September 2026) is a Rust engine rewrite. Query language is openCypher. Built-in vector and full-text search for GraphRAG. Thousands of isolated graphs in one deployment (multi-tenancy). SOC 2 Type II. The license is not stated on the site (Atlan says SSPLv1), so leave it out unless confirmed.
  - **Versus Neo4j** (https://www.falkordb.com/falkordb-vs-neo4j/, the company's own table): FalkorDB is in-memory, Neo4j on disk. Multi-tenancy on every FalkorDB plan, Neo4j enterprise only. Full on-prem for FalkorDB, Neo4j single-instance only. Horizontal scaling "flexible" versus "limited". The benchmark claims (for example P99 latency 83 ms versus 41,157 ms, from FalkorDB's own open benchmark at https://benchmark.falkordb.com/, not read) are FalkorDB's own. Leave numbers out, or label them as the company's.
  - **Business model.** Open source core. FalkorDB Cloud has a free tier and paid tiers by memory size, plus an Enterprise tier with VPC, 24/7 support and a dedicated account manager. Also self-hosted with an enterprise console. No exact prices in the article.
  - **Customers.** AdaptX (healthcare clinical data, multi-graph tenancy for clinicians and facilities, qualitative results only, quote from Matthew Goose): https://www.falkordb.com/case-studies/how-adaptx-uncovers-hidden-potential-in-their-clinical-data/. SERGAS Group (LPG distribution in the Gulf, a legal-review assistant on a FalkorDB knowledge graph, delivered as a Claude Skill, a UAE beta, claimed "roughly half" fewer legal escalations): https://www.falkordb.com/case-studies/legal-graphrag-claude-skill-falkordb/. Homepage logos (Walmart, HSBC, BMW, Maersk, Snowflake and others) are logos only, not confirmed customers.
  - **Author's My Take, as dictated.** Nice to see a totally different approach to implementing a graph database. Still the impression that the graph database market is not big and is limited to specific use cases. PostgreSQL 19 was expected to include graph queries (SQL/PGQ) and eventually did not. Once it ships, it will be interesting to see how much of the market goes to Postgres: probably slower, but simpler because it is the same database. The author expects the same flow as with built-in analytics. "I will be smarter once it is released." Add a few warm words about the founders being Israeli.
  - **Postgres 19 facts (approved by the author for use, the SQL/PGQ news).** Released November 19, 2026. SQL/PGQ was committed and then reverted on September 7, 2026, and beta 4 (September 24) listed the revert. The earliest return is PostgreSQL 20, around September 2027. The details come from blog posts, so keep to the main fact (graph queries were pulled from 19) and label the rest as reported. Official release notes: https://www.postgresql.org/docs/19/release-19.html.
  - **Image.** The author supplied the homepage banner, saved at `assets/images/falkordb/hero.png` (4 MB, not referenced by any article yet, to be resized). Source credit: FalkorDB homepage.
  - **Likely filename if published:** `048_FUND_falkordb_...md`. The publication date and article title wait for the confirmed round.

Related: Fivetran also has a missing logo in the Market Moves cards. Check if Fivetran already appears in `_data/events.yml` before writing.

## Idea: a separate category for seed rounds

Seed rounds are different from later rounds: there are usually no public numbers and no customers, so the funding template (Competitive Landscape, Previous Rounds, capital trajectory) has little to say. A seed article would focus on the idea: the problem, the approach, the founders and why it might matter. Open questions to discuss:

- Is it a new type in `_data/events.yml` and a new prompt, or a shorter variant of the funding prompt?
- What is the bar for writing one, given that facts are thin and the trusted-sources rule leaves little to say?
- Seed and Series A articles already share the Founder Background and Summary sections (see 010 Keewano, 040 Edelbyte). A seed type could start from those.
