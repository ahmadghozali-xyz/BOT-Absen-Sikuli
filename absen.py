import sys, time, re, datetime, getpass
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://sikuli.umri.ac.id"
LOGIN_URL = f"{BASE_URL}/auth/aksi/"
SCHEDULE_URL = f"{BASE_URL}/mahasiswa/jadwal"

SESSION = requests.Session()
SESSION.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

def login(nim, password):
    payload = {'nim': nim, 'password': password, 'remember': '1'}
    try:
        resp = SESSION.post(LOGIN_URL, data=payload, allow_redirects=True)
        resp.raise_for_status()
        if "login" in resp.url.lower() or "auth" in resp.url.lower() and "aksi" not in resp.url.lower():
            if "salah" in resp.text.lower() or "gagal" in resp.text.lower():
                return False, "NIM atau Password salah"
            return False, "Login gagal, diperiksa kembali kredensial Anda"
        return True, "Login Berhasil"
    except Exception as e:
        return False, str(e)

def get_student_info():
    try:
        resp = SESSION.get(SCHEDULE_URL)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        nama = "N/A"
        nim = "N/A"
        semester = "N/A"
        
        # Cari info profil di header / sidebar / badge
        profile_box = soup.find(class_=re.compile(r'(user|profile|mahasiswa|biodata)', re.I))
        if profile_box:
            text = profile_box.get_text()
            m_nim = re.search(r'\b\d{7,10}\b', text)
            if m_nim: nim = m_nim.group(0)
            
        # Fallback cari elemen nama / nim / semester
        for el in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'div', 'span']):
            t = el.get_text(strip=True)
            if "Semester" in t and len(t) < 30 and semester == "N/A":
                semester = t
            elif "NIM" in t and len(t) < 40 and nim == "N/A":
                nim = t.replace("NIM", "").strip(" :")
                
        return {'nama': nama, 'nim': nim, 'semester': semester, 'html': resp.text}
    except Exception as e:
        return {'nama': 'Error', 'nim': 'Error', 'semester': 'Error', 'html': ''}

def parse_schedule(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    courses = []
    
    # Cari semua kartu / card / row mata kuliah
    cards = soup.find_all(class_=re.compile(r'(card|box|item|jadwal-item|row)', re.I))
    if not cards:
        cards = soup.find_all('tr')
        
    for c in cards:
        text = c.get_text(" ", strip=True)
        if "Ruangan" in text or "Detail" in text or "Dosen" in text:
            # Parse detail MK
            mk_name = ""
            ruangan = ""
            detail = ""
            dosen = ""
            
            # Cari judul / nama MK
            header = c.find(['h3', 'h4', 'h5', 'h6', 'strong', 'b', 'a'])
            if header:
                mk_name = header.get_text(strip=True)
                
            m_ruang = re.search(r'Ruangan\s*:\s*\[?([^\]\n]+)\]?', text, re.I)
            if m_ruang: ruangan = m_ruang.group(1).strip()
            
            m_detail = re.search(r'Detail\s*:\s*\[?([^\]\n]+)\]?', text, re.I)
            if m_detail: detail = m_detail.group(1).strip()
            
            m_dosen = re.search(r'Dosen\s*(?:Pengampu)?\s*:\s*([^\n]+)', text, re.I)
            if m_dosen: dosen = m_dosen.group(1).strip()
            
            # Cari link absen / presensi jika ada
            absen_link = None
            for a in c.find_all('a', href=True):
                if any(k in a.get_text().lower() or k in a['href'].lower() for k in ['absen', 'presensi', 'hadir', 'masuk']):
                    absen_link = a['href']
                    if not absen_link.startswith('http'):
                        absen_link = BASE_URL + absen_link
                    break
                    
            if mk_name or ruangan or detail:
                courses.append({
                    'mk': mk_name or "Mata Kuliah",
                    'ruangan': ruangan,
                    'detail': detail,
                    'dosen': dosen,
                    'absen_link': absen_link
                })
    return courses

def check_and_do_attendance(courses):
    success_logs = []
    for c in courses:
        if c['absen_link']:
            try:
                # Buka link absen
                resp = SESSION.get(c['absen_link'])
                if resp.status_code == 200:
                    # Cek form submit jika ada
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    form = soup.find('form')
                    if form:
                        action = form.get('action', c['absen_link'])
                        if not action.startswith('http'):
                            action = BASE_URL + action
                        data = {}
                        for inp in form.find_all('input'):
                            if inp.get('name'):
                                data[inp['name']] = inp.get('value', 'hadir')
                        post_resp = SESSION.post(action, data=data)
                        if post_resp.status_code == 200:
                            success_logs.append(f"[SUCCESS] Absen BERHASIL untuk {c['mk']} - {c['detail']}")
                    else:
                        success_logs.append(f"[SUCCESS] Akses Presensi Berhasil: {c['mk']}")
            except Exception as e:
                pass
    return success_logs

def print_header(info):
    print("=" * 60)
    print("          BOT AUTO ABSEN SIKULI UMRI (CLI VERSION)")
    print("=" * 60)
    print(f" Nama Mahasiswa : {info['nama']}")
    print(f" NIM            : {info['nim']}")
    print(f" Semester       : {info['semester']}")
    print("-" * 60)

def main():
    print("=" * 60)
    print("         LOGIN SIKULI MAHASISWA UMRI (CLI)")
    print("=" * 60)
    nim = input("Masukkan NIM      : ").strip()
    password = getpass.getpass("Masukkan Password : ").strip()
    
    print("\n[+] Sedang melakukan login ke Sikuli...")
    ok, msg = login(nim, password)
    if not ok:
        print(f"[-] Login Gagal: {msg}")
        sys.exit(1)
        
    print("[+] Login BERHASIL! Mengambil data profil dan jadwal...\n")
    
    info = get_student_info()
    if info['nim'] == "N/A": info['nim'] = nim
    print_header(info)
    
    courses = parse_schedule(info['html'])
    print(f"[+] Terdeteksi {len(courses)} Mata Kuliah pada Jadwal:\n")
    for idx, c in enumerate(courses, 1):
        print(f"  {idx}. {c['mk']}")
        if c['ruangan']: print(f"     Ruangan : {c['ruangan']}")
        if c['detail']:  print(f"     Detail  : {c['detail']}")
        if c['dosen']:   print(f"     Dosen   : {c['dosen']}")
        print()
        
    print("=" * 60)
    print("[+] Bot Absen Aktif! Berjalan 24 jam (Auto refresh per 30s)")
    print("[+] Menunggu sesi absen terbuka...")
    print("=" * 60)
    
    try:
        while True:
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Fetch jadwal terbaru
            try:
                r = SESSION.get(SCHEDULE_URL, timeout=10)
                if r.status_code == 200:
                    current_courses = parse_schedule(r.text)
                    logs = check_and_do_attendance(current_courses)
                    for log in logs:
                        print(f"[{now_str}] {log}")
            except Exception:
                pass
                
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n[!] Bot dihentikan oleh pengguna.")

if __name__ == "__main__":
    main()
