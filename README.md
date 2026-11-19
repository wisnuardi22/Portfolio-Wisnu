# Portfolio — Wisnu Ardi Nugroho

Situs portofolio statis (HTML + CSS) untuk **wisnuardi22**.
Live: <https://wisnuardi22.github.io/Portfolio-Wisnu/>

Tidak ada framework, tidak ada build step. Satu file HTML, satu file CSS.

## Isi

| Path | Keterangan |
| --- | --- |
| `index.html` | Satu halaman: hero, about, process, experience, projects, certificates, contact, footer |
| `assets/style.css` | Seluruh gaya halaman (hand-written CSS, token warna di `:root`) |
| `assets/img/` | Gambar WebP: `*-thumb.webp` (kartu, maks 900px) dan `*-full.webp` (galeri, maks 1600px) |
| `assets/favicon.svg`, `assets/apple-touch-icon.png`, `assets/og-cover.jpg` | Ikon & gambar preview share |
| `cv-wisnu-ardi-nugroho.pdf` | CV yang diunduh dari tombol "Download CV" |
| `image/` | Gambar sumber (tidak dirujuk langsung oleh halaman) |
| `scripts/` | Skrip satu kali dari migrasi lama (lihat catatan di bawah) |

## Mengubah gaya

Semua di `assets/style.css`. Token warna, font, dan radius ada di blok `:root`; versi gelap di
`[data-theme="dark"]`. Ubah nilainya di situ, bukan di banyak tempat.

- Font: Poppins (400/500/600) untuk teks dan judul; Instrument Serif italic untuk kata aksen.
  Dimuat dari Google Fonts di `index.html`.
- Halaman tidak memakai Tailwind lagi — tidak perlu `npm`/`npx` untuk mengubah tampilan.

## Menambah gambar proyek

1. Taruh file asli di `image/`.
2. Jalankan `python scripts/optimize_images.py` (butuh Pillow) → menghasilkan
   `assets/img/<slug>-thumb.webp` dan `<slug>-full.webp`.
3. Rujuk `assets/img/<slug>-thumb.webp` di kartu, dan daftarkan `<slug>-full.webp` di objek
   `projectData` pada `index.html` untuk galeri.

## Catatan implementasi

- Tema memakai atribut `data-theme="dark"` di `<html>`; pilihan disimpan di `localStorage` (`theme`).
- Bahasa memakai atribut `data-i18n` + objek `translations` di `index.html`; pilihan disimpan di
  `localStorage` (`lang`), default mengikuti `navigator.language` dengan `en` sebagai fallback.
- Judul hero mengandung HTML (`<em>`), ditandai lewat `data-i18n-html` yang di-set oleh skrip.
- Galeri: satu `<div id="gallery">` + data di `projectData`; navigasi keyboard `Esc`, `←`, `→`.
- Nav desktop punya penanda bagian aktif (`IntersectionObserver`); di bawah 720px diganti menu hamburger.
- Gambar non-hero memakai `loading="lazy"`; foto hero `fetchpriority="high"`.
- `scripts/transform.py` dan `scripts/make_assets.py` adalah utilitas satu kali dari migrasi lama.
  Jangan dijalankan ulang — `transform.py` menulis ulang `index.html`.

## Deploy

Push ke branch `main`; GitHub Pages menyajikan langsung dari root repo. Tidak ada proses build di server.
