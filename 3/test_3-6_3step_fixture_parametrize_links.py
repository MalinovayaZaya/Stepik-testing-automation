import pytest
from selenium import webdriver
import time
import math


def answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link_value', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, link_value):
    link = f"https://stepik.org/lesson/{link_value}/step/1"
    browser.get(link)

    textarea_for_answer = browser.find_element_by_css_selector("textarea.ember-text-area")
    textarea_for_answer.send_keys(answer())

    send_button = browser.find_element_by_css_selector("button.submit-submission")
    send_button.click()

    result_space = browser.find_element_by_css_selector("div.smart-hints__feedback")
    assert result_space.text == "Correct!", result_space.text
