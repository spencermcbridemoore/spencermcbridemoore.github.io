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

- The post is generated. Don't edit it by hand: the wording lives in
  `tools/talk-post/transcript.md`, and `python tools/talk-post/build_post.py` (run from
  the repo root) writes the post from it. See "How the talk post is built" below.
- The text beside each slide is that slide's own text, verbatim. Don't paraphrase,
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
  All are LibreOffice renders of the deck at 1920×1080. Slides 2–4 and 30–32 were
  rendered on Windows with the real Trebuchet MS (`make_regions.py --write-rendered`);
  the other 25 come from a Linux sandbox that used stand-ins of the same widths for
  Calibri and Cambria. Stray `*` characters the deck builder left on slides 18 and
  22–24 were removed before rendering. Replacing a slide image moves its text, so
  regenerate `regions.json` with it.
- Slide 3's screen capture is `…-03.mp4`, with `…-03-poster.png` as its poster.

### How the talk post is built

Each slide is a `div.sl`: the image in `.sl-fig`, the slide's text in `.sl-txt`, side by
side when the column is wide enough and stacked otherwise. Slides 9 and 10, whose text is
a wide table, get `.sl-stack`, which pins the slide on top instead. Hovering a piece of
text or its place on the slide highlights both: a text element and the empty
`<span class="sl-r">` boxes laid over the image are paired by a shared `data-k` value.

It all comes from `tools/talk-post/`, which is not published (`tools` is excluded in
`_config.yml`):

- `transcript.md`: the plain post, text under each slide. Edit wording here, under the
  rules above, then run `build_post.py`.
- `regions.json`: where each paragraph of native slide text sits on its image, as
  fractions of the slide. `make_regions.py` reads it from the deck's own layout and
  snaps it to the published image.
- `figure-regions.json`: the same for text inside the pictures on slides 7, 9, 12 and
  16, found by text recognition (`make_figure_regions.py`, Windows only). Best effort:
  a line it can't find is simply not linked.
- `style.css`, `script.js`: inlined into the post. The production build joins lines, so
  the script keeps its semicolons and uses no `//` comments. Chirpy sets
  `white-space: nowrap` on table cells; the stylesheet undoes that so sentence-length
  cells wrap.
- `check_post.py`: the post matches the generator's output and carries the transcript's
  text unchanged. With `--html <built page>` it also checks the links on the built page;
  with `--deck <pptx>` it checks the transcript against the deck, word for word (slide
  12's tier tag is deliberately not transcribed).

The two `make_*` scripts need the deck and a scratch folder, both kept outside the repo.
After running either, look at the overlay images it writes before trusting the boxes.

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
