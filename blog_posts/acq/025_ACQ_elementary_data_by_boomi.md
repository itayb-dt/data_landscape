---
title: "Boomi acquires Elementary Data to make the data behind its AI agents trustworthy"
published: 2026-11-03
---
Boomi [announced on October 19, 2026](https://boomi.com/resources/resources-library/boomi-acquires-elementary/) that it has acquired Elementary Data, a Tel Aviv startup that builds data observability tools. The price was not disclosed by the companies. [Calcalist reports](https://www.calcalistech.com/ctechnews/article/b1zgj8mnzg) about $40-45 million in cash and stock, without naming its source. All 17 employees are in Israel and join Boomi.

<figure class="shot narrow">
  <img src="{{ '/assets/images/elementary/hero.png' | relative_url }}" alt="Boomi acquires Elementary Data" loading="lazy">
  <figcaption>Boomi acquires Elementary Data. Source: <a href="https://boomi.com/resources/resources-library/boomi-acquires-elementary/">Boomi</a>.</figcaption>
</figure>

## The Problem: Data breaks silently, and AI acts on it anyway

Pipelines fail in quiet ways. A table stops updating, a column changes meaning, the row count drops by half, and nothing crashes. A dashboard shows a wrong number until someone notices.

With AI agents the cost grows, because an agent acts on the data immediately and nobody reviews each step. Take an agent that approves refunds from an orders table: if the table is a day stale, it approves the wrong ones. Teams need to know that data is fresh, complete and correct before something relies on it.

## The Solution: Observability built into the dbt workflow

[Elementary](https://www.elementary-data.com/) started in 2022 as an open source project, a CLI for monitoring [dbt](https://www.getdbt.com/) data pipelines. It tests data and detects anomalies in freshness, volume and quality. In 2024 it launched Elementary Cloud, a commercial product that adds enterprise features, catalog, lineage and incident handling. The open source part is Apache 2.0 licensed and has about [2.4k GitHub stars](https://github.com/elementary-data/elementary).

The company says over 1.1 million downloads a month. Its own post claims [more than 2,000 data teams](https://www.elementary-data.com/post/elementary-joins-boomi), while Calcalist reports 1,500, so I would treat both as approximate. Calcalist names Fiverr and Patagonia as customers.

### Funding history

Seed - By end of 2022 - $8.5M total - [Calcalist](https://www.calcalistech.com/ctechnews/article/b1zgj8mnzg), from TLV Partners, Cowboy Ventures, Y Combinator and angel investors. No later round found.

## Understanding the Acquisition

Boomi is an integration platform: it moves data between applications and systems. Elementary adds the layer that checks that the data is trustworthy. Boomi CEO Steve Lucas framed it this way: ["AI is only as trustworthy as the data behind it."](https://www.calcalistech.com/ctechnews/article/b1zgj8mnzg)

The plan is to bring Elementary's observability, quality, governance and discovery into the Boomi Enterprise Platform, so monitoring covers data in warehouses and data moving between systems. Calcalist also lists a shared catalog, lineage and an MCP server that exposes data context and health to agents.

For users, Elementary says [nothing changes for now](https://www.elementary-data.com/post/elementary-joins-boomi): the product continues as a standalone offering, the open source project continues, and existing agreements stay as they are.

## Relevant Products and Companies

- [Monte Carlo](https://www.montecarlodata.com/): the best-known commercial data observability platform.
- [dbt](https://www.getdbt.com/): the transformation tool Elementary is built around.
- [Boomi](https://boomi.com/): the buyer, an integration platform.

## My Take

This is not the first Israeli company Boomi has acquired. Rivery, a data integration company, came in December 2024, and Lunar.dev, an AI gateway, was announced in May 2026. Elementary is the third, according to Calcalist.
