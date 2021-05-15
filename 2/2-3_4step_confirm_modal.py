from selenium import webdriver
import math

def calcX(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_confirm = browser.find_element_by_css_selector("button.btn")
    button_confirm.click()

    confirm_modal = browser.switch_to_alert()
    confirm_modal.accept()

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
