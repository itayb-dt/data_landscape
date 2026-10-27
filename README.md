# data_landscape

A blog about the data landscape from a business perspective: funding rounds, acquisitions, technical concepts, and product reviews — with a focus on the impact of AI on the data industry.

## Blog Post Types

Each post follows a structured prompt template stored in [product/prompts/](product/prompts/). Posts are organized into subfolders under [blog_posts/](blog_posts/) by category.

---

### General — Blog Meta Posts
**Folder:** [blog_posts/general/](blog_posts/general/)

Posts about the blog itself: its purpose, format, and editorial approach. Anything that does not fall into a specific category below goes here.

Example: [001 — About This Blog](blog_posts/general/001_about_this_blog.md)

---

### Random Thoughts
**Folder:** [blog_posts/random/](blog_posts/random/)

Opinions and observations that don't fit a funding round, an acquisition or a product review. Listed under Random Thoughts on the site.

Example: [014 — The Unstoppable Rise of PostgreSQL](blog_posts/random/014_RND_unstoppable_rise_of_postgresql.md)

---

### ACQ — Acquisition Analysis
**Prompt:** [acquisition_blog_post_prompt.md](product/prompts/acquisition_blog_post_prompt.md)
**Folder:** [blog_posts/acq/](blog_posts/acq/)

Covers a company acquisition in the data/AI space. Explains the industry problem the acquired company solves, the strategic rationale for the buyer, and what it means for customers and the broader ecosystem.

Structure: title "X acquires Y to <reason>" → lead paragraph → the problem → the solution (with funding history) → understanding the acquisition → relevant products and companies → my take (optional).

Example: [002 — Waii acquired by Salesforce](blog_posts/acq/002_ACQ_waii_by_salesforce.md), [003 — Dremio acquired by SAP](blog_posts/acq/003_ACQ_dremio_by_sap.md)

---

### CNCPT — Concept Explainer
**Prompt:** [concept_blog_post_prompt.md](product/prompts/concept_blog_post_prompt.md)
**Folder:** [blog_posts/cncpt/](blog_posts/cncpt/)

A structured explainer for a data or AI technical concept aimed at both technical and business readers. Covers what the concept is, what problem it solves, its advantages and tradeoffs, real-world use cases, and a practical decision framework.

Structure: opening context → definition → problem → advantages → use cases → relevant companies → tradeoffs → decision framework → further reading.

Example: [004 — Separation of Storage and Compute](blog_posts/cncpt/004_CNCPT_separation_storage_compute.md)

---

### FUND — Funding Round
**Prompt:** [funding_round_blog_post_prompt.md](product/prompts/funding_round_blog_post_prompt.md)
**Folder:** [blog_posts/fund/](blog_posts/fund/)

Analyzes a startup funding announcement in the data/AI space. Covers the problem the startup addresses, how its technology solves it, how it compares to competitors, and why the round matters strategically.

Structure: technical overview (startup, round, investors) → the problem → how they solve it → competitive landscape → previous rounds → founder background (optional) → why this round matters.

---

### TECHREV — Technology Review
**Prompt:** [tech_review_blog_post_prompt.md](product/prompts/tech_review_blog_post_prompt.md)
**Folder:** [blog_posts/techrev/](blog_posts/techrev/)

A business-focused review of a new technology, product feature, or capability. Translates technical details into business impact — what problem it solves, how it helps the team using it, implementation considerations, and tradeoffs.

Structure: opening context → problem → what it does → how it helps → implementation notes → tradeoffs and limitations → who should care → further reading.

Example: [005 — LangSmith SmithDB Agent Observability](blog_posts/techrev/005_TECHREV_langsmith_smithdb_agent_observability.md)

---

### DB — Database Review
**Prompt:** [db_review_blog_post_prompt.md](product/prompts/db_review_blog_post_prompt.md)
**Folder:** [blog_posts/db/](blog_posts/db/)

An opinionated review of a database product — new release, emerging engine, or a tool worth a closer look. Covers what the database is best suited for, the problems it is designed to solve, how it stacks up against competitors, and a personal take on whether it is worth adopting.

Structure: opening context → what it is → problems it solves → best for → not good for → competitive landscape → my take → further reading.

---

## Writing a New Post

1. Pick the prompt template that matches your post type from [product/prompts/](product/prompts/).
2. Fill in the input variables at the bottom of the prompt.
3. Name the output file using the convention: `NNN_TYPE_short_description.md` (e.g., `006_ACQ_company_x_by_company_y.md`, `007_DB_duckdb_local_analytics.md`).
4. Place the finished post in the matching subfolder under [blog_posts/](blog_posts/).
