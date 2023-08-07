from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import function_math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    trollbutton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    trollbutton.click()

    #confirm = browser.switch_to.alert
    #confirm.accept()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    submit2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()