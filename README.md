# withemes.github.io

The WiThemes website — static HTML, published with GitHub Pages at
<https://withemes.github.io/>.

## Layout

```
site.toml       site meta, navigation, and the theme catalogue
content/        one markdown file per page
content/themes/ one markdown file per theme (body copy only)
assets/         theme screenshots
style.css       the only stylesheet; inlined into every page at build time
build.py        content/ + site.toml -> docs/
docs/           build output — what GitHub Pages publishes
```

## Building

```
python3 build.py
```

Requires `python-markdown`. The build wipes and rewrites `docs/` every time, so
never edit anything in there by hand.

Preview locally with:

```
python3 -m http.server -d docs
```

## Adding a theme

1. Add a `[[theme]]` block to `site.toml` (slug, name, tagline, group, demo,
   purchase and docs links, screenshot filename).
2. Drop the screenshot into `assets/` under that filename.
3. Write `content/themes/<slug>.md` — front matter plus body copy. The title,
   action buttons and screenshot come from `site.toml`, so the markdown only
   needs the prose.
4. Rebuild and commit.

Theme documentation is a separate project and lives at
<https://themedocs.github.io/>.
