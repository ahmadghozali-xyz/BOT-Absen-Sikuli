from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def bot_absen_sikuli(username, password, url):
    # Sesuaikan path dengan lokasi ChromeDriver di komputer Anda
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    driver.get(url)

    # Tunggu hingga elemen dengan ID 'username' tersedia
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

    # Tunggu hingga elemen dengan ID 'password' tersedia
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )

    # Tunggu hingga elemen dengan teks 'MASUK' tersedia
    masuk_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'MASUK')]"))
    )

    # Masukkan NIM dan kata sandi
    username_input.send_keys(NIM)
    password_input.send_keys(password)

    # Klik tombol MASUK
    masuk_button.click()

    # Jika diperlukan, tambahkan langkah-langkah absen berikutnya sesuai kebutuhan

    # Tutup browser setelah selesai
    driver.quit()

    # Ganti dengan informasi login Anda
    bot_absen_sikuli(username='NIM', password='password',

    # Tidur pun nyenyak tanpa takut ketinggalan absen                 
