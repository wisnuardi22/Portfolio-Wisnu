# Catatan Perbaikan — Portfolio-Wisnu

Tanggal: 19 November 2026

Semua perubahan sudah diuji di browser (desktop 1440px, mobile 390px, mode terang & gelap,
lightbox galeri). Tidak ada error console, tidak ada gambar rusak, tidak ada scroll horizontal.

## Yang diperbaiki

### 1. Navigasi mobile (paling penting)
- Sebelumnya: link nav `hidden md:flex` tanpa pengganti → di HP tidak ada navigasi sama sekali.
- Sekarang: tombol hamburger (`#menu-btn`) + panel `#mobile-menu`, dengan ikon ☰/✕,
  `aria-expanded`, `aria-controls`, dan menu otomatis menutup setelah link diklik
  atau saat layar diperbesar ≥768px. Ada tombol "Download CV" di dalam menu.

### 2. Gambar: 9,8 MB → 337 KB
- Semua gambar dikonversi ke WebP, dua ukuran:
  - `assets/img/<slug>-thumb.webp` (maks 900px) untuk kartu & hero
  - `assets/img/<slug>-full.webp` (maks 1600px) untuk galeri/lightbox
- Contoh: `FotoWisuda.jpg` 2,9 MB (6240×4160) → 32 KB (ditampilkan 446px).
- Semua gambar non-hero diberi `loading="lazy" decoding="async"`; foto hero
  `fetchpriority="high"`.
- Total halaman saat dibuka: **±429 KB** (HTML 71 KB + CSS 21 KB + 15 gambar 337 KB).

### 3. Tailwind CDN → CSS hasil build
- `cdn.tailwindcss.com` (±400 KB JS, compiler runtime, memblokir render) diganti
  `assets/tailwind.css` (21 KB, sudah di-minify).
- Sumber: `src/input.css` + `tailwind.config.js` (`darkMode: ["selector", '[data-theme="dark"]']`).
- Cara build ulang ada di README.md.

### 4. SEO & preview tautan
- Tambah `meta description`, `canonical`, Open Graph (og:title/description/image/url),
  Twitter card, `theme-color`, `favicon.svg`, `apple-touch-icon.png`, `og-cover.jpg` (1200×630).
- `<title>` jadi "Wisnu Ardi Nugroho — Accounting, Finance & Data Analytics".

### 5. Bahasa
- `<html lang>` sebelumnya `id` padahal konten default Inggris → sekarang `en`, dan
  diperbarui otomatis saat bahasa diganti.
- Pilihan bahasa disimpan di `localStorage` (key `lang`), default mengikuti
  `navigator.language`; sebelumnya reset ke Inggris tiap reload.
- Label tombol sekarang menampilkan bahasa **tujuan** ("🌐 ID" saat halaman Inggris).
- Key `data-i18n` tetap sama; menu mobile ikut diterjemahkan.

### 6. Aksesibilitas
- `aria-label` untuk tombol ikon: tema, bahasa, hamburger, panah slider, tutup galeri,
  panah galeri.
- Semua `target="_blank"` diberi `rel="noopener noreferrer"` (8 tautan).
- Kontras copyright footer dinaikkan (`text-slate-500` → `text-slate-400`, 4,18:1 → 6,9:1).
- `prefers-reduced-motion` mematikan transisi tema.
- Gambar modal tidak lagi punya `src=""` (sebelumnya muncul sebagai gambar rusak).

