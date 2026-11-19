"""Transformasi index.html: gambar WebP, lazy-load, rel noopener, aria, CV rename."""
import os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(ROOT, "index.html")
html = open(p, encoding="utf-8").read()
orig_len = len(html)
log = []

def slug(name):
    base = os.path.splitext(os.path.basename(name))[0]
    s = base.lower().replace("&", "dan")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "img"

# 1) projectData (galeri) -> versi full
start = html.index("const projectData")
end = html.index("\n      };", start)
block = html[start:end]
def to_full(m):
    ref = m.group(0)
    if "EduTax3" in ref:
        return ref  # ditangani di bawah
    return f"assets/img/{slug(ref)}-full.webp"
block_new = re.sub(r"image/[A-Za-z0-9 _.\-]+", to_full, block)
block_new = re.sub(r',\s*"image/EduTax3\.png"', "", block_new)  # file tidak ada
block_new = block_new.replace('"image/EduTax3.png"', "")
html = html[:start] + block_new + html[end:]
log.append(("galeri -> full webp", block.count("image/")))

# 2) sisanya -> thumb
def to_thumb(m):
    return f"assets/img/{slug(m.group(0))}-thumb.webp"
html, n_thumb = re.subn(r"image/[A-Za-z0-9 _.\-]+", to_thumb, html)
log.append(("html -> thumb webp", n_thumb))

# 3) CV rename
html, n_cv = re.subn(r'CV - Wisnu Ardi Nugroho\.pdf', "cv-wisnu-ardi-nugroho.pdf", html)
log.append(("cv rename", n_cv))

# 4) target=_blank tanpa rel
def fix_blank(m):
    tag = m.group(0)
    if "rel=" in tag:
        return tag
    return tag.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
html, n_blank = re.subn(r'<a\b[^>]*target="_blank"[^>]*>', fix_blank, html)
log.append(("rel noopener", n_blank))

# 5) lazy-load gambar (hero pertama tetap eager)
def fix_img(m):
    tag = m.group(0)
    if "loading=" in tag:
        return tag
    if "foto-wisnu-thumb" in tag:
        return tag.replace("<img", '<img fetchpriority="high" decoding="async"', 1)
    return tag.replace("<img", '<img loading="lazy" decoding="async"', 1)
html, n_img = re.subn(r"<img\b[^>]*>", fix_img, html)
log.append(("lazy img", n_img))

# 6) aria-label tombol galeri & slider
labels = {
    "prevProfileImage()": "Foto profil sebelumnya",
    "nextProfileImage()": "Foto profil berikutnya",
    "closeGallery()": "Tutup galeri",
    "changeImage(-1)": "Gambar sebelumnya",
    "changeImage(1)": "Gambar berikutnya",
}
n_aria = 0
for call, label in labels.items():
    pat = re.compile(r'<button\s+onclick="' + re.escape(call) + r'"')
    def add_aria(m, label=label):
        return m.group(0) + f' aria-label="{label}"'
    html, k = pat.subn(add_aria, html)
    n_aria += k
log.append(("aria tombol", n_aria))

# 7) Sertifikat: tampilkan utuh (bukan crop)
html, n_cert = re.subn(
    r'(src="assets/img/(?:ibm|softskill|hardskill)-thumb\.webp"\s+alt="[^"]*"\s+class=")w-full h-56 object-cover',
    r"\1w-full h-56 object-contain bg-slate-100 dark:bg-slate-900",
    html,
)
log.append(("sertifikat object-contain", n_cert))

open(p, "w", encoding="utf-8", newline="").write(html)
for k, v in log:
    print(f"{k:28s} {v}")
print("len", orig_len, "->", len(html))
print("sisa ref image/ :", len(re.findall(r'image/', html)))
