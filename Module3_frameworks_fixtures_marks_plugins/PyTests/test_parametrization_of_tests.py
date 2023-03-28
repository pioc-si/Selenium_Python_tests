import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(4)
    browser.quit()


@pytest.mark.parametrize('url_number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904""236905"])

class TestLogin:    
    def test_answer_in_form(self, browser, url_number):
            link = f"https://stepik.org/lesson/{url_number}/step/1"
            browser.get(link)
            answer = math.log(int(time.time()))
            
            time.sleep(3)
            login_button = browser.find_element(By.ID, 'ember33')
            login_button.click()

            login_email = browser.find_element(By.ID, 'id_login_email')
            login_email.send_keys('victoriia.davydova@yandex.ru')
            login_password = browser.find_element(By.ID, 'id_login_password')
            login_password.send_keys("2StepiC2)")

            login_button_in_form = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn')
            login_button_in_form.click()
            
            time.sleep(3)
            answer_textarea = browser.find_element(By.CSS_SELECTOR, 'textarea')
            answer_textarea.send_keys(answer)
            
            submit_button = browser.find_element(By.CLASS_NAME, 'submit-submission')
            submit_button.click()
            time.sleep(4)

            actual_answer = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text

            assert "Correct!" == actual_answer


if __name__ == "__main__":
    pytest.main()

