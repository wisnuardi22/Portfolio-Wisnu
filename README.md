# Portfolio — Wisnu Ardi Nugroho

Situs portofolio statis (HTML + Tailwind) untuk **wisnuardi22**.
Live: <https://wisnuardi22.github.io/Portfolio-Wisnu/>

## Isi

| Path | Keterangan |
| --- | --- |
| `index.html` | Satu halaman: hero, skills, experience, projects, certificates, footer |
| `assets/tailwind.css` | Tailwind hasil build (JANGAN diedit manual) |
| `assets/img/` | Gambar WebP: `*-thumb.webp` (kartu, maks 900px) dan `*-full.webp` (galeri, maks 1600px) |
| `assets/favicon.svg`, `assets/apple-touch-icon.png`, `assets/og-cover.jpg` | Ikon & gambar preview share |
| `cv-wisnu-ardi-nugroho.pdf` | CV yang diunduh dari tombol "Download CV" |
| `src/input.css` | Sumber Tailwind (`@tailwind base/components/utilities`) |
| `scripts/` | Utilitas build (optimasi gambar, transform HTML, aset) |

## Build CSS (wajib setiap menambah/mengubah class Tailwind)

```bash
npm install -D tailwindcss@3
npx tailwindcss -i src/input.css -o assets/tailwind.css --minify
```

Atau sekali jalan tanpa install:

```bash
npx --yes tailwindcss@3.4.17 -i src/input.css -o assets/tailwind.css --minify
```

Tailwind membaca class dari `index.html` (lihat `tailwind.config.js`). Class baru yang hanya
muncul di JavaScript tetap harus ada di `index.html`, atau tambahkan ke `safelist`.

## Menambah gambar proyek

1. Taruh file asli di `image/`.
2. Jalankan `python scripts/optimize_images.py` (butuh Pillow) → menghasilkan
   `assets/img/<slug>-thumb.webp` dan `<slug>-full.webp`.
3. Rujuk `assets/img/<slug>-thumb.webp` di kartu dan `<slug>-full.webp` di `projectData`.

## Catatan implementasi

- Dark mode memakai atribut `data-theme="dark"` di `<html>` (`darkMode: ["selector", ...]`).
- Tema dan bahasa disimpan di `localStorage` (`theme`, `lang`); bahasa default mengikuti
  `navigator.language`, dengan `en` sebagai fallback.
- Teks dua bahasa memakai atribut `data-i18n` + objek `translations` di dalam `index.html`.
- Gambar non-hero memakai `loading="lazy"`; foto hero `fetchpriority="high"`.

## Deploy

Push ke branch `main`; GitHub Pages menyajikan langsung dari root repo. Tidak ada proses build
di server — CSS harus sudah dibuild sebelum push.
