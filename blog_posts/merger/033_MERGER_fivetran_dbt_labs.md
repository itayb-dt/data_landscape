---
title: "Fivetran and dbt Labs merge to build open data infrastructure"
published: 2025-10-16
---
Fivetran and dbt Labs [announced on October 13, 2025](https://www.getdbt.com/blog/dbt-labs-and-fivetran-merge-announcement) that they are merging in an all-stock deal. The two companies say the combined business has about $600 million in annual recurring revenue (ARR). This is a merger, not an acquisition: neither company is the buyer, and the companies did not disclose a valuation or an ownership split.

<figure class="shot">
  <img src="{{ '/assets/images/fivetran-dbt/architecture.png' | relative_url }}" alt="Diagram of the combined company: orchestration, observability and metadata on top; Fivetran ingestion, dbt transformation and Census reverse ETL as pipelines; open compute; and a data lake with catalog and storage" loading="lazy">
  <figcaption>The combined platform as dbt Labs draws it. Source: <a href="https://www.getdbt.com/blog/dbt-labs-and-fivetran-merge-announcement">dbt Labs</a>.</figcaption>
</figure>

## What Each Company Does

**dbt Labs** makes dbt, which turns raw tables in a warehouse into clean, tested tables that analysts can trust. Each step is a SQL query kept in Git like software, with tests that catch bad data before it reaches a dashboard. Take the ticketing company [AXS](https://www.getdbt.com/case-studies/axs): on Snowflake, with Fivetran loading the data, it built dbt models, tested changes before they went live, and used lineage graphs to find what broke. It reports 40% fewer maintenance hours, a company-published figure. dbt Core is open source, and dbt Labs [acquired SDF Labs](https://www.getdbt.com/blog/dbt-labs-acquires-sdf-labs) in January 2025.

**Fivetran** copies data from the apps and databases a company runs on into a central warehouse, with no pipeline code to maintain. Take [Springly](https://www.fivetran.com/case-studies/springly-accelerates-business-growth-with-centralized-data-built-on-fivetran), a nonprofit membership software company with no data team and a habit of working from spreadsheets. It connected MySQL, HubSpot, Zendesk and Calendly to Google BigQuery. Springly says its marketing team now reviews a week of data in under 20 minutes, where five people each used to present their own. Fivetran also owns Census, which sends warehouse data back into business apps.

Fivetran loads the data and dbt shapes it, which is why most stacks ran both.

## Understanding the Merger

- **Structure**: an all-stock merger of two private companies. Both boards and shareholders approved it, and closing needed regulatory approvals. The valuation and ownership split were not disclosed.
- **Leadership**: George Fraser, Fivetran's co-founder, is CEO. Tristan Handy, dbt Labs' founder, is co-founder and President, with a board seat and responsibility for community and open source strategy.
- **Scale**: about $600 million in combined ARR. dbt Labs says "well north of 10,000 customers"; Fivetran says dbt has more than 80,000 data teams. These are company figures, and the two counts measure different things.
- **Products and brands**: "dbt will still be dbt. Fivetran will still be Fivetran." No renaming and no disruptive product changes are planned.
- **Open source**: both companies say dbt Core and dbt Fusion keep their current licenses, and dbt Core will continue to be maintained with the community.
- **Name of the combined company**: not stated in the announcements.

**Why they say they merged.** Handy says the reason is "maturity": both companies "have reached a stage where we have a level of predictability around our existing businesses". He says the deal "has seemed obvious for a while". The shared idea is what they call open data infrastructure: pipelines that "work with any underlying data platform" and do not assume one compute engine. Martin Casado of Andreessen Horowitz, who sits on both boards, says it is "just such an obvious win for everyone involved". Fraser's own post sets the goal as a data platform "for every workload for the next 10 years", with data lakes on open table formats as a priority.

**Why neither company simply bought the other.** The companies don't say this, so the following is my analysis, not fact.

- **No cash price both sides would accept.** Both are private, venture-backed companies, and the announcement gives no split of the $600 million between them. If their sizes are comparable, neither could write a check for the other, and neither set of shareholders would want to be the one that gets acquired. An all-stock merger avoids that argument.
- **dbt's community.** dbt's value rests on an open source community and a neutral stance toward every warehouse. A commercial vendor buying dbt would raise the question of who controls the standard. Handy's promises that dbt stays dbt, and that dbt Core stays open, are aimed at that fear.
- **Fivetran's business model.** In the other direction, dbt Labs buying a large ingestion company would mean taking on a very different sales and pricing model.
- **The same investor on both sides.** With one investor on both boards, the two sides could agree on a structure that an adversarial deal would have made hard.

## Relevant Products and Companies

- [dbt Labs](https://www.getdbt.com/): dbt Core, dbt Fusion and the hosted platform.
- [Fivetran](https://www.fivetran.com/): data movement, and the owner of Census.
- [Andreessen Horowitz](https://a16z.com/): the investor on both boards.

## The Announcements

- [dbt Labs, by Tristan Handy: "dbt Labs + Fivetran: Open data infrastructure for analytics and AI"](https://www.getdbt.com/blog/dbt-labs-and-fivetran-merge-announcement)
- [Fivetran press release: "Fivetran and dbt Labs Unite to Set the Standard for Open Data Infrastructure"](https://www.fivetran.com/press/fivetran-and-dbt-labs-unite-to-set-the-standard-for-open-data-infrastructure-2025)
- [Fivetran, by George Fraser: "The data platform for the next 10 years"](https://www.fivetran.com/blog/the-data-platform-for-the-next-10-years)

---

## Updates

*Late additions, published after the original article and not part of the official announcements.*

### June 2026: the merger closes

Fivetran [announced on June 1, 2026](https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents) that the merger is complete, about seven and a half months after signing. The company initially operates as "Fivetran + dbt Labs", and the final brand name is not stated. Fraser is CEO and Handy is President and Co-Founder. The release says the company serves more than 100,000 data teams. It also announces dbt Core v2.0 in alpha, which open sources the dbt Fusion engine runtime under Apache 2.0.
