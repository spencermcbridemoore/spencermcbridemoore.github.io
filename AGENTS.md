# Blog maintenance notes

Personal blog at https://spencermcbridemoore.github.io — Jekyll with the Chirpy theme
(gem `jekyll-theme-chirpy ~> 7.3`). Most posts are write-ups of slide presentations
(physics, quantum computing, numerical methods, ML/LLM interpretability).

**Pushing to `main` publishes.** `.github/workflows/pages-deploy.yml` builds and deploys
to GitHub Pages on every push to `main`. Commit and push only when asked.

## Writing a post

File: `_posts/YYYY-MM-DD-slug.md`. The URL is `/YYYY/MM/DD/` (set in `_config.yml`
defaults) — don't change the permalink scheme, it would break existing links.

Front matter, as used by existing posts:

```yaml
---
title: "..."
author: Spencer Moore
date: YYYY-MM-DD
math: true                 # only when the post has LaTeX
categories: [machine learning, LLM]
tags: [...]
description: "..."         # one line; shown in the post list and link previews
image: /assets/img/posts/YYYY-MM-DD-slug-NN.png   # home-page thumbnail + social card
---
```

- Reuse existing categories where they fit: `hackathon`, `quantum computing`,
  `Unreal Engine`, `Education`, `numerical`, `quantum`, `machine learning`, `LLM`.
- Every post should have `image:` — it's what shows as the thumbnail on the home page.
- Presentation posts: one slide image per section, a `##` heading, a few paragraphs of
  commentary, sections separated by `---`. Don't embed the title slide; use a markdown
  `#` heading instead.

## Images

- Store in `assets/img/posts/`, named `YYYY-MM-DD-slug-NN.png` (NN = slide number).
  Older posts use other names; leave them.
- Always reference with absolute, forward-slash paths: `![Alt text](/assets/img/posts/...)`.
  Relative (`../assets/...`) or backslash (`..\assets\...`) paths break on the built site.
- About-page images go in `assets/img/about/`.

## Math

Set `math: true`. Use `$...$` inline and `$$` on their own lines (blank line before and
after) for display equations. `\(...\)` / `\[...\]` delimiters do not render here.
`_posts/2025-12-01-map6197-base-vs-sft.md` is a working reference.

## Hover-to-switch slide widget

`_posts/2026-02-09-cot-faithfulness.md` groups related slides into a tab strip where
hovering a tab swaps the image. It is entirely inline in that post, not a shared include:
a `<style>` block at the top, a `<div class="slide-switcher">` block per section, and a
`<script>` at the bottom. To reuse it in another post, copy all three parts.

## Tabs (About, Archives, Categories, Tags)

- Live in `_tabs/`. The tab default permalink in `_config.yml` is `/:year/:month/:title/`,
  so each tab sets an explicit `permalink:` (e.g. `/about/`). A new tab needs one too.
- `_tabs/about.md`: the commented-out blocks are placeholders waiting on real photos/text,
  not dead code — leave them unless asked.

## Local preview

```bash
git submodule update --init   # assets/lib (chirpy-static-assets)
bundle install
bash tools/run.sh             # http://127.0.0.1:4000
bash tools/test.sh            # production build + html-proofer link check
```

## Repo files that aren't site content

Root-level files Jekyll shouldn't publish (like this one and `CLAUDE.md`) must be listed
under `exclude:` in `_config.yml`.