### 7. Kartu proyek & sertifikat
- Dua kartu yang belum punya tombol ("CFU Enterprise Dashboard", "Accounts Payable
  Submission Automation") sekarang punya CTA yang membuka galeri — tinggi kartu jadi rata.
- Thumbnail sertifikat memakai `object-contain` + latar netral, jadi seluruh sertifikat
  terlihat (sebelumnya ter-crop `object-cover`).

### 8. Kebersihan repo
- `CV - Wisnu Ardi Nugroho.pdf` → `cv-wisnu-ardi-nugroho.pdf` (tanpa spasi/%20 di URL).
- Tambah `README.md` dan `.gitignore`.
- Skrip bantu dipindah ke `scripts/` (`optimize_images.py`, `transform.py`, `make_assets.py`).
- Referensi `image/EduTax3.png` dihapus karena file tersebut tidak ada (galeri EduTax
  sebelumnya menyertakan gambar rusak).

## Cara memakai

**Opsi A — timpa langsung**
1. Ekstrak zip.
2. Salin seluruh isi folder `Portfolio-Wisnu/` ke repo lokal kamu (timpa `index.html`, tambah
   `assets/`, `src/`, `scripts/`, `tailwind.config.js`, `README.md`, `.gitignore`; hapus
   `CV - Wisnu Ardi Nugroho.pdf` yang lama).
3. `git add -A && git commit -m "Perbaikan tampilan & performa" && git push`.

**Opsi B — cek dulu di lokal**
```bash
cd Portfolio-Wisnu
python -m http.server 8000
# buka http://localhost:8000
```

## Yang belum dikerjakan (opsional)

- Screenshot dashboard putih masih menyala di mode gelap (bisa diberi overlay/border halus).
- Hero punya 3 tombol sejajar; bisa diringkas jadi 2 kalau mau lebih tegas.
- Folder `image/` (sumber asli, 9,8 MB) masih disertakan agar skrip optimasi bisa dijalankan
  ulang. Boleh dihapus dari repo kalau tidak diperlukan — situs tidak merujuknya lagi.

---

## Redesign — 19 November 2026

Seluruh tampilan dibangun ulang. Tailwind dibuang, diganti `assets/style.css` (hand-written CSS).

### Yang berubah
- **Tipografi**: Poppins (400/500/600) untuk teks & judul, Instrument Serif italic hanya untuk
  kata aksen dan nama peran di header. Skala konsisten, lebar baris dibatasi (`66ch` untuk bullet
  pengalaman, `28rem` untuk paragraf pendukung).
- **Palet**: kertas gading `#faf8f3`, tinta `#17160f`, satu aksen hijau tua `#2c5a4a`.
  Mode gelap: `#0d0e0c` / `#f0ede4`. Semua lewat token di `:root` dan `[data-theme="dark"]`.
- **Struktur**: hero dua kolom (teks + foto), strip logo magang, About + tabel fakta,
  Process 5 langkah, Experience dengan logo & periode, Projects 6 kartu, Certificates 3 kartu,
  Contact gelap + footer. Section "Skills" lama dilebur ke About.
- **Navigasi**: penanda bagian aktif (`IntersectionObserver`), menu hamburger < 720px,
  `scroll-padding-top` supaya judul section tidak tertutup header.
- **Aksesibilitas**: kontras teks sekunder dinaikkan, target sentuh ikon ≥ 40px di mobile,
  `skip to content`, `aria-label` pada tombol ikon, dukungan `prefers-reduced-motion`.
- **Tanpa build step**: hapus `tailwind.config.js`, `src/input.css`, `assets/tailwind.css`.
  Cukup edit `index.html` / `assets/style.css` lalu push.

### Ukuran
- `index.html` ± 41 KB, `assets/style.css` ± 14 KB, tanpa JavaScript pihak ketiga.
- Font Google dimuat dengan `display=swap` dan `preconnect`.

### Perbaikan lanjutan — 19 November 2026 (malam)

- **Kontras mode gelap**: blok Contact dan footer sebelumnya hanya mengganti latar
  (`#080907`) tanpa ikut mengganti warna teks, sehingga teks `#0d0e0c` di atas `#080907`
  praktis tidak terbaca. Sekarang pakai token lokal `--c-fg`/`--c-bg` (Contact) dan
  `--f-fg` (footer) yang ikut berganti per tema. Hasil audit: 0 kegagalan kontras WCAG AA
  di mode terang maupun gelap.
- **Header**: nama brand dipaksa satu baris (`white-space: nowrap`) — sebelumnya pecah jadi
  tiga baris dan membuat header 75px. Header kini grid `1fr auto 1fr` sehingga menu benar
  di tengah (terukur 712px dari 712.5px pusat viewport), turun ke `1fr auto` di ≤720px.
- **Sertifikat**: kotak gambar `4/3` diganti `16/9` mengikuti rasio sumber 900×506, jadi
  tidak ada pita kosong di atas-bawah.
- **Headline mobile**: `clamp()` di ≤900px dan ≤390px dikecilkan; `scrollWidth` =
  `innerWidth` di 360px, 390px, dan 1440px.
- Stylesheet sekarang dirujuk dengan `assets/style.css?v=20261119f` agar CDN Pages tidak
  menyajikan versi lama.
