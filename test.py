from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100"))

    btn = browser.find_element(By.ID, "book")
    btn.click()

    value = browser.find_element(By.ID, "input_value")
    result = calc(int(value.text))

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(result)

    btn = browser.find_element(By.ID, "solve")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()

