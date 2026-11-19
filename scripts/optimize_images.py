"""Optimasi gambar: thumb (maks 900px) + full (maks 1600px), format WebP."""
import os, re, sys, json
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "image")
OUT = os.path.join(ROOT, "assets", "img")
os.makedirs(OUT, exist_ok=True)

html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
refs = sorted(set(re.findall(r"image/[A-Za-z0-9 _.\-]+", html)))
print("refs:", len(refs))

def slug(name):
    base = os.path.splitext(os.path.basename(name))[0]
    s = base.lower().replace("&", "dan")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "img"

mapping = {}
total_old = total_new = 0
for ref in refs:
    path = os.path.join(ROOT, ref)
    if not os.path.exists(path):
        print("MISSING:", ref)
        continue
    sl = slug(ref)
    im = Image.open(path)
    if im.mode in ("P", "LA", "RGBA"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    w, h = im.size
    total_old += os.path.getsize(path)
    for kind, maxw, q in (("thumb", 900, 78), ("full", 1600, 82)):
        if w <= maxw:
            out = im
        else:
            out = im.resize((maxw, round(h * maxw / w)), Image.LANCZOS)
        dst = os.path.join(OUT, f"{sl}-{kind}.webp")
        out.save(dst, "WEBP", quality=q, method=6)
        total_new += os.path.getsize(dst)
    mapping[ref] = {"slug": sl, "w": w, "h": h, "orig_kb": round(os.path.getsize(path)/1024)}

json.dump(mapping, open(os.path.join(ROOT, "_imgmap.json"), "w"), indent=1)
print(f"old {total_old/1024/1024:.2f} MB -> new {total_new/1024/1024:.2f} MB for {len(mapping)} images (thumb+full)")
