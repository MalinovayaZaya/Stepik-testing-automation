from selenium import webdriver
import math

def calcX(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_switch_new_tab = browser.find_element_by_css_selector("button.trollface")
    button_switch_new_tab.click()

    riddle_window = browser.window_handles[1]
    switch_new_tab = browser.switch_to.window(riddle_window)

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