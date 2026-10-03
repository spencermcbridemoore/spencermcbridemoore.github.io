#!/usr/bin/env python3
"""Generate _posts/2026-09-18-ai-environmental-impact.md from the plain transcript.

    python tools/talk-post/build_post.py            write the post
    python tools/talk-post/build_post.py --check    write nothing; fail if the post on disk is out of date

Inputs, all in this folder:
  transcript.md         the talk as plain text under each slide; the only place the wording lives
  regions.json          where each paragraph of native slide text sits on its slide image
  figure-regions.json   the same for text inside the figure images on slides 7, 9, 12 and 16
  style.css, script.js  inlined into the post

The transcript's lines are passed through untouched. This script only adds wrappers, kramdown
attribute lists (data-k="...") and one empty <span class="sl-r"> per highlighted area of a slide.
A text element and the areas that share its data-k value light up together (see script.js).
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
POST = ROOT / "_posts" / "2026-09-18-ai-environmental-impact.md"

SPACES = dict.fromkeys(map(ord, "\u00a0\u2009\u202f\t\v"), " ")
IAL = re.compile(r"^\{:(.*)\}\s*$")
LIST_ITEM = re.compile(r"^(- |\d+\. )(.*)$")
TABLE_RULE = re.compile(r"\|(\s*:?-+:?\s*\|)+")


def na(s):
    """Text as compared between the deck and the transcript: the deck types its bullets as a
    leading em dash and has a few stray asterisks, neither of which is wording."""
    s = unicodedata.normalize("NFC", s).translate(SPACES)
    s = re.sub(r" +", " ", s).strip()
    s = re.sub(r"^\u2014 ", "", s).replace("*", "")
    return re.sub(r" +", " ", s).strip()


def plain(md):
    """Visible text of one markdown line."""
    return na(re.sub(r"<[^>]+>", "", md))


def gfm_id(text):
    """The id kramdown's GFM parser gives a heading; written out explicitly so adding data-k keeps it."""
    t = re.sub(r"[*_`]", "", text).lower()
    t = re.sub(r"[^\w\- ]", "", t, flags=re.UNICODE)
    return t.replace(" ", "-")


def split_post(text):
    """Front matter, then the body split into sections at the horizontal rules."""
    assert "\r" not in text, "expected LF line endings"
    fm_end = text.index("\n---\n", 4) + 5
    lines = text[fm_end:].split("\n")
    cuts = [i for i, line in enumerate(lines) if line == "---"]
    sections = [lines[a + 1:b] for a, b in zip([-1] + cuts, cuts + [len(lines)])]
    return text[:fm_end], sections


def blocks_of(lines):
    out, i = [], 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        j = i
        while j < len(lines) and lines[j].strip():
            j += 1
        out.append(lines[i:j])
        i = j
    return out


class El:
    """One hoverable element on the text side, with the areas of the slide linked to it."""

    def __init__(self, units):
        self.units = units
        self.paras = []
        self.key = None


