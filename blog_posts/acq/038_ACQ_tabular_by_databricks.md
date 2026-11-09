---
title: "Databricks acquires Tabular to settle the Delta Lake and Iceberg table format split"
published: 2024-06-07
---
Databricks [announced on June 4, 2024](https://www.databricks.com/blog/databricks-tabular) that it agreed to acquire Tabular, a data management company founded by the creators of Apache Iceberg. Databricks did not disclose the price. [CNBC reported](https://www.cnbc.com/2024/06/04/databricks-is-buying-data-optimization-startup-tabular.html) that Databricks paid more than $1 billion. The one thing that matters: Databricks now employs the people behind both of the open table formats that its customers choose between.

<figure class="shot">
  <img src="{{ '/assets/images/tabular/hero.png' | relative_url }}" alt="Databricks and Tabular logos" loading="lazy">
  <figcaption>Databricks and Tabular. Source: <a href="https://www.databricks.com/blog/databricks-tabular">Databricks</a>.</figcaption>
</figure>

## The Problem: The data lake has two table formats, and choosing one means choosing a camp

A modern data lake is a pile of files in object storage, usually Parquet. A table format turns those files into tables: it records which files belong to a table, what the schema is, and lets many engines read and write safely at the same time. Without one, two jobs writing to the same folder can leave readers with half a table.

The market has more than one such format. Delta Lake comes from Databricks, and Apache Iceberg began at Netflix and is backed by many other vendors, Snowflake among them. Apache Hudi is a third. An engine that speaks one format may not read another, so a company that picks Delta can find that a tool it wants only supports Iceberg. The format is where the data lives, so switching later means rewriting petabytes of files.

Imagine a retailer that stores its sales history as Delta tables and then buys a second analytics tool that reads only Iceberg. It either keeps two copies of the data or gives up the tool. This is what customers mean when they say they want "open" data: the format should not decide which products they can use.

## The Solution: An independent Iceberg platform from its creators

[Tabular](https://tabular.io/) was founded in 2021 by Ryan Blue, Daniel Weeks and Jason Reid. Databricks says Ryan and Daniel developed Iceberg at Netflix and donated it to the Apache Software Foundation. The company sold an independent data platform built on Iceberg, positioned as neutral between the engines that read it ([VentureBeat](https://venturebeat.com/business/tabular-the-independent-data-platform-from-apache-iceberg-creators-scores-26m)). The Databricks announcement does not describe Tabular's product, customers or features, and Tabular's own post was not available to me, so I do not go further.

### Funding history

- Early round - Aug 2021 - $11M - [aggregator](https://clay.com/dossier/tabular-funding), reportedly led by Andreessen Horowitz. I could not confirm it from a primary source.
- Round - Sep 2023 - $26M - [Business Wire](https://www.businesswire.com/news/home/20230919876739/en), led by Altimeter Capital with Andreessen Horowitz participating. Some outlets call it a Series B.

About $37M in total, according to aggregators.

## Understanding the Acquisition

Databricks says the deal "brings the original creators of Apache Iceberg and those of Linux Foundation Delta Lake" together. Its plan is to "work closely with the Iceberg and Delta Lake communities", in the short term inside Delta Lake UniForm, and in the long term "by evolving toward a single, open, and common standard of interoperability". It adds that "this is a long journey, one that will likely take several years". It also says the acquisition shows its "commitment to open formats and open source data in the cloud".

<figure class="shot narrow">
  <img src="{{ '/assets/images/tabular/uniform.png' | relative_url }}" alt="Diagram: with UniForm, Delta Lake tables can be read by the Iceberg and Hudi ecosystems as well as Java, Rust and Python engines" loading="lazy">
  <figcaption>UniForm lets a Delta Lake table be read as Iceberg or Hudi. Source: <a href="https://www.databricks.com/blog/delta-lake-universal-format-uniform-iceberg-compatibility-now-ga">Databricks</a>.</figcaption>
</figure>

UniForm is Databricks' existing answer: a Delta table also writes the metadata that Iceberg readers expect, so one copy of the data serves both. Databricks announced UniForm's general availability a day before the Tabular deal. The neighbouring post says it will "invest heavily to greatly broaden the ambitions of Delta Lake UniForm".

**How the price can be justified.** Databricks does not give a justification in numbers, and Tabular's revenue is not public. These are my hypotheses, not statements from either side:

- **The standard itself.** If Iceberg becomes the default format, Databricks needs a say in where it goes. Employing its creators gives it influence over the project, even though it is still run by the Apache Software Foundation.
- **Removing a reason not to buy.** Customers who want Iceberg can be offered Databricks without being asked to give up their format.
- **A scarce team.** Few people have built a table format that the whole industry adopted.

For Tabular customers and the Iceberg project, the announcement states nothing. It does not say whether the Tabular product continues, and it does not describe Iceberg governance after the deal.

## Relevant Products and Companies

- [Apache Iceberg](https://iceberg.apache.org/): the open table format Tabular's founders created, supported by many engines.
- [Delta Lake](https://delta.io/): Databricks' own table format, hosted by the Linux Foundation.
- [Snowflake](https://www.snowflake.com/): Databricks' main rival, which supports Iceberg tables.
- [Apache Hudi](https://hudi.apache.org/): the third open table format, also covered by UniForm.

## My Take

$1 billion is a lot of money. Is there real business value in it? I'm not sure the numbers alone explain it. Tabular was a small company with a young product, and nothing that has been published shows revenue anywhere near that scale. What Databricks bought is strategic: the Iceberg creators, and with them some control over a standard that its customers care about.

I'm not fully convinced by the price, if it is true. But I look at Databricks, and these people seem to know what they are doing. They have a record of paying for the ground their platform stands on, and the table format is that ground. I would not bet against them on this one.

---

## Updates

*Late additions, published after the original article and not part of the official announcements.*

### May 2025: Another reported $1 billion for a small team

On May 14, 2025, Databricks [agreed to acquire Neon](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems), a serverless Postgres company, for a price reported at about $1 billion. See my [Neon article]({{ '/blog_posts/acq/015_ACQ_neon_by_databricks.html' | relative_url }}).
