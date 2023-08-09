from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium_course.function_math import calc
import time

class test_reg_page:
    def test_registration_page_1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text,
                         "Registration page #1 — not passed")

    def test_registration_page_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text,
                         "Registration page #2 — not passed")


if __name__ == "__main__":
    pytest.main()