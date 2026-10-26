---
title: "The unstoppable rise of PostgreSQL"
show_title: true
---
*Originally published on Substack on August 9, 2025: [The Unstoppable Rise of PostgreSQL](https://itaybraun.substack.com/p/the-unstoppable-rise-of-postgresql).*

If you're building an application today, the question isn't if you should use a relational database, but which one. For a growing majority of developers, the answer is unequivocally PostgreSQL. Once considered a niche, academic database, PostgreSQL (or "PG") has surged to become the leading open-source relational database, leaving its rivals in the dust.

### A Strong Market Signal from the Database-as-a-Service Ecosystem
How do we know PG is on top? Just follow the money. The ecosystem of companies providing PostgreSQL as a service (DBaaS) is exploding with investment and innovation, a phenomenon we don't see with any other database engine.

- **[Neon](https://neon.com/)** built a cutting-edge serverless PostgreSQL platform and was [acquired](https://techcrunch.com/2025/05/14/databricks-to-buy-open-source-database-startup-neon-for-1b/) for a reported $1B by Databricks. 
- **[Crunchy Data](https://www.crunchydata.com/)**, a long-time enterprise PostgreSQL provider, was [acquired](https://techcrunch.com/2025/06/02/snowflake-to-acquire-database-startup-crunchy-data/) for a reported $250 million by Snowflake.
- **[Supabase](https://supabase.com/)**, a Postgres development platform [raised $200M](https://techcrunch.com/2025/04/22/vibe-coding-helps-supabase-nab-200m-at-2b-valuation-just-seven-months-after-its-last-raise/) at staggering $2 billion valuation.
- **PlanetScale**, a MySQL provider, recently announced it will now offer PostgreSQL, acknowledging overwhelming customer demand.
- **[TigerData](https://www.tigerdata.com/)** (AKA TimescaleDB) [raised $110M](https://www.tigerdata.com/blog/year-of-the-tiger-110-million-to-build-the-future-of-data-for-developers-worldwide) to build an analytics database based on Postgres. 

You simply don't see this level of venture-backed, high-growth activity around MySQL or any other open-source relational database. The market has spoken, and it's betting big on Postgres.

### Understanding the Present Through the Past
Analyzing PostgreSQL's current dominance is straightforward—the numbers don't lie. But understanding how we got here is the trickier and more interesting question. It's like a history lesson, tracing the convergence of technical innovation, licensing decisions, corporate missteps, and perfect timing that transformed an academic database into the foundation of modern applications. The present tells us what happened; the past tells us why.

### The Secret Sauce: A Permissive License and Powerful Extensions
So, what makes PostgreSQL so special? Two key factors are its license and its unparalleled extensibility.

First, the **PostgreSQL License is a permissive, MIT-style license**. This is a game-changer. It allows anyone—from a solo developer to a cloud giant like Amazon (with its Aurora and RDS services)—to use, modify, and even sell services based on PostgreSQL without being forced to open-source their proprietary changes. This business-friendly approach encourages commercial investment and innovation in the ecosystem, a stark contrast to MySQL's more restrictive GPL license.

Second, and arguably more important, is its **extension architecture**. PostgreSQL isn't just a database; it's a platform. Extensions are plugins that can be installed to add powerful new functionalities directly into the database engine itself. This means you can tailor your database to your specific needs without adding complex, external services.

Here are a few examples of how extensions solve common developer problems:

**Zero ETL Analytics:** Need to analyze vast amounts of data without costly ETL pipelines? Extensions like Citus and Hydra create a hybrid database that combines PostgreSQL's row-oriented engine for transactions with columnar storage for lightning-fast analytics—all in one system.

**Advanced Geo-Location:** Building location-based features but standard SQL can't handle geographic queries? PostGIS transforms your database into a full GIS system with spatial data types and functions.

**Time-Series Data:** Collecting massive amounts of sensor data or metrics that bog down regular tables? TimescaleDB automatically partitions your time-series data and provides specialized functions for time-based queries and aggregations.

**Semantic Search powered by AI:** Want to perform vector similarity searches without managing a separate vector database? The pgvector extension lets you store and query embeddings directly alongside your relational data.

There are literally over 1,000 extensions available to solve problems ranging from full-text search and encryption to audit logging and job queues. This extensibility means you can often use a single, familiar database for tasks that would have previously required three or four different specialized systems.

### But Extensions Don't Tell the Whole Story

However, extensions alone can't explain PostgreSQL's complete dominance. The reality is that most developers using cloud-managed PostgreSQL services like AWS RDS, Google Cloud SQL, or Azure Database only have access to 80-100 pre-approved extensions. While users can run PostgreSQL on raw compute instances (like EC2) to install any extension they want, this means taking on the burden of managing high availability, replication, backups, and version upgrades - tasks most organizations prefer to offload to managed services. 

So PostgreSQL's success isn't just about its advantages; it's also about the relative disadvantages of the main alternatives. MySQL and MariaDB.

### How Did We Get Here? A Look Back
It wasn't always this way. Fifteen, or even ten years ago, **the database world looked very different**. The enterprise space was locked down by proprietary giants like Oracle and Microsoft SQL Server. In the open-source world, MySQL was the undisputed champion, powering the famous **LAMP stack** (Linux, Apache, MySQL, PHP) and virtually every startup. PostgreSQL was respected for its correctness and feature set but was often seen as slower, more complex, and less user-friendly.

The major turning point came in 2010 when **Oracle acquired Sun Microsystems**, and with it, MySQL. This sent a wave of fear, uncertainty, and doubt (FUD) through the open-source community. Developers worried that Oracle, whose primary business was selling its own competing database, would neglect MySQL's development or use licensing to push users towards its paid products.

#### The Trust Factor: Predictability in an Uncertain World
But the Oracle acquisition did more than create licensing concerns. It shattered something more fundamental: trust in the development roadmap. Under Oracle's management, MySQL's release schedule became erratic and unpredictable. MySQL 6.0 was announced, then cancelled. Version 8.0 followed 7.0, skipping an entire major version number. Developers couldn't count on when new versions would arrive, what features they'd contain, or whether upgrades would introduce breaking changes. The infamous gap between MySQL 5.7 (2015) and 8.0 (2018) left developers wondering if the project was effectively stalled.

Meanwhile, PostgreSQL established something invaluable in the software world: **predictability**. Every September, like clockwork, a new major version would be released. Developers and system architects knew they could count on **consistent improvement**: better performance, new features, enhanced reliability, without the uncertainty that plagued MySQL. 

This wasn't about specific features or benchmark wars over 3% performance gains. It was about trust. Organizations could plan multi-year technical roadmaps knowing PostgreSQL would be there, evolving steadily, with minimal breaking changes and a clear upgrade path.

I found some interesting insights here: [Oracle’s MySQL Layoffs — Strategy, Timing, and What It Means for Enterprise Customers](https://www.linkedin.com/pulse/oracles-mysql-layoffs-strategy-timing-what-means-patrik-backman-a5g3f/). TLDR: The future MySQL, from Oracle’s perspective is the cloud (OCI) + premium features ([HeatWave](https://www.oracle.com/heatwave/features/))

In response, MySQL's original creators forked the project to create MariaDB, aiming to be a community-governed, "drop-in replacement." While MariaDB is a solid database and found a niche, it never fully captured the momentum from the MySQL exodus. It remained architecturally similar to MySQL and didn't innovate at the same pace as PostgreSQL. More importantly, it couldn't restore the predictable development cadence that developers had lost.

Throughout this turmoil, the PostgreSQL project, with its stable, non-corporate, community-driven development model, just kept getting better. It consistently improved its performance, added features, and nurtured the extension ecosystem that has become its defining advantage. While others were dealing with corporate politics, version number confusion, and development uncertainty, PostgreSQL was busy building the future with the reliability of a Swiss watch. And today, that future is here.

MariaDB Stock - It didn’t go well, unfortunately

![MariaDB stock price chart]({{ '/assets/images/mariadb-stock.png' | relative_url }})

## The Future: PostgreSQL as the Universal Data Platform
There is a famous quote: It's tough to make predictions, especially about the future 😀. But I’ll try. 

PostgreSQL's trajectory suggests it's here to stay, though the landscape won't be about database monocultures. Instead, PostgreSQL is positioning itself as the central hub in increasingly complex data architectures. Through **Change Data Capture** (CDC), PostgreSQL can seamlessly stream changes to specialized systems—feeding **real-time analytics** engines, search platforms, and machine learning pipelines without disrupting core operations. **Foreign Data Wrappers** are transforming PostgreSQL into a query engine that can reach into data lakes like **Apache Iceberg**, making it the single entry point for queries regardless of where data actually lives. 

This "PostgreSQL as universal interface" approach means developers can write familiar SQL queries while the database intelligently routes operations to the most appropriate storage layer. Your transactional data stays in PostgreSQL, your archived data lives in object storage, but your application sees one consistent interface. 

The **$250M [acquisition](https://techcrunch.com/2025/06/02/snowflake-to-acquire-database-startup-crunchy-data/) of CrunchyData by Snowflake** is a strong example of this trend. CrunchyData helps integrate Postgres with [Data Lakes](https://www.snowflake.com/en/engineering-blog/pg-lake-postgres-lakehouse-integration/). 

Meanwhile, the extension ecosystem continues its relentless march toward feature parity with specialized databases. MongoDB might excel at petabyte-scale document storage, but for applications needing "only" terabytes of document data, PostgreSQL's JSON capabilities, ACID guarantees, and rich ecosystem often provide what many developers consider a superior experience (though other developers would strongly disagree with that assessment, as they have a totally different interpretation for what a superior dev experience actually means). 

The same pattern applies across use cases - PostgreSQL may not win every benchmark, but it increasingly offers "good enough" performance with significantly better operational simplicity.

The future isn't PostgreSQL versus the world; it's **PostgreSQL as the reliable foundation** that plays well with everything else, reducing architectural complexity while maintaining the flexibility to optimize specific workloads when truly necessary.

