---
title: "dbt Labs acquires SDF Labs to bring SQL comprehension into dbt"
published: 2025-01-17
---
dbt Labs [announced on January 14, 2025](https://www.getdbt.com/blog/dbt-labs-acquires-sdf-labs) that it has acquired SDF Labs, a startup that builds a Rust toolchain for understanding and compiling SQL. The terms were not disclosed. The one thing that matters: dbt only runs SQL as text, and SDF is the piece that understands it.

<figure class="shot">
  <img src="{{ '/assets/images/sdf/architecture.png' | relative_url }}" alt="SDF architecture diagram from dbt Labs' announcement" loading="lazy">
  <figcaption>SDF architecture diagram. Source: <a href="https://www.getdbt.com/blog/dbt-labs-acquires-sdf-labs">dbt Labs</a>.</figcaption>
</figure>

## The Problem: dbt does not understand the SQL it runs

A dbt project is a set of SQL files with Jinja templating. dbt turns the templates into plain SQL and sends it to the warehouse. It does not parse that SQL or check it, so most mistakes show up only when the warehouse runs the query and fails. Take a column renamed in one model. Nothing warns you that three models downstream still use the old name, until the nightly run breaks and the warehouse bills for it.

Every warehouse also speaks its own SQL dialect, with different types, functions and rules. A tool that wants to catch errors before execution must know all of that. This is why editors for dbt have mostly offered syntax highlighting, and not the type-ahead and instant error checks that developers get in other languages.

## The Solution: A SQL compiler that runs locally

According to dbt Labs, [SDF](https://www.getdbt.com/sdf) is "a high performance toolchain for SQL development packaged into one CLI: a multi-dialect SQL compiler, type system, transformation framework, linter, and language server". It is written in Rust. Each dialect is described as a complete grammar with datatypes, coercion rules and functions. SDF adopted dbt's syntax, configuration and Jinja natively, so it can read existing dbt projects.

dbt Labs credits it with:
- compiling dbt projects about two orders of magnitude faster than dbt Core;
- type-ahead in the editor and errors caught without connecting to the remote database;
- local execution of a query plan;
- "the highest-fidelity lineage on the market".

These are dbt Labs' claims about SDF, not independent measurements. SDF's own announcement posts now redirect to dbt Labs, so I could not read SDF's side of the story.

According to dbt Labs, SDF [emerged from stealth in June 2024](https://www.getdbt.com/blog/dbt-labs-acquires-sdf-labs). It was founded by Lukas Schulte (CEO) and Wolfram Schulte (CTO), a father and son. Wolfram was hired at Meta to build the system that tracked personal data across the company's data pipelines. The team includes database researchers from Microsoft Research and Meta.

### Funding history

Seed - June 2024 - about $9M - [VCBacked](https://www.vcbacked.co/company/sdf), an aggregator. Reports name investors including Founders' Co-op, RTP Ventures, Two Sigma Ventures and Sequoia, and disagree on who led. I could not confirm it from a primary source. No later round found.

## Understanding the Acquisition

dbt Labs CEO Tristan Handy says [the first goal](https://www.getdbt.com/blog/dbt-labs-acquires-sdf-labs) is "to get SDF's SQL parsing capabilities integrated into dbt". The [press release](https://www.getdbt.com/blog/dbt-labs-announces-sdf-labs-acquisition) quotes him: "We are acquiring SDF to bring SQL comprehension into dbt". It says the new metadata adds to dbt's existing table-level and column-level lineage.

What this should change for users: errors found as you type instead of at run time, faster compiles, and more accurate lineage. Handy says "it will take some work" and "won't happen overnight", and that users should expect it to show up in more dbt experiences over the coming 12 months.

The open source question is the one to watch. Handy says SDF "won't be included as part of the Apache 2.0 code base", but that dbt plans to make "meaningful parts" of its capabilities available to all dbt users, whether on dbt Core or dbt Cloud. So parts of SDF may not be open source. The posts do not say which parts, and they do not say what happens to the standalone SDF product and its customers. Handy says the benefits are already realized in production by SDF's existing customers. The SDF team joins dbt Labs.

## Relevant Products and Companies

- [dbt](https://www.getdbt.com/): the buyer and the standard tool for SQL transformations in the warehouse.
- [SQLMesh](https://sqlmesh.com/): an open source alternative to dbt that also parses SQL to understand it.
- [SQLGlot](https://github.com/tobymao/sqlglot): an open source SQL parser and transpiler for many dialects, the library SQLMesh builds on.
