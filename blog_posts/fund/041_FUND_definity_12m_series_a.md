---
title: "definity raises $12M to use AI agents to optimize and protect Spark data pipelines"
published: 2026-05-02
---
# definity Raises $12M to Use AI Agents to Optimize and Protect Spark Data Pipelines

<p class="disclaimer" style="color:#ff5a5a;font-weight:700;border-left:3px solid #ff5a5a;background:rgba(255,90,90,.1);padding:10px 14px;border-radius:0 8px 8px 0"><strong style="color:#ff5a5a">Disclosure: Dynatrace, where I work, took part in this funding round. I am not involved in the investment in any way. Everything here is my personal opinion and does not represent Dynatrace.</strong></p>

<figure class="shot">
  <img src="{{ '/assets/images/definity/hero.png' | relative_url }}" alt="definity homepage: Agentic Data Engineering for Lakehouse and Spark" loading="lazy">
  <figcaption>The definity homepage. Source: <a href="https://www.definity.ai/">definity</a>.</figcaption>
</figure>

## Technical Overview

- Startup: definity ([definity.ai](https://www.definity.ai/)), Chicago
- Amount Raised: $12M
- Funding Round: Series A, [announced April 29, 2026](https://www.definity.ai/blog/agentic-data-engineering-12m-series-a)
- Main Investors: GreatPoint Ventures (lead), with Dynatrace, StageOne Ventures and Hyde Park Venture Partners
- Problem Area: Cost, reliability and operation of Apache Spark data pipelines

---

## The Problem

Spark runs a large part of the world's data pipelines: nightly jobs that clean, join and aggregate data on a cluster. At scale they are expensive, and in definity's words, [too manual, too reactive and too expensive](https://www.definity.ai/blog/agentic-data-engineering-12m-series-a) to operate.

The usual tools look at a job after it has finished. [VentureBeat](https://venturebeat.com/data/definity-embeds-agents-inside-spark-pipelines-to-catch-failures-before-they-reach-agentic-ai-systems) describes the existing options, such as Datadog, Databricks system tables, Unravel and Acceldata, as reading metrics once the run is over. By then the cluster has been paid for and the bad data has moved on to the next job. Take a pipeline that loads a stale table: it finishes green, and the dashboard that uses it is wrong until someone notices.

---

## How They Solve It

definity puts an agent inside the pipeline. A small JVM agent is installed with [one line of configuration](https://venturebeat.com/data/definity-embeds-agents-inside-spark-pipelines-to-catch-failures-before-they-reach-agentic-ai-systems) in the Spark driver, with no changes to the job's code. While the job runs, it records how the queries execute, memory pressure, data skew, shuffles and infrastructure use, and it works out the lineage between pipelines and tables as it goes.

Because it sits in the run, it can act, not only report. It can change resources during a run, stop a job before bad data spreads, or hold back a downstream pipeline when its input is stale. VentureBeat's example is exactly that: a downstream pipeline stopped because the upstream job had been preempted and its input table was out of date. Root cause analysis and recommendations come on request, when an engineer asks the assistant.

It works on Databricks, AWS EMR, GCP Dataproc and Spark on Kubernetes, in the cloud or on premises. The company says only metadata leaves the customer's environment, and a full on-premises deployment is available.

The results are claims from the company and its customers:

- Nexxen, an ad tech company running Spark on premises, [found 33% of its optimization opportunities in the first week](https://venturebeat.com/data/definity-embeds-agents-inside-spark-pipelines-to-catch-failures-before-they-reach-agentic-ai-systems) and cut the engineering effort spent on troubleshooting and optimization by 70%.
- The company says customers cut platform costs by more than 30% and resolve complex Spark issues ten times faster.

---

## Competitive Landscape

VentureBeat names Datadog, which bought Metaplane, Databricks system tables, Unravel and Acceldata as the alternatives. The difference definity points to is timing: those tools see the run afterwards, and definity says it sees and acts during it.

The agent approach also means definity has to be installed in the customer's Spark environment, which is a bigger step than connecting a tool to a metrics feed.

---

## Previous Rounds and Capital Trajectory

- Series A - Apr 2026 - $12M, led by GreatPoint Ventures - [definity](https://www.definity.ai/blog/agentic-data-engineering-12m-series-a), [StartMidwest](https://www.start-midwest.com/news/chicagos-definity-unveils-agentic-data-engineering-platform-with-12m-series-a)

The company says the round was oversubscribed and brings its total funding to $16.5M. The money goes to "continued development of its agentic capabilities, expansion of ecosystem integrations, and growth of go-to-market operations". It also says revenue tripled over six months.

---

## Founder Background

- **Roy Daniel**, CEO and co-founder.
- **Ohad Raviv**, CTO.
- **Tom Bar-Yacov**, VP R&D.

The company says it "came to life from our own experiences leading enterprise data engineering, platform, and product teams".

---

## Summary

Spark bills grow with the data, and most of the tooling around Spark reports after the job has finished. That works while people run the pipelines. When agents start running them, being told afterwards is too late: someone has to be able to change or stop the job while it runs. definity is one of the new players that put that control inside the pipeline.

---

## My Take

Spark is not going away, and neither are Spark bills. A company that makes the bill smaller has an easy pitch, because a saving is easier to prove than a feature.

---

## Updates

*Late additions, published after the original article and not part of the announcement.*

### August 25, 2026: Databricks Serverless

definity [extended its agentic optimization and observability to Databricks Serverless](https://www.definity.ai/blog/expanding-to-databricks-serverless).
