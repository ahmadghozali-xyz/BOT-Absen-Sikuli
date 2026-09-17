# ?? BOT Auto Absen Sikuli UMRI (Headless Mode)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

**BOT Auto Absen Sikuli** adalah solusi cerdas bagi mahasiswa Universitas Muhammadiyah Riau (UMRI) untuk memastikan kehadiran presensi di portal [Sikuli](https://sikuli.umri.ac.id) tetap terjaga secara otomatis. Program ini dirancang untuk berjalan ringan di terminal (layar hitam) tanpa perlu membuka browser (Chrome/Edge), sehingga sangat hemat memori dan bisa aktif 24 jam.

---

## ? Fitur Unggulan

*   **?? Mode Senyap (Headless):** Bekerja di balik layar tanpa membuka jendela browser.
*   **?? Otomatisasi Cerdas:** Mendeteksi jadwal kuliah, ruangan, dan dosen secara otomatis.
*   **? Anti-Ketinggalan:** Melakukan pengecekan ulang (auto-refresh) setiap 30 detik untuk memastikan tidak ada sesi absen yang terlewat.
*   **?? Keamanan Data:** Login dilakukan secara lokal di komputer Anda. Password tidak disimpan secara permanen.
*   **?? Laporan Real-time:** Menampilkan nama mahasiswa, NIM, semester, dan riwayat absen yang berhasil dilakukan.

---

## ??? Persiapan Awal (Sangat Mudah!)

Sebelum memulai, pastikan komputer Anda sudah terpasang Python. Jika belum, download di [python.org](https://www.python.org/downloads/).

1.  **Download Script:** Unduh file `absen.py` dari repository ini.
2.  **Buka Terminal / Command Prompt:** (Cari "cmd" atau "powershell" di menu Start).
3.  **Instal Modul Pendukung:** Ketik perintah berikut dan tekan Enter:
    ```bash
    pip install requests beautifulsoup4
    ```

---

## ?? Cara Menjalankan

Ikuti langkah sederhana ini untuk mulai menggunakan bot:

1.  Masuk ke folder tempat Anda menyimpan script.
2.  Jalankan program dengan mengetik:
    ```bash
    python absen.py
    ```
3.  **Login:** Masukkan NIM dan Password Sikuli Anda saat diminta.
4.  **Selesai!** Biarkan terminal tetap terbuka. Bot akan memantau jadwal Anda secara otomatis.

---

## ?? Contoh Tampilan Output
```text
============================================================
          BOT AUTO ABSEN SIKULI UMRI (CLI VERSION)
============================================================
 Nama Mahasiswa : Ahmad Ghozali
 NIM            : 220401XXX
 Semester       : Semester 4
------------------------------------------------------------
[+] Bot Aktif! Menunggu sesi absen terbuka...
[2026-09-18 08:00:05] [SUCCESS] Absen BERHASIL untuk BAHASA INDONESIA
```

---

## ?? Catatan Penting
*   **Koneksi Internet:** Pastikan perangkat Anda selalu terhubung ke internet.
*   **Terminal:** Jangan menutup jendela terminal agar bot tetap bisa bekerja.
*   **Edukasi:** Program ini dibuat untuk tujuan efisiensi. Tetap utamakan kejujuran akademik.

---

Developed with ?? for UMRI Students.
