from selenium import webdriver
import time
import math

def calcX(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calcX(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robot_radiobutton = browser.find_element_by_id("robotsRule")
    robot_radiobutton.click()

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
