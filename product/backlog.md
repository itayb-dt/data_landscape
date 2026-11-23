# Product Backlog

Site features and workflow ideas. Priorities are a first proposal: P1 = next, P2 = soon, P3 = later. Article ideas live in [backlog/backlog.md](../backlog/backlog.md).

## 1. Add analytics (P1)

Measure visits, top articles and where readers come from, to see which stories and tweets bring traffic. PostHog was the candidate. It needs a project key (public, safe to keep in the repo) and a decision on cookies and consent.

## 2. Automation to scan main sources for new articles (P1)

A scheduled job that watches the main sources (key Twitter/X accounts, company blogs, press releases) and lists new acquisitions and funding rounds worth covering. Output is a short candidate list with links, not auto-published articles. Must respect the trusted-sources rule in the writing rules.

## 3. News feed with 4-5 items a week (P2)

A short feed of other interesting stories that do not deserve a full article: one line, one link, one sentence on why it matters. Needs a data file, a page and a weekly routine for filling it.

## 4. List of subjects to write my thoughts about (P2)

A running list of topics for opinion pieces rather than news, for example "What is DuckDB" or "The current state of the modern data stack". Each entry gets a working title and a one-line angle, so it can be picked up later.

## 5. Ontology of subjects (P3)

A map of the core technologies, such as Flink, Parquet, Kafka and dbt, with short explanations and links to the related articles, companies and events. Open questions: a data file or a page per subject, and how articles get tagged to it.
