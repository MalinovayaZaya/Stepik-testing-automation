from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    desired_button = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    desired_button.click()

    input_name = browser.find_element_by_tag_name("input")
    input_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_name("last_name")
    input_last_name.send_keys("Petrov")
    input_city = browser.find_element_by_class_name("city")
    input_city.send_keys("Smolensk")
    input_country = browser.find_element_by_id("country")
    input_country.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
