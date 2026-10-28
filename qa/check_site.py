#!/usr/bin/env python3
"""Static checks. Run from anywhere: python3 qa/check_site.py

Jekyll cannot be built on every machine, so this checks the things that most often break the
site before you push: the events file, front matter, article structure, links between pages,
and Liquid tag balance. It needs only Python 3 and PyYAML.
"""
import re, sys, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors, warnings = [], []


def err(where, msg):
    errors.append(f"{where}: {msg}")


def warn(where, msg):
    warnings.append(f"{where}: {msg}")


def rel(p):
    return str(p.relative_to(ROOT))


def split_front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 5:]


# ---------- events file ----------
events = yaml.safe_load((ROOT / "_data/events.yml").read_text(encoding="utf-8"))
REQUIRED = {"acq": ["acquirer", "target", "value"], "fund": ["company", "stage"]}
CARD = {"acq": ["headline", "tldr", "why"], "fund": ["headline"]}
seen, posts_in_events = set(), {}
for i, e in enumerate(events):
    name = e.get("target") or e.get("company") or f"#{i}"
    where = f"events.yml [{name}]"
    t = e.get("type")
    if t not in REQUIRED:
        err(where, f"type must be acq or fund, got {t!r}")
        continue
    for k in ["date", "when"] + REQUIRED[t]:
        if not e.get(k):
            err(where, f"missing required field '{k}'")
    d = e.get("date")
    if not isinstance(d, datetime.date):
        err(where, f"date is not a valid YYYY-MM-DD date: {d!r}")
    key = (t, e.get("acquirer"), e.get("target"), e.get("company"), e.get("stage"))
    if key in seen:
        err(where, "duplicate event")
    seen.add(key)
    if t == "fund" and isinstance(d, datetime.date) and d < datetime.date.today().replace(year=datetime.date.today().year - 3):
        warn(where, "funding round is older than 3 years; the events file only keeps the last 3 years")
    if not e.get("post") and not e.get("source"):
        warn(where, "has neither 'source' nor 'post'; compact view will have no link")
    for url in [e.get("source")] + [l.get("url") for l in e.get("links", [])]:
        if url and not str(url).startswith("https://"):
            err(where, f"URL is not https: {url}")
    if e.get("post"):
        post = e["post"]
        path = ROOT / (post.lstrip("/").removesuffix(".html") + ".md")
        if post in posts_in_events:
            err(where, f"post {post} is also used by {posts_in_events[post]}")
        posts_in_events[post] = name
        if not path.exists():
            err(where, f"post file not found: {rel(path)}")
            continue
        for k in CARD[t]:
            if not e.get(k):
                err(where, f"analysed event needs card field '{k}'")
        if not e.get("links"):
            warn(where, "analysed event has no 'links' (official announcements)")
        fm, _ = split_front_matter(path)
        if fm and fm.get("title") != e.get("headline"):
            err(where, f"headline differs from article title\n      event:   {e.get('headline')}\n      article: {fm.get('title')}")
        if "status" in e:
            warn(where, "status is ignored by the site; remove it")

# ---------- posts ----------
ACQ_HEADINGS = [
    r"^## The Problem: .+",
    r"^## The Solution: .+",
    r"^### Funding history",
    r"^## Understanding the Acquisition$",
    r"^## Relevant Products and Companies$",
]
post_files = sorted((ROOT / "blog_posts").rglob("*.md"))
for f in post_files:
    where = rel(f)
    fm, body = split_front_matter(f)
    if fm is None:
        err(where, "missing front matter")
        continue
    if not fm.get("title"):
        err(where, "front matter needs a title")
    pub = fm.get("published")
    if pub is not None and not isinstance(pub, datetime.date):
        err(where, f"published must be YYYY-MM-DD, got {pub!r}")
    if f.parent.name == "acq":
        if not pub:
            warn(where, "acquisition posts should have 'published'")
        if f"/blog_posts/acq/{f.stem}.html" not in posts_in_events:
            err(where, "no event in events.yml points to this article")
        pos = 0
        for pat in ACQ_HEADINGS:
            m = re.compile(pat, re.M).search(body, pos)
            if not m and "Funding history" in pat:
                warn(where, "no '### Funding history' section")
            elif not m:
                err(where, f"missing or out-of-order heading matching /{pat}/")
            else:
                pos = m.end()
        if re.search(r"^(##|###) .*\bStatus\b", body, re.M | re.I):
            err(where, "articles must not show deal status")
        first = body.strip().split("\n", 1)[0]
        if first.startswith("#"):
            err(where, "needs a lead paragraph before the first heading")
        if "## Updates" in body and "late additions" not in body.lower() and "added after" not in body.lower():
            err(where, "## Updates needs the italic 'added after the original article' line")
        if not re.search(r"^## My Take$", body, re.M):
            warn(where, "acquisition posts need a '## My Take' section")
        elif "## Updates" in body and body.index("## My Take") > body.index("## Updates"):
            err(where, "## My Take must come before ## Updates")
        words = len(re.sub(r"\s+", " ", body.split("## My Take")[0].split("## Updates")[0]).split())
        if not 600 <= words <= 1500:
            warn(where, f"{words} words (target 700-1200, excluding My Take/Updates)")

# ---------- links and Liquid ----------
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)")
RELURL = re.compile(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}")
permalinks = set()
for f in [ROOT / "index.html", ROOT / "posts.html", ROOT / "random.html", ROOT / "ontology.html"]:
    fm, _ = split_front_matter(f)
    permalinks.add((fm or {}).get("permalink", "/"))
permalinks.add("/")
html_like = list(post_files) + [ROOT / "index.html", ROOT / "posts.html", ROOT / "random.html", ROOT / "ontology.html"] + sorted((ROOT / "_layouts").glob("*.html"))
for f in html_like:
    where = rel(f)
    text = f.read_text(encoding="utf-8")
    # Liquid balance
    for opener, closer in [("if", "endif"), ("for", "endfor"), ("case", "endcase"), ("capture", "endcapture"), ("unless", "endunless")]:
        o = len(re.findall(r"\{%-?\s*" + opener + r"\b", text))
        c = len(re.findall(r"\{%-?\s*" + closer + r"\b", text))
        if o != c:
            err(where, f"Liquid {opener}/{closer} unbalanced ({o} vs {c})")
    if text.count("{%") != text.count("%}") or text.count("{{") != text.count("}}"):
        err(where, "unbalanced Liquid delimiters")
    for target in RELURL.findall(text):
        p = ROOT / target.lstrip("/")
        if target in permalinks:
            continue
        if target.endswith(".html"):
            ok = p.with_suffix(".md").exists() or p.exists()
        else:
            ok = p.exists()
        if not ok:
            err(where, f"relative_url target not found: {target}")
    if f.suffix == ".md":
        for link in MD_LINK.findall(text):
            if re.match(r"(https?:|mailto:|#|\{\{)", link):
                continue
            if link.startswith("http://"):
                err(where, f"non-https link {link}")
            path = (f.parent / link.split("#")[0]).resolve()
            if not path.exists():
                err(where, f"broken relative link: {link}")
        for link in re.findall(r"\]\((http://[^)\s]+)", text):
            err(where, f"non-https link: {link}")

# ---------- config ----------
cfg = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
if not str(cfg.get("baseurl", "")).startswith("/"):
    err("_config.yml", "baseurl should start with /")

# ---------- report ----------
for w in warnings:
    print("WARN ", w)
for e_ in errors:
    print("FAIL ", e_)
print(f"\n{len(events)} events, {len(post_files)} posts checked: {len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
