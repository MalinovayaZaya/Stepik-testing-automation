from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    # "w" открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
    with open("test.txt", "w") as test_file:
        test_file.write("Test")

    # current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла

    test_file_path = os.getcwd() + "/" + test_file.name

    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_name("firstname")
    input_last_name = browser.find_element_by_name("lastname")
    input_email = browser.find_element_by_name("email")

    input_name.send_keys("Poly")
    input_last_name.send_keys("Molly")
    input_email.send_keys("test@test.ru")

    button_send_file = browser.find_element_by_name("file")
    button_send_file.send_keys(test_file_path)

    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

finally:
    time.sleep(30)
    browser.quit()
    os.remove("test.txt")
