from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calcX(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element_by_id("book")
    book_button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calcX(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

    alert_modal = browser.switch_to_alert()
    print(alert_modal.text.split(': ')[-1])
finally:
    browser.quit()