from math import sin, log
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get('https://suninjuly.github.io/math.html')
    x = browser.find_element(By.ID, 'input_value').text
    result = log(abs(12 * sin(int(x))))
    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(result)
    i_am_robot = browser.find_element(By.ID, 'robotCheckbox').click()
    robots_rule = browser.find_element(By.ID, 'robotsRule').click()
    submit = browser.find_element(By.XPATH, '//button[@type="submit"]').click()
finally:
    time.sleep(30)
    browser.quit()
