# 📋 Tentang Project Ini

<p align="center">
  <img src="https://img.shields.io/badge/Versi-2.0-blue?style=for-the-badge" alt="Versi">
  <img src="https://img.shields.io/badge/Terakhir_Diperbarui-2025--09--18-green?style=for-the-badge" alt="Last Updated">
</p>

---

## 🧑‍💻 Tentang Developer

| | |
|---|---|
| **Nama** | Ahmad Ghozali |
| **Status** | Mahasiswa Universitas Muhammadiyah Riau (UMRI) |
| **Program Studi** | Teknik Informatika / Sistem Informasi |
| **GitHub** | [github.com/ahmadghozali-xyz](https://github.com/ahmadghozali-xyz) |

> *"Dibuat oleh mahasiswa, untuk mahasiswa — solusi sederhana masalah sehari-hari di kampus."*

---

## 🎯 Latar Belakang & Motivasi

### 💭 Mengapa Bot Ini Dibuat?

Sebagai mahasiswa aktif, saya sering mengalami masalah berikut:

1. **Lupa Absen** — Sedang fokus mengerjakan tugas, tiba-tiba dosen tutup sesi presensi
2. **Sinyal/Internet Buruk** — Portal Sikuli *loading* lama, saat berhasil dibuka absen sudah ditutup
3. **Jadwal Padat** — Kadang ada jadwal kuliah bertabrakan atau pindah ruangan, sulit memantau semua
4. **Notifikasi Tidak Muncul** — Tidak selalu ada pemberitahuan ketika dosen membuka absen

### 💡 Solusi

Dari permasalahan di atas, lahir ide untuk membuat **bot otomatis** yang:
- ✅ Memantau portal Sikuli secara terus-menerus
- ✅ Langsung mengisi absen begitu sesi dibuka
- ✅ Bekerja di latar belakang tanpa mengganggu aktivitas lain
- ✅ Ringan dan tidak membebani komputer

---

## 🏗️ Arsitektur & Cara Kerja

### 🔄 Alur Sistem (Sederhana)

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   USER      │ ──▶ │    LOGIN    │ ──▶ │  AMBIL      │ ──▶ │   CEK       │
│ Input NIM   │     │ ke Sikuli   │     │  JADWAL     │     │  ABSEN      │
│ + Password  │     │             │     │  MK         │     │  Setiap 30s │
└─────────────┘     └─────────────┘     └─────────────┘     └──────┬──────┘
                                                              │
                                                              ▼
                                                    ┌─────────────────┐
                                                    │  SESI TERBUKA?  │
                                                    └────────┬────────┘
                                                             │
                                               ┌─────────────┴─────────────┐
                                               │                           │
                                               ▼                           ▼
                                        ┌───────────┐              ┌───────────┐
                                        │   YA ✓    │              │   TIDAK ✗ │
                                        └─────┬─────┘              └─────┬─────┘
                                              │                          │
                                              ▼                          ▼
                                       ┌───────────┐              ┌───────────┐
                                       │  ISI      │              │  TUNGGU   │
                                       │  ABSEN    │              │  30       │
               ┌────────────────────────┘   OTOMATIS│              │  DETIK    │
               ▼                         └─────┬─────┘              └─────┬─────┘
        ┌─────────────┐                         │                          │
        │  LAPORAN    │◀────────────────────────┘                          │
        │  SUCCESS    │◀───────────────────────────────────────────────────┘
        └─────────────┘
```

### 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi | Versi |
|-----------|--------|-------|
| **Python** | Bahasa pemrograman utama | 3.8+ |
| **requests** | Library untuk HTTP request (login, ambil halaman) | ≥2.28 |
| **BeautifulSoup4** | Library untuk parsing HTML (baca jadwal, cari form) | ≥4.12 |
| **Regex (re)** | Pola pencarian teks (NIM, ruangan, dosen) | Built-in |
| **getpass** | Input password tersembunyi | Built-in |
| **datetime** | Timestamp untuk log | Built-in |

---

## 📊 Statistik Project

| Metrik | Nilai |
|--------|-------|
| **Bahasa Pemrograman** | Python 100% |
| **Jumlah Baris Kode** | ~230 baris |
| **Ukuran File Utama** | ~7.6 KB |
| **Dependencies Eksternal** | 2 (requests, beautifulsoup4) |
| **Target Platform** | Windows (utama), Linux/macOS (kompatibel) |
| **Lisensi** | MIT Open Source |

---

## 🗺️ Roadmap Pengembangan

### ✅ Selesai (Versi Saat ini)
- [x] Login otomatis ke portal Sikuli
- [x] Ambil data jadwal mahasiswa
- [x] Parse informasi MK (nama, ruangan, dosen, waktu)
- [x] Deteksi link absen/presensi
- [x] Submit absen otomatis
- [x] Auto-refresh setiap 30 detik
- [x] Log real-time ke terminal

### 🚧 Dalam Pengembangan (Coming Soon)
- [ ] **Notifikasi Desktop** — Popup Windows saat absen berhasil
- [ ] **Log File** — Simpan riwayat absen ke file `.txt` / `.csv`
- [ ] **Multi-Akun** — Support beberapa NIM sekaligus
- [ ] **Config File** — Setting eksternal tanpa edit kode (`config.ini`)

### 🔮 Rencana Masa Depan
- [ ] **Versi GUI** — Interface grafis (bukan hanya terminal)
- [ ] **Aplikasi Android** — Versi mobile (Termux/native)
- [ ] **Discord/Telegram Bot** — Notifikasi & kontrol via chat
- [ ] **Web Dashboard** — Pantau status absen via browser
- [ ] **API Public** — Untuk integrasi dengan sistem lain

---

## 🙏 Credit & Terima Kasih

### 📚 Sumber Belajar & Referensi
- [Documentation Python](https://docs.python.org/3/) — Dokumentasi resmi Python
- [Requests Library](https://docs.python-requests.org/) — HTTP for Humans
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) — Parsing HTML mudah
- [Portal Sikuli UMRI](https://sikuli.umri.ac.id) — Sistem informasi kampus

### 🤝 Kontributor

| Kontribusi | Dari |
|------------|------|
| **Ide & Pengembangan Utama** | Ahmad Ghozali |
| **Tester Beta** | *(Terbuka untuk siapa saja)* |
| **Saran & Feedback** | Mahasiswa UMRI |

### 🏫 Institusi

<div align="center">

**Universitas Muhammadiyah Riau**

*Program ini dikembangkan independen dan tidak berafiliasi resmi dengan pihak kampus.*

</div>

---

## 📜 Sejarah Versi (Changelog)

| Versi | Tanggal | Perubahan |
|-------|---------|-----------|
| **v2.0** | 2025-09-18 | ✨ Rewrite ulang kode, parsing HTML lebih robust, README profesional |
| **v1.5** | 2025-xx-xx | 🔧 Perbaikan deteksi form absen, penanganan error lebih baik |
| **v1.0** | 2025-xx-xx | 🎉 Release awal, fitur dasar login + absen otomatis |

---

## 📞 Hubungi Saya

| Platform | Link/Info |
|----------|-----------|
| **GitHub** | [github.com/ahmadghozali-xyz](https://github.com/ahmadghozali-xyz) |
| **Email** | (tersedia via GitHub) |
| **Issues/Bug Report** | [Buka Issue baru](https://github.com/ahmadghozali-xyz/BOT-Absen-Sikuli/issues) |

---

## ⚖️ Legal & Etika

### ✅ Yang Boleh
- Menggunakan untuk keperluan pribadi
- Modifikasi kode untuk kebutuhan sendiri
- Membagikan ke teman satu kelas
- Membuat *fork* dan mengembangkan lebih lanjut

### ❌ Yang Dilarang
- Menjual program ini dalam bentuk apapun
- Mengklaim sebagai milik sendiri tanpa kredit
- Menggunakan untuk kecurangan akademik massal
- Memb reverse-engineer untuk mencuri data orang lain

### ⚠️ Disclaimer

> **Bot ini hanyalah alat bantu.** Kehadiran fisik di kelas tetap yang utama. Gunakan dengan bijak dan tetap prioritaskan pembelajaran. Developer tidak bertanggung jawab atas penyalahgunaan tool ini.

---

<div align="center">

### 🌟 Terima Kasih Telah Menggunakan Bot Ini!

**Made with ❤️ and ☕ by Ahmad Ghozali**

*[UMRI — 2025]*

[⬆️ Kembali ke atas](#--tentang-project-ini-about) · [🏠 Beranda README](./README.md)

</div>
