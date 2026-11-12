# Writing rules for every article

These rules apply to every prompt in this folder. Read them before writing. They win over anything else in a prompt.

## 1. The article contains facts and the author's view, never the research process

Never write about what you could or could not read, find, check or confirm. These phrases and anything like them are banned in an article:

- "I could not read / find / confirm / verify ..."
- "not stated in the sources I could read"
- "I did not find ..." and "I found no ..."
- "the site returned nothing", "the page was not available to me"
- "one headline mentions ... but I could not verify it"
- "according to the sources I read"

The reader does not care what the research looked like. They need what is true.

## 2. Unverified data is left out unless the author approves it

Trusted sources:

- The announcement, the company's own site and blog, and the investors' posts.
- Established news outlets that report first-hand: for example Globes, CTech, TheMarker, Reuters, Bloomberg, TechCrunch, CNBC, The Information. Israeli business press (Globes, CTech, TheMarker) counts as trusted for Israeli companies, and a detail it reports can be used even when the press release omits it.

Not trusted: blogs and small tech sites (Geektime, personal blogs, newsletters), aggregators and trackers (Crunchbase-style pages, Clay, DefiLlama, Tracxn, startupintros), AI-generated news summaries, social posts, and press-release reposts that add their own claims.

Use a fact only if it comes from a trusted source. Everything else is out of the article: single-source numbers, aggregator figures, rumors, headlines you could not open, valuations nobody confirmed, details that two sources disagree on.

If you think a doubtful fact matters, do not put it in the article. Tell the author in your chat message, give the source, and let the author decide. Only after an explicit "yes" does it go in, and then it is labeled with its source ("reported by Globes").

No approval means the fact is ignored.

## 3. Missing information is skipped, not explained

If you have no valuation, no price, no customer name, no license, no date: leave the line or sentence out. Do not write that it is missing.

One exception: when the company itself said something was not disclosed, and that is part of the story, state it as a plain fact about the company: "Databricks did not disclose the price." That is a fact about the deal, not about your research.

## 4. Conflicting sources

Use the primary source (the company announcement). If the conflict changes the meaning of the article, ask the author in your chat message. Do not describe the conflict in the article.

## 5. After writing, report to the author in chat

List what you left out and why (unconfirmed number, conflicting sources, missing source), and ask what to do with each. Keep this out of the article.

## 6. The text must not read as written by an AI

Write like a person who knows the subject and is in a hurry: plain words, short sentences, concrete numbers and names, one idea per paragraph.

Avoid these patterns:

- Narrating your own process in the first person (see rule 1).
- Stacks of hedges: "may", "could potentially", "it appears that", "seems to suggest".
- The contrast formula: "It's not X, it's Y", "less about X, more about Y".
- Lists of exactly three adjectives or three parallel phrases.
- Filler openers and transitions: "Moreover", "Furthermore", "Additionally", "In conclusion", "It's worth noting", "Here's the thing", "Let's dive in".
- Buzzwords: landscape, ecosystem, unlock, leverage, game-changer, robust, seamless, delve, navigate, journey, paradigm shift, "in today's fast-moving world".
- A closing sentence that repeats the article or announces a lesson.
- Strings of rhetorical questions.
- Em dashes. Use a comma, a colon or a new sentence.
- Bold labels at the start of every bullet. Use them only where a reader scans for them.
- Symmetrical, rhythmic sentences that sound good and say little.

Prefer one specific fact to three general statements. If a sentence would fit any company, delete it.

## 7. Titles are plain and cannot be misread

A title says who did what, in one clear sentence. Test it by asking whether a reader could take it to mean something else. "Edelbyte raises $70M from the people who built Kusto" reads as if those people were the investors, so it is wrong. Put background and context in the article, not the title. Funding articles follow `<startup> raises <amount> to <what it does>`.
