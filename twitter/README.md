# Twitter

Threads for X/Twitter, one file per article. This folder is not part of the site.

## Layout

- `prompts/`: one prompt per article type. Read `prompts/_tweet_rules.md` first, it applies to all of them.
- `threads/`: one file per thread, named after the article: `037_ACQ_xata_by_clickhouse.md`.

## Thread file format

```md
---
article: /blog_posts/acq/037_ACQ_xata_by_clickhouse.html
type: acq
status: draft        # draft, ready, posted
posted: 2026-11-11   # fill in when posted
url:                 # link to the thread on X, once posted
---

## 1
Text of the first post.

## 2
Text of the second post.
```

The article link goes into post 1 as a full URL: `https://itayb-dt.github.io/data_landscape` plus the article path.

## Workflow

1. Pick the prompt that matches the article type.
2. Write the thread from the article, not from memory.
3. Save it in `threads/` with `status: draft`.
4. Approve, post, then set `status: posted` with the date and the link to the thread.
