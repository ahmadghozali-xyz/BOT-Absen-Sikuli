# 🎓 BOT Auto Absensi Sikuli UMRI — Versi CLI (Terminal)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Aktif-brightgreen?style=flat-square" alt="Status Aktif">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square&logo=windows&logoColor=white" alt="Platform Windows">
  <img src="https://img.shields.io/badge/Lisensi-MIT-yellow?style=flat-square" alt="Lisensi MIT">
</p>

---

## 📖 Apa Itu Bot Ini?

**BOT Auto Absen Sikuli** adalah program pintar yang membantu mahasiswa **Universitas Muhammadiyah Riau (UMRI)** untuk melakukan presensi otomatis di portal **[Sikuli](https://sikuli.umri.ac.id)**.

> 💡 **Gambaran sederhana:** Bayangkan Anda punya "asisten pribadi" yang setiap 30 detik mengecek apakah dosen sudah membuka sesi absen. Jika ya, asisten tersebut langsung mengisi kehadiran Anda secara otomatis. Anda tinggal menjalankan program ini sekali, lalu biarkan bekerja di latar belakang.

### ✨ Kenapa Menggunakan Bot Ini?

| Tanpa Bot | Dengan Bot |
|-----------|------------|
| Harus buka browser & login manual | Cukup jalankan sekali di terminal |
| Bisa lupa absen jika sibuk | Auto‑deteksi & isi otomatis |
| Harus terus mengecek Sikuli | Bot cek tiap **30 detik** otomatis |
| Boros memori (browser terbuka) | Sangat ringan, seperti notepad |

---

## 🛠️ Persyaratan Sistem

Sebelum memulai, pastikan komputer/laptop Anda memiliki:

| Komponen | Keterangan |
|----------|------------|
| **Python** | Versi 3.8 atau lebih baru ([Download di sini](https://www.python.org/downloads/)) |
| **Koneksi Internet** | Stabil (untuk akses portal Sikuli) |
| **Sistem Operasi** | Windows 10/11 (bisa juga Linux/macOS) |

---

## 📦 Cara Instalasi (Langkah demi Langkah)

### Langkah 1: Download Repository

Klik tombol hijau **\< Code ›** → pilih **Download ZIP**, atau gunakan Git:

```bash
git clone https://github.com/ahmadghozali-xyz/BOT-Absen-Sikuli.git
cd BOT-Absen-Sikuli
```

### Langkah 2: Install Library Pendukung

Buka **Command Prompt** atau **PowerShell**, lalu ketik perintah berikut:

```bash
pip install requests beautifulsoup4
```

> ⚠️ Jika muncul error `pip tidak dikenal`, coba gunakan: `python -m pip install requests beautifulsoup4`

### Langkah 3: Siap Digunakan!

Setelah library terinstall, program siap dijalankan.

---

## 🚀 Cara Menjalankan Program

### ▶️ Jalankan Bot

1. Buka folder tempat menyimpan file `absen.py`
2. Klik kanan pada folder → **"Open in Terminal"** atau **"Buka di Windows PowerShell"**
3. Ketik perintah berikut lalu tekan **Enter**:

```bash
python absen.py
```

### 🔐 Proses Login

Setelah program berjalan, Anda akan diminta memasukkan:

```
============================================================
         LOGIN SIKULI MAHASISWA UMRI (CLI)
============================================================
Masukkan NIM      : [ketik NIM Anda di sini]
Masukkan Password : [ketik password Anda di sini] ← tidak terlihat (aman)
```

> 🔒 **Keamanan:** Password yang Anda ketik **tidak akan tampak** di layar (fitur bawaan Python). Data login hanya digunakan sesaat dan **tidak disimpan** permanen di komputer.

---

## 📸 Contoh Tampilan Program (Screenshot)

### Tampilan Saat Login Berhasil & Menampilkan Jadwal

```
============================================================
          BOT AUTO ABSEN SIKULI UMRI (CLI VERSION)
============================================================
 Nama Mahasiswa : Ahmad Ghozali
 NIM            : 220401XXXX
 Semester       : Semester 5 (Ganjil 2025/2026)
------------------------------------------------------------
[+] Terdeteksi 6 Mata Kuliah pada Jadwal:

  1. Pemrograman Web
     Ruangan : Lab Komputer A101
     Detail  : Senin, 08:00 - 10:00
     Dosen   : Dr. Ahmad Fauzi, M.Kom

  2. Basis Data
     Ruangan : Ruang 203
     Detail  : Senin, 10:00 - 12:00
     Dosen   : Prof. Siti Nurhaliza, M.T

  3. Jaringan Komputer
     Ruangan : Lab Jaringan B205
     Detail  : Selasa, 08:00 - 10:00
     Dosen   : Ir. Budi Setiawan, M.Kom

  ... (dan seterusnya)

============================================================
[+] Bot Absen Aktif! Berjalan 24 jam (Auto refresh per 30s)
[+] Menunggu sesi absen terbuka...
============================================================
```

### Tampilan Saat Absen Berhasil Dilakukan

```
[2026-09-18 07:59:45] [SUCCESS] Absen BERHASIL untuk Pemrograman Web - Senin, 08:00 - 10:00
[2026-09-18 07:59:45] [SUCCESS] Absen BERHASIL untuk Basis Data - Senin, 10:00 - 12:00
[2026-09-18 10:01:02] [SUCCESS] Absen BERHASIL untuk Jaringan Komputer - Selasa, 08:00 - 10:00
[2026-09-18 13:30:15] [SUCCESS] Akses Presensi Berhasil: Kecerdasan Buatan
```

### Tampilan Saat Bot Dihentikan

```
^C
[!] Bot dihentikan oleh pengguna.
```

> 💡 **Tips:** Tekan `Ctrl + C` di keyboard untuk menghentikan bot kapan saja.

---

## 🖼️ Screenshot Asli

<!-- Letakkan screenshot Anda di folder ini -->
<!--
<p align="center">
  <img src="assets/screenshot-login.png" width="700" alt="Tampilan Login">
  <em>Tampilan saat proses login</em>
</p>

<p align="center">
  <img src="assets/screenshot-jadwal.png" width="700" alt="Tampilan Jadwal">
  <em>Tampilan daftar mata kuliah terdeteksi</em>
</p>

<p align="center">
  <img src="assets/screenshot-absen.png" width="700" alt="Tampilan Absen Berhasil">
  <em>Tampilan saat absen berhasil dilakukan</em>
</p>
-->

> 📷 **Cara ambil screenshot:** Tekan `Win + Shift + S` di Windows, lalu potong area terminal yang ingin diabadikan.

---

## ❓ Pertanyaan Umum (FAQ)

<details>
<summary><strong>❓ Apakah aman menggunakan bot ini?</strong></summary>

✅ **Ya, aman.** Program ini hanya melakukan apa yang biasa Anda lakukan secara manual (login → buka halaman → klik tombol absen). Perbedaannya, semuanya dilakukan secara otomatis via *script*. Password Anda tidak disimpan atau dikirim ke mana pun.
</details>

<details>
<summary><strong>❓ Apakah harus menyalakan komputer 24 jam?</strong></summary>

🔄 **Tidak wajib**, tapi disarankan. Bot akan aktif selama program berjalan di terminal. Jika komputer mati / terminal ditutup, bot berhenti. Anda bisa menjalankannya lagi kapan saja.
</details>

<details>
<summary><strong>❓ Kok absennya belum berhasil padahal bot sudah jalan?</strong></summary>

⏱️ Bot mengecek setiap **30 detik**. Absen hanya berhasil jika:
1. Dosen sudah **membuka sesi presensi** di Sikuli
2. Waktu kuliah sudah **mendekati atau sudah masuk** jadwal
3. Koneksi internet Anda stabil

Jika di luar jadwal kuliah, bot akan menunggu dengan status "idle".
</details>

<details>
<summary><strong>❓ Muncul error saat dijalankan?</strong></summary>

🔧 Coba langkah berikut:
1. Pastikan Python terinstall → ketik `python --version` di terminal
2. Pastikan library terinstall → jalankan `pip install requests beautifulsoup4` ulang
3. Cek koneksi internet
4. Pastikan NIM dan password benar
</details>

<details>
<summary><strong>❓ Apakah bisa dijalankan di HP/Android?</strong></summary>

📱 Secara default dirancang untuk **PC/Laptop (Windows)**. Untuk HP Android, Anda bisa menggunakan aplikasi seperti **Termux** + Python, namun memerlukan penyesuaian tambahan.
</details>

---

## ⚙️ Konfigurasi Lanjutan (Opsional)

Jika ingin mengubah pengaturan, edit bagian berikut di file `absen.py`:

| Pengaturan | Nilai Default | Keterangan |
|------------|---------------|------------|
| `time.sleep(30)` | 30 detik | Interval pengecekan jadwal |
| `BASE_URL` | sikuli.umri.ac.id | Alamat portal Sikuli |
| `timeout=10` | 10 detik | Batas waktu tunggu respons server |

---

## 📁 Struktur File Project

```
BOT-Absen-Sikuli/
│
├── absen.py              # File utama program bot
├── README.md             # Dokumentasi ini
├── requirements.txt      # Daftar library (opsional)
└── assets/               # Folder screenshot (opsional)
    ├── screenshot-login.png
    ├── screenshot-jadwal.png
    └── screenshot-absen.png
```

---

## 🐛 Melapor Bug / Saran

Jika menemukan masalah atau memiliki saran, silakan buka **Issue** di repository ini atau hubungi developer:

- **GitHub Issues:** [Klik di sini untuk buat Issue baru](https://github.com/ahmadghozali-xyz/BOT-Absen-Sikuli/issues)

---

## 📜 Lisensi

Project ini bersifat **open-source** under lisensi [MIT License](LICENSE). Bebas digunakan, dimodifikasi, dan disebarluaskan.

---

## ⚠️ Disclaimer

Program ini dibuat untuk tujuan **efisiensi dan pembelajaran**. Pengguna bertanggung jawab penuh atas penggunaan tool ini. Tetap utamakan **kejujuran akademik** dan kehadiran fisik di kelas.

---

<div align="center">

**Dibuat dengan ❤️ untuk Mahasiswa UMRI**

© 2025 Ahmad Ghozali — [GitHub](https://github.com/ahmadghozali-xyz) · [Sikuli UMRI](https://sikuli.umri.ac.id)

</div>

---

## 📖 Dokumen Lainnya

| Dokumen | Deskripsi |
|---------|-----------|
| [**📋 Tentang Project (About)**](./ABOUT.md) | Profil developer, arsitektur sistem, roadmap & sejarah versi |
