"""Aset tambahan: favicon SVG, apple-touch-icon, og-cover 1200x630."""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
os.makedirs(A, exist_ok=True)

favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#0B0F17"/>
  <path d="M13 20l6.4 24h6.2l6.4-17 6.4 17h6.2L51 20h-6.6l-3.9 17.6L34.6 20h-5.2l-5.9 17.6L19.6 20z" fill="#FFFFFF"/>
  <circle cx="49" cy="15" r="3.2" fill="#3B82F6"/>
</svg>
"""
open(os.path.join(A, "favicon.svg"), "w", encoding="utf-8").write(favicon)

# Apple touch icon 180x180
im = Image.open(os.path.join(ROOT, "image", "FotoWisnu.jpeg")).convert("RGB")
s = min(im.size)
sq = im.crop(((im.width - s) // 2, 0, (im.width + s) // 2, s)).resize((180, 180), Image.LANCZOS)
sq.save(os.path.join(A, "apple-touch-icon.png"), "PNG", optimize=True)

# OG cover 1200x630 dari foto wisuda
src = Image.open(os.path.join(ROOT, "image", "FotoWisuda.jpg")).convert("RGB")
tw, th = 1200, 630
ratio = tw / th
w, h = src.size
if w / h > ratio:
    nw = int(h * ratio)
    box = ((w - nw) // 2, 0, (w + nw) // 2, h)
else:
    nh = int(w / ratio)
    box = (0, 0, w, nh)
cov = src.crop(box).resize((tw, th), Image.LANCZOS)
cov.save(os.path.join(A, "og-cover.jpg"), "JPEG", quality=84, optimize=True, progressive=True)
print("ok", [f for f in sorted(os.listdir(A)) if os.path.isfile(os.path.join(A, f))])
