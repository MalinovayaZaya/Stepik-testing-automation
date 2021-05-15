from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#   link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    x_element = browser.find_element_by_id("num2")
    x += int(x_element.text)

    select_numb = Select(browser.find_element_by_id("dropdown"))
    select_numb.select_by_visible_text(str(x))

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
finally:
    time.sleep(15)
    browser.quit()