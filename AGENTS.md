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
- Acronyms: Spencer prefers hover definitions to using fewer acronyms. Define them with
  kramdown abbreviations at the end of the post (`*[IEA]: International Energy Agency`);
  every occurrence then renders as `<abbr title="…">`. Only add expansions you're sure of.
- Local video: `{% include embed/video.html src='/assets/img/posts/….mp4' poster='/assets/img/posts/….png' title='…' %}`
  (Chirpy's own include; it always shows controls, and `loop=true muted=true autoplay=true`
  are optional).

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

## The AI environmental-impact talk post

`_posts/2026-09-18-ai-environmental-impact.md` is Spencer's AI-PER community meeting
talk (18 Sep 2026) on AI's environmental footprint. It is a transcription of the deck,
not a write-up, and it has rules the other posts don't:

- The text under each slide is that slide's own text, verbatim. Don't paraphrase,
  shorten, tidy or add to it. Every number carries its boundary (a share of what, which
  year, measured or modelled), and dropping a clause changes the claim. The only added
  text is the intro box, structural labels ("Text in the figure:", "Image captions:",
  "Photo caption:") and the closing line.
- Don't add numbers, sources, links or commentary that weren't on a slide. The research
  and source checking live outside this repo, in Spencer's claude.ai Project "Slide for
  Dr. Chen on AI Impact"; a change to any figure starts there.
- No reference list, source table or link to one until Spencer says the
  reference-vetting pass is done. Codes like "P12" on some slides point at that table;
  leave them as they are.
- Never commit the source deck (`ai-footprint-talk-*.pptx`) here: its speaker notes are
  internal working notes and would be published with the site.
- Images: `assets/img/posts/2026-09-18-ai-environmental-impact-NN.png`, NN = slide
  number. Slide 1 (the title) isn't embedded, and `-29` doubles as the post's `image:`.
  They were rendered from the deck at 1920×1080 with LibreOffice, so slides 2–4 and
  30–32 show a substitute for Trebuchet MS; a PowerPoint export (File → Export → PNG)
  can replace them under the same names. Stray `*` characters the deck builder left on
  slides 18 and 22–24 were removed before rendering.
- Slide 3's screen capture is `…-03.mp4`, with `…-03-poster.png` as its poster.
- The `<style>` block at the top lets this post's table cells wrap. Chirpy sets
  `white-space: nowrap` on table cells, which turns sentence-length cells into one very
  long line.

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
