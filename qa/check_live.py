#!/usr/bin/env python3
"""Smoke test of the deployed site: python3 qa/check_live.py [--external]

Checks that the latest GitHub Pages build succeeded for the commit you are on, then fetches
every page and looks for the things that break after a deploy: HTTP errors, Liquid that was
never rendered, missing titles, broken internal links and images. With --external it also
checks outbound links (many sites block bots, so those are warnings only).
Uses only the Python standard library. Uses the unauthenticated GitHub API.
"""
import re, subprocess, sys, json, urllib.request, urllib.error
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://itayb-dt.github.io/data_landscape"
REPO = "itayb-dt/data_landscape"
UA = {"User-Agent": "data-landscape-qa/1.0"}
errors, warnings = [], []


def get(url, method="GET"):
    req = urllib.request.Request(url, headers=UA, method=method)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace") if method == "GET" else ""
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # network errors
        return 0, str(e)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.images, self.title, self._in_title, self.h1 = [], [], "", False, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.images.append(a["src"])
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self.h1 += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


# ---- 1. latest Pages build ----
head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
status, body = get(f"https://api.github.com/repos/{REPO}/actions/runs?per_page=10")
if status != 200:
    warnings.append(f"could not read GitHub Actions runs (HTTP {status}); skipping build check")
else:
    runs = json.loads(body)["workflow_runs"]
    mine = [r for r in runs if r["head_sha"] == head]
    if not mine:
        warnings.append(f"no Pages build found yet for {head[:7]}; push it, or wait a minute")
    else:
        r = mine[0]
        if r["status"] != "completed":
            errors.append(f"build for {head[:7]} is still {r['status']}; re-run in a minute")
        elif r["conclusion"] != "success":
            errors.append(f"build for {head[:7]} {r['conclusion']}: {r['html_url']}")
        else:
            print(f"OK   build for {head[:7]} succeeded")

# ---- 2. pages to fetch ----
published = {}
pages = {"/": "Market Moves", "/posts/": "All posts", "/random/": "Random thoughts", "/ontology/": "ONTOLOGY"}
for f in sorted((ROOT / "blog_posts").rglob("*.md")):
    text = f.read_text(encoding="utf-8")
    fm = yaml.safe_load(text[4:text.find("\n---\n", 4)]) or {}
    url_path = "/" + str(f.relative_to(ROOT)).removesuffix(".md") + ".html"
    pages[url_path] = fm.get("title", "")
    if fm.get("published"):
        published[url_path] = fm["published"].strftime("%b %d, %Y")

external = {}
checked = {}
for path, expect in pages.items():
    url = SITE + path
    status, html = get(url)
    if status != 200:
        errors.append(f"{path}: HTTP {status}")
        continue
    p = Page()
    p.feed(html)
    if "{{" in html or "{%" in html:
        errors.append(f"{path}: unrendered Liquid in output")
    if expect and expect.lower() not in html.lower().replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"').replace("’", "'"):
        errors.append(f"{path}: expected text not found: {expect[:60]!r}")
    if path in published and published[path] not in html:
        errors.append(f"{path}: published date {published[path]} is not shown")
    if path.startswith("/blog_posts/") and p.h1 != 1:
        warnings.append(f"{path}: {p.h1} <h1> elements (expected 1)")
    for ref in p.links + p.images:
        if ref.startswith(("mailto:", "#", "javascript:")):
            continue
        target = urljoin(url, ref).split("#")[0]
        if urlparse(target).netloc == urlparse(SITE).netloc:
            if target not in checked:
                checked[target] = get(target, "HEAD")[0] or get(target)[0]
            if checked[target] not in (200, 301, 302):
                errors.append(f"{path}: broken internal link/image {ref} (HTTP {checked[target]})")
        elif ref.startswith("http"):
            external.setdefault(target, path)
    print(f"{'OK  ' if not any(x.startswith(path + ':') for x in errors) else 'FAIL'} {path}")

# ---- 3. outbound links (optional) ----
if "--external" in sys.argv:
    print(f"\nChecking {len(external)} outbound links...")
    for url, src in sorted(external.items()):
        code = get(url, "HEAD")[0]
        if code in (0, 403, 405, 429, 501):
            code = get(url)[0]
        if code == 404 or code == 410:
            errors.append(f"{src}: dead link {url} (HTTP {code})")
        elif code != 200 and not (300 <= code < 400):
            warnings.append(f"{src}: {url} returned HTTP {code} (may block bots)")

for w in warnings:
    print("WARN ", w)
for e in errors:
    print("FAIL ", e)
print(f"\n{len(pages)} pages, {len(checked)} internal targets: {len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
