from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link)

    login_btn = browser.find_element(By.ID, "ember33")
    login_btn.click()

    email_btn = browser.find_element(By.ID, "id_login_email")
    email_btn.send_keys("404tm2@mail.ru	")

    pass_btn = browser.find_element(By.ID, "id_login_password")
    pass_btn.send_keys("1q2w3e4rQz")



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

