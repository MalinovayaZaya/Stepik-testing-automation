import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

# фикстура browser, которая будет создавать объект WebDriver. Этот объект можно использовать в тестах для
# взаимодействия с браузером. Метод browser, указываем, что он является фикстурой с помощью декоратора @pytest.fixture.
# После этого мы можем вызывать фикстуру в тестах, передав ее как параметр.
# По умолчанию фикстура будет создаваться для каждого тестового метода, для каждого теста запустится свой браузер.

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    print("kill browser..")
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")