def parse(lines, els):
    """Describe a slide's text as nodes, registering its elements in `els` in document order."""
    nodes = []
    for blk in blocks_of(lines):
        ial = None
        if len(blk) > 1 and IAL.match(blk[-1]) and not blk[-1].startswith(">"):
            ial = blk[-1]
            blk = blk[:-1]
        first = blk[0]
        if first.startswith("{%"):
            nodes.append(("liquid", blk))
        elif first.startswith("|"):
            rows = []
            for row in blk:
                if TABLE_RULE.fullmatch(row.strip()):
                    rows.append(("sep", row))
                    continue
                cells = []
                for cell in row.strip()[1:-1].split("|"):
                    parts = re.split(r"<br\s*/?>", cell)
                    part_els = [El([plain(p)]) if plain(p) else None for p in parts]
                    els.extend(e for e in part_els if e)
                    cells.append((cell, parts, part_els))
                rows.append(("row", cells))
            nodes.append(("table", rows, ial))
        elif first.startswith(">"):
            inner = [re.sub(r"^> ?", "", line) for line in blk]
            nodes.append(("quote", parse(inner, els), ial))
        elif LIST_ITEM.match(first):
            items = []
            for line in blk:
                if LIST_ITEM.match(line):
                    items.append([line])
                else:
                    items[-1].append(line)
            parsed = []
            for item in items:
                m = LIST_ITEM.match(item[0])
                e = El([plain(m.group(2))] + [plain(x) for x in item[1:]])
                els.append(e)
                parsed.append((m.group(1), m.group(2), item[1:], e))
            nodes.append(("list", parsed, ial))
        elif first.startswith("### "):
            e = El([plain(first[4:])])
            els.append(e)
            nodes.append(("h3", first, e))
        else:
            # A paragraph links as a whole, or line by line (see line_mode in link_slide).
            per_line = [El([plain(line)]) for line in blk]
            whole = El([plain(line) for line in blk])
            nodes.append(("para", blk, ial, whole, per_line))
            els.append(whole)
            els.extend(per_line)
    return nodes


def merge_ial(ial, key):
    add = f'data-k="{key}"'
    if ial is None:
        return "{: " + add + "}"
    return "{: " + IAL.match(ial).group(1).strip() + " " + add + " }"


def emit(nodes, prefix=""):
    out = []

    def put(line):
        out.append((prefix + line).rstrip() if not line else prefix + line)

    for node in nodes:
        kind = node[0]
        if kind == "liquid":
            continue  # the video include goes after the block, at full width
        if kind == "table":
            _, rows, ial = node
            keys = []
            for row in rows:
                if row[0] == "sep":
                    put(row[1])
                    continue
                cells_out = []
                for cell, parts, part_els in row[1]:
                    real = [e for e in part_els if e is not None]
                    keyed = [e for e in real if e.key]
                    if len(real) >= 2 and keyed:
                        # several slide paragraphs in one cell: each line links on its own
                        lead = re.match(r"^\s*", cell).group(0)
                        trail = re.search(r"\s*$", cell).group(0)
                        segs = []
                        for part, e in zip(parts, part_els):
                            t = part.strip()
                            segs.append(f'<span data-k="{e.key}">{t}</span>' if e is not None and e.key else t)
                        cells_out.append(lead + "<br>".join(segs) + trail)
                        keys.append("-")
                    else:
                        cells_out.append(cell)
                        keys.append(keyed[0].key if keyed else "-")
                put("|" + "|".join(cells_out) + "|")
            if any(k != "-" for k in keys):
                # kramdown cannot put attributes on a cell; script.js hands these out in cell order
                put('{: data-keys="' + " ".join(keys) + '"' + (" " + IAL.match(ial).group(1).strip() if ial else "") + "}")
            elif ial:
                put(ial)
        elif kind == "quote":
            _, inner, ial = node
            for line in emit(inner, ""):
                out.append(prefix + ">" + (" " + line if line else ""))
            if ial:
                put(ial)
        elif kind == "list":
            _, items, ial = node
            for marker, text, cont, e in items:
                put(marker + (f'{{: data-k="{e.key}"}} ' if e.key else "") + text)
                for line in cont:
                    put(line)
            if ial:
                put(ial)
        elif kind == "h3":
            _, line, e = node
            put(line)
            put('{: id="' + gfm_id(line[4:]) + '"' + (f' data-k="{e.key}"' if e.key else "") + "}")
        elif kind == "para":
            _, blk, ial, whole, per_line = node
            if any(e.key for e in per_line):
                for line, e in zip(blk, per_line):
                    m = re.match(r"^(.*?)(  )?$", line)
                    put((f'<span data-k="{e.key}">{m.group(1)}</span>' if e.key else m.group(1)) + (m.group(2) or ""))
                if ial:
                    put(ial)
            else:
                for line in blk:
                    put(line)
                if whole.key:
                    put(merge_ial(ial, whole.key))
                elif ial:
                    put(ial)
        out.append(prefix.rstrip())
    while out and not out[-1].strip():
        out.pop()
    return out


