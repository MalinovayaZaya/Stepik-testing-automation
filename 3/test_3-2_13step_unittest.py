from selenium import webdriver
import unittest

class TestStepik(unittest.TestCase):
    def test_passing_without_error(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        input_name = browser.find_element_by_css_selector(".first_block .first")
        input_name.send_keys("Ivan")
        input_last_name = browser.find_element_by_css_selector(".first_block .second")
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element_by_css_selector(".first_block .third")
        input_email.send_keys("test@test.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Oops, it was not possible to register :с")

        browser.quit()


    def test_passing_with_error(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        input_name = browser.find_element_by_css_selector(".first_block .first")
        input_name.send_keys("Ivan")
        input_last_name = browser.find_element_by_css_selector(".first_block .second")
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element_by_css_selector(".first_block .third")
        input_email.send_keys("test@test.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Oops, it was not possible to register :с")

        browser.quit()

if __name__ == "__main__":
    unittest.main()