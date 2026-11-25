---
title: "Zipher raises $53M to let AI agents run data workloads"
published: 2026-11-26
---
# Zipher Raises $53M to Let AI Agents Run Data Workloads

<figure class="shot">
  <img src="{{ '/assets/images/zipher/hero.png' | relative_url }}" alt="Zipher: Data Infrastructure Built for Agents, by Agents" loading="lazy">
  <figcaption>The Zipher banner. Source: <a href="https://zipher.ai/">Zipher</a>.</figcaption>
</figure>

## Technical Overview

- Startup: Zipher ([zipher.ai](https://zipher.ai/)), founded in 2024, headquartered in New York with offices in Tel Aviv
- Amount Raised: $53M
- Funding Round: Seed and Series A together, [announced November 24, 2026](https://zipher.ai/zipher-is-out-of-stealth-data-infrastructure-for-agents-by-agents/)
- Main Investors: TLV Partners, Maor Investments and Glilot Capital Partners. Angels and advisers include Tomer Shiran (Dremio), Barr Moses and Lior Gavish (Monte Carlo) and Clint Sharp (Cribl), per [SiliconANGLE](https://siliconangle.com/2026/11/24/zipher-lands-53m-to-put-ai-agents-not-data-engineers-in-charge-of-data-workloads/)
- Problem Area: The cost and reliability of running data jobs in the cloud

---

## The Problem

A data job, such as a nightly pipeline that feeds a report, comes with settings: how big a cluster it gets, which engine runs it, when it starts. An engineer picks them once, when the job is written. After that the job runs every night, and nobody goes back to check whether the settings still fit.

Zipher's customers describe the result. OpenWeb, an ad-tech company that ran tens of thousands of Databricks jobs a month, says in its [case study](https://zipher.ai/case-studies/how-openweb-reduced-spend-by-59-with-zipher/) that "clusters often had to be provisioned for peak loads, leading to significant wasted spend during off-peak periods." Yotpo, with about 75,000 scheduled jobs a month, says in [its own](https://zipher.ai/case-studies/yotpo-reduces-costs-by-39-and-boosts-performance-with-zipher-real-time-optimization/) that "our data team cannot chase every job and adjust the configurations." Yotpo had tried the Databricks autoscaler, and its costs kept rising.

AI agents make the problem bigger. Anyone can create a new job in seconds, and agents create them faster than people can tune them. TLV Partners' Shahar Tzafrir puts the bet this way: "Agents are becoming the largest creators of data workloads."

---

## How They Solve It

Zipher puts software agents between the data jobs and the cloud bill. According to its announcement, "customers give Zipher their code, an SLA and a budget." The agents learn each workload and what depends on it. Then they decide how it runs: which engine, hardware and configuration, which framework and language, and when and where. They can go as far as rewriting a job's framework, code and syntax, according to SiliconANGLE.

The company stresses that the agents act. In its words, "Zipher doesn't hand your team a list of recommendations. It acts, before each run and while the workload is running."

It runs on AWS, Azure and Google Cloud. The site lists Spark, Databricks, DuckDB, EMR, Trino and Snowflake, and SiliconANGLE adds Databricks Workflows, Apache Airflow, dbt and Azure Data Factory. Setup connects to an existing data platform "in minutes", with no migration.

Zipher's own claim is that Fortune 500 customers see "40 to 60% cost-efficiency gains, up to 80% better SLA adherence", with results typically within two weeks. The company does not define "cost-efficiency gain."

Three customers, with results published by Zipher or by the customers themselves:

- **OpenWeb:** a 63% cut in AWS compute costs and a 59% cut in Databricks spending. Zipher was connected to Airflow and Terraform within minutes.
- **Yotpo:** a 39% cut in annual Databricks and AWS costs, against a goal of 20%, and "2 weeks from installation to actual savings."
- **Hertz:** Gaurav Rastogi, senior director of enterprise data analytics and BI platforms, says that "depending on the workload, we've seen compute cost reductions in the range of 25% to 40%." The workloads are not described.

### Business model

Zipher is a paid service. The Growth plan is pay as you go with a 30-day free trial. The Enterprise plan has custom pricing, with discounts for volume and long-term commitments, round-the-clock support and a dedicated customer success manager.

---

## Competitive Landscape

The first competitor is the platform itself. Databricks has its own autoscaling, and Yotpo's case study says its costs kept rising even with the Databricks autoscaler on. A tool built into one platform can tune only that platform, while Zipher lists several engines and three clouds.

Among startups, Espresso AI is the closest. It came out of stealth in 2024 with an $11M seed and started with Snowflake costs, then launched an agentic product for Databricks in October 2025, also built around cutting costs without manual work.

The honest comparison is hard to make from the outside. Both companies publish their own savings figures, and the definitions differ.

---

## Previous Rounds and Capital Trajectory

The $53M covers both the seed and the Series A. The announcement reports one number for the two rounds. Zipher was founded in 2024, so the whole sum was raised within about two years.

The company says the money goes to research and development and to building a US enterprise sales team, and to expanding in EMEA, Latin America and Asia-Pacific.

---

## Founder Background

Dan Coster, CEO and co-founder, led a big data analytics unit within the Israeli military's Unit 8200. He holds an M.Sc. in computer science and bioinformatics and is completing a Ph.D. in computer science at Tel Aviv University.

Yoav Gill Ben Ephraim, CTO and co-founder, previously worked at Spott, Microsoft and Forter, according to Zipher's site, and SiliconANGLE adds that he was director of data platform at Payoneer. He studied computer science and statistics at Tel Aviv University and served as an intelligence project manager in Unit 8200.

---

## Summary

Data jobs used to be written by people, who chose the settings once and moved on. When software writes the jobs, the number of jobs grows with no one watching the bill, and tuning by hand cannot keep up. The vendors in this space are now trying to take the decision away from the engineer and give it to an agent, which is told only the deadline and the budget.

---

## My Take

It is hard to fully understand what Zipher does. From the outside, the pitch is autonomy: give it the jobs, a deadline and a budget, and it works out the rest.

What I find interesting is what has changed. Until recently, people wrote data pipelines, and a team could tune the few that mattered. Now AI writes them. There are many more pipelines than before, they handle many more types of data, and the data they process is more complicated. I think that is the new part: nobody can scan all of it by hand anymore. A person cannot look at that many jobs, understand each one and keep the settings right as the data changes. The volume and the variety are beyond what a team handled before, so I think this needs a different approach, and an agent that decides on its own is a reasonable answer.

The Hertz case was the clearest for me. A named customer says compute costs fell by 25 to 40 percent, depending on the workload, and that is a big saving for a company of that size.

I like the direction of almost no work. It connects in minutes, learns the jobs and does its work quietly in the background, with nothing for the data team to run. That helps adoption a lot, because a tool that asks for a project never gets installed.

The company also says results typically show up within two weeks, and that the return is fast. I have no way to check that claim from the outside. If it is true, it is amazing, and it might explain such a big round for a company founded in 2024.

It is also nice to see another team from the Israeli data scene. The founders come out of Unit 8200 and Tel Aviv University, there is an office in Tel Aviv, and three Israeli funds are behind them. The company is headquartered in New York, but the roots are here.
