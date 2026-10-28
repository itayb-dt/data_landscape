# QA

Two scripts that check the site without needing a local Jekyll build. Both need Python 3; the first also needs PyYAML (`pip install pyyaml`).

| Script | When to run | What it checks |
|--------|-------------|----------------|
| [check_site.py](check_site.py) | Before every push | The files in the repo |
| [check_live.py](check_live.py) | After every push, once the Pages build is done | The deployed site |

```
python3 qa/check_site.py
python3 qa/check_live.py             # add --external to also check outbound links
```

Exit code 1 means at least one `FAIL`. `WARN` lines are worth reading but do not fail the run.

## check_site.py (before pushing)

- **events.yml**: valid YAML, required fields per type, valid dates, no duplicates, https URLs only.
- **Analysed events**: the `post` file exists, the card fields are present, and `headline` is identical to the article title (a rule from the acquisition prompt).
- **Acquisition articles**: front matter has `title`, the headings appear in the required order (Problem, Solution, Understanding the Acquisition, Relevant Products and Companies), a My Take section exists (warning) and comes before Updates, a lead paragraph comes before the first heading, no deal status heading, `## Updates` carries its "added after" line, and every article has an event pointing to it. Word count is a warning outside 600-1500.
- **Links**: relative Markdown links and `relative_url` targets point to files that exist; no `http://` links.
- **Liquid**: `if`, `for`, `case`, `capture` tags and `{{ }}` / `{% %}` delimiters are balanced in layouts, pages and posts. This catches the typo that would otherwise fail the GitHub build.

## check_live.py (after pushing)

- The latest GitHub Pages build for the commit you are on succeeded (unauthenticated GitHub API; it may say "no build found yet" for the first minute after a push).
- Every page returns HTTP 200: home, All Posts, Random Thoughts and every article.
- No Liquid is left unrendered in the output (`{{` or `{%`).
- Each article's title appears on the page, and a post with `published` shows that date.
- Internal links and images resolve.
- `--external`: outbound links. A 404 or 410 fails; other errors are warnings because many sites block scripts.

## What it does not check

How the page looks. Colors, spacing and the header layout still need a look in the browser. A visual check would need a headless browser (for example Playwright screenshots), which is not set up yet.

## Known warnings

- Seven articles render two `<h1>` elements: the layout title plus a `# heading` in the Markdown body, which CSS hides. Harmless to readers, but worth removing from the Markdown.
- Waii, Dremio and Rockset have no `published` date. Waii has no Funding history section.
- Several older events still carry a `status` field that the site ignores.
