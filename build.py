#!/usr/bin/env python3
"""
withemes.github.io — static build.

    python3 build.py        site.toml + content/ + assets/ -> docs/

Every page is a markdown file under content/. The theme catalogue lives in
site.toml, which also drives the nav, the listing pages, and the per-theme
action links. Output is plain HTML with one inlined stylesheet: no JS, no
webfonts, no build dependencies beyond python-markdown.
"""

import html
import re
import shutil
import tomllib
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
ASSETS = ROOT / "assets"
BUILD = ROOT / "docs"
STYLE = ROOT / "style.css"

MD = ["extra", "smarty", "attr_list", "sane_lists"]


def load_toml(path):
    with open(path, "rb") as fh:
        return tomllib.load(fh)


def split_front_matter(text):
    """Minimal `key: value` front matter, same dialect as the docs repos."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[3:end].splitlines():
        key, _, value = line.partition(":")
        if key.strip():
            meta[key.strip()] = value.strip().strip("\"'")
    return meta, text[end + 4 :].lstrip("\n")


def minify_css(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s*([{}:;,>])\s*", r"\1", text)
    return text.replace(";}", "}")


def render(text):
    return markdown.markdown(text, extensions=MD)


def esc(value):
    return html.escape(str(value))


class Site:
    def __init__(self):
        cfg = load_toml(ROOT / "site.toml")
        self.meta = cfg["site"]
        self.nav = cfg["nav"]
        self.footer = cfg["footer"]
        self.themes = cfg["theme"]
        self.groups = cfg["group"]
        self.css = minify_css(STYLE.read_text(encoding="utf-8"))
        self.base = self.meta["base"].rstrip("/")
        self.urls = []

    # ------------------------------------------------------------ chrome

    def head(self, *, title, description, url):
        full = title if title == self.meta["name"] else f"{title} — {self.meta['name']}"
        out = [
            "<!doctype html><html lang=en><head><meta charset=utf-8>",
            '<meta name=viewport content="width=device-width,initial-scale=1">',
            f"<title>{esc(full)}</title>",
        ]
        if description:
            out.append(f'<meta name=description content="{esc(description)}">')
        out += [
            f'<link rel=canonical href="{self.base}{url}">',
            f'<meta property="og:title" content="{esc(full)}">',
            f'<meta property="og:url" content="{self.base}{url}">',
            '<meta property="og:type" content="website">',
            '<meta name="twitter:card" content="summary_large_image">',
            f"<style>{self.css}</style>",
        ]
        return "".join(out) + "</head><body>"

    def masthead(self, url, cls):
        links = "".join(
            f'<a href="{item["url"]}"'
            + (" aria-current=page" if url.startswith(item["url"]) and item["url"] != "/" else "")
            + f">{esc(item['title'])}</a>"
            for item in self.nav
        )
        return (
            f'<header class=masthead><div class="{cls}">'
            f'<a class=brand href="/">{esc(self.meta["name"])}</a>'
            f"<nav>{links}</nav>"
            "</div></header>"
        )

    def pagefoot(self, cls):
        links = "".join(f'<a href="{i["url"]}">{esc(i["title"])}</a>' for i in self.footer)
        return (
            f'<footer class=pagefoot><div class="{cls}">'
            f"<nav>{links}</nav>"
            f'<p>© 2013–2026 {esc(self.meta["name"])}. {esc(self.meta["tagline"])}</p>'
            "</div></footer>"
        )

    def write(self, url, *, title, description, body, wide=False, index=True):
        # Header, content and footer share one measure so everything lines up.
        cls = "wrap wide" if wide else "wrap"
        page = (
            self.head(title=title, description=description, url=url)
            + '<a class=skip href="#main">Skip to content</a>'
            + self.masthead(url, cls)
            + f'<main id=main><div class="{cls}">'
            + body
            + "</div></main>"
            + self.pagefoot(cls)
            + "</body></html>"
        )
        target = BUILD / (url.lstrip("/") + "index.html" if url.endswith("/") else url.lstrip("/"))
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf-8")
        if index:
            self.urls.append(url)

    # ------------------------------------------------------------ pieces

    def card(self, theme):
        return (
            f'<a class=card href="/themes/{theme["slug"]}/">'
            f'<span class=shot><img src="/assets/{theme["image"]}" alt="{esc(theme["name"])} '
            f'WordPress theme" loading=lazy width=1200 height=900></span>'
            f'<b>{esc(theme["name"])}</b>'
            f'<span>{esc(theme["tagline"])}</span>'
            f'<span class=tag>{esc(theme["price"])}</span>'
            "</a>"
        )

    def grid(self, themes):
        return f'<div class=grid>{"".join(self.card(t) for t in themes)}</div>'

    def grouped(self):
        out = []
        for key, group in self.groups.items():
            themes = [t for t in self.themes if t["group"] == key]
            if not themes:
                continue
            out.append(
                f"<section class=group><h2>{esc(group['title'])}</h2>"
                f'<p class=note>{esc(group["note"])}</p>{self.grid(themes)}</section>'
            )
        return "".join(out)

    # ------------------------------------------------------------- pages

    def build_page(self, path):
        meta, raw = split_front_matter(path.read_text(encoding="utf-8"))
        title = meta.get("title", path.stem.replace("-", " ").title())
        layout = meta.get("layout", "page")
        url = "/" if path.stem == "index" else f"/{path.stem}/"
        body_md = render(raw)

        if layout == "home":
            body = (
                f'<div class=hero><h1>{esc(meta["headline"])}</h1>{body_md}</div>'
                f"<h2>Themes</h2>{self.grid(self.themes)}"
            )
            self.write(url, title=self.meta["name"], description=meta.get("description", ""),
                       body=body, wide=True)
            return

        if layout == "themes":
            body = f"<h1>{esc(title)}</h1><p class=lede>{body_md[3:-4]}</p>{self.grouped()}"
            self.write(url, title=title, description=meta.get("description", ""),
                       body=body, wide=True)
            return

        updated = f'<p class=updated>Last updated: {esc(meta["updated"])}</p>' if meta.get("updated") else ""
        self.write(url, title=title, description=meta.get("description", ""),
                   body=f"<h1>{esc(title)}</h1>{updated}{body_md}")

    def build_theme(self, theme):
        path = CONTENT / "themes" / f"{theme['slug']}.md"
        meta, raw = split_front_matter(path.read_text(encoding="utf-8"))
        actions = [(theme["get_label"], theme["get"], True), ("Live preview", theme["demo"], False),
                   ("Docs", theme["docs"], False), ("Support", theme["support"], False)]
        buttons = "".join(
            f'<a href="{url}"{" class=primary" if primary else ""}>{esc(label)}</a>'
            for label, url, primary in actions
        )
        body = (
            f'<h1>{esc(theme["name"])}</h1>'
            f'<div class=actions>{buttons}</div>'
            f'<figure class="shot full"><img src="/assets/{theme["image"]}" '
            f'alt="{esc(theme["name"])} WordPress theme" width=1200 height=900></figure>'
            + render(raw)
        )
        self.write(f'/themes/{theme["slug"]}/', title=theme["name"],
                   description=meta.get("description", theme["tagline"]), body=body)

    def build_404(self):
        self.write(
            "/404.html",
            title="Page not found",
            description="",
            body='<h1>Page not found</h1><p>That page has moved or never existed. '
                 '<a href="/">Start from the home page</a>, or browse '
                 '<a href="/themes/">all themes</a>.</p>',
            index=False,
        )

    def build_meta_files(self):
        (BUILD / ".nojekyll").write_text("")
        (BUILD / "robots.txt").write_text(
            f"User-agent: *\nAllow: /\n\nSitemap: {self.base}/sitemap.xml\n"
        )
        entries = "".join(f"<url><loc>{self.base}{u}</loc></url>" for u in sorted(self.urls))
        (BUILD / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            f"{entries}</urlset>"
        )

    def run(self):
        if BUILD.exists():
            shutil.rmtree(BUILD)
        BUILD.mkdir(parents=True)

        for path in sorted(CONTENT.glob("*.md")):
            self.build_page(path)
        for theme in self.themes:
            self.build_theme(theme)

        shutil.copytree(ASSETS, BUILD / "assets")
        self.build_404()
        self.build_meta_files()
        print(f"  {len(self.urls)} pages + 404 · {len(self.themes)} themes")


if __name__ == "__main__":
    Site().run()
