import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


def test_1():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    browser.get(link1)

    # найдём обязательные поля
    elements = browser.find_elements(
        By.XPATH, "//label[contains(text(), '*')]/following-sibling::input"
    )

    # заполним их
    for element in elements:
        element.send_keys("Мой ответ")

    # отправим заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # найдём элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    result = welcome_text_elt.text

    # с помощью assertEqual проверяем, что смогли зарегистрироваться, т.е.ожидаемый текст совпадает с текстом на странице сайта
    assert result == 'Congratulations! You have successfully registered!'

def test_2():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link2)
    answer = 42

    first_name = browser.find_element(
        By.XPATH, '//*[@class="form-control first"]'
    )
    first_name.send_keys(answer)

    first_name = browser.find_element(
        By.XPATH, '//*[@class="form-control third"]'
    )
    first_name.send_keys(answer)

    # отправим заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    # # ждем загрузки страницы
    time.sleep(1)

    # # найдём элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h11")
    result = welcome_text_elt.text

    # # с помощью assertEqual проверяем, что смогли зарегистрироваться, т.е.ожидаемый текст совпадает с текстом на странице сайта
    assert result == 'Congratulations! You have successfully registered!!!!!!!!!!'