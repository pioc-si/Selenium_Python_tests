from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'

class TestSubmitButton(unittest.TestCase):

    def get_welcome_text(link):
        browser = webdriver.Chrome()
        browser.get(link)

        input_name = browser.find_element(By.CLASS_NAME, 'first')
        input_name.send_keys("Ivan")
        input_surname = browser.find_element(By.CLASS_NAME, 'second')
        input_surname.send_keys("Petrov")
        input_mail = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input_mail.send_keys("cat@mail.com")
        input_phone = browser.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
        input_phone.send_keys("+79811500000")
        input_adress = browser.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
        input_adress.send_keys("Georgia,Ilia st.,6m")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        browser.quit()

        return welcome_text


    def test_form1(self):
            welcome_text = TestSubmitButton.get_welcome_text(link1)
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта 1
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def test_form2(self):
            welcome_text = TestSubmitButton.get_welcome_text(link2)
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта 2
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()

