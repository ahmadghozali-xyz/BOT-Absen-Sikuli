# BOT Auto Absen Sikuli UMRI (Terminal / Headless)

Bot otomatisasi absen Sikuli UMRI berbasis Terminal (CLI) tanpa membuka browser. Berjalan 24 jam dan melakukan auto-refresh per 30 detik.

## Fitur
- **Headless Mode**: Menggunakan HTTP Requests & BeautifulSoup (ringan, tanpa GUI browser).
- **Interactive Login**: Input NIM & Password langsung di terminal.
- **Informasi Profil**: Menampilkan Nama, NIM, dan Semester Mahasiswa.
- **Scraping Jadwal**: Mengambil detail mata kuliah, ruangan, jadwal, dan dosen pengampu.
- **Auto Detection & Attendance**: Pengecekan otomatis per 30 detik untuk tombol/tautan presensi aktif.
- **Logging Real-time**: Hanya menampilkan log ketika absen berhasil dilakukan.

## Cara Menggunakan

1. **Jalankan Bot**:
   ```bash
   python bot_absen_sikuli.py
   ```
2. **Masukkan NIM & Password** saat diminta di terminal.
3. Biarkan terminal tetap terbuka. Bot akan memantau presensi 24 jam secara otomatis.

