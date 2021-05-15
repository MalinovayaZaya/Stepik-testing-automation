from selenium import webdriver
import time

try:
    # ссылка на сайт, с прохождением теста с ошибкой
    link = "http://suninjuly.github.io/registration2.html"

    # ссылка на сайт, с удачным прохождением теста
    # link = "http://suninjuly.github.io/registration1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_css_selector(".first_block .first")
    input_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_css_selector(".first_block .second")
    input_last_name.send_keys("Petrov")
    input_email = browser.find_element_by_css_selector(".first_block .third")
    input_email.send_keys("test@test.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()