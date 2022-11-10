import os
import random
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


load_dotenv()
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
link = 'https://stepik.org/lesson/236895/step/1'

try:
    browser.get(link)
    browser.implicitly_wait(10)
    inp = browser.find_element(By.TAG_NAME, 'textarea')
    inp.send_keys(random.randint(1, 10))
    submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
    submit.click()
    browser.implicitly_wait(10)
    login_tab = browser.find_element(By.CSS_SELECTOR, '.ember-view.light-tabs__switch')
    login_tab.click()
    browser.implicitly_wait(10)
    email_input = browser.find_element(By.ID, 'id_login_email')
    email_input.send_keys(os.getenv('EMAIL'))
    password_input = browser.find_element(By.ID, 'id_login_password')
    password_input.send_keys(os.getenv('PASSWORD'))
    submit = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
    submit.click()
finally:
    time.sleep(30)
    browser.quit()
