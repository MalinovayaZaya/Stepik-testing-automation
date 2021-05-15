from selenium import webdriver
import time
import math

def calcX(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calcX(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView();", robot_checkbox)
    robot_checkbox.click()

    robot_radiobutton = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView();", robot_radiobutton)
    robot_radiobutton.click()

    button_submit = browser.find_element_by_xpath('//button[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView();", button_submit)
    button_submit.click()
finally:
    time.sleep(30)
    browser.quit()
