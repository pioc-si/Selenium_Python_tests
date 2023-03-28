from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(3)

login_button = browser.find_element(By.ID, 'ember33')
time.sleep(3)
login_button.click()

login_email = browser.find_element(By.ID, 'id_login_email')
login_email.send_keys('your email')
login_password = browser.find_element(By.ID, 'id_login_password')
login_password.send_keys("your password ;)")

time.sleep(3)    
login_button_in_form = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn')
login_button_in_form.click()
time.sleep(3) 


browser.quit()