def pct(v):
    return ("%.2f" % (v * 100)).rstrip("0").rstrip(".")


def link_slide(heading, body_lines, entries):
    """Parse one slide's text and attach each region entry ({text, box}) to the element that shows it.
    Returns (title element, all elements, nodes, entries that matched nothing)."""
    els = []
    title = El([plain(heading[3:])])
    els.append(title)
    nodes = parse(body_lines, els)
    para_nodes = [nd for nd in nodes if nd[0] == "para"] + [x for nd in nodes if nd[0] == "quote" for x in nd[1] if x[0] == "para"]
    line_mode = set()
    for nd in para_nodes:  # a paragraph of 3+ hard-broken lines is a list in disguise: link line by line
        if len(nd[1]) >= 3 and all(line.endswith("  ") for line in nd[1][:-1]):
            line_mode.update(id(e) for e in nd[4])
    per_line_ids = {id(e) for nd in para_nodes for e in nd[4]}
    whole_in_line_mode = {id(nd[3]) for nd in para_nodes if any(id(e) in line_mode for e in nd[4])}
    candidates = [e for e in els if not (id(e) in per_line_ids and id(e) not in line_mode) and id(e) not in whole_in_line_mode]
    by_text = defaultdict(deque)
    for e in candidates:
        for unit in e.units:
            by_text[unit].append(e)
    left = []
    for p in entries:
        queue = by_text.get(na(p["text"]))
        if queue:
            queue.popleft().paras.append(p)
        else:
            left.append(p)
    unassigned = []
    ordered = [nd for nd in nodes if nd[0] == "list" and nd[1][0][0][0].isdigit()]
    for p in left:
        t = na(p["text"])
        if re.fullmatch(r"\d", t) and ordered and int(t) <= len(ordered[0][1]):
            ordered[0][1][int(t) - 1][3].paras.append(p)  # the numeral beside a numbered item
            continue
        hit = next((e for e in candidates if len(t) >= 4 and any(t in unit for unit in e.units)), None)
        if hit:
            hit.paras.append(p)  # e.g. two image captions joined on one transcript line
        else:
            unassigned.append(p)
    k = 0
    for e in els:
        if e.paras:
            if e is title:
                e.key = "t"
            else:
                k += 1
                e.key = str(k)
    return title, els, nodes, unassigned


def build(transcript, regions, figure_regions, css, js):
    """Return (post text, per-slide report rows, links: {slide: {key: [linked texts]}})."""
    front, sections = split_post(transcript)
    assert len(sections) == 33, f"expected a title block, 31 slides and a closing block, got {len(sections)} sections"
    report, links = [], {}
    new_sections = []
    for si in range(1, 32):
        n = si + 1
        sec = sections[si]
        heading = next(line for line in sec if line.startswith("## "))
        ii = next(i for i, line in enumerate(sec) if line.startswith("!["))
        image = sec[ii]
        entries = regions.get(str(n), []) + figure_regions.get(str(n), [])
        title, els, nodes, unassigned = link_slide(heading, sec[ii + 1:], entries)
        spans = []
        for e in els:
            for p in e.paras:
                x0, y0, x1, y1 = p["box"]
                spans.append(f'<span class="sl-r" data-k="{e.key}" style="left:{pct(x0)}%;top:{pct(y0)}%;width:{pct(x1 - x0)}%;height:{pct(y1 - y0)}%"></span>')
        # a wide table of sentences does not fit beside the slide: pin the slide on top instead
        wide = any(nd[0] == "table" and max(len(r[1]) for r in nd[1] if r[0] == "row") >= 4 and sum(1 for r in nd[1] if r[0] == "row") >= 4 for nd in nodes)
        out = [""]
        out.append(heading)
        out.append('{: id="' + gfm_id(heading[3:]) + '"' + (' data-k="t"' if title.key else "") + "}")
        out.append("")
        out.append('<div class="sl' + (" sl-stack" if wide else "") + '" markdown="1">')
        out.append('<div class="sl-fig" markdown="1">')
        out.append(image + "".join(spans))
        out.append("</div>")
        out.append('<div class="sl-txt" markdown="1">')
        out.append("")
        out.extend(emit(nodes))
        out.append("")
        out.append("</div>")
        out.append("</div>")
        for nd in nodes:
            if nd[0] == "liquid":
                out.append("")
                out.extend(nd[1])
        out.append("")
        new_sections.append(out)
        links[str(n)] = {e.key: [p["text"] for p in e.paras] for e in els if e.key}
        report.append({"slide": n, "entries": len(entries), "areas": len(spans), "elements": sum(1 for e in els if e.key),
                       "unlinked": [p["text"] for p in unassigned], "stacked": wide})
    head = "\n".join(sections[0])
    assert head.count("<style>") == 1
    head = re.sub(r"<style>.*?</style>", lambda m: "<style>\n" + css.rstrip("\n") + "\n</style>", head, flags=re.S)
    tail_lines = sections[32]
    ai = next(i for i, line in enumerate(tail_lines) if line.startswith("*["))
    tail = "\n".join(tail_lines[:ai] + ["<script>", js.rstrip("\n"), "</script>", ""] + tail_lines[ai:])
    body = "\n---\n".join([head] + ["\n".join(s) for s in new_sections] + [tail])
    return front + body, report, links


