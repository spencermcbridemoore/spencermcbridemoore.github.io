#!/usr/bin/env python3
"""Find where each paragraph of the deck's native text sits on its slide image -> regions.json

    python tools/talk-post/make_regions.py --deck path/to/deck.pptx --work path/to/scratch-folder

Run from the repo root. The deck and the scratch folder stay OUTSIDE the repo: the deck's speaker
notes are internal, and this script writes a copy of the deck into the scratch folder. It reads
slide text only, never the notes.
Needs python-pptx, pymupdf, opencv-python, numpy, pillow and LibreOffice.

What it does:
  1. copies the deck, removing the stray '*' characters on slides 18 and 22-24 (the published
     images were rendered that way);
  2. lays the copy out to PDF with LibreOffice and renders each page at 1920x1080 (work/pages);
  3. reads the position of every paragraph from the PDF;
  4. snaps each position onto the published slide image in assets/img/posts. Most published images
     were rendered elsewhere with stand-in fonts of the same widths but slightly different vertical
     metrics, so headings and table rows sit a few pixels off the PDF layout. Slides listed in
     RENDERED_HERE are published from this script's own render, so their positions are exact;
  5. writes regions.json (only the paragraphs the transcript shows) and overlay images in
     work/overlays. LOOK AT THE OVERLAYS (sheet-*.png): every box should sit on its text.

With --write-rendered the pages in RENDERED_HERE are also copied over the published images.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

try:
    import pymupdf as fitz
except ImportError:  # older PyMuPDF
    import fitz

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_post as bp  # noqa: E402

W, H = 1920, 1080
IMAGE = "assets/img/posts/2026-09-18-ai-environmental-impact-%02d.png"
STRAY_ASTERISKS = {18, 22, 23, 24}
RENDERED_HERE = {2, 3, 4, 30, 31, 32}  # the Trebuchet MS slides: published from work/pages/pNN.png
BULLETS = {"\u2022", "\u25cf", "\u25cb", "\u25aa", "\u25e6", "\uf0b7", "\u2023"}
QUOTES = {ord("\u201c"): '"', ord("\u201d"): '"', ord("\u2018"): "'", ord("\u2019"): "'"}
SOFFICE = [r"C:\Program Files\LibreOffice\program\soffice.com", "/usr/bin/soffice", "/Applications/LibreOffice.app/Contents/MacOS/soffice"]


def squash(s):
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", s).translate(QUOTES))


def walk(shapes):
    for s in shapes:
        if s.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(s.shapes)
        else:
            yield s


def text_frames(shape):
    """(text frame, [row, column] or None) for a shape."""
    if getattr(shape, "has_table", False) and shape.has_table:
        for ri, row in enumerate(shape.table.rows):
            for ci, cell in enumerate(row.cells):
                yield cell.text_frame, [ri, ci]
    elif getattr(shape, "has_text_frame", False) and shape.has_text_frame:
        yield shape.text_frame, None


def clean_copy(deck, out):
    prs = Presentation(str(deck))
    removed = 0
    for n, slide in enumerate(prs.slides, 1):
        if n not in STRAY_ASTERISKS:
            continue
        for shape in walk(slide.shapes):
            for frame, _ in text_frames(shape):
                for p in frame.paragraphs:
                    for run in p.runs:
                        if "*" in run.text:
                            removed += run.text.count("*")
                            run.text = run.text.replace("*", "")
    prs.save(str(out))
    return removed


def to_pdf(soffice, deck, outdir):
    # LibreOffice's normal profile is used on purpose: a throwaway profile under a long temp path
    # makes soffice crash on Windows.
    subprocess.run([soffice, "--headless", "--norestore", "--convert-to", "pdf", "--outdir", str(outdir), str(deck)], check=True, capture_output=True)
    pdf = outdir / (deck.stem + ".pdf")
    if not pdf.exists():
        sys.exit("LibreOffice did not produce a PDF")
    return pdf


def paragraphs_of(slide, sw, sh):
    out = []
    for si, shape in enumerate(walk(slide.shapes)):
        sbox = (shape.left / sw, shape.top / sh, (shape.left + shape.width) / sw, (shape.top + shape.height) / sh) if shape.width is not None else None
        for frame, cell in text_frames(shape):
            for p in frame.paragraphs:
                if p.text.strip():
                    out.append({"text": p.text.replace("\v", " "), "shape": si, "sbox": sbox, "cell": cell, "box": None})
    return out


def locate(paras, page):
    """Give each paragraph the union box of its words in the PDF, as fractions of the page."""
    pw, ph = page.rect.width, page.rect.height
    words = [w for w in page.get_text("words", sort=False) if w[4].strip() and w[4].strip() not in BULLETS]
    chunks, owner = [], []
    for wi, w in enumerate(words):
        t = squash(w[4])
        chunks.append(t)
        owner.extend([wi] * len(t))
    pagestr = "".join(chunks)
    starts, pos = set(), 0
    for t in chunks:
        starts.add(pos)
        pos += len(t)
    ends = set(starts) | {len(pagestr)}
    used = [False] * len(words)
    for p in paras:
        key = squash(p["text"])
        if not key:
            continue
        cands = []
        i = pagestr.find(key)
        while i != -1:
            j = i + len(key)
            if i in starts and j in ends:
                wis = sorted(set(owner[i:j]))
                if not any(used[k] for k in wis):
                    x0 = min(words[k][0] for k in wis) / pw
                    y0 = min(words[k][1] for k in wis) / ph
                    x1 = max(words[k][2] for k in wis) / pw
                    y1 = max(words[k][3] for k in wis) / ph
                    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
                    sb = p["sbox"]
                    inside = sb is not None and sb[0] - 0.03 <= cx <= sb[2] + 0.03 and sb[1] - 0.05 <= cy <= sb[3] + 0.25
                    cands.append((0 if inside else 1, i, wis, [x0, y0, x1, y1]))
            i = pagestr.find(key, i + 1)
        if cands:
            cands.sort(key=lambda c: (c[0], c[1]))
            for k in cands[0][2]:
                used[k] = True
            p["box"] = cands[0][3]
    return [p["text"] for p in paras if p["box"] is None]


def edges(rgb):
    g = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY).astype(np.float32)
    gx = cv2.Sobel(g, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(g, cv2.CV_32F, 0, 1, ksize=3)
    return cv2.GaussianBlur(cv2.magnitude(gx, gy), (0, 0), 2.0)


def ink_bbox(img, x0, y0, x1, y1):
    """Tight box around whatever differs from the window's dominant colour; also returns that colour."""
    win = img[y0:y1, x0:x1].astype(np.int16)
    if win.size == 0:
        return None, None
    flat = win.reshape(-1, 3)
    q = (flat // 16).astype(np.int32)
    codes = q[:, 0] * 256 + q[:, 1] * 16 + q[:, 2]
    bg = flat[codes == np.bincount(codes).argmax()].mean(axis=0)
    ys, xs = np.where(np.abs(win - bg).sum(axis=2) > 110)
    if len(xs) < 6:
        return None, bg
    return [x0 + int(xs.min()), y0 + int(ys.min()), x0 + int(xs.max()) + 1, y0 + int(ys.max()) + 1], bg


def snap(n, paras, ren, pub):
    """Move each box from the PDF layout onto the published image; returns notes worth a look."""
    exact = n in RENDERED_HERE
    e_ren, e_pub = edges(ren), edges(pub)
    flagged = []

    def pixel_box(p):
        x0, y0, x1, y1 = [int(round(v)) for v in (p["box"][0] * W, p["box"][1] * H, p["box"][2] * W, p["box"][3] * H)]
        return max(0, x0 - 2), max(0, y0 - 2), min(W, x1 + 2), min(H, y1 + 2)

    for p in paras:  # 1: where does the rendered text patch best match the published image?
        if p["box"] is None:
            continue
        x0, y0, x1, y1 = pixel_box(p)
        dx = dy = 0
        score = 1.0
        if not exact:
            # a moderate search window first; widen only when the best match sits on its edge
            for mx, my in ((30, 48), (30, 120)):
                sx0, sy0, sx1, sy1 = max(0, x0 - mx), max(0, y0 - my), min(W, x1 + mx), min(H, y1 + my)
                tpl, srch = e_ren[y0:y1, x0:x1], e_pub[sy0:sy1, sx0:sx1]
                if tpl.std() < 1e-3 or srch.shape[0] < tpl.shape[0] or srch.shape[1] < tpl.shape[1]:
                    score = 0.0
                    break
                res = cv2.matchTemplate(srch, tpl, cv2.TM_CCOEFF_NORMED)
                yy, xx = np.indices(res.shape)
                ddx, ddy = xx + sx0 - x0, yy + sy0 - y0
                pen = res - 0.0015 * (np.abs(ddx) + np.abs(ddy))  # prefer small shifts when scores tie
                iy, ix = np.unravel_index(np.argmax(pen), res.shape)
                dx, dy, score = int(ddx[iy, ix]), int(ddy[iy, ix]), float(res[iy, ix])
                if abs(dy) < my - 2:
                    break
        p["_s"] = (dx, dy, score)
    rows = {}  # 2: cells of one table row move together (near-identical rows can fool the matching)
    for p in paras:
        if p["cell"] and p.get("_s"):
            rows.setdefault((p["shape"], p["cell"][0]), []).append(p)
    for members in rows.values():
        med = float(np.median([m["_s"][1] for m in members]))
        for m in members:
            if abs(m["_s"][1] - med) > 6:
                flagged.append(f"{m['text'][:38]!r}: row-consistency, dy {m['_s'][1]} -> {int(round(med))}")
                m["_s"] = (m["_s"][0] if abs(m["_s"][0]) < 8 else 0, int(round(med)), m["_s"][2])
    shifts = []
    for p in paras:  # 3: tighten to the ink actually there, then pad
        if p["box"] is None:
            continue
        x0, y0, x1, y1 = pixel_box(p)
        dx, dy, score = p.pop("_s")
        sx0, sy0, sx1, sy1 = x0 + dx, y0 + dy, x1 + dx, y1 + dy
        wx0, wx1 = max(0, sx0 - 3), min(W, sx1 + 3)
        ib, bg = ink_bbox(pub, wx0, max(0, sy0 - 3), wx1, min(H, sy1 + 3))
        if ib is not None and not exact:
            # the published font can be a little wider: where the text runs into the edge of the
            # window, keep going until there is a clear 10px gap in the same background colour
            band = pub[max(0, ib[1]):min(H, ib[3])].astype(np.int16)
            for side, step in ((0, -1), (2, 1)):
                touching = (ib[0] - wx0 <= 2) if side == 0 else (wx1 - ib[2] <= 2)
                if not touching:
                    continue
                edge, gap, grown = ib[side], 0, 0
                x = edge - 1 if side == 0 else edge
                while 0 <= x < W and grown < 70 and gap < 10:
                    d = np.abs(band[:, x] - bg).sum(axis=1)
                    if (d > 110).sum() >= 2 and (d > 110).mean() < 0.9:  # some ink, not a change of fill
                        edge, gap = (x if side == 0 else x + 1), 0
                    elif (d > 110).mean() >= 0.9:
                        break  # ran into a different background
                    else:
                        gap += 1
                    x += step
                    grown += 1
                ib[side] = edge
        if ib is None:
            ib = [sx0, sy0, sx1, sy1]
            flagged.append(f"{p['text'][:38]!r}: no ink found")
        px, py = 7, 5
        p["box"] = [round(max(0, ib[0] - px) / W, 5), round(max(0, ib[1] - py) / H, 5), round(min(W, ib[2] + px) / W, 5), round(min(H, ib[3] + py) / H, 5)]
        shifts.append((dx, dy))
        if score < 0.35:
            flagged.append(f"{p['text'][:38]!r}: weak match {score:.2f}, shift ({dx},{dy})")
        elif abs(dy) >= 118 or abs(dx) >= 29:
            flagged.append(f"{p['text'][:38]!r}: shift at the search limit ({dx},{dy})")
    return shifts, flagged


def overlay(pub, paras, path):
    ov = pub.copy()
    colours = [(230, 60, 60), (40, 120, 230), (30, 160, 70), (220, 140, 0), (150, 60, 200)]
    for i, p in enumerate(paras):
        if p["box"] is None:
            continue
        b = p["box"]
        cv2.rectangle(ov, (int(b[0] * W), int(b[1] * H)), (int(b[2] * W), int(b[3] * H)), colours[i % 5], 3)
    Image.fromarray(ov).save(path)


def contact_sheets(folder, numbers, prefix="s"):
    for si in range(0, len(numbers), 4):
        sheet = np.full((H, W, 3), 255, np.uint8)
        for j, n in enumerate(numbers[si:si + 4]):
            im = cv2.resize(np.array(Image.open(folder / f"{prefix}{n:02d}.png").convert("RGB")), (W // 2, H // 2), interpolation=cv2.INTER_AREA)
            cv2.putText(im, str(n), (8, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255), 3)
            y, x = (j // 2) * (H // 2), (j % 2) * (W // 2)
            sheet[y:y + H // 2, x:x + W // 2] = im
        Image.fromarray(sheet).save(folder / f"sheet-{si // 4 + 1}.png")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--deck", required=True, help="the talk's .pptx; keep it outside the repo")
    ap.add_argument("--work", required=True, help="scratch folder outside the repo")
    ap.add_argument("--soffice", help="path to LibreOffice's soffice executable")
    ap.add_argument("--reuse-pdf", action="store_true", help="skip steps 1-2 and use the PDF already in the scratch folder")
    ap.add_argument("--write-rendered", action="store_true", help="copy the RENDERED_HERE pages over the published images")
    args = ap.parse_args()
    work = Path(args.work).resolve()
    if bp.ROOT == work or bp.ROOT in work.parents:
        sys.exit("--work must be outside the repo: it will hold a copy of the deck")
    for sub in ("pages", "overlays"):
        (work / sub).mkdir(parents=True, exist_ok=True)
    clean = work / "deck-clean.pptx"
    pdf = work / "deck-clean.pdf"
    if not args.reuse_pdf:
        print("stray asterisks removed:", clean_copy(args.deck, clean))
        soffice = args.soffice or shutil.which("soffice") or next((s for s in SOFFICE if Path(s).exists()), None)
        if not soffice:
            sys.exit("LibreOffice not found; pass --soffice")
        to_pdf(soffice, clean, work)
    prs = Presentation(str(clean))
    doc = fitz.open(str(pdf))
    found = {}
    print("slide | paragraphs | not located | max |dx| | max |dy| | notes")
    notes = []
    for n, slide in enumerate(prs.slides, 1):
        page = doc[n - 1]
        pix = page.get_pixmap(matrix=fitz.Matrix(W / page.rect.width, H / page.rect.height), alpha=False)
        ren = np.frombuffer(pix.samples, dtype=np.uint8).reshape(H, W, 3).copy()
        Image.fromarray(ren).save(work / "pages" / f"p{n:02d}.png")
        if n == 1:
            continue  # the title slide is not in the post
        if args.write_rendered and n in RENDERED_HERE:
            shutil.copyfile(work / "pages" / f"p{n:02d}.png", bp.ROOT / (IMAGE % n))
        pub = ren if n in RENDERED_HERE else np.array(Image.open(bp.ROOT / (IMAGE % n)).convert("RGB"))
        paras = paragraphs_of(slide, prs.slide_width, prs.slide_height)
        missing = locate(paras, page)
        shifts, flagged = snap(n, paras, ren, pub)
        overlay(pub, paras, work / "overlays" / f"s{n:02d}.png")
        found[str(n)] = [{"text": p["text"], "box": p["box"]} for p in paras if p["box"] is not None]
        a = np.array(shifts) if shifts else np.zeros((1, 2))
        print(f"{n:5d} | {len(paras):10d} | {len(missing):11d} | {int(np.abs(a[:, 0]).max()):8d} | {int(np.abs(a[:, 1]).max()):8d} | {len(flagged) + len(missing)}")
        notes += [f"slide {n}: {f}" for f in flagged] + [f"slide {n}: not located: {t[:50]!r}" for t in missing]
    for line in notes:
        print(line)
    contact_sheets(work / "overlays", list(range(2, len(prs.slides) + 1)))
    kept, unused = bp.used_entries((bp.HERE / "transcript.md").read_text(encoding="utf-8"), found)
    for n, text in unused:
        print(f"slide {n}: left out, not in the transcript: {text[:50]!r}")
    bp.dump_regions(bp.HERE / "regions.json", kept)
    print(f"wrote regions.json: {sum(len(v) for v in kept.values())} paragraphs. Now look at {work / 'overlays'} (sheet-*.png).")


if __name__ == "__main__":
    main()
