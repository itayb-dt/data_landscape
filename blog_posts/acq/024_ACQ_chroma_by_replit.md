---
title: "Replit acquires Chroma to give its agents memory, and winds down Chroma Cloud"
published: 2026-11-03
---
Chroma [announced on October 23, 2026](https://www.trychroma.com/blog/chroma-joins-replit) that it has signed a definitive agreement to join Replit. The price was not disclosed, and I could not read Replit's own announcement, so the facts here come from Chroma and from [Dealroom's report](https://dealroom.co/news/167742-replit-buys-chroma-to-give-its-agents-memory-shuts-cloud-in-60-days/). The detail that matters: Chroma, an open source vector database, is [shutting down its hosted service](https://www.trychroma.com/cloud-wind-down).

<figure class="shot">
  <img src="{{ '/assets/images/chroma/hero.png' | relative_url }}" alt="Chroma joins Replit" loading="lazy">
  <figcaption>Chroma joins Replit. Source: <a href="https://www.trychroma.com/blog/chroma-joins-replit">Chroma</a>.</figcaption>
</figure>

## The Problem: AI applications need to find relevant data by meaning, and a classic database cannot

A language model only knows what is in its prompt. To answer questions about a company's documents, a codebase or a conversation history, an application has to find the relevant pieces first and hand them to the model. That means searching by meaning, not by exact words.

The common technique is to turn text into vectors, lists of numbers where similar meaning gives nearby numbers, and search for the nearest ones. A SQL database with an index on a text column cannot do that. Take a coding agent that must find where an app handles login: the code never uses the word "login" in the same way twice, and a keyword search misses most of it.

## The Solution: An open source database built for vector search

[Chroma](https://www.trychroma.com/) describes itself as "open-source search infrastructure for AI", with vector, full-text, regex and metadata search, built on object storage and released under Apache 2.0. Its clients are available for Python, TypeScript and Rust. The project says it has about 6M downloads a month and [just shy of 30k GitHub stars](https://www.trychroma.com/blog/chroma-joins-replit), and names Mintlify, Retool, Krea and Paramount among its users. The company also sold Chroma Cloud, a hosted serverless version.

### Funding history

Public Funding Rounds: Not publicly available from credible sources. [Dealroom lists](https://dealroom.co/news/167742-replit-buys-chroma-to-give-its-agents-memory-shuts-cloud-in-60-days/) $18M raised in total, without rounds. Chroma's post says Replit's CEO Amjad Masad and President Michele Catasta were early investors.

## Understanding the Acquisition

Replit builds software with agents, and an agent needs memory: what it did before, and what is in the project. Chroma's post says its infrastructure for context and memory combines with Replit's agent platform, and Chroma states its aim as the context layer for the "self-driving company".

For users, the effect is split. Open source Chroma [continues under Apache 2.0](https://www.trychroma.com/cloud-wind-down), and Replit says it will contribute back to the project. Chroma Cloud does not continue. Writes stop on November 22, 2026, and reads stop on December 22, 2026. Customers have to move to another Chroma deployment or another database. The wind-down page names no migration tool.

The announcement does not say what Chroma's CEO Jeff Huber or the rest of the team will do at Replit.

## Relevant Products and Companies

- [Pinecone](https://www.pinecone.io/): the best-known managed vector database, which [raised $100M in April 2023](https://www.pinecone.io/newsroom/pinecone-raises-usd100m-in-series-b-funding-to-provide-long-term-memory-for-ai/) at a $750M valuation.
- [pgvector](https://github.com/pgvector/pgvector): the open source extension that adds vector search to Postgres.
- [Turso](https://turso.tech/): SQLite-compatible database with vector search. See my [Supabase and Turso article]({{ '/blog_posts/acq/022_ACQ_turso_by_supabase.html' | relative_url }}).

## My Take

We need vectors in a database, but not necessarily a dedicated database. Vector search is a feature, and it is already inside Postgres through pgvector. Turso lists vector search too, though its README says exact search works today and vector indexing is still on the roadmap. When the main database can do it, a separate system needs a strong reason to exist.

That is why I wonder how Pinecone is doing. It raised $100M in 2023, and I found no later priced round. I do not know its numbers, so this is a question, not a claim.

Chroma is open source, which is why the code lives on. Its cloud, the business, did not. The lesson is the same as in other shutdowns: a new database vendor needs a very clear business justification.