def dump_regions(path, data):
    """Write {slide: [{text, box}]} with one entry per line, so diffs stay readable."""
    lines = ["{"]
    slides = sorted(data, key=int)
    for i, n in enumerate(slides):
        lines.append(f' "{n}": [')
        entries = data[n]
        for j, e in enumerate(entries):
            item = json.dumps({"text": e["text"], "box": [round(v, 5) for v in e["box"]]}, ensure_ascii=False)
            lines.append("  " + item + ("," if j < len(entries) - 1 else ""))
        lines.append(" ]" + ("," if i < len(slides) - 1 else ""))
    lines.append("}")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def used_entries(transcript, regions):
    """The subset of `regions` that links to some text in the transcript, plus the rest as (slide, text)."""
    _, sections = split_post(transcript)
    kept, unused = {}, []
    for si in range(1, 32):
        n = str(si + 1)
        sec = sections[si]
        heading = next(line for line in sec if line.startswith("## "))
        ii = next(i for i, line in enumerate(sec) if line.startswith("!["))
        entries = regions.get(n, [])
        _, _, _, unassigned = link_slide(heading, sec[ii + 1:], entries)
        dropped = {id(p) for p in unassigned}
        kept[n] = [p for p in entries if id(p) not in dropped]
        unused.extend((n, p["text"]) for p in unassigned)
    return kept, unused


def load():
    read = lambda name: (HERE / name).read_text(encoding="utf-8")
    return read("transcript.md"), json.loads(read("regions.json")), json.loads(read("figure-regions.json")), read("style.css"), read("script.js")


def main():
    post, report, _ = build(*load())
    for row in report:
        for text in row["unlinked"]:
            print(f"slide {row['slide']}: region not used, no matching text in the transcript: {text[:70]!r}")
    print(f"{sum(r['elements'] for r in report)} text elements linked to {sum(r['areas'] for r in report)} areas on {len(report)} slides;",
          "pinned-on-top layout for slides", ", ".join(str(r["slide"]) for r in report if r["stacked"]) or "none")
    if "--check" in sys.argv:
        current = POST.read_bytes().decode("utf-8").replace("\r\n", "\n")
        if current != post:
            sys.exit(f"{POST.relative_to(ROOT)} is out of date: run tools/talk-post/build_post.py")
        print(f"{POST.relative_to(ROOT)} is up to date")
        return
    with open(POST, "w", encoding="utf-8", newline="\n") as f:
        f.write(post)
    print(f"wrote {POST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
