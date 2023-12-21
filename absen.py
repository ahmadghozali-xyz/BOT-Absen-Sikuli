from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Sesuaikan path dengan lokasi ChromeDriver di komputer Anda
driver = webdriver.Chrome(executable_path='path/to/chromedriver')
driver.get('https://sikuli.umri.ac.id/')

# Tunggu hingga elemen dengan ID 'username' tersedia
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'username'))
)

# Tunggu hingga elemen dengan ID 'password' tersedia
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'password'))
)

# Tunggu hingga elemen dengan ID 'id_tombol_absensi' tersedia
absensi_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'id_tombol_absensi'))
)

# Masukkan nama pengguna dan kata sandi
username_input.send_keys('210401225')
password_input.send_keys('lostsaga1234')

# Klik tombol absensi
absensi_button.click()
