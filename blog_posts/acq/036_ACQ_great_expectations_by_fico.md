---
title: "FICO acquires GX Cloud from Great Expectations to build data quality into its decisioning platform"
published: 2026-05-08
---
Great Expectations (GX) [announced on May 6, 2026](https://greatexpectations.io/blog/an-update-from-great-expectations/) that it and FICO have agreed that FICO acquires GX Cloud, the company's commercial product, and builds it into the FICO platform. The price was not disclosed. The one thing that matters: only GX Cloud is sold. For the company, this looks like the end of the business. That is my reading, not a statement from either side.

## The Problem: Bad data fails silently, and rules only catch what you thought of

Pipelines rarely crash on bad data. A table arrives a day late, a column fills with nulls, a price field changes from dollars to cents, and every job still reports success. A model or a report built on top of it simply gives wrong answers.

The standard defence is to write checks: this column is never null, this value is between 0 and 100, this table has at least a thousand new rows a day. The checks run in the pipeline and can stop it, which teams call a quality gate. The difficulty is that someone has to write and maintain every rule, and rules only catch the failures their authors imagined. As more decisions are made automatically by models, the cost of the failure nobody imagined goes up.

## The Solution: An open source library of data tests, with a paid cloud on top

[Great Expectations](https://greatexpectations.io/) began as an open source Python library, GX Core, in which you describe "expectations" about your data and run them as tests. It is Apache 2.0 licensed. The company, originally named Superconductive, built GX Cloud as the commercial product: a hosted service that adds collaboration, scheduling and management of those expectations.

According to its own announcement, GX Cloud "will no longer be publicly available beginning June 1", and current customers "should have already received information about timelines, support, and next steps". The post does not say what happens to the team.

### Funding history

- Series A - May 2021 - $21M - [reported by aggregators](https://www.employbl.com/companies/Superconductive/funding-rounds). I could not find the original announcement.
- Series B - Feb 2022 - $40M - [Superconductive press release](https://prnewswire.com/news-releases/superconductive-raises-40m-in-series-b-funding-to-revolutionize-the-speed-and-integrity-of-data-collaboration-301479510.html), led by Tiger Global, with Index Ventures, CRV and Root Ventures participating. [TechCrunch's coverage](https://techcrunch.com/?p=2268908) puts the total raised at $64.5M, which implies an earlier seed round of a few million dollars.

## Understanding the Acquisition

GX says FICO will "incorporate it into the FICO platform as the foundation for its next-generation data quality". FICO is a public analytics company best known for credit scores and decision software. Data quality fits its business: if a model decides who gets a loan, the data feeding it has to be checked. This is GX's description of the plan. I could not read FICO's own announcement, so the FICO side, including quotes, is not covered here.

The deal covers GX Cloud. The open source project goes elsewhere: GX says Fivetran will become the new steward of the GX community and GX Core, which will continue as an open source, community-driven project. The announcement does not name the price, the closing date or the team's future.

For existing GX Cloud users the practical meaning is clear: it is no longer publicly sold after June 1, and they have to move to FICO's platform or to something else. For users of GX Core, nothing changes in the license.

## Relevant Products and Companies

- [Monte Carlo](https://www.montecarlodata.com/): data observability that detects anomalies without hand-written rules.
- [Soda](https://www.soda.io/): data quality checks and contracts, similar in approach to GX.
- [Elementary](https://www.elementary-data.com/): data quality built around dbt. See my [Elementary article]({{ '/blog_posts/acq/025_ACQ_elementary_data_by_boomi.html' | relative_url }}).
- [Fivetran](https://www.fivetran.com/): the new steward of GX Core, and merging with dbt Labs. See my [merger article]({{ '/blog_posts/merger/033_MERGER_fivetran_dbt_labs.html' | relative_url }}).

## My Take

*Draft for the author to confirm.*

GX started as a good idea, but it is a feature, not a company. Data quality through rules and quality gates is useful, yet hard to justify at this scale: more than $60M raised, against a product that ends up folded into someone else's platform. I would call this practically the end of Great Expectations as a startup. The brand lives on as an open source project.

How much demand is there for that project? As of November 9, 2026, GX Core has about 11.9k stars on GitHub, according to the repository page, now under the Fivetran organisation. The package shows around 19 million downloads a month on [PyPI Stats](https://pypistats.org/packages/great-expectations). Those downloads are real usage, but they include automated installs in CI jobs, so they say more about how widely the library is embedded than about how many people pay for anything. Plenty of use, and little willingness to pay for the cloud on top, is the pattern that makes a startup hard to build on an open source library.

---

## Updates

*Late additions, published after the original article and not part of the official announcements.*

### May 2026: Fivetran to steward GX Core

On May 13, 2026, [Fivetran announced](https://www.fivetran.com/press/fivetran-to-become-steward-of-the-great-expectations-open-source-community-and-gx-core-project) plans to become steward of the Great Expectations open source community and the GX Core project. Its release says it expects to hire engineers with experience on GX Core to support maintenance and development, and that more detail will follow after the agreement completes. It does not mention FICO or GX Cloud.
