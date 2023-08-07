from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("123")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("321")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("mail.ru")


    current_dir = os.path.abspath(os.path.dirname('file.txt'))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()