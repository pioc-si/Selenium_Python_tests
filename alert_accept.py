from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

Magic_button = browser.find_element(By.CLASS_NAME, 'btn').click()

confirm = browser.switch_to.alert
confirm.accept()

element = browser.find_element(By.ID, 'input_value')
x = element.text
y = calc(x)

answer_form = browser.find_element(By.ID, 'answer').send_keys(y)

button = browser.find_element(By.CLASS_NAME, 'btn').click()
time.sleep(2)

browser.quit()

