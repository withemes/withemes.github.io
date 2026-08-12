# withemes.github.io

The WiThemes site — thiết kế website & SEO. Static HTML published with GitHub
Pages from `main` at <https://withemes.github.io/>, and served as the same set
of files on <https://withemes.com/>.

The HTML is generated. Do not hand-edit the output directories.

```
_src/build.py     generator: template, header/nav/footer, sitemap, robots
_src/blocks.py    reusable fragments (pricing table, FAQ, steps, boxes)
_src/p_core.py    home, about, service hub, pricing, process, projects, FAQ,
                  contact + thank-you, terms, privacy
_src/p_svc.py     the eight service pages
_src/p_kb.py      knowledge hub + articles
_src/pages.py     the page list, in sitemap order
style-3.css       the only stylesheet
assets/           images
```

Edit the content in `_src/`, then:

```
python3 _src/build.py      # rewrites the HTML, sitemap.xml, robots.txt
python3 -m http.server -d .  # preview at http://localhost:8000
```

Commit and push — live in under a minute.

Old English slugs (`/about/`, `/contact/`, `/projects/`, `/terms/`,
`/privacy/`) are kept as meta-refresh stubs pointing at the Vietnamese ones.

Asset filenames are cache-busted by renaming (the stylesheet is `style-3.css`,
not `style.css`) because withemes.com sits behind a 30-day edge cache.